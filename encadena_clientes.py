from paho.mqtt.client import Client
import paho.mqtt.publish as publish
from sympy import isprime
from multiprocessing import Process
from time import sleep
from multiprocessing import Lock


def celebracion(modulo, cant):
    print('A celebrar que ha llegado un multiplo de', modulo, 'ya llevamos', cant)
    mensaje='Llevamos '+str(cant)+' multiplos de '+str(modulo)
    sleep(modulo%5+1)
    publish.single('clients/noticias', payload=mensaje,hostname='simba.fdi.ucm.es')
    print('TODOS LO SABEN')
    

def revision_primos(lista, cant):
    print('CHECKEO de los ultimos',cant, 'primos')
    ultimos=lista[-cant:]
    mensaje='Los ultimos primos son '+str(ultimos)
    media=sum(lista)/len(lista)
    mensaje+='\nY la media total es '+str(media)
    print(mensaje)
    publish.single('clients/primos', payload=mensaje, hostname="simba.fdi.ucm.es")

def on_message(client, userdata, message):
    num_float=float(message.payload)
    numero=round(num_float)
    print('Recibido el numero', numero)
    if isprime(numero):
        lock=userdata['lock']
        lock.acquire()
        
        try:
            userdata['list_primes'].append(numero)
            if len(userdata['list_primes'])%userdata['frecuencia']==0:
                revision_primos(userdata['list_primes'], userdata['frecuencia'])
        finally:
            lock.release()
            
        
    elif numero%userdata['modulo']==0:
        userdata['cont']+=1
        p=Process(target=celebracion, args=(userdata['modulo'],userdata['cont']))
        p.start()
        
        

def main():
    datos={'list_primes':[], 'frecuencia':3, 'modulo':7,'cont':0, 'lock':Lock()}
    cliente=Client(userdata=datos)
    cliente.on_message=on_message
    cliente.connect("simba.fdi.ucm.es")
    cliente.subscribe('numbers')
    cliente.loop_forever()

if __name__=='__main__':
    main()
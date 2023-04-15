from paho.mqtt.client import Client
from multiprocessing import Lock
from time import sleep

def on_message(client, userdata, message):
    print ('En el canal', message.topic,'recibido el mensaje', message.payload)
    a_quitar = len('temperature/')
    
    
    lock = userdata['lock']
    lock.acquire()
    
    
    try:
        canal = message.topic[a_quitar:]
        if canal in userdata['temp']:
            userdata['temp'][canal].append(int(message.payload))
        else:
            userdata['temp'][canal]=[int(message.payload)]
    finally:
        lock.release()
    
    print('Lo recabado es', userdata['temp'])



def main():
    datos = {'lock':Lock(), 'temp':{}}
    cliente = Client(userdata=datos)
    cliente.on_message = on_message
    cliente.connect('simba.fdi.ucm.es')
    cliente.subscribe('temperature/#')
    cliente.loop_start()

    while True:
        sleep(4)
        print('CONTROL DE LOS CANALES')
        maximas=[]
        minimas=[]
        sum_temps=0
        num_temps=0
        for canal,temperaturas  in datos['temp'].items():
            maxima=max(temperaturas)
            maximas.append(maxima)
            minima=min(temperaturas)
            minimas.append(minima)
            sum_temps+=sum(temperaturas)
            num_temps+=len(temperaturas)
            media = sum(temperaturas)/len(temperaturas)
            print('En el canal',canal,'maxima',maxima,'minima', minima, 'media', media)
            datos['temp'][canal]=[]
        max_total=max(maximas)
        min_total=min(minimas)
        media_total=sum_temps/num_temps
        print('En GENERAL maxima', max_total, 'minima', min_total, 'media', media_total)


if __name__ == "__main__":
    main()

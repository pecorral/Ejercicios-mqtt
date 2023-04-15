from paho.mqtt.client import Client




def on_message(client, userdata, message):
    numero=float(message.payload)
    num_int=round(numero)
    if numero==num_int:
        userdata['suma_entera']+=num_int
        print('Ultimo numero recibido', num_int,'es ENTERO y la suma de los numeros enteros es', userdata['suma_entera'])
    else:
        userdata['suma_real']+=numero
        print('Ultimo numero recibido', numero, 'es REAL y la suma de los numeros reales es', userdata['suma_real'])


def main():
    datos={'suma_entera':0, 'suma_real':0}
    cliente=Client(userdata=datos)
    cliente.on_message=on_message
    cliente.connect("simba.fdi.ucm.es")
    cliente.subscribe('numbers')
    cliente.loop_forever()

if __name__=='__main__':
    main()
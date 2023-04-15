from paho.mqtt.client import Client
import paho.mqtt.publish as publish
from multiprocessing import Process
from time import sleep

def mensajero(message, broker):
    print('Cuerpo del pedido', message)
    tiempo_espera,topic, mensaje = message[2:-1].split(',')
    print('Tiempo de espera', tiempo_espera, 'Topic', topic,'Mensaje' ,mensaje)
    sleep(int(tiempo_espera))
    publish.single(topic, payload=mensaje, hostname=broker)
    print('Mensaje enviado')

def on_message(client, userdata, message):
    print('Nuevo pedido', message.payload)
    programar_mensaje = Process(target=mensajero, args=(str(message.payload), 'simba.fdi.ucm.es'))
    programar_mensaje.start()
    print('Pedido en proceso')


# Estructura de cómo tienen que ser los mensajes para que se programe el envío del mensaje correctamente:
    # message=b'tiempo_de_espera,nombre_del_topic,mensaje_que_mandar'

def main():
    cliente = Client()
    cliente.on_message = on_message
    cliente.connect('simba.fdi.ucm.es')
    cliente.subscribe('clients/timeout')
    cliente.loop_forever()


if __name__ == "__main__":
    main()
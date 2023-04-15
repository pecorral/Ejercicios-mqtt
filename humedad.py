from paho.mqtt.client import Client



def on_message(client, userdata, message):
    print ('En el canal', message.topic,'recibido el mensaje', message.payload)
    if message.topic=='temperature/t1':
        temp=int(message.payload)
        if temp>=userdata['umbral_temp']:
            if not userdata['miramos_humedad']:
                userdata['miramos_humedad']=True
                print('La temperatura', temp, 'ha superado el umbral de temperatura', userdata['umbral_temp'], 'nos conectamos a humidity')
        else:
            if userdata['miramos_humedad']:
                userdata['miramos_humedad']=False
                print('La temperatura', temp, 'es inferior umbral de temperatura', userdata['umbral_temp'], 'nos DESconectamos de humidity')
            
    if message.topic=='humidity':
        humedad=int(message.payload)
        if humedad>50:
            userdata['miramos_humedad']=False
            print('La humedad', humedad, 'ha superado el umbral de humedad', userdata['umbral_humedad'], 'nos DESCONECTAMOS de humidity')
        
 
    if userdata['miramos_humedad']:
        client.subscribe('humidity')
    else:
        client.unsubscribe('humidity')

def main():
    datos = {'miramos_humedad':False, 'umbral_temp':10, 'umbral_humedad':50}
    cliente = Client(userdata=datos)
    cliente.on_message = on_message
    cliente.connect('simba.fdi.ucm.es')
    cliente.subscribe('temperature/t1')
    cliente.loop_forever()




if __name__ == "__main__":
    main()

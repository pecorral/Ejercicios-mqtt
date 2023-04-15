import sys
from paho.mqtt.client import Client


# broker=simba.fdi.ucm.es



def on_message(client, userdata, message):
    print("In channel", message.topic, "received", message.payload)

    
    
def main(broker,topic_publish,topic_subscribe):
    cliente=Client()
    cliente.on_message=on_message
    cliente.connect(broker)
    
    cliente.publish(topic_publish, "Informacion buena e interesante")
    
    cliente.subscribe(topic_subscribe)
    cliente.loop_forever()
    
    
    
if __name__=="__main__":
    if len(sys.argv)<4:
        print(f"Usage: {sys.argv[0]} broker topic_publish topic_subscribe")
        sys.exit(1)
    # print(sys.argv)
    broker=sys.argv[1]
    topic_publish=sys.argv[2]
    topic_subscribe=sys.argv[3]
    main(broker,topic_publish,topic_subscribe)
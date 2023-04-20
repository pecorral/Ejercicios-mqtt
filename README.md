# Ejercicios-mqtt
En este repositorio se hacen 6 archivos de python distintos que realizan las siguientes acciones:

1) broker: una implementación básica de un broker (intermediario) que permite que el usuario
   publique un mensaje básico en el canal "topic_publish" y que se subscriba al canal "topic_subscribe" 
   para recibir la información que se vaya publicando ahí.
   
2) numeros: programa que conecta al usuario al broker "simba.fdi.ucm.es" y le subscribe al canal "numbers"
   de tal manera que cada vez que reciba un número, distingue si es entero o no, y lo añade a la suma total
   de números de ese tipo (entero o float) que ya ha recibido.

3) temperaturas: programa que conecta al usuario al broker "simba.fdi.ucm.es" y le subscribe a todos los 
   canales de la forma "temperature/" y va recogiendo las temperaturas que se vayan publicando en cada uno
   de ellos, para que cada 4 segundos mida la media, la temperatura máxima y mínima de las temperaturas recibidas
   en cada canal y en general.
   
4) humedad: programa que conecta al usuario al broker "simba.fdi.ucm.es" y le subscribe al canal "temperature/t1"
   donde va recogiendo las temperaturas que se publican, si estas superan un cierto umbral se conectará al canal 
   "humidity", y si bajan de ese umbral, o los datos recogidos en el canal "humidity" son superiores a un umbral
   de humedad, se desconectará del canal "humidity".
   
5) temporizador: programa que conecta al usuario al broker "simba.fdi.ucm.es" y le subscribe al canal "clients/timeout"
   donde irá recibiendo mensajes con la estructura de:   tiempo_espera,topic, mensaje; que serán pedidos para este usuario
   para que publique por el canal topic el mensaje pedido tras esperar el tiempo de espera. 
   
6) encadena_clientes: programa que conecta al usuario al broker "simba.fdi.ucm.es" y le subscribe al canal "numbers"
   de tal manera que cada vez que reciba un número, distingue si es primo o no, y si lo es lo añade a una lista de primos
   de tal manera que si contiene una cantidad múltiplo de frecuencia de números, publica por el canal "clients/primos"
   la media de los últimos "frecuencia" números primos de la lista. Si sin embargo el número recibido es múltiplo de "módulo"
   entoces lo celebra publicando en el canal "clients/noticias" que ha recibido un múltiplo más.

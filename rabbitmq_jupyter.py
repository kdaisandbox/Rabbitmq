import pika
import datetime
import json
import base64
import io
from PIL import Image
from io import BytesIO
import string
import random
import os



host="10.19.87.55"
port=5672   
user="admin"
passw="123456"
rabbitqueue="AIVerse_Queue"


x = {
  "ContactFileNo": 234232,
  "ChassisNo": "nx23r32",
  "VehicleVariant": "1.5L TCDI 95PS EU6",
  "Parts": [
      "Arka Tampon",
 "Ayna",
 "Bagaj Kapak",
  ],

 "LaborItems": [
      "341","455"
  ],

 "Damages": [
     {
      "id" : "123456",
      "DamageData" : [
          [[0.2,0.3],[0.1,0.4],[0.5,0.1]],
          [[0.2,0.3],[0.1,0.4],[0.5,0.1]]
      ]
     },
          {
      "id" : "123457",
      "DamageData" : [
          [[0.2,0.3],[0.1,0.4],[0.5,0.1]],
          [[0.2,0.3],[0.1,0.4],[0.5,0.1]]
      ]
     }
  ],
 "InvalidImages": [
     "123458",
     "123459"
  ],
}


print(x)



#Queue Create
connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, '/', pika.PlainCredentials(user, passw)))
channel = connection.channel() 
channel.queue_declare(queue=rabbitqueue,durable= True) # queue creating


# Send message The Queue
message = json.dumps(x)  
channel.basic_publish(exchange='', routing_key='BusraMuratTest', body=message)  

connection.close()
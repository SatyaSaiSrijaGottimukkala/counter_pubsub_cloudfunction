import base64
import json
import os
from google.cloud import pubsub_v1
publisher = pubsub_v1.PublisherClient()
PROJECT_ID = os.getenv("cedar-chemist-341514")
def counter (data,arg2):
     # if there is no data
     if data is None:
          print("request.data is empty")
          return("request.data is empty",400)
     # decoding the message passed into cloud function 
     value = base64.b64decode(data['data']).decode('utf-8')
     # converting string type decoded value to dictionary
     value_dict= json.loads(value)
     data_value = value_dict['counter']
     # for topic path check in google cloud console by clicking on topic
     topic_path = 'projects/cedar-chemist-341514/topics/counter-responses'
     try:
          if data_value>2:
               #if data_value i.e counter value > 2 this block gets activated 
               str1= json.dumps({"counter":data_value-1}) #to create a string
               encoded_message = str1.encode('utf-8')  #encoding
               publish_future= publisher.publish(topic_path, data=encoded_message) 
               #publishing the encoded value this contains value = countervalue-1 by this it will publish values till 2
               publish_future.result()
               return("message recived and published to pubsub",200)
          else:
               print(f'cannot publish message data value provided is not >1')
               raise Exception (f'value is {data_value}') #exception is raised if countervalue provided is  <=1
     except Exception as e:
          print(e)
          return(e,500)



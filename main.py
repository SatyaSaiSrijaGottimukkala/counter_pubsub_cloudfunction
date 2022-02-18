import base64
import json
import os
from google.cloud import pubsub_v1
publisher = pubsub_v1.PublisherClient()
PROJECT_ID = os.getenv("cedar-chemist-341514")
def counter (data,arg2):
     print("data : ",data)
     if data is None:
          print("request.data is empty")
          return("request.data is empty",400)
     value = base64.b64decode(data['data']).decode('utf-8')
     value_dict= json.loads(value)
     data_value = value_dict['counter']
     topic_path = 'projects/cedar-chemist-341514/topics/counter-responses'
     try:
          if data_value>2:
               print(data_value)
               str1= json.dumps({"counter":data_value-1})
               encoded_message = str1.encode('utf-8')
               # encoded_message= str(data_value-1).encode('utf-8')
               publish_future= publisher.publish(topic_path, data=encoded_message)
               publish_future.result()
               return("message recived and published to pubsub",200)
          else:
               print(f'cannot publish message data value provided is not >1')
               raise Exception (f'value is {data_value}')
     except Exception as e:
          print(e)
          return(e,500)



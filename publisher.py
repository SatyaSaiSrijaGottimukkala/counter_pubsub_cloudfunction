import os
import json
from google.cloud import pubsub_v1
#Providing project you are working in 
PROJECT_ID = os.getenv("cedar-chemist-341514")
#providing path of key we have created and downloaded
credentials_path = "cedar-chemist-341514-1b7b579e88f1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= credentials_path
publisher = pubsub_v1.PublisherClient()
#providing pubsub topic path
topic_path = 'projects/cedar-chemist-341514/topics/counter-responses'
#taking user input
data = int(input("enter starting value : "))
#converting into string and encoding it to byte string
data_json = json.dumps({"counter":data}).encode('utf-8')
#publishing 
future = publisher.publish(topic_path, data= data_json)
print(f'publish image id {future.result()}')



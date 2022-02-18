import os
import json
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError
#Providing project you are working in 
PROJECT_ID = os.getenv("cedar-chemist-341514")
#providing path of key we have created and downloaded
credentials_path = "/Users/a845604yara.com/Documents/gcloud-practice/pubsub-cloudfunction/cedar-chemist-341514-1b7b579e88f1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= credentials_path
subscriber = pubsub_v1.SubscriberClient()
# providing subscription path
subscription_path = 'projects/cedar-chemist-341514/subscriptions/responses'
#call back fucntion to get the message and printing the message after converting it to dictionary
def callback(message):
     print(json.loads(message.data))
     message.ack() #message acknowledgement
#initialising streaming path 
streaming_future = subscriber.subscribe(subscription_path, callback= callback)
print(f'Listening to message on {subscription_path}')

with subscriber:
     try:
          streaming_future.result() #to pull messages from subscription continously
     except TimeoutError:
          streaming_future.cancel() 
          streaming_future.result()

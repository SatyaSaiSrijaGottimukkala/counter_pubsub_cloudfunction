import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError
PROJECT_ID = os.getenv("cedar-chemist-341514")
credentials_path = "/Users/a845604yara.com/Documents/gcloud-practice/pubsub-cloudfunction/cedar-chemist-341514-1b7b579e88f1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= credentials_path
subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'projects/cedar-chemist-341514/subscriptions/responses'
def callback(message):
     print(f'counter : {message.data}')
     message.ack()

streaming_future = subscriber.subscribe(subscription_path, callback= callback)
print(f'Listening to message on {subscription_path}')

with subscriber:
     try:
          streaming_future.result()
     except TimeoutError:
          streaming_future.cancel()
          streaming_future.result()

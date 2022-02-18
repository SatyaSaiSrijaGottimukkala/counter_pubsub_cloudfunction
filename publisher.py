import os
from google.cloud import pubsub_v1
PROJECT_ID = os.getenv("cedar-chemist-341514")
credentials_path = "/Users/a845604yara.com/Documents/gcloud-practice/pubsub-cloudfunction/cedar-chemist-341514-1b7b579e88f1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= credentials_path
publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/cedar-chemist-341514/topics/counter-responses'

data = input("enter starting value : ")
data = data.encode('utf-8')

future = publisher.publish(topic_path, data)
print(f'publish image id {future.result()}')
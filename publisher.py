import os
import json
from google.cloud import pubsub_v1
PROJECT_ID = os.getenv("cedar-chemist-341514")
credentials_path = "/Users/a845604yara.com/Documents/gcloud-practice/pubsub-cloudfunction/cedar-chemist-341514-1b7b579e88f1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= credentials_path
publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/cedar-chemist-341514/topics/counter-responses'

data = int(input("enter starting value : "))

data_json = json.dumps({"counter":data}).encode('utf-8')

future = publisher.publish(topic_path, data= data_json)
print(f'publish image id {future.result()}')

#to create from commandline
# gcloud pubsub topics create counter-responses
# gcloud pubsub subscrptions create responses --topic counter-responses
# gcloud functions deploy counter --runtime python39 --trigger-topic counter-responses
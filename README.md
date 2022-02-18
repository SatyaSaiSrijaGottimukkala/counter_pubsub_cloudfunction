# counter_pubsub_cloudfunction
create a cloudfunction trigger using pubsub send messages back to pubsub

Clone the repository, 

  git clone https://github.com/SatyaSaiSrijaGottimukkala/counter-pubsub-cloudfunction.git
  
create a pubsub topic and respective subscriber through google cloud console
get your private key to publish message and to get subscriber messages


in main.py, 

                  PROJECT_ID = os.getenv("PROJECT_NAME")
                  
                  topic_path = 'YOUR_TOPIC_PATH'

in publisher.py, 

                   credentials_path = "PATH OF YOUR KEY"
                   
                   PROJECT_ID = os.getenv("PROJECT_NAME")
                   
                   topic_path = 'YOUR_TOPIC_PATH' 
                 
in subscriber.py 

                   subscription_path = 'YOUR_SUBSCRIPTION_PATH'
                   
                   credentials_path = "PATH OF YOUR KEY"
                   
                   PROJECT_ID = os.getenv("PROJECT_NAME")
                   
in 3 different terminals run the following commands:

               1 gcloud functions deploy YOUR_FUNCTION_NAME --runtime python39 --trigger-topic YOUR_TOPIC_NAME
                
               2 python publisher.py   
                
               3 python subscriber.py 
               
 1st command => to create cloud function that is being triggered by your pubsub topic
 
 2nd command => run your publisher script to publish a value to counter that triggers cloud function
 
 3rd command => run your subscriber script to subscribe to your pubsub topic to check counter values
 
      

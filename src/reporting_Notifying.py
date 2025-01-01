import boto3
import getCreds

config = getCreds.get_creds()

#Boto3 client object for AWS SNS Service
sns = boto3.client('sns',region_name='us-east-1', 
                aws_access_key_id=config['creds']['aws_access_key_id'],   
                aws_secret_access_key=config['creds']['aws_secret_access_key']
                )

#Create SNS topic
response = sns.create_topic(Name='Topic1')

# Get TopicARN for the created topic
topic_arn = response['TopicArn']

#Make sure IAM role has permission to publish to the topic --> SNSfullAccess

#Delete the topic
deleted_topic = sns.delete_topic(TopicArn=topic_arn)


#Subscribe to the topic
res = sns.subscribe(TopicArn=topic_arn, 
                    Protocol='email', 
                    Endpoint = "")

#List subscription by the topic
list_topics = sns.list_subscriptions_by_topic(TopicArn=topic_arn)

#Publish message to the topic
message = sns.publsih(topic_arn=topic_arn, 
                      Message="Hello World", 
                      Subject="Test")
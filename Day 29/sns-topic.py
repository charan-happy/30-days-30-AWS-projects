import boto3

client = boto3.client('sns') 

sns_topic = client.create_topic(Name='W16_SNS_topic')

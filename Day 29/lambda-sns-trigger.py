import boto3
import json

def lambda_handler(event, context):
    sns = boto3.client('sns', region_name = 'us-east-1')
    for message in event['Records']:
        print(message)
        body = message['body']
        pub_mess = sns.publish(
            TopicArn = 'arn:aws:sns:us-east-1:217495474303:W16_SNS_topic', 
            Message = body)
        print(pub_mess)
        
    return { 
        'statusCode': 200
    }
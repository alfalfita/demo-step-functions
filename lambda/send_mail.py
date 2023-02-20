import boto3
import os

ses = boto3.client('ses')

def lambda_handler(event, context):
    VERIFIED_EMAIL = os.environ['VERIFIED_EMAIL']
    ses.send_email(
        Source=VERIFIED_EMAIL,
        Destination={
            'ToAddresses': [event['email']]
        },
        Message={
            'Subject': {'Data': 'Demo de AWS Step Functions'},
            'Body': {'Text': {'Data': event['message']}}
        }
    )
    return 'Success!'
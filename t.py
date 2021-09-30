import os
import boto3
TABLE_NAME = os.getenv('DB_TABLE', 'rk-employee_info')
client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)
table.scan()
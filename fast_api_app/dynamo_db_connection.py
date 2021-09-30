'''
    This file is to maintain a table in dynamo db for employee info
    where 'emp_id' is primary key and sorting keys are 'name' and 'department'.
'''

import os
from uuid import uuid4

import boto3

# os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAUID72KDDVJ2WXAVL'
# os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
# os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

TABLE_NAME = os.getenv('DB_TABLE', 'rk-employee_info')

client = boto3.client('dynamodb')

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table(TABLE_NAME)


def db_put_item(name, department, details):
    formatted_data = {
        'name': name,
        'emp_id': str(uuid4()),
        'department': department,
        'details': details
    }

    response = table.put_item(
        Item=formatted_data
    )
    return response


def db_get_item(emp_id):
    response = client.get_item(
        Key={
            'emp_id': {
                'S': ''
            }
        },
        TableName=TABLE_NAME,
    )
    return response


def get_all_item():
    return table.scan()


# if __name__ == "__main__":
#     r = db_put_item(name="Prashant", department="Development", details={})
#     print(r)
#     r = db_get_item()
#     print(r)
#     r = table.scan()
#     print(r)
import json
import os
import requests

from fastapi import FastAPI

from dynamo_db_connection import get_all_item, db_get_item, db_put_item

app = FastAPI()

CALCULATION_SERVICE_URL = "http://{}:5000".format(os.getenv('CALCULATION_SERVICE_URL', '127.0.0.1'))


@app.get("/")
def get_all_data_from_db() -> dict:
    try:
        data = get_all_item()
        return {'data': data, 'message': 'Data Retrieved', 'status': 200}
    except Exception as e:
        return {'err_message': 'Some thing went wrong. {}'.format(str(e)), 'status': 500}


@app.post("/create_data")
def create_data_to_db(name: str, department: str) -> dict:
    try:
        r = db_put_item(name=name, department=department, details={})
        return {'status': 200, 'message': 'Data Saved', 'response': r}
    except Exception as e:
        return {'err_message': 'Some thing went wrong. {}'.format(str(e)), 'status': 500}


@app.post("/create_and_compute")
def create_data_to_db_with_compute(name: str, department: str, numbers: list) -> dict:
    try:
        response = requests.post(CALCULATION_SERVICE_URL, data=json.dumps({
            "numbers": numbers
        }))
        total = response.json()['sum']
        r = db_put_item(name=name, department=department, details={'sum': total})
        return {'status': 200, 'message': 'Data Saved', 'response': r}
    except Exception as e:
        return {'err_message': 'Some thing went wrong. {}'.format(str(e)), 'status': 500}

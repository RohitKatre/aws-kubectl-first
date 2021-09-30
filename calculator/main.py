import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['POST'])
def summation():
    if request.method == 'POST':
        try:
            numbers = json.loads(request.data)['numbers']
            addition = sum(numbers)
            return jsonify(
                sum=addition,
                status=200
            )
        except Exception as e:
            return jsonify(
                status=500,
                err_message="Internal server error. {}".format(str(e))
            )
    else:
        return jsonify(
            status=500,
            err_message="Method not accepted"
        )

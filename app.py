import os

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

app = Flask(__name__, template_folder='./template')

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/sum', methods=['POST'])
def cal_sum():
    request_json = request.json

    required = ['values']
    if not all(k in request_json for k in required):
        return 'Missing values', 400

    values = request_json['values']

    val_sum = 0
    for value in values:
        val_sum += value

    response = {
        'values': values,
        'sum': val_sum
    }
    return jsonify(response), 201

@app.route('/average', methods=['POST'])
def cal_average():
    request_json = request.json

    required = ['values']
    if not all(k in request_json for k in required):
        return 'Missing values', 400

    values = request_json['values']

    val_sum = 0
    for value in values:
        val_sum += value
    
    val_average = val_sum / len(values)

    response = {
        'values': values,
        'average': val_average
    }
    return jsonify(response), 201

@app.route('/max', methods=['POST'])
def cal_max():
    request_json = request.json

    required = ['values']
    if not all(k in request_json for k in required):
        return 'Missing values', 400

    values = request_json['values']

    val_max = values[0]
    for value in values:
        if value > val_max:
            val_max = value

    response = {
        'values': values,
        'max': val_max
    }
    return jsonify(response), 201

@app.route('/min', methods=['POST'])
def cal_min():
    request_json = request.json

    required = ['values']
    if not all(k in request_json for k in required):
        return 'Missing values', 400

    values = request_json['values']

    val_min = values[0]
    for value in values:
        if value < val_min:
            val_min = value

    response = {
        'values': values,
        'min': val_min
    }
    return jsonify(response), 201

@app.route('/sort/up', methods=['POST'])
def sort_up():
    request_json = request.json

    required = ['values']
    if not all(k in request_json for k in required):
        return 'Missing values', 400

    values = request_json['values']

    val_sort_up = sorted(values)

    response = {
        'values': values,
        'up_sort_values': val_sort_up
    }
    return jsonify(response), 201

@app.route('/sort/down', methods=['POST'])
def sort_down():
    request_json = request.json

    required = ['values']
    if not all(k in request_json for k in required):
        return 'Missing values', 400

    values = request_json['values']

    val_sort_down = sorted(values, reverse=True)

    response = {
        'values': values,
        'down_sort_values': val_sort_down
    }
    return jsonify(response), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
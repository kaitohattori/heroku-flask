import os

from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/weather/today', methods=['GET'])
def today():
    response = {
        'weather': 'sunny',
        'temperature': 30
    }
    return jsonify(response), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
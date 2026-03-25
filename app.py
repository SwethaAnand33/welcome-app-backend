import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/welcome')
def welcome():
    return jsonify({"message": "Welcome Master"})

@app.route('/')
def home():
    return "Backend is running 🚀"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

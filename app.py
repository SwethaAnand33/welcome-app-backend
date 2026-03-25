from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to call backend

@app.route('/welcome')
def welcome():
    return jsonify({"message": "Welcome Master"})

if __name__ == '__main__':
    app.run()

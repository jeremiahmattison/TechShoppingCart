from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, how are you?"

if __name__ == "__main__":
    print("Starting Python Flask Server for Online Shopping Store Management System")
    app.run(port=5000)
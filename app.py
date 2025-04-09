from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the DevOps Toolbox API!"})

@app.route('/ip')
def get_ip():
    return jsonify({"ip": request.remote_addr})

@app.route('/headers')
def get_headers():
    return jsonify(dict(request.headers))

@app.route('/env')
def get_env():
    keys = ['PATH', 'HOME', 'SHELL', 'USER']
    return jsonify({key: os.getenv(key, 'Not Set') for key in keys})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

# Only the server run call should be inside this block
if __name__ == '__main__':
    app.run(debug=True)

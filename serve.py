from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Return the private IP address of the EC2 instance
    return socket.gethostbyname(socket.gethostname())

@app.route('/', methods=['POST'])
def stress():
    # Start a new process to run the stress_cpu function without blocking
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return jsonify({"message": "Stressing CPU now"}), 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

# Function to fetch hostname and IP address
def fetchDetails():
    hostname = socket.gethostname()
    addr = socket.gethostbyname(hostname)
    return str(hostname), str(addr)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, addr = fetchDetails()
    return render_template('index.html', hostname=hostname, IP=addr)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, jsonify, render_template, request, redirect, url_for, send_from_directory, flash
from flask_uploads import IMAGES, UploadSet, configure_uploads
import socket
import os

app = Flask(__name__)
photos=UploadSet("photos", IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = '/mnt/azure'
app.config["SECRET_KEY"] = os.urandom(24)
configure_uploads(app, photos)

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

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        photos.save(request.files['photo'])
        flash("Photo saved successfully.")
        return render_template('upload.html')
    return render_template('upload.html')

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

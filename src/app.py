from flask import Flask, jsonify, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES
import socket
 

app = Flask(__name__)


# Configure the upload set
screenshots = UploadSet('screenshots', IMAGES)
configure_uploads(app, (screenshots,))


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
    if request.method == 'POST' and 'screenshot' in request.files:
        filename = screenshots.save(request.files['screenshot'])
        return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="screenshot">
        <input type="submit" value="Upload">
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADED_SCREENSHOTS_DEST'], filename)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

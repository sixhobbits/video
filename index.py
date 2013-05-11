import os
from flask import Flask, render_template, request, send_from_directory
import youtube
import shutil
import sys
import subprocess
import random

       
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__)) + "uploads"

def get_title():
	s = ""
	for c in range(25):
		s += chr(random.randint(65,90))
	return s


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    print "index()"
    return render_template("index.html")

@app.route('/download', methods=['POST'])
def download():
    print request.form.get("url")
    link = request.form.get("url")
    title = get_title()
    download_videos = subprocess.call(['youtube-dl', '-f', '85/84/83/82/38/37/22/18/120/35/34','-o','uploads/' + title  + '.%(ext)s', link])
    title += ".mp4"
    return send_from_directory(UPLOAD_FOLDER, title, as_attachment=True)



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
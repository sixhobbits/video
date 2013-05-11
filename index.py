import os
from flask import Flask, render_template, request, send_from_directory
import youtube
import shutil
import sys
import subprocess
import random
import youtube_dl

       

UPLOAD_FOLDER = "/var/www/video/uploads"
print UPLOAD_FOLDER


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
    try:
        print os.path.join(UPLOAD_FOLDER,title)
        youtube_dl.main(['-f', '85/84/83/82/38/37/22/18/120/35/34','-o','/var/www/video/uploads/testasdf.mp4' + '.%(ext)s', link])
    except: # messy hack - this triggers each time, but all seems to work ok. if omitted an exception is thrown
        pass
    title += ".mp4"
    print "garethDebug",UPLOAD_FOLDER,title
    return send_from_directory(UPLOAD_FOLDER, title, as_attachment=True)



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

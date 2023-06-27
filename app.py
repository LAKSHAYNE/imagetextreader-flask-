from flask import Flask,render_template,request,Response,redirect,flash
import os
from werkzeug.utils import secure_filename
from scriptss.pdftocsv import convert
app = Flask(__name__)

# Create a directory in a known location to save files to.
uploads_dir = os.path.join(app.instance_path, 'uploads')
if not os.path.exists("uploads"):
    os.makedirs(uploads_dir,exist_ok=True)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/file_upload', methods=['POST'])
def file_upload():
    if 'file' not in request.files:
        print('No file part')
        return redirect('/')
    file = request.files['file']
    file.save(os.path.join(uploads_dir, secure_filename(file.filename)))
    result=convert()
    return render_template('data.html',result=result)

if __name__=='__main__':
    app.run(debug=True)
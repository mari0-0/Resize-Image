from flask import Flask, request, render_template, send_file
import os
from resizer import resize_image


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESIZED_FOLDER = 'resized'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESIZED_FOLDER'] = RESIZED_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESIZED_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            width = int(request.form['width'])
            height = int(request.form['height'])
            resized_filename = f"resized_{filename}"
            resized_path = os.path.join(app.config['RESIZED_FOLDER'], resized_filename)
            
            resize_image(file_path, resized_path, width, height)
            
            return render_template('result.html', filename=resized_filename)
    
    return render_template('upload.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['RESIZED_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

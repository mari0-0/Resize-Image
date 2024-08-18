from flask import Flask, request, render_template, send_file
import os
from resizer import resize_image

app = Flask(__name__)

# Create /tmp if it doesn't exist for LOCAL MACHINE ONLY
# os.makedirs('/tmp', exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        if file:
            # Check the file size
            file.seek(0, os.SEEK_END)  # Move the cursor to the end of the file
            file_size = file.tell()  # Get the current position of cursor
            file.seek(0, os.SEEK_SET)  # Reset the cursor to the start of the file

            max_size = 4.48 * 1024 * 1024  # 4.5 MB

            if file_size > max_size:
              return render_template('upload.html', isLarge=True)

            filename = file.filename
            file_path = os.path.join('/tmp', filename)  # Save the uploaded file to /tmp
            file.save(file_path)
            
            width = int(request.form['width'])
            height = int(request.form['height'])
            resized_filename = f"resized_{filename}"
            resized_path = os.path.join('/tmp', resized_filename)  # Save the resized image to /tmp
            resize_image(file_path, resized_path, width, height)
            
            return render_template('result.html', filename=resized_filename)
    
    return render_template('upload.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join('/tmp', filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

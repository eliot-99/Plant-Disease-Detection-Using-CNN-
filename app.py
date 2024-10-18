from flask import Flask, render_template, request, redirect, url_for, flash
import os
import random
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg','png'}

# Dummy list of plant diseases
plant_diseases = ["Image uploaded successfully!!"]

# Check if file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['image']

    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect to display the image and disease info
        return redirect(url_for('result', filename=filename))
    else:
        flash('Allowed image types are .jpg and .jpeg')
        return redirect(request.url)

@app.route('/result/<filename>')
def result(filename):
    # Randomly pick a plant disease for demo purposes
    disease = random.choice(plant_diseases)
    return render_template('result.html', filename=filename, disease=disease)

if __name__ == "__main__":
    app.run(debug=True)

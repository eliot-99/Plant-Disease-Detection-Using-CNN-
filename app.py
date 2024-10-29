from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg'}

# Load the trained model
model = tf.keras.models.load_model('cnn_plant_disease_model.keras')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_image(filepath):
    img = image.load_img(filepath, target_size=(128, 128))  # Adjust target size if needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize if model requires
    return img_array

# Updated class names without underscores
disease_names = [
    "Apple Apple scab", "Apple Black rot", "Apple Cedar apple rust", "Apple healthy",
    "Blueberry healthy", "Cherry Powdery mildew", "Cherry healthy",
    "Corn Cercospora leaf spot Gray leaf spot", "Corn Common rust", "Corn Northern Leaf Blight", "Corn healthy",
    "Grape Black rot", "Grape Esca (Black Measles)", "Grape Leaf blight (Isariopsis Leaf Spot)", "Grape healthy",
    "Orange Haunglongbing (Citrus greening)", "Peach Bacterial spot", "Peach healthy",
    "Pepper bell Bacterial spot", "Pepper bell healthy", "Potato Early blight", "Potato Late blight", "Potato healthy",
    "Raspberry healthy", "Soybean healthy", "Squash Powdery mildew", "Strawberry Leaf scorch", "Strawberry healthy",
    "Tomato Bacterial spot", "Tomato Early blight", "Tomato Late blight", "Tomato Leaf Mold",
    "Tomato Septoria leaf spot", "Tomato Spider mites Two-spotted spider mite", "Tomato Target Spot",
    "Tomato Yellow Leaf Curl Virus", "Tomato mosaic virus", "Tomato healthy"
]

def predict_disease(filepath):
    img_array = preprocess_image(filepath)
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction, axis=1)[0]
    disease = disease_names[class_index]
    return disease

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
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Predict disease based on the uploaded image
        disease = predict_disease(filepath)

        # Return JSON response with filename and disease
        return {
            "filename": filename,
            "disease": disease
        }, 200
    else:
        flash('Allowed image types are .jpg and .jpeg')
        return redirect(request.url)

@app.route('/result/<filename>')
def result(filename):
    # Retrieve disease name from URL parameters
    disease = request.args.get('disease', 'Unknown')
    return render_template('result.html', filename=filename, disease=disease)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)

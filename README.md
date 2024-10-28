# Plant Disease Classification


## Overview

The **Plant Disease Classification** project leverages Convolutional Neural Networks (CNNs) to identify plant diseases from images. This innovative tool provides a web application where users can upload crop images and receive instant predictions, aiding farmers and agricultural experts in early disease detection.

## Features

- **Image Classification**: Utilizes a state-of-the-art CNN architecture to classify various plant diseases based on uploaded images.
- **Real-time Predictions**: Users can get immediate feedback on the health status of their plants, enabling timely interventions.
- **Web Interface**: A user-friendly Flask web application that streamlines the upload and prediction process, making it accessible for non-technical users.
- **Data Augmentation**: Enhances the training dataset with augmented images for improved model performance.
- **Visualization**: Displays class distribution and feature extraction results, helping to understand model behavior.

## Dataset

The project is trained on the **New Plant Diseases Dataset** (Augmented) from [Kaggle](https://www.kaggle.com/datasets/). This dataset includes a wide variety of images of healthy and diseased plants, organized into classes for different diseases.

### Structure

The dataset is structured into the following directories: '''/New Plant Diseases Dataset(Augmented)/ ├── train/ │ ├── Apple___Apple_scab/ │ ├── Apple___Black_rot/ │ ├── Apple___Cedar_apple_rust/ │ ├── Apple___healthy/ │ ├── Blueberry___healthy/ │ ├── Cherry___Powdery_mildew/ │ ├── Cherry___healthy/ │ ├── Corn___Cercospora_leaf_spot_Gray_leaf_spot/ │ ├── Corn___Common_rust/ │ ├── Corn___Northern_Leaf_Blight/ │ ├── Corn___healthy/ │ ├── Grape___Black_rot/ │ ├── Grape___Esca_(Black_Measles)/ │ ├── Grape___Leaf_blight_(Isariopsis_Leaf_Spot)/ │ ├── Grape___healthy/ │ ├── Orange___Haunglongbing_(Citrus_greening)/ │ ├── Peach___Bacterial_spot/ │ ├── Peach___healthy/ │ ├── Pepper_bell___Bacterial_spot/ │ ├── Pepper_bell___healthy/ │ ├── Potato___Early_blight/ │ ├── Potato___Late_blight/ │ ├── Potato___healthy/ │ ├── Raspberry___healthy/ │ ├── Soybean___healthy/ │ ├── Squash___Powdery_mildew/ │ ├── Strawberry___Leaf_scorch/ │ ├── Strawberry___healthy/ │ ├── Tomato___Bacterial_spot/ │ ├── Tomato___Early_blight/ │ ├── Tomato___Late_blight/ │ ├── Tomato___Leaf_Mold/ │ ├── Tomato___Septoria_leaf_spot/ │ ├── Tomato___Spider_mites_Two-spotted_spider_mite/ │ ├── Tomato___Target_Spot/ │ ├── Tomato___Yellow_Leaf_Curl_Virus/ │ ├── Tomato___mosaic_virus/ │ └── Tomato___healthy/ └── valid/ ├── Apple___Apple_scab/ ├── Apple___Black_rot/ ├── Apple___Cedar_apple_rust/ ├── Apple___healthy/ ├── Blueberry___healthy/ ├── Cherry___Powdery_mildew/ ├── Cherry___healthy/ ├── Corn___Cercospora_leaf_spot_Gray_leaf_spot/ ├── Corn___Common_rust/ ├── Corn___Northern_Leaf_Blight/ ├── Corn___healthy/ ├── Grape___Black_rot/ ├── Grape___Esca_(Black_Measles)/ ├── Grape___Leaf_blight_(Isariopsis_Leaf_Spot)/ ├── Grape___healthy/ ├── Orange___Haunglongbing_(Citrus_greening)/ ├── Peach___Bacterial_spot/ ├── Peach___healthy/ ├── Pepper_bell___Bacterial_spot/ ├── Pepper_bell___healthy/ ├── Potato___Early_blight/ ├── Potato___Late_blight/ ├── Potato___healthy/ ├── Raspberry___healthy/ ├── Soybean___healthy/ ├── Squash___Powdery_mildew/ ├── Strawberry___Leaf_scorch/ ├── Strawberry___healthy/ ├── Tomato___Bacterial_spot/ ├── Tomato___Early_blight/ ├── Tomato___Late_blight/ ├── Tomato___Leaf_Mold/ ├── Tomato___Septoria_leaf_spot/ ├── Tomato___Spider_mites_Two-spotted_spider_mite/ ├── Tomato___Target_Spot/ ├── Tomato___Yellow_Leaf_Curl_Virus/ ├── Tomato___mosaic_virus/ └── Tomato___healthy/'''


## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/eliot-99/Plant-Disease-Detection-Using-CNN-.git
   cd plant-disease-classification

##Install required packages:


pip install -r requirements.txt
Download the dataset from Kaggle and place it in the specified directory structure.

##Run the application:

python app.py
Access the web application in your browser at http://127.0.0.1:5000.

##Usage
Navigate to the home page.
Upload an image of a plant.
View the predicted disease and additional information about the plant's health.
Conclusion
This project assists farmers and agricultural experts in early disease detection, promoting healthier crops and more efficient farming practices. By harnessing the power of machine learning and computer vision, the Plant Disease Classification tool represents a significant advancement in agricultural diagnostics.

##License
This project is licensed under the MIT License - see the LICENSE file for details.

##Acknowledgments
Kaggle for providing the dataset.
Flask for the web framework.
TensorFlow for the deep learning library.



This README provides all the essential information needed for installation, usage, and acknowledgments. Let me know if you need further adjustments!

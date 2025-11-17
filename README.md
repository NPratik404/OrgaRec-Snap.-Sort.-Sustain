OrgaRec: The AI-Powered Waste Classifier

Tagline: Smart sorting for a greener planet.

OrgaRec is a deep learning project that intelligently classifies common household waste into two categories: Organic or Recyclable. This tool leverages a Convolutional Neural Network (CNN) to analyze user-uploaded images and provide instant sorting recommendations, aiming to reduce recycling contamination and promote sustainable habits.

🚀 Project Overview

The core of this project is a CNN model built and trained using TensorFlow and Keras. The model was trained on a binary dataset of waste images, utilizing data augmentation techniques (like rotation, zoom, and flipping) to build a robust classifier that can generalize well to new, unseen images.

This repository includes the complete, user-facing application built with Streamlit. This simple web app provides an intuitive interface where a user can upload a photo of a waste item and receive an immediate, real-time classification.

🛠️ Technology Stack

Model Development: Python, TensorFlow (Keras)

Web Application: Streamlit

Core Libraries: NumPy, Pillow (for image processing)

✨ Features

Deep Learning Model: A trained CNN (my_model.h5) that serves as the classification engine.

Interactive Web App: A user-friendly Streamlit application (app.py) for easy interaction.

Real-Time Predictions: Upload any 'jpg', 'jpeg', or 'png' image and get an instant classification.

Simple & Scalable: The architecture is clean, making it easy to understand, modify, and potentially retrain with more categories.

📁 How It Works

The user visits the Streamlit web app.

They upload an image of a waste item.

The app.py script opens the image using Pillow, resizes it to 150x150 pixels, and normalizes the pixel values (dividing by 255.0) to match the model's training format.

This preprocessed image is fed into the loaded my_model.h5 model.

The model returns a probability score, which the app translates into a clear "Organic" or "Recyclable" prediction for the user.

🏁 How to Run This Project

Clone the repository:

git clone [https://github.com/your-username/OrgaRec.git](https://github.com/your-username/OrgaRec.git)
cd OrgaRec


Install the required libraries:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


Open your browser to the local URL provided by Streamlit and start sorting!

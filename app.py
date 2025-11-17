import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- 1. Load your Keras model ---
# This replaces the pickle.load() line from your example
# Make sure 'my_model.h5' is in the same folder
try:
    model = tf.keras.models.load_model('wasteclassification_model.keras')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# --- 2. Define the class names ---
# Check your training `class_indices` to ensure the order is correct
# E.g., if 0=organic, 1=recyclable
CLASS_NAMES = ['Organic', 'Recyclable']

st.title('Organic or Recyclable?')
st.write("Upload an image of waste to classify it.")

# --- 3. Get image from user ---
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # --- 4. Preprocess the image ---
    # This is the main difference from your example
    
    # Open and resize the image
    image = Image.open(uploaded_file)
    # model expects 244x244 RGB images
    image = image.resize((244, 244))
    
    # Convert to numpy array and rescale (like in training)
    image_array = np.array(image) / 255.0
    
    # Handle grayscale/RGBA images
    if len(image_array.shape) == 2: # Grayscale
        image_array = np.stack((image_array,) * 3, axis=-1)
    if image_array.shape[2] == 4: # RGBA
        image_array = image_array[:, :, :3]
        
    # Create a batch of 1
    image_batch = np.expand_dims(image_array, axis=0)

    # --- 5. Make a prediction ---
    prediction = model.predict(image_batch)  # likely shape (1, 2)

    # If model outputs two probabilities (one per class), pick the class with highest score
    pred_probs = prediction[0]
    pred_index = int(np.argmax(pred_probs))
    predicted_class = CLASS_NAMES[pred_index]
    confidence = float(pred_probs[pred_index]) * 100
        
    st.success(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}%")
    
    # Display the image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
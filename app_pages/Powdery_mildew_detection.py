import os
import sys
import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np
import logging
import matplotlib.pyplot as plt
from PIL import Image

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get model path from environment variable or use default path
model_path = os.getenv("MODEL_PATH", "jupyter_notebooks/outputs/v1/cherry_leaves_model.keras")

# Log the model path
logging.info(f"Model path: {model_path}")

# Function to load the trained model
def load_model():
    logging.info("Loading the model...")
    
    if os.path.isfile(model_path):
        try:
            logging.info("Model file found. Loading the model...")
            model = tf.keras.models.load_model(model_path)
            logging.info("Model loaded successfully.")
            return model
        except Exception as e:
            logging.error(f"Failed to load the model. Error: {e}")
            st.error(f"Failed to load the model. Error: {e}")
            return None
    else:
        if os.path.exists(model_path):
            error_message = "The path exists but is not a file. Please check the model file path."
        else:
            error_message = "Model file not found. Please check the model file path."
        
        logging.error(error_message)
        st.error(error_message)
        return None

# Example call to the function
model = load_model()

# Function to predict image class
def predict_image_class(image_array, model):
    logging.info("Predicting image class...")
    labels = ["healthy", "powdery_mildew"]
    img_array = np.expand_dims(image_array, axis=0) / 255.0
    pred_proba = model.predict(img_array)[0]
    predicted_class_index = np.argmax(pred_proba)
    predicted_class = labels[predicted_class_index]
    pred_probability = pred_proba[predicted_class_index]
    logging.info(f"Image class prediction: {predicted_class}, Probability: {pred_probability}")
    return predicted_class, pred_probability

# Function to check if image is a leaf
def is_leaf(image_array):
    logging.info("Checking if image is a leaf...")
    # Placeholder logic to determine if the image is a leaf
    aspect_ratio = image_array.shape[0] / image_array.shape[1]
    if aspect_ratio < 0.8 or aspect_ratio > 1.2:
        logging.info("Aspect ratio does not indicate a leaf.")
        return False
    
    green_pixels = np.mean(image_array[:, :, 1] / 255.0)
    if green_pixels < 0.2:
        logging.info("Not enough green pixels, image is not a leaf.")
        return False
    
    logging.info("Image identified as a leaf.")
    return True

# Streamlit app
def main():
    st.title("Powdery Mildew Detection App")

    # Load the model
    logging.info("Initializing the application...")
    model = load_model()
    if model is None:
        st.error("Failed to load the model. Please check the model file path.")
        return

    # File uploader
    uploaded_files = st.file_uploader("Choose up to 10 images...", accept_multiple_files=True, type=["jpg", "jpeg", "png"], key="fileuploader")

    if uploaded_files:
        results = []
        for uploaded_file in uploaded_files[:10]:
            # Convert the uploaded file to image array
            logging.info(f"Processing uploaded file: {uploaded_file.name}")
            img = Image.open(uploaded_file)
            img = img.resize((256, 256))
            img_array = keras_image.img_to_array(img)

            # Check if image is a leaf
            if not is_leaf(img_array):
                logging.info("Image could not be identified as a leaf.")
                result = (uploaded_file.name, "Image could not be identified as a leaf.", "")
            else:
                # Predict the class
                logging.info("Predicting image class...")
                predicted_class, pred_probability = predict_image_class(img_array, model)
                result = (uploaded_file.name, predicted_class, f"{pred_probability:.4f}")

            results.append(result)

        # Convert results to DataFrame
        results_df = pd.DataFrame(results, columns=["Image Name", "Predicted Class", "Predicted Probability"])

        # Display results table
        st.table(results_df)

        # Button to download the results
        if st.button("Download Results"):
            # Save results to CSV file
            results_df.to_csv("predictions.csv", index=False)
            st.success("Results downloaded successfully. You can find them in 'predictions.csv'.")

# Run the app
if __name__ == "__main__":
    main()

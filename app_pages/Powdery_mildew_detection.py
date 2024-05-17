import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np
import os
import io
import tensorflow as tf

# Function to load the trained model
def load_model():
    model_path = '/workspace/project5_cherryleaves/jupyter_notebooks/outputs/v1/cherry_leaves_model.keras'
    model = tf.keras.models.load_model(model_path)  # This line loads the entire SavedModel directory
    return model
    
# Function to predict image class
def predict_image_class(image_array, model):
    labels = ["healthy", "powdery_mildew"]
    img_array = np.expand_dims(image_array, axis=0) / 255
    pred_proba = model.predict(img_array)[0]
    predicted_class_index = np.argmax(pred_proba)
    predicted_class = labels[predicted_class_index]
    pred_probability = pred_proba[predicted_class_index]
    
    if predicted_class == "healthy":
        print("Image has healthy leaves.")
    elif predicted_class == "powdery_mildew":
        print("Image has powdery mildew.")
    else:
        print("Image could not be identified.")
    
    return predicted_class, pred_probability

# Function to check if image is a leaf
def is_leaf(image_array):
    # Placeholder logic to determine if the image is a leaf
    # For example, you can check the aspect ratio, color distribution, etc.
    # Here, we're just checking if the image array shape matches a typical leaf image shape
    return image_array.shape == (256, 256, 3)

# Streamlit app
def main():
    st.title("Powdery Mildew Detection App")

    # Load the model
    model = load_model()

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Classifying...")

        # Convert the uploaded file to image array
        img = keras_image.load_img(uploaded_file, target_size=(256, 256))
        img_array = keras_image.img_to_array(img)  # Define img_array here

        # Check if image is a leaf
        is_leaf_image = is_leaf(img_array)

        # Display image shape
        st.write(f"Image Shape: {img_array.shape}")

        # Check if image is a leaf
        if not is_leaf_image:
            print("Image could not be identified as a leaf.")
            st.write("Image could not be identified as a leaf.")
            return

        # Predict the class
        predicted_class, pred_probability = predict_image_class(img_array, model)

        # Display the result
        st.write(f"Predicted Class: {predicted_class}")
        st.write(f"Predicted Probability: {pred_probability:.4f}")

        # Check if the predicted class is not a leaf
        if predicted_class != "healthy" and predicted_class != "powdery_mildew":
            st.write("Image could not be identified.")

# Run the app
if __name__ == "__main__":
    main()

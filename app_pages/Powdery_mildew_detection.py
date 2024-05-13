import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
os.chdir('/workspace/project5_cherryleaves/jupyter_notebooks/')


# Function to load the trained model
def load_model():
    model_path = '/workspace/project5_cherryleaves/jupyter_notebooks/outputs/v1/cherry_leaves_model.keras'
    model = tf.keras.models.load_model(model_path)
    return model

# Function to predict image class
def predict_image_class(image_path, model):
    labels = ["healthy", "powdery_mildew"]
    img = image.load_img(image_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255
    pred_proba = model.predict(img_array)[0]
    predicted_class_index = np.argmax(pred_proba)
    predicted_class = labels[predicted_class_index]
    pred_probability = pred_proba[predicted_class_index]
    return predicted_class, pred_probability

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

        # Save the uploaded file to a temporary directory
        temp_dir = "temp_images"
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Predict the class
        predicted_class, pred_probability = predict_image_class(temp_file_path, model)

        # Display the result
        st.write(f"Predicted Class: {predicted_class}")
        st.write(f"Predicted Probability: {pred_probability:.4f}")

# Run the app
if __name__ == "__main__":
    main()

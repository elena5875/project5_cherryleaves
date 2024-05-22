import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np

# Function to load the trained model
def load_model():
    model_path = 'outputs/v1/cherry_leaves_model.keras'  
    model = tf.keras.models.load_model(model_path)
    return model

    
# Function to predict image class
def predict_image_class(image_array, model):
    labels = ["healthy", "powdery_mildew"]
    img_array = np.expand_dims(image_array, axis=0) / 255
    pred_proba = model.predict(img_array)[0]
    predicted_class_index = np.argmax(pred_proba)
    predicted_class = labels[predicted_class_index]
    pred_probability = pred_proba[predicted_class_index]
    
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
    uploaded_files = st.file_uploader("Choose up to 10 images...", accept_multiple_files=True, type=["jpg", "jpeg", "png"], key="fileuploader")

    if uploaded_files:
        results = []
        for uploaded_file in uploaded_files[:10]:
            # Convert the uploaded file to image array
            img = keras_image.load_img(uploaded_file, target_size=(256, 256))
            img_array = keras_image.img_to_array(img)  # Define img_array here

            # Check if image is a leaf
            is_leaf_image = is_leaf(img_array)

            # Check if image is a leaf
            if not is_leaf_image:
                result = ("Image could not be identified as a leaf.", "", "")
            else:
                # Predict the class
                predicted_class, pred_probability = predict_image_class(img_array, model)
                result = (uploaded_file.name, predicted_class, f"{pred_probability:.4f}")

            results.append(result)

        # Convert results to DataFrame
        results_df = pd.DataFrame(results, columns=["Image Name", "Predicted Class", "Predicted Probability"])

        # Display results table
        st.table(results_df)

        # Button to download or print the results
        if st.button("Download/Print Results"):
            # Save results to CSV file
            with st.spinner("Downloading..."):
                results_df.to_csv("predictions.csv", index=False)
            st.success("Results downloaded successfully. You can find them in 'predictions.csv'.")

# Run the app
if __name__ == "__main__":
    main()

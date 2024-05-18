import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def page5_function(losses):
    st.title("Summary")
        
    st.subheader("Model Training Results:")
    st.write("The machine learning model showed positive results with minimal accuracy loss as depicted in the table below.")
    st.write(losses)

    st.subheader("Model Training Accuracy Plot")
    # Plotting model training accuracy
    fig, ax = plt.subplots()
    sns.set_style("whitegrid")
    losses[['accuracy', 'val_accuracy']].plot(ax=ax, style='.-')
    ax.set_title("Accuracy")
    st.pyplot(fig)

    st.subheader("Model Training Losses Plot")
    # Plotting model training losses
    fig, ax = plt.subplots()
    sns.set_style("whitegrid")
    losses[['loss', 'val_loss']].plot(ax=ax, style='.-')
    ax.set_title("Loss")
    st.pyplot(fig)

    st.subheader("Code Snippets:")
    st.write("Plotting model training accuracy:")
    st.code("""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("\nPlotting model training accuracy...")
losses[['accuracy', 'val_accuracy']].plot(style='.-')
plt.title("Accuracy")
plt.savefig('outputs/v1/model_training_acc.png', bbox_inches='tight', dpi=150)
plt.show()
""", language="python")

    st.write("Plotting model training losses:")
    st.code("""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("\nPlotting model training losses...")
losses[['loss', 'val_loss']].plot(style='.-')
plt.title("Loss")
plt.savefig('outputs/v1/model_training_losses.png', bbox_inches='tight', dpi=150)
plt.show()
""", language="python")

    st.write("""The machine learning model exhibits commendable accuracy in distinguishing between cherry leaves infected with powdery mildew and healthy ones, even when confronted with unclear images. This high accuracy underscores the effectiveness of the model in identifying subtle manifestations of powdery mildew on cherry leaves.

However, there remains a significant area for improvement as the model struggles with the task of verifying whether the uploaded image indeed contains a cherry leaf. This indicates a need more test and training to enhance the model's ability to accurately distinguish between images of cherry leaves and other objects.

Therefore, while the model demonstrates promising performance in detecting powdery mildew, there is still  room for improvement in its leaf identification capabilities.""")


# Sample data (losses) should be provided when calling page5_function
# page5_function(losses)

# Cherry Leaves ML Project

## Business Requirements

       The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

       To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

       - 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
       - 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

       To identify the mildew leaves.
       The primary goal for this project is to distinguish the difference between a healthy leaves and a mildew one. Data visualization can help understand the pattern in understanding the visual patterns and features associated with healthy and diseased leaves.

       To be able to improve efficiency
       Machine learning can help in automating the identification process, reducing the time and resources required for manual inspections.

       To be able to use in different crop disease detection
       This Machine learning might also be a help in detecting diseases or pests that is affecting the cherry trees. 


##  The Hypothesis and How to validate?

       - Hypothesis:
       By creating a  machine learning algorithms, it is possible to develop a model capable of accurately distinguishing between healthy cherry leaves and leaves affected by powdery mildew based on distinct visual features. It is believe  that  with these characteristics value such as color, texture, and patterns it will be able to discern the differences between healthy and infected leaves, enabling the ML to classify images with high accuracy.

       Validation:
       To validate our hypothesis, we will undertake the following steps:

       1. Data Collection: Collect different dataset consisting of images for both healthy cherry leaves and leaves affected with powdery mildew. This is to ensure that the dataset encompasses various stages of infection and environmental conditions to enhance the accuracy of the model.

       2. Data Preprocessing: Process the collected images to standardize their format, resolution, and orientation. Additionally, perform preprocessing techniques such as augmentation to enhance the model's ability to generalize across different samples.

       3. Model Development: Design the model to learn discriminative features from the input images and make accurate predictions regarding leaf health status.

       4. Training and Validation:  Train the model on the training data while looking at the  performance on the validation set. Adjust hyperparameters and network architecture as necessary to optimize model performance.

       5. Evaluation: Assess the trained model's performance using the reserved testing set. Measure key metrics such as accuracy, and F1-score to quantify the model's ability to correctly classify healthy and infected leaves.


       By  following these steps, we aim to validate our hypothesis and demonstrate the accuracy of using machine learning algorithms for  detection of powdery mildew in cherry leaves in a fast way.

## ML Business Case

       To be able to implement a machine learning solution that utilizes image classification techniques to differentiate between healthy cherry leaves and those infected with powdery mildew. The solution will involve the following steps:

       1. Data Collection. Gather a diverse dataset collection between healthy leaves and powdery mildew leaves of the Cherry Trees. It should be from different angle, lighting conditions and of differenct stages of the disease, powdery mildew.

       2. Data Processing. We process the dataset by cleaning and preprocessing it. We also try to enhance the quality of the images and the consistency of the dataset. This might involve augmentation and resizing techniques to improve the quality of the dataset. 

       3. Model Development. Train the machine learning model, such as CNN ( Convulutional Nueral Network), on the proprocessed data. This is so that it optimize the model architecture and hyperparameters to maximize accuracy and minimize overfitting.

       4. Model Evaluation. validate the train model using datasets to assess its performance in accurately classifying cherry leaves as healthy or infected. Metrics such as accuracy, precision, recall, and F1-score will be used to evaluate model performance. It needs to pass the criteria of 97% accuracy.

       5. Deployment. Create a web interface to interate the trained machine learning model for capturing and analyzing the leaf images. This platform should be a user friendly and easily accessible to the workers in the field.

## Expected Outcome
       1. Accuracy Enhancement. The machine learning model is expected to have a high accuracy level in determining if the leaves have mildew or not.

       2. Efficiency Improvement. By doing automation in detecting the disease it saves time in inspecting every tree on the field all the time. The model should be able to shorten the time in inspecting the cherry leaves.

       4. Cost Saving. The business will be able to save time and labor with this model. 

## Dataset Content

       - The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
       - The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.


## Dashboard Design

### The dashboard 
       You should see in the dashboard the following:

       PAGE 1 A project summary page, explaining the concept of the ML app and why this is being done.

       PAGE 2 A page indicating your project hypothesis and how you validated it across the project.A page where the user can see an image showing the difference between a healthy cherry leaves to a powdery mildew leaves

       PAGE 3 A page where the user can see 2 images showing the difference between a healthy cherry leaves to a powdery mildew leaves
       The user also has a change to download some pictures from kaggle as a source of reference and later on can be used to test the ML app.

       PAGE 4 The user can upload an image and the ML should be able to determine if the image is healthy or has mildew.
       The user can also see the table of the image name and the classification of the leaf. Once the user is done the user has the option to download it or print it.

       PAGE 5 A page indicating your project hypothesis and how you validated it across the project.
       A technical page displaying your model performance.






## How to use this repo

       1. Use this template to create your GitHub project repo

       2. Log in to Gitpod with your GitHub account.

       3. On your Dashboard, click on the New Workspace button

       4. Paste in the URL you copied from GitHub earlier

       5. Click Create

       6. Wait for the workspace to open. This can take a few minutes.

       7. Open a new terminal and `pip3 install -r requirements.txt`

       8. Open the jupyter_notebooks directory with this code ' jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser ' copy the token code and click the browser button. 

       9. Paste the token code and click openlogin
 
       10. Choose the notebook you want to open

       11. Click the kernel button and choose Python Environments. Also don't forget to click and choose trusted.


## Unfixed Bugs
       1.I tried to create another machine learning for the ML app wherein the ML app can also detect if the image is a leaf or not. But has been unsuccessful.
       
       2.Deploying the ML app to heroku. For days I have been trying to deploy my ML app in Heroku and it seems to sometimes work sometimes not. 
       
       3.For Some reason when I run my ML app locally everything works fine but if I run my app in Heroku. Heroku has decided that SavedModel file does not exist at: jupyter_notebooks/outputs/v1/cherry_leaves_model.keras/{saved_model.pbtxt|saved_model.pb}. I tried everything however nothing is working until the deadline.

## Deployment

### Heroku

       - The App live link is: `https://cherryleaves5904-854d3ae19318.herokuapp.com/`
       - runtime.txt is python-3.8.19 and I used Heroku 20


       I deployed the repository in Heroku

       I used the toolbelt CLI in gitpod and did the following:

       1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
       2. Scroll down to the _API Key_ and click _Reveal_
       3. Copy the key
       4. In the terminal. type in heroku login -i
       5. Give the email and password. Password should be the API key: HRKU-3e5a6715-3b88-4520-b0b8-bc3aa1e90124
       6. once done write heroku git:remote -a cherryleaves5904
       7. Write: git push heroku main
       8. Write: heroku open


## Main Data Analysis and Machine Learning Libraries
       Libraries I used
       - tensorflow-cpu 2.6.0  used for creating the model
       - numpy 1.19.2          used for converting to array 
       - scikit-learn 0.24.2   used for evaluating the model
       - streamlit 0.85.0      used for creating the dashboard
       - pandas 1.1.2          used for creating/saving as dataframe
       - matplotlib 3.3.1      used for plotting the sets' distribution
       - keras 2.6.0           used for setting model's hyperparamters
       - plotly 5.12.0         used for plotting the model's learning curve 
       - seaborn 0.11.0        used for plotting the model's confusion matrix
       - streamlit             used for creating and sharing this project's interface
## Credits and References

       https://github.com/GyanShashwat1611/WalkthroughProject01/blob/main/jupyter_notebooks/02%20-%20DataVisualization.ipynb
       https://joblib.readthedocs.io/en/latest/index.html
       https://matplotlib.org/stable/api/figure_api.html
       https://docs.python.org/3/library/os.html#querying-the-size-of-a-terminal
       https://devcenter.heroku.com/categories/command-line
       https://stackoverflow.com/
       https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves.git
       https://discuss.streamlit.io/t/streamlit-app-works-locally-but-not-on-heroku/14772


### Content
       The content of the Multipage, Hypothesis and Summary were partly reference on the following website

       https://en.wikipedia.org/wiki/Powdery_mildew
       https://www.gardendesign.com/how-to/powdery-mildew.html

### Media

My dataset photOs were provided by https://www.kaggle.com/codeinstitute/cherry-leaves

### Acknowledgements 
       I would just like to thank myself for being patient  and not trying to kill the following apps. CodeAnywhere, Gitpod and most specially Heroku. 
       I know I might encounter them again but I think I have the patience and the tools to not go crazy when working with them. Sorry just need to vent it out here.



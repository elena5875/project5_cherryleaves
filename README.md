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

- There are distinguishable different features to see the difference between a healthy cherry leaves and on with mildew. With this in mind we can create a Machine learning Algorithm wherein it can detect the difference between a healthy leaves and mildew just by present the picture. 


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

### The dashboard should contain the following:
A project summary page, showing the dataset summary and the client's requirements
A page where the user can see an image showing the difference between a healthy cherry leaves to a powdery mildew leaves

The user can upload an image and the ML should be able to determine if the image is healthy or has mildew.
A table with the image name and prediction results, and a download button to download the table.
A page indicating your project hypothesis and how you validated it across the project.
A technical page displaying your model performance.


- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Deployment


## How to use this repo

1. Use this template to create your GitHub project repo

2. Log into your cloud IDE with your GitHub account.

3. On your Dashboard, click on the New Workspace button

4. Paste in the URL you copied from GitHub earlier

5. Click Create

6. Wait for the workspace to open. This can take a few minutes.

7. Open a new terminal and `pip3 install -r requirements.txt`

8. Open the jupyter_notebooks directory with this code ' jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser ' copy the token code and click the browser. Paste the token code and click openlogin
 
9. Choose the notebook you want to open

1. Click the kernel button and choose Python Environments. Also don't forget to click and choose trusted.

Note that the kernel says Python 3.8.18 as it inherits from the workspace, so it will be Python-3.8.18 as installed by our template. To confirm this, you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, then you can create a new one with _Regenerate API Key_.

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.


### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.

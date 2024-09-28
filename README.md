# Heart Disease Level Prediction

This repository contains the code and model for predicting heart disease severity levels using machine learning. The project aims to provide a user-friendly interface to input health data and predict whether a person has heart disease or not.

## Files in this Repository

1. **Model_creation.ipynb**  
   This Jupyter notebook contains the steps for training the machine learning model that predicts heart disease. It includes data preprocessing, model training, and evaluation steps. The notebook also explores various features and model accuracy.

2. **app.py**  
   This is the main application file for the Streamlit interface. The app allows users to:
   - Input personal health data to predict the likelihood of heart disease.
   
   It contains a mode for heart disease prediction:
   - **Heart Disease Prediction**: Users input health data (age, cholesterol, etc.) to predict the severity of heart disease.

3. **heart_disease_model.pkl**  
   This file contains the pre-trained machine learning model for predicting heart disease. It is loaded in the Streamlit app to make predictions based on user input.

## Model Accuracy and Performance

The model achieved an accuracy of **80%** during testing. Below is the classification report detailing :
```bash
            precision   recall   F1-score    support 
       0       0.76      0.84      0.79        85
       1       0.71      0.57      0.63        81
       2       0.75      0.85      0.80        72
       3       0.81      0.83      0.82        84
       4       0.96      0.92      0.94        89

accuracy                           0.80       411
macro avg      0.80      0.80      0.80       411 
weighted avg   0.80      0.80      0.80       411
```

## How to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/heart-disease-level.git
  ```
2.Navigate to the project directory:
   ```bash
    cd heart-disease-level
   ```
3.Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.Run the Streamlit app:
```bash
streamlit run app.py
```
## Future Work
- Improving model accuracy through further hyperparameter tuning.
- Adding more health metrics to improve the prediction model.

# Fraud-Detection
# Fraud-Detection-Logistic-Regression
Using credit card data to classify fradulent transactions. Based on [this](https://www.kaggle.com/c/ieee-fraud-detection/data) Kaggle dataset. 

# Method:

- SMOTE to balance the the target variable
- PCA to reduce dimensionality
- Recall as loss function to minimise (because we want to minimise false negatives)
- Logistic regression to make predictions

# Issues encountered:

- Computational power
  - Google Colab too low for full dataset
  - Only trained on 20 000 observations
- Hyperparameter tuning
  - Need more computation for grid search
  - Could improve model with gradient descent or genetic algo
- Bias
  - Model is too simple, not enough data used
  - Related to computational power
  - LightGBM or XGBoost would've been better

# Result
Model had ~70% recall on training data.

# API
Next part of the project is to build an API with Stripe (payment) and Firebase (Customer data). The API is fully functional on our local system with a Flask app as the backend.

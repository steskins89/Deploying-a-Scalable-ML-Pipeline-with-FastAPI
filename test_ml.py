import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import compute_model_metrics, train_model
from ml.data import apply_label
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    Use a small dataset to verify the ML model uses a Random Forest Classifier
    """
    X_train = np.array([
       [1, 2],
       [2, 3],
       [3, 4],
       [4, 5],
       [5, 6],
    ])
    y_train = np.array([0, 0, 1, 1, 1])
    
    model = train_model(X_train, y_train)
    
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test compute_model_metrics to verify the function returns the expected values
    """
    y = np.array([0, 1, 1, 0])
    preds = np.array([0, 1, 1, 0])
    
    precision, recall, fbeta = compute_model_metrics(y, preds)
    
    assert precision == 1.0
    assert recall == 1.0
    assert fbeta == 1.0


# TODO: implement the third test. Change the function name and input as needed
def test_apply_label():
    """
    Test the apply_label function to check if salary labels are converted correctly from binary
    """
    assert apply_label([1]) == ">50K"
    assert apply_label([0]) == "<=50K"
    

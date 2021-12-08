import pandas as pd
import getsuperset
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from bson import json_util
from flask import Response
    
def getNeuronal(vectors):
    
    mlr = MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
    mlr.fit(vectors['X_train_norm'], vectors['y_train_norm'])
    
    return mlr
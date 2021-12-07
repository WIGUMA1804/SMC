import pandas as pd
import numpy as np
import getsuperset
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
from bson import json_util
from flask import Response

def minmax_norm(df_input):
    return (df_input - df_input.min()) / ( df_input.max() - df_input.min())
    
def getNeuronal(database):
    
    df = getsuperset.get_superset(database)
    x = df[['MESPAEA_rCurrent_401','SIFOC_sif401_LEC']]
    y = df['MESPAEA_udiEnergyConsumed_401']

    X_train, X_test, y_train, y_test = train_test_split(x,y)
    
    X_train_norm = minmax_norm(X_train)
    y_train_norm = minmax_norm(y_train)
    
    mlr = MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
    mlr.fit(X_train_norm, y_train_norm)
    
    expected_y  = y_test
    predicted_y = mlr.predict(X_test)
    
    prediction = mlr.predict(X_test)
    error = prediction - y_test
    
    r2_score = metrics.r2_score(expected_y, predicted_y)
    mean_squared = metrics.mean_squared_log_error(expected_y, predicted_y)
    mlr_score = mlr.score(X_train_norm, y_train_norm)
    mlr_params = mlr.get_params(deep=True)
    
    data_dict = dict()
    data_dict['r2_score'] = r2_score
    data_dict['mean_squared'] = mean_squared
    data_dict['mlr_score'] = mlr_score
    data_dict['mlr_params'] = mlr_params
    
    data_dict['expected_y'] = expected_y
    data_dict['predicted_y'] = predicted_y

    response = json_util.dumps(data_dict)
    return Response(response, mimetype='application/json')






























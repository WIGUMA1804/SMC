from bson import json_util
from flask import Response
from sklearn import metrics
import numpy as np

def show_results(model, vectors):
    expected_y  = vectors['y_test']
    predicted_y = model.predict(vectors['X_test'])
    error = predicted_y - vectors['y_test']
    
    r2_score = metrics.r2_score(expected_y, predicted_y)
    mean_squared = metrics.mean_squared_log_error(expected_y, predicted_y)
    model_score = model.score(vectors['X_train_norm'], vectors['y_train_norm'])
    model_params = model.get_params(deep=True)
    
    data_dict = dict()
    data_dict['r2_score'] = r2_score
    data_dict['mean_squared'] = mean_squared
    data_dict['model_score'] = model_score
    data_dict['model_params'] = model_params
    
    data_dict['expected_y'] = np.array(expected_y)
    data_dict['predicted_y'] = predicted_y

    response = json_util.dumps(data_dict)
    return Response(response, mimetype='application/json')
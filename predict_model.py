import joblib
from sklearn.neural_network import MLPRegressor
from bson import json_util
from flask import Response

def predict_model(vector):
    mlr1 = joblib.load('mlr_saved.pkl');
    test_vector = vector
    response = mlr1.predict(test_vector)
    
    data_dict = dict()
    data_dict['model'] = response;
    
    resp = json_util.dumps(data_dict)
    return Response(resp, mimetype='application/json')
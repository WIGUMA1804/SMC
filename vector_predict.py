from bson import json_util
from flask import Response

def prediction(model, userVector):
    out = model.predict(userVector)
    
    data_dict = dict()
    data_dict['vector_predict'] = out
    response = json_util.dumps(data_dict)
    return Response(response, mimetype='application/json')
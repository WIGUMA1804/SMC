from flask import Response
from bson import json_util
from flask.json import jsonify
import numpy as np
import pandas as pd
import csv
import getsuperset

def manage_superset(database):

    df = getsuperset.get_superset(database)
    data_dict = dict()
    for col in df.columns:
        data_dict[col] = df[col].values.tolist()
    response = json_util.dumps(data_dict)
    return Response(response, mimetype='application/json')

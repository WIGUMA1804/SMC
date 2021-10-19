from flask import Response
from bson import json_util
from flask.json import jsonify
import numpy as np
import pandas as pd

def minmax_norm(df_input):
    return (df_input - df_input.min()) / (df_input.max() - df_input.min())

def get_collections_superset(database):
    data_SIF_401 = database.db.SIF_401.find()
    data_SIF_402 = database.db.SIF_402.find()
    data_SIF_405 = database.db.SIF_405.find()
    data_SIF_407 = database.db.SIF_407.find()
    data_SIF_408 = database.db.SIF_408.find()
    data_SIF_409 = database.db.SIF_409.find()

    response = json_util.dumps(data_SIF_401)
    return Response(response, mimetype='application/json')
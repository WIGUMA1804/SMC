from flask import Response
from bson import json_util

def get_statistics(collection_name, database):
    if str(collection_name) == 'SIF_401':
        data = database.db.SIF_401.find()
        response = json_util.dumps(data)
        return Response(response, mimetype='application/json')

    if str(collection_name) == 'SIF_402':
        data = database.db.SIF_402.find()
        response = json_util.dumps(data)
        return Response(response, mimetype='application/json')

    if str(collection_name) == 'SIF_405':
        data = database.db.SIF_405.find()
        response = json_util.dumps(data)
        return Response(response, mimetype='application/json')

    if str(collection_name) == 'SIF_407':
        data = database.db.SIF_407.find()
        response = json_util.dumps(data)
        return Response(response, mimetype='application/json')

    if str(collection_name) == 'SIF_408':
        data = database.db.SIF_408.find()
        response = json_util.dumps(data)
        return Response(response, mimetype='application/json')

    if str(collection_name) == 'SIF_409':
        data = database.db.SIF_409.find()
        response = json_util.dumps(data)
        return Response(response, mimetype='application/json')
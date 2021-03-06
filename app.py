import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import regresion
import database
import basic_statistics
import superset
import Estadistica
import regresion
import neuronal
import superset1
import manage_superset
import neuronal_aux
import determine_neuronal
import vector_predict
import predict_model

app = Flask(__name__)
CORS(app)


@app.route('/regression/<collection>/<var1>/<var2>', methods=['GET'])
def estimate_regression(collection, var1, var2):
    return regresion.Regression(collection, var1, var2, database.mongo_connect(app))

# post method to test connection with bd

@app.route('/users', methods=['POST'])
def create_user():
    # Receiving data
    username = request.json['username']
    password = request.json['password']

    print('entra')
    if username and password:
        print('entra if')
        id = database.mongo_connect(app).db.SIF_405.insert(
            {
                'username': username,
                'password': password
            }
        )
        response = {
            'id': str(id),
            'username': username,
            'success': 'success'
        }

        return response
    else:
        {'message': 'received'}

    return {'message': 'received'}

# get method to obtain all information related with a specific collection

@app.route('/data/<collection_name>', methods=['GET'])
def data_collections(collection_name):
    return basic_statistics.get_statistics(collection_name, database.mongo_connect(app))

@app.route('/regresion', methods=['POST'])
def get_regresion():
    inputs = request.json['inputs']
    output = request.json['output']
    data = regresion.Regression(database.mongo_connect(app), inputs, output)
    return data

@app.route('/neuronal', methods=['POST'])
def get_neuronal():
    inputs = request.json['inputs']
    output = request.json['output']
    data = neuronal_aux.show_results(
    neuronal.getNeuronal(determine_neuronal.get_vectors(database.mongo_connect(app), inputs, output)),
    determine_neuronal.get_vectors(database.mongo_connect(app), inputs, output))
    return data


@app.route('/predict', methods=['POST'])
def get_vector_predict():
    inputs = request.json['inputs']
    data = vector_predict.prediction(
    neuronal.getNeuronal(determine_neuronal.get_vectors(database.mongo_connect(app))),
    inputs)
    return data


@app.route('/getsuperset', methods=['GET'])
def get_superset():
    return superset1.superset1(database.mongo_connect(app))

# NUEVO ENDPOINT PARA OBTENER EL SUPERSET
@app.route('/superset', methods=['GET'])
def getsuperset():
    return manage_superset.manage_superset(database.mongo_connect(app))


@app.route('/modelPredict', methods=['POST'])
def getModelSaved():
    vector = request.json['vector']
    return predict_model.predict_model(vector);


if __name__ == "__main__":
    app.run(debug=True)

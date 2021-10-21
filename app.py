import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import regresion
import database
import basic_statistics
import superset
import Estadistica
import regresion
import NN
import superset1
import manage_superset

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


# @app.route('/ ', methods=['GET'])
# def get_superset():
#     # data=superset.get_superset()
#     # df_list=data.values.tolist()
#     # json_data=jsonify(df_list)
#     return superset.get_superset(database.mongo_connect(app))


@app.route('/estadistica', methods=['GET'])
def get_estadistica():
    data = Estadistica.Basic_Stats()
    # df_list=data.values.tolist()
    # json_data=jsonify(df_list)
    return data
# @app.route('/regresion', methods=['GET'])
# def get_regresion():
#     data = regresion.Regression()
#     # df_list=data.values.tolist()
#     # json_data=jsonify(df_list)
#     return data

@app.route('/Neural_Network', methods=['GET'])
def get_NN():
    data = NN.Neural_Network()
    # df_list=data.values.tolist()
    # json_data=jsonify(df_list)
    return data
@app.route('/superset', methods=['GET'])
def get_superset():
    # data=superset.get_superset()
    # df_list=data.values.tolist()
    # json_data=jsonify(df_list)
    return superset1.superset1(database.mongo_connect(app))

# @app.route('/superset', methods=['GET'])
# def get_collections():
#     return manage_superset.get_collections_superset(database.mongo_connect(app))
#     # data.headers.add('Access-Control-Allow-Origin', '*')
#     # return data

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request
from flask_cors import CORS
import regresion
import database
import basic_statistics

app = Flask(__name__)
CORS(app)

@app.route('/regression', methods=['GET'])
def estimate_regression():
    return regresion.Regression()

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

if __name__ == "__main__":
    app.run(debug=True)
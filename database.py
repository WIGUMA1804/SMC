from flask_pymongo import PyMongo

def mongo_connect(app):
    app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@smcsifoccluster.poz4u.mongodb.net/SMC_SIFOC?retryWrites=true&w=majority'
    mongo = PyMongo(app)
    return mongo
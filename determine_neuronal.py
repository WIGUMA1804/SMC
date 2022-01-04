import numpy as np
import getsuperset
from sklearn.model_selection import train_test_split
    
def get_vectors(database, inputs, output):
    
    df = getsuperset.get_superset(database)
    print(inputs);
    x = df[inputs]
    y = df[output]

    X_train, X_test, y_train, y_test = train_test_split(x,y)
    
    data_dict = dict()
    data_dict['X_train'] = X_train
    data_dict['y_train'] = y_train
    data_dict['X_test'] = X_test
    data_dict['y_test'] = y_test
    
    return data_dict

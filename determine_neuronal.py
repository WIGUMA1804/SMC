import numpy as np
import getsuperset
from sklearn.model_selection import train_test_split

def minmax_norm(df_input):
    return (df_input - df_input.min()) / ( df_input.max() - df_input.min())
    
def get_vectors(database):
    
    df = getsuperset.get_superset(database)
    x = df[['MESPAEA_rCurrent_401','SIFOC_sif401_LEC']]
    y = df['MESPAEA_udiEnergyConsumed_401']

    X_train, X_test, y_train, y_test = train_test_split(x,y)
    
    X_train_norm = minmax_norm(X_train)
    y_train_norm = minmax_norm(y_train)
    
    data_dict = dict()
    data_dict['X_train'] = X_train
    data_dict['X_test'] = X_test
    data_dict['y_train'] = y_train
    data_dict['y_test'] = y_test
    data_dict['X_train_norm'] = X_train_norm
    data_dict['y_train_norm'] = y_train_norm
    
    return data_dict

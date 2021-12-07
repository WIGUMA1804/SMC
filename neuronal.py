import pandas as pd
import numpy as np
import getsuperset
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn import metrics

def minmax_norm(df_input):
    return (df_input - df_input.min()) / ( df_input.max() - df_input.min())
    
def getNeuronal(database):
    
    # data_SIF_401=pd.read_csv("C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_401.csv")
    # x = data_SIF_401[['MESPAEA_rCurrent_401','SIFOC_sif401_LEC']]
    # y =data_SIF_401['MESPAEA_udiEnergyConsumed_401']
    
    df = getsuperset.get_superset(database)
    x = df[['MESPAEA_rCurrent_401','SIFOC_sif401_LEC']]
    y = df['MESPAEA_udiEnergyConsumed_401']

    X_train, X_test, y_train, y_test = train_test_split(x,y)
    
    X_train_norm = minmax_norm(X_train)
    y_train_norm = minmax_norm(y_train)
    
    mlr = MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
    mlr.fit(X_train_norm, y_train_norm)
    
    #graficar,se deben enviar por el json
    expected_y  = y_test
    predicted_y = mlr.predict(X_test)
    
    prediction = mlr.predict(X_test)
    error = prediction - y_test
    
    #se debe enviar
    print(metrics.r2_score(expected_y, predicted_y))
    print(metrics.mean_squared_log_error(expected_y, predicted_y))
    print(mlr.score(X_train_norm, y_train_norm))
    print(mlr.get_params(deep=True))





























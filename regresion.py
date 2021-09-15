import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import matplotlib.pyplot as plt
def Regression(collection,var1,var2):

    datos= "C:\DOCTORADO\SEMESTRE 7\PASANTIA\DATOS\AGOSTO-10-2021_1\{}".format(collection)+".csv"
    print(datos)
    print(collection)
    print(var1)
    print(var2)
    data=pd.read_csv(datos)
    data.head()
    print(data.head())
    X = data[var1]
    y = data[var2]

    X_train, X_test, y_train, y_test = train_test_split(
                                            X.values.reshape(-1,1),
                                            y.values.reshape(-1,1),
                                            train_size   = 0.8,
                                            random_state = 1234,
                                            shuffle      = True
                                        )
    print(X_train)      
    X_train = sm.add_constant(X_train, prepend=True)
    modelo = sm.OLS(endog=y_train, exog=X_train,)
    modelo = modelo.fit()
    print(modelo.summary())     
    modelo.conf_int(alpha=0.05)   
    predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
    print(predicciones.head(4))
    predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
    predicciones['x'] = X_train[:, 1]
    predicciones['y'] = y_train
    predicciones = predicciones.sort_values('x')
    predicciones_list=predicciones.to_numpy().tolist()
    response = predicciones_list
    temp={"data1":response}
    return temp
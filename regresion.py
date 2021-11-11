import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
#from bson import json_util
import csv
import json

def Regression(collection,var1,var2, database):

    # datos= "C:\DOCTORADO\SEMESTRE 7\PASANTIA\DATOS\AGOSTO-10-2021_1\{}".format(collection)+".csv"

    response = ""
    if (collection == 'SIF_401'):
        data = database.db.SIF_401.find()
        response = json_util.dumps(data)

    # sif_401 = open('sif_401.csv', 'wb+')
    # csv_writer = csv.writer(sif_401)

    # csv_writer.writerow(["Hora", "MESPAEA_rActivePower", "MESPAEA_rAir", "MESPAEA_rCurrent", "MESPAEA_rPowerFactor",
    # "MESPAEA_rVoltage", "MESPAEA_udiAirConsumed", "MESPAEA_udiEnergyConsumed", "SIFOC_sif401_LEC", "Segundos",
    # "SetV_1", "SetV_2", "_id", "minutos"])

    # for x in response:
    #     csv_writer.writerow([
    #         x["Hora"],
    #         x["MESPAEA_rActivePower"],
    #         x["MESPAEA_rAir"],
    #         x["MESPAEA_rCurrent"],
    #         x["MESPAEA_rPowerFactor"],
    #         x["MESPAEA_rVoltage"],
    #         x["MESPAEA_udiAirConsumed"],
    #         x["MESPAEA_udiEnergyConsumed"],
    #         x["SIFOC_sif401_LEC"],
    #         x["Segundos"],
    #         x["SetV_1"],
    #         x["SetV_2"],
    #         x["_id"],
    #         x["minutos"]
    #     ])
    datos = response
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
    recta=modelo.params
    print(recta)
    predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
    print(predicciones.head(4))
    predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
    predicciones['x'] = X_train[:, 1]
    predicciones['y'] = y_train
    predicciones = predicciones.sort_values('x')
    predicciones_list=predicciones.to_numpy().tolist()
    response = predicciones_list
    temp={"data1":response,"pendiente":recta[1],"intercepto":recta[0]}
    return temp
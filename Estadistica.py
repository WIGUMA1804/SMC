from flask.json import jsonify
import pandas as pd

def Basic_Stats():

    data_SIF_401 = pd.read_csv("C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_401.csv")
    esta = data_SIF_401.describe()
    df = esta
    data_dict = dict()
    for col in df.columns:
        data_dict[col] = df[col].values.tolist()
    return jsonify(data_dict)

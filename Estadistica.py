import pandas as pd


def Basic_Stats():


    data_SIF_401 = pd.read_csv("C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_401.csv")
    esta = data_SIF_401.describe()
    print(esta)
    return(esta)

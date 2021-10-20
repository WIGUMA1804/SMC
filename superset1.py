import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Response
from bson import json_util
from flask.json import jsonify


def minmax_norm(df_input):
    return (df_input - df_input.min()) / (df_input.max() - df_input.min())


def superset1(database):
    data_SIF_401 = database.db.SIF_401.find()
    data_SIF_402 = database.db.SIF_402.find()
    data_SIF_405 = database.db.SIF_405.find()
    data_SIF_407 = database.db.SIF_407.find()
    data_SIF_408 = database.db.SIF_408.find()
    data_SIF_409 = database.db.SIF_409.find()

    response_401 = json_util.dumps(data_SIF_401)
    df_sifoc_401 = pd.read_json(response_401)

    response_402 = json_util.dumps(data_SIF_402)
    df_sifoc_402 = pd.read_json(response_402)

    response_405 = json_util.dumps(data_SIF_405)
    df_sifoc_405 = pd.read_json(response_405)

    response_407 = json_util.dumps(data_SIF_407)
    df_sifoc_407 = pd.read_json(response_407)

    response_408 = json_util.dumps(data_SIF_408)
    df_sifoc_408 = pd.read_json(response_408)

    response_409 = json_util.dumps(data_SIF_409)
    df_sifoc_409 = pd.read_json(response_409)


    #data_SIF_401 = pd.read_csv("C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_401.csv")
    #data_SIF_402 = pd.read_csv("C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_402.csv")
    #data_SIF_405 = pd.read_csv("C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_405.csv")
    #data_SIF_407 = pd.read_csv("C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_407.csv")
    #data_SIF_408 = pd.read_csv("C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_408.csv")
    #data_SIF_409 = pd.read_csv("C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_409.csv")

    columns = ['MESPAEA_rActivePower', 'MESPAEA_rVoltage',
            'MESPAEA_udiAirConsumed', 'MESPAEA_udiEnergyConsumed']
    scaled_df_401 = minmax_norm(data_SIF_401[columns])
    columns1 = ['MESPAEA_rActivePower',
                'MESPAEA_rVoltage', 'MESPAEA_udiEnergyConsumed']
    scaled_df_402 = minmax_norm(data_SIF_402[columns1])
    scaled_df_405 = minmax_norm(data_SIF_405[columns1])
    scaled_df_407 = minmax_norm(data_SIF_407[columns1])
    scaled_df_408 = minmax_norm(data_SIF_408[columns1])
    scaled_df_409 = minmax_norm(data_SIF_409[columns1])

    scaled_df_401.columns = ['MESPAEA_rActivePower_401', 'MESPAEA_rVoltage_401',
                            'MESPAEA_udiAirConsumed_401', 'MESPAEA_udiEnergyConsumed_401']
    scaled_df_402.columns = ['MESPAEA_rActivePower_402',
                            'MESPAEA_rVoltage_402', 'MESPAEA_udiEnergyConsumed_402']
    scaled_df_405.columns = ['MESPAEA_rActivePower_405',
                            'MESPAEA_rVoltage_405', 'MESPAEA_udiEnergyConsumed_405']
    scaled_df_407.columns = ['MESPAEA_rActivePower_407',
                            'MESPAEA_rVoltage_407', 'MESPAEA_udiEnergyConsumed_407']
    scaled_df_408.columns = ['MESPAEA_rActivePower_408',
                            'MESPAEA_rVoltage_408', 'MESPAEA_udiEnergyConsumed_408']
    scaled_df_409.columns = ['MESPAEA_rActivePower_409',
                            'MESPAEA_rVoltage_409', 'MESPAEA_udiEnergyConsumed_409']

    scaled_df_401['Alarma_401'] =df_sifoc_401['Alarma']
    scaled_df_401['MESPAEA_rCurrent_401'] =df_sifoc_401['MESPAEA_rCurrent']
    scaled_df_401['MESPAEA_rPowerFactor_401'] =df_sifoc_401['MESPAEA_rPowerFactor']
    scaled_df_401['SIFOC_sif401_LEC'] =df_sifoc_401['SIFOC_sif401_LEC']
    scaled_df_401['MESPAEA_rAir_401'] =df_sifoc_401['MESPAEA_rAir']
    scaled_df_401['SetV_1_401'] =df_sifoc_401['SetV_1']
    scaled_df_401['SetV_2_401'] =df_sifoc_401['SetV_2']
    scaled_df_401['Time'] =df_sifoc_401['Time']

    scaled_df_402['Alarma_402'] =df_sifoc_402['Alarma']
    scaled_df_402['MESPAEA_rCurrent_402'] =df_sifoc_402['MESPAEA_rCurrent']
    scaled_df_402['MESPAEA_rPowerFactor_402'] =df_sifoc_402['MESPAEA_rPowerFactor']
    scaled_df_402['SIFOC_sif402_LEC'] =df_sifoc_402['SIFOC_sif402_LEC']
    scaled_df_402['SetV_1_402'] =df_sifoc_402['SetV_1']
    scaled_df_402['SetV_2_402'] =df_sifoc_402['SetV_2']

    scaled_df_405['Alarma_405'] =df_sifoc_405['Alarma']
    scaled_df_405['MESPAEA_rCurrent_405'] =df_sifoc_405['MESPAEA_rCurrent']
    scaled_df_405['MESPAEA_rPowerFactor_405'] =df_sifoc_405['MESPAEA_rPowerFactor']
    scaled_df_405['SIFOC_sif405_V1'] =df_sifoc_405['SIFOC_sif405_V1']
    scaled_df_405['SIFOC_sif405_V2'] =df_sifoc_405['SIFOC_sif405_V2']
    scaled_df_405['SetV_1_405'] =df_sifoc_405['SetV_1']
    scaled_df_405['SetV_2_405'] =df_sifoc_405['SetV_2']

    scaled_df_407['Alarma_407'] =df_sifoc_407['Alarma']
    scaled_df_407['MESPAEA_rCurrent_407'] =df_sifoc_407['MESPAEA_rCurrent']
    scaled_df_407['MESPAEA_rPowerFactor_407'] =df_sifoc_407['MESPAEA_rPowerFactor']
    scaled_df_407['SIFOC_sif407_V1'] =df_sifoc_407['SIFOC_sif407_V1']
    scaled_df_407['SIFOC_sif407_V2'] =df_sifoc_407['SIFOC_sif407_V2']
    scaled_df_407['SIFOC_sif407_V3'] =df_sifoc_407['SIFOC_sif407_V3']
    scaled_df_407['SetV_1_407'] =df_sifoc_407['SetV_1']
    scaled_df_407['SetV_2_407'] =df_sifoc_407['SetV_2']

    scaled_df_408['Alarma_408'] =df_sifoc_408['Alarma']
    scaled_df_408['MESPAEA_rCurrent_408'] =df_sifoc_408['MESPAEA_rCurrent']
    scaled_df_408['MESPAEA_rPowerFactor_408'] =df_sifoc_408['MESPAEA_rPowerFactor']
    scaled_df_408['SIFOC_sif408_ROBOT'] =df_sifoc_408['SIFOC_sif408_ROBOT']
    scaled_df_408['SetV_1_408'] =df_sifoc_408['SetV_1']
    scaled_df_408['SetV_2_408'] =df_sifoc_408['SetV_2']

    scaled_df_409['Alarma_409'] =df_sifoc_409['Alarma']
    scaled_df_409['MESPAEA_rCurrent_409'] =df_sifoc_409['MESPAEA_rCurrent']
    scaled_df_409['MESPAEA_rPowerFactor_409'] =df_sifoc_409['MESPAEA_rPowerFactor']
    scaled_df_409['SetV_409'] =df_sifoc_409['SetV']

    scaled_df_402 = scaled_df_402.drop(range(1207, 1226, 1), axis=0)
    scaled_df_405 = scaled_df_405.drop(range(1207, 1222), axis=0)
    scaled_df_407 = scaled_df_407.drop(range(1207, 1221, 1), axis=0)
    scaled_df_408 = scaled_df_408.drop(range(1207, 1224, 1), axis=0)
    scaled_df_409 = scaled_df_409.drop(range(1207, 1229, 1), axis=0)

    scaled_df_401['Tiempo'] = np.arange(0, 1207, 1)

    df = pd.concat([scaled_df_401, scaled_df_402, scaled_df_405,
                scaled_df_407, scaled_df_408, scaled_df_409], axis=1)

    data_dict = dict()
    for col in df.columns:
        data_dict[col] = df[col].values.tolist()
    response = json_util.dumps(data_dict)
    return Response(response, mimetype='application/json')

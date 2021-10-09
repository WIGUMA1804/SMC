from flask.json import jsonify
import numpy as np
import pandas as pd


def minmax_norm(df_input):
    return (df_input - df_input.min()) / (df_input.max() - df_input.min())


def get_superset():

    data_SIF_401 = pd.read_csv(
        "C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_401.csv")
    data_SIF_402 = pd.read_csv(
        "C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_402.csv")
    data_SIF_405 = pd.read_csv(
        "C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_405.csv")
    data_SIF_407 = pd.read_csv(
        "C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_407.csv")
    data_SIF_408 = pd.read_csv(
        "C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_408.csv")
    data_SIF_409 = pd.read_csv(
        "C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_409.csv")
    data_SIF_401['Time'] = [pd.to_datetime(d) for d in data_SIF_401['Time']]

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
    scaled_df_402.head()

    columns1 = ['MESPAEA_rActivePower_401', 'MESPAEA_rVoltage_401',
                'MESPAEA_udiAirConsumed_401', 'MESPAEA_udiEnergyConsumed_401']
    scaled_df_401.columns = columns1
    columns2 = ['MESPAEA_rActivePower_402',
                'MESPAEA_rVoltage_402', 'MESPAEA_udiEnergyConsumed_402']
    scaled_df_402.columns = columns2
    columns5 = ['MESPAEA_rActivePower_405',
                'MESPAEA_rVoltage_405', 'MESPAEA_udiEnergyConsumed_405']
    scaled_df_405.columns = columns5
    columns7 = ['MESPAEA_rActivePower_407',
                'MESPAEA_rVoltage_407', 'MESPAEA_udiEnergyConsumed_407']
    scaled_df_407.columns = columns7
    columns8 = ['MESPAEA_rActivePower_408',
                'MESPAEA_rVoltage_408', 'MESPAEA_udiEnergyConsumed_408']
    scaled_df_408.columns = columns8
    columns9 = ['MESPAEA_rActivePower_409',
                'MESPAEA_rVoltage_409', 'MESPAEA_udiEnergyConsumed_409']
    scaled_df_409.columns = columns9
    scaled_df_401.head()

    scaled_df_401['Alarma_401'] = data_SIF_401['Alarma']
    scaled_df_401['MESPAEA_rCurrent_401'] = data_SIF_401['MESPAEA_rCurrent']
    scaled_df_401['MESPAEA_rPowerFactor_401'] = data_SIF_401['MESPAEA_rPowerFactor']
    scaled_df_401['SIFOC_sif401_LEC'] = data_SIF_401['SIFOC_sif401_LEC']
    scaled_df_401['SetV_1_401'] = data_SIF_401['SetV_1']
    scaled_df_401['SetV_2_401'] = data_SIF_401['SetV_2']
    scaled_df_401['Time'] = data_SIF_401['Time']
    scaled_df_401.head()

    scaled_df_402['Alarma_402'] = data_SIF_401['Alarma']
    scaled_df_402['MESPAEA_rCurrent_402'] = data_SIF_402['MESPAEA_rCurrent']
    scaled_df_402['MESPAEA_rPowerFactor_402'] = data_SIF_402['MESPAEA_rPowerFactor']
    scaled_df_402['SIFOC_sif402_LEC'] = data_SIF_402['SIFOC_sif402_LEC']
    scaled_df_402['SetV_1_402'] = data_SIF_402['SetV_1']
    scaled_df_402['SetV_2_402'] = data_SIF_402['SetV_2']
    scaled_df_402['Time'] = data_SIF_402['Time']
    scaled_df_402.head()

    scaled_df_405['Alarma_405'] = data_SIF_405['Alarma']
    scaled_df_405['MESPAEA_rCurrent_405'] = data_SIF_405['MESPAEA_rCurrent']
    scaled_df_405['MESPAEA_rPowerFactor_405'] = data_SIF_405['MESPAEA_rPowerFactor']
    scaled_df_405['SIFOC_sif405_V1'] = data_SIF_405['SIFOC_sif405_V1']
    scaled_df_405['SIFOC_sif405_V2'] = data_SIF_405['SIFOC_sif405_V2']
    scaled_df_405['SetV_1_405'] = data_SIF_405['SetV_1']
    scaled_df_405['SetV_2_405'] = data_SIF_405['SetV_2']
    scaled_df_405['Time'] = data_SIF_405['Time']
    scaled_df_405.head()

    scaled_df_407['Alarma_407'] = data_SIF_407['Alarma']
    scaled_df_407['MESPAEA_rCurrent_407'] = data_SIF_407['MESPAEA_rCurrent']
    scaled_df_407['MESPAEA_rPowerFactor_407'] = data_SIF_407['MESPAEA_rPowerFactor']
    scaled_df_407['SIFOC_sif407_V1'] = data_SIF_407['SIFOC_sif407_V1']
    scaled_df_407['SIFOC_sif407_V2'] = data_SIF_407['SIFOC_sif407_V2']
    scaled_df_407['SIFOC_sif407_V3'] = data_SIF_407['SIFOC_sif407_V3']
    scaled_df_407['SetV_1_407'] = data_SIF_407['SetV_1']
    scaled_df_407['SetV_2_407'] = data_SIF_407['SetV_2']
    scaled_df_407['Time'] = data_SIF_407['Time']
    scaled_df_407.head()

    scaled_df_408['Alarma_408'] = data_SIF_408['Alarma']
    scaled_df_408['MESPAEA_rCurrent_408'] = data_SIF_408['MESPAEA_rCurrent']
    scaled_df_408['MESPAEA_rPowerFactor_408'] = data_SIF_408['MESPAEA_rPowerFactor']
    scaled_df_408['SIFOC_sif408_ROBOT'] = data_SIF_408['SIFOC_sif408_ROBOT']
    scaled_df_408['SetV_1_408'] = data_SIF_408['SetV_1']
    scaled_df_408['SetV_2_408'] = data_SIF_408['SetV_2']
    scaled_df_408['Time'] = data_SIF_408['Time']
    scaled_df_408.head()

    scaled_df_409['Alarma_409'] = data_SIF_409['Alarma']
    scaled_df_409['MESPAEA_rCurrent_409'] = data_SIF_409['MESPAEA_rCurrent']
    scaled_df_408['MESPAEA_rPowerFactor_409'] = data_SIF_409['MESPAEA_rPowerFactor']
    scaled_df_409['SIFOC_sif409_LEC'] = data_SIF_409['SIFOC_sif409_LEC']
    scaled_df_409['SetV_409'] = data_SIF_409['SetV']
    scaled_df_409['Time'] = data_SIF_409['Time']
    scaled_df_409.head()

    scaled_df_402 = scaled_df_402.drop(range(1207, 1226, 1), axis=0)
    # scaled_df_402=scaled_df_402.drop(range(1222,1223,1224,1225,1226),axis=0)
    scaled_df_402.shape

    scaled_df_405 = scaled_df_405.drop(range(1207, 1222), axis=0)
    scaled_df_405.shape

    scaled_df_407 = scaled_df_407.drop(range(1207, 1221, 1), axis=0)
    print(scaled_df_407.shape)
    scaled_df_408 = scaled_df_408.drop(range(1207, 1224, 1), axis=0)
    print(scaled_df_408.shape)
    scaled_df_409 = scaled_df_409.drop(range(1207, 1229, 1), axis=0)
    print(scaled_df_409.shape)

    scaled_df_401['Tiempo'] = np.arange(0, 1207, 1)
    scaled_df_401.head()
    scaled_df_401.shape

    scaled_df_402['Tiempo'] = np.arange(0, 1207, 1)
    scaled_df_402.head()
    print(scaled_df_402.shape)
    scaled_df_405['Tiempo'] = np.arange(0, 1207, 1)
    scaled_df_405.head()
    print(scaled_df_405.shape)
    scaled_df_407['Tiempo'] = np.arange(0, 1207, 1)
    scaled_df_407.head()
    print(scaled_df_407.shape)
    scaled_df_408['Tiempo'] = np.arange(0, 1207, 1)
    scaled_df_408.head()
    print(scaled_df_408.shape)
    scaled_df_409['Tiempo'] = np.arange(0, 1207, 1)
    scaled_df_409.head()
    print(scaled_df_409.shape)
    scaled_df_409.head()

    df = pd.merge(scaled_df_401, scaled_df_402, left_on='Tiempo',
                  right_on='Tiempo', how='outer')
    print(df.shape)

    df = pd.merge(df, scaled_df_405, left_on='Tiempo',
                  right_on='Tiempo', how='outer')

    df = pd.merge(df, scaled_df_407, left_on='Tiempo',
                  right_on='Tiempo', how='outer')
    print(df.shape)

    df = pd.merge(df, scaled_df_408, left_on='Tiempo',
                  right_on='Tiempo', how='outer')
    df.head()

    df = pd.merge(df, scaled_df_409, left_on='Tiempo',
                  right_on='Tiempo', how='outer')
    print(df.shape)

    #df["Alarma_401"] = pd.get_dummies(df['Alarma_401'], prefix="Alarma_401")
    # df["Alarma_402"] = pd.get_dummies(df['Alarma_402'], prefix="Alarma_402")
    # df["Alarma_405"] = pd.get_dummies(df['Alarma_405'], prefix="Alarma_405")
    # df["Alarma_407"] = pd.get_dummies(df['Alarma_407'], prefix="Alarma_407")
    # df["Alarma_408"] = pd.get_dummies(df['Alarma_408'], prefix="Alarma_408")
    # df["Alarma_409"] = pd.get_dummies(df['Alarma_409'], prefix="Alarma_409")



    # df["SIFOC_sif405_V1"] = pd.get_dummies(
    # df['SIFOC_sif405_V1'], prefix="SIFOC_sif405_V1")
    # df["SIFOC_sif405_V2"] = pd.get_dummies(
    #     df['SIFOC_sif405_V2'], prefix="SIFOC_sif405_V2")
    # df["SIFOC_sif407_V1"] = pd.get_dummies(
    #     df['SIFOC_sif407_V1'], prefix="SIFOC_sif407_V1")
    # df["SIFOC_sif407_V2"] = pd.get_dummies(
    #     df['SIFOC_sif407_V2'], prefix="SIFOC_sif407_V2")
    # df["SIFOC_sif407_V3"] = pd.get_dummies(
    #     df['SIFOC_sif407_V3'], prefix="SIFOC_sif407_V3")



    data_dict = dict()
    for col in df.columns:
        data_dict[col] = df[col].values.tolist()
    return jsonify(data_dict)


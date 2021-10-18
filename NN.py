def Neural_Network():
    import pandas as pd
    import numpy as np
    
    from sklearn.neural_network import MLPRegressor
    data_SIF_401=pd.read_csv("C:\DOCTORADO\SEMESTRE8\exportacion\DATOS\SIF_401.csv")
    x = data_SIF_401[['MESPAEA_rCurrent_401','SIFOC_sif401_LEC']]
    #x = scaled_df_401['Tiempo']
    y =data_SIF_401['MESPAEA_udiEnergyConsumed_401']
    #X=x[:,np.newaxis].reshape(-1, 1)
    while True:
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(x,y)
        mlr=MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
        mlr.fit(X_train,y_train)
        print(mlr.score(X_train,y_train))
        if mlr.score(X_train,y_train)>0.95:
            break
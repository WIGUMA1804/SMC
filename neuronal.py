from sklearn.neural_network import MLPRegressor
    
def getNeuronal(vectors):
    
    mlr = MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
    mlr.fit(vectors['X_train'], vectors['y_train'])
    
    return mlr
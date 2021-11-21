from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import getsuperset
from bson import json_util
from flask import Response
import numpy as np


def results_summary_to_dataframe(results):
    '''take the result of an statsmodel results table and transforms it into a dataframe'''
    pvals = results.pvalues
    coeff = results.params
    conf_lower = results.conf_int()[0]
    conf_higher = results.conf_int()[1]

    results_df = pd.DataFrame({'pvals': pvals,
                               'coeff': coeff,
                               'conf_lower': conf_lower,
                               'conf_higher': conf_higher
                               })

    # Reordering...
    results_df = results_df[["coeff", "pvals",
                             "conf_lower", "conf_higher"]].fillna(0)
    return results_df


def Regression(database, inputs, output):
    print(inputs)
    print(output)
    df = getsuperset.get_superset(database)
    entry = inputs
    out = output

    X = df[entry]
    y = df[out]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y.values.reshape(-1, 1),
        train_size=0.8,
        random_state=1234,
        shuffle=True
    )

    X_train = sm.add_constant(X_train, prepend=True)
    modelo = sm.OLS(endog=y_train.astype(float), exog=X_train.astype(float))
    modelo = modelo.fit()

    y_train = y_train.flatten()
    prediccion_train = modelo.predict(exog=X_train)
    dfr = results_summary_to_dataframe(modelo)

    data_dict = dict()
    for col in dfr.columns:
        data_dict[col] = dfr[col].values.tolist()
    data_dict['y_train'] = y_train
    data_dict['prediccion_train'] = prediccion_train
    response = json_util.dumps(data_dict)
    return Response(response, mimetype='application/json')

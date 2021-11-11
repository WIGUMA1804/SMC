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

    results_df = pd.DataFrame({"pvals":pvals,
                               "coeff":coeff,
                               "conf_lower":conf_lower,
                               "conf_higher":conf_higher
                                })

    #Reordering...
    results_df = results_df[["coeff","pvals","conf_lower","conf_higher"]]
    return results_df

def Regression(database):
    


    df = getsuperset.get_superset(database)
    input=['SIFOC_sif405_V1', 'SIFOC_sif405_V2','SIFOC_sif407_V1','SIFOC_sif407_V2','SIFOC_sif407_V3','Tiempo']
    output='MESPAEA_udiEnergyConsumed_401'
    #X = df[['SIFOC_sif405_V1', 'SIFOC_sif405_V2','SIFOC_sif407_V1','SIFOC_sif407_V2','SIFOC_sif407_V3','Tiempo']]
    #X = df[['SIFOC_sif405_V1','SIFOC_sif407_V2','SIFOC_sif407_V3','Tiempo']]
    X=df[input]

    y = df[output]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y.values.reshape(-1, 1),
        train_size=0.8,
        random_state=1234,
        shuffle=True
    )
    
    X_train = sm.add_constant(X_train, prepend=True)
    modelo =sm.OLS(endog=y_train.astype(float), exog=X_train.astype(float))
    modelo = modelo.fit()
    #datos=modelo.summary()
    dfr=results_summary_to_dataframe(modelo)
    #dato1=modelo.pvalues[-1]
    #return {'dato1':str(dato1)}
    #response = json_util.dumps(datos)
    #return{response}
    #print(datos)   
    #param=np.asarray(modelo.params)
    #y_train = y_train.flatten()
    #prediccion_train = modelo.predict(exog=X_train)
    #residuos_train = prediccion_train - y_train
    data_dict = dict()
    for col in dfr.columns:
        data_dict[col] = dfr[col].values.tolist()
    response = json_util.dumps(data_dict)
    return Response(response, mimetype='application/json')
    #return 
    # # Gráficos
    # # ==============================================================================
    # fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(9, 8))

    # axes[0, 0].scatter(y_train, prediccion_train,
    #                    edgecolors=(0, 0, 0), alpha=0.4)
    # axes[0, 0].plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()],
    #                 'k--', color='black', lw=2)
    # axes[0, 0].set_title('Valor predicho vs valor real',
    #                      fontsize=10, fontweight="bold")
    # axes[0, 0].set_xlabel('Real')
    # axes[0, 0].set_ylabel('Predicción')
    # axes[0, 0].tick_params(labelsize=7)

    # axes[0, 1].scatter(list(range(len(y_train))), residuos_train,
    #                    edgecolors=(0, 0, 0), alpha=0.4)
    # axes[0, 1].axhline(y=0, linestyle='--', color='black', lw=2)
    # axes[0, 1].set_title('Residuos del modelo', fontsize=10, fontweight="bold")
    # axes[0, 1].set_xlabel('id')
    # axes[0, 1].set_ylabel('Residuo')
    # axes[0, 1].tick_params(labelsize=7)

    # sns.histplot(
    #     data=residuos_train,
    #     stat="density",
    #     kde=True,
    #     line_kws={'linewidth': 1},
    #     color="firebrick",
    #     alpha=0.3,
    #     ax=axes[1, 0]
    # )

    # axes[1, 0].set_title('Distribución residuos del modelo', fontsize=10,
    #                      fontweight="bold")
    # axes[1, 0].set_xlabel("Residuo")
    # axes[1, 0].tick_params(labelsize=7)

    # sm.qqplot(
    #     residuos_train,
    #     fit=True,
    #     line='q',
    #     ax=axes[1, 1],
    #     color='firebrick',
    #     alpha=0.4,
    #     lw=2
    # )
    # axes[1, 1].set_title('Q-Q residuos del modelo',
    #                      fontsize=10, fontweight="bold")
    # axes[1, 1].tick_params(labelsize=7)


    # axes[2, 0].scatter(prediccion_train, residuos_train,
    #                 edgecolors=(0, 0, 0), alpha=0.4)
    # axes[2, 0].axhline(y=0, linestyle='--', color='black', lw=2)
    # axes[2, 0].set_title('Residuos del modelo vs predicción',
    #                     fontsize=10, fontweight="bold")
    # axes[2, 0].set_xlabel('Predicción')
    # axes[2, 0].set_ylabel('Residuo')
    # axes[2, 0].tick_params(labelsize=7)

    # # Se eliminan los axes vacíos
    # fig.delaxes(axes[2, 1])

    # fig.tight_layout()
    # plt.subplots_adjust(top=0.9)
    # fig.suptitle('Diagnóstico residuos', fontsize=12, fontweight="bold")

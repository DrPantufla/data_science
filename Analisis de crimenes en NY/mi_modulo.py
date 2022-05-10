import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_graphviz
from sklearn.metrics import roc_curve, roc_auc_score, auc, accuracy_score, recall_score, precision_score, f1_score, precision_recall_curve, mean_squared_error
from sklearn.model_selection import train_test_split, learning_curve, validation_curve
from sklearn.tree import export_graphviz
import pydotplus


def recod_sentiment(data, words, num):
    '''
    Esta funcion se utilizará para recodificar el atributo sentiment en un dataset cualquiera.
    Se ingresan los valores de data, words y num:
    data = dataframe donde se encuentra el atributo sentiment.
    words = va a ser una lista de palabras que serán reformuladas con esta funcion.
    num = será el nuevo valor que tomara el dataset.
    '''
    for emotion in words:
        data['sentiment']=np.where(data['sentiment']==emotion, num, data['sentiment'])
    return 

def datos_perdidos(data_set):
    """
    En esta funcion ingresa un data set y  su salida es un grafico que muestra los valores 
    perdidos por columna.
    """
    sns.heatmap(data_set.isnull(), cbar=False)
    plt.title('Valores Perdidos \n', fontdict={'fontsize':40})
    plt.show()
    return

def binarizacion(df):
    """
    Se ingresa el dataframe en el que se requieren binarizar las variales tipo object y sale el dataframe 
    binarizado.
    """
    for cols in df.select_dtypes(include=['object']).columns:
         df = pd.concat([df, pd.get_dummies(df[cols], prefix=cols, drop_first=True)], axis=1).drop(cols, axis=1)
    return df

def plot_importance(fit_model, feat_names):
    """TODO: Docstring for plot_importance.
    :fit_model: TODO
    :: TODO
    :returns: TODO
    """
    tmp_importance = fit_model.feature_importances_
    sort_importance = np.argsort(tmp_importance)[::-1]
    names = [feat_names[i] for i in sort_importance]
    plt.title("Feature importance")
    plt.barh(range(len(feat_names)), tmp_importance[sort_importance])
    plt.yticks(range(len(feat_names)), names, rotation=0)
    
    
def ver_datos_perdidos(df):
    for cols in df.columns:
        df[cols]=np.where(df[cols]==' ', np.nan, df[cols])
    return df

def conditional_pr(df, A_var, A_condition, B_var, B_condition):
    """
    conditional_pr: retrieve conditional probability given the following
    formula:
                    Pr(A and B)
        Pr(A|B) = --------------
                      Pr(B)
    parameters:
        df: dataframe.
        A_var: event to be conditioned by B.
        A_condition: specific outcome on A.
        B_var: conditioning event on A.
        B_condition: specific conditioning event on B.
    """
    get_a_and_b = 0
    for i, r in df.iterrows():
        if (r[A_var] == A_condition and r[B_var] == B_condition):
            get_a_and_b += 1
    get_b_pr = df[B_var].value_counts().loc[B_condition]
    print("Pr(" , A_condition, "|" , B_condition, ") = ", round((get_a_and_b / get_b_pr)*100, 2),"%")
    
    
    
    
    
    
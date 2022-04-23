from pickletools import read_uint1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
from pickletools import read_uint1
import seaborn as sns
import matplotlib.pyplot as plt
from sympy import O

def suma(num1, num2):
    """
    En la siguiente funcion entran 2 numeros: num1 y num2, los cuales se suman y 
    la salida entrega la suma del resultado.
    """
    return num1+num2

def inspeccion_previa(data_set):
    """
    En la siguiente funcion entra el data set completo y se analiza si la columna contiene 
    variables categoricas o numericas. Y si son categoricas les aplica un value_counts para
    ver que elementos contiene y su proporcion.
    Retorna una serie de tablas con el numbre de la columna y las variables que contiene.

    """
    for col in data_set.columns:
        if isinstance((data_set[col][0]),str):
            print(f'{data_set[col].value_counts().to_frame()}\n')


def histogramas(data_set):
    """
    Ingresa el data_set y se seleccionan todas las variables continuas y retorna 
    histograma de cada columna.
    
    """
    
    for col in data_set.columns:
        if isinstance(data_set[col][0], str):
            continue
        sns.histplot(data=data_set, x=col, kde=True)
        plt.title(col, loc='center', fontdict={'fontsize':20}, fontstyle='italic' )
        plt.show()
    return

def grafico_barras(data_set):
    """
    Ingresa el data_set y se seleccionan todas las variables categoricas y retorna 
    el grafico de barras de cada columna.
    """
    sns.set(rc={'figure.figsize':(8,5)})
    for col in data_set.columns:
        if isinstance(data_set[col][0], str):

            sns.countplot(x=col, data=data_set)
            plt.title(col, loc='center', fontdict={'fontsize':20}, fontstyle='italic' )
            plt.xlabel("")
            plt.xticks(rotation=45)
            plt.show()
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

def heatmap_corr(data_set):
    """
    Ingresa el data set a estudiar y a la salida se crea un grafico heatmap con los valores
    de correlacion entre todas las variables.
    """
    sns.set(rc={'figure.figsize':(28,14)})
    sns.heatmap(data_set.corr(), cmap='Blues', annot=True)
    plt.show()
    return
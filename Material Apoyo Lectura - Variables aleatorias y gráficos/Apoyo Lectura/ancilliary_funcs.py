import pandas as pd
import numpy as np


def funcion(dataframe):
    parametros = ['undp_hdi','gle_cgdpc','imf_pop','wef_imort', 'who_alc2000', 'who_tobt', 'wdi_exph']
    df = pd.DataFrame(columns=['name','media', 'desv_standar', 'median' ])
    for parametro in parametros:
        promedios = dataframe[parametro].dropna().mean()
        desv_standar = dataframe[parametro].dropna().std()
        median = dataframe[parametro].dropna().median()
        df = df.append({'name': parametro,'media':promedios, 'desv_standar':desv_standar, 'median':median}, ignore_index=True)
    frecuencias_region = dataframe['ht_region'].value_counts()
    frecuencias_pais = dataframe['ccodealp'].value_counts()
    return [df, frecuencias_region, frecuencias_pais]


def observaciones_perdidas(dataframe, variable, print_list = False):
    cantidad_perdidos = dataframe[variable].isnull().value_counts()[True]
    porcentaje_perdido = (cantidad_perdidos/dataframe[variable].isnull().value_counts().sum()).round(3)
    print(f'''La cantidad de datos perdido en la variable \'{variable}\' es de {cantidad_perdidos}, lo que representa un de {porcentaje_perdido*100}% de datos perdidos.''')
    if print_list:
        return dataframe[dataframe[variable].isnull() == True]['ccodealp']    


def generate_histogram(sample_df, full_df, var, sample_mean = False, true_mean = False):
    dropna_filter_sample_df = sample_df[var].dropna()
    dropna_filter_full_df = full_df[var].dropna()
    plt.figure(figsize=(18,5))
    plt.subplot(1,2,1)
    plt.hist(dropna_filter_sample_df, color='tomato', alpha=.4)
    if sample_mean:
        plt.axvline(dropna_filter_sample_df.mean(), color = 'dodgerblue', linestyle = '--', lw=2)
    plt.title('Sample Dataframe')
    
    
    plt.figure(figsize=(18,5))
    plt.subplot(1,2,2)
    plt.hist(dropna_filter_full_df, color = 'grey', alpha=0.4)
    if true_mean:
        plt.axvline(dropna_filter_sample_df.mean(), color = 'dodgerblue', linestyle = '--', lw=2)
    plt.title('Full Dataframe')   
    return 


def dotplot(dataframe, plot_var, plot_by, statistic = 'mean', global_stat=False):
    if statistic.lower() == 'mean':
        agrupar = dataframe.groupby([plot_by]).mean()[plot_var]
    elif statistic.lower() == 'median':
        agrupar = dataframe.groupby([plot_by]).median()[plot_var]
    if global_stat:
        plt.axvline(dataframe[plot_var].mean(), color = 'tomato', linestyle = '--')
    plt.plot(agrupar.values, agrupar.index, 'o', color = 'grey')
    
    return







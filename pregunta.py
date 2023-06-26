"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
from datetime import datetime
import pandas as pd
import re


def clean_data():
    """
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    """
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    #
    # Inserte su código aquí
    #

    df.dropna(inplace=True)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower();
    df['sexo'] = df['sexo'].str.lower();
    df.idea_negocio = [str.lower(idea.replace("_", " ").replace("-", " ")) for idea in df.idea_negocio]
    df.barrio = [str.lower(barrio).replace("_", " ").replace("-", " ") for barrio in df.barrio]
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)
    df.estrato = df.estrato.astype(int)
    df["línea_credito"] = [str.lower(linea.strip().replace("-", " ").replace("_", " ").replace(". ", ".")) for linea in df["línea_credito"]]
    df['monto_del_credito']=df['monto_del_credito'].apply(lambda x: x.strip("$").replace(",","")).astype(float)
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(convertir_fecha)

    df.drop_duplicates(inplace=True)

    return df

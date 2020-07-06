import pandas as pd
import numpy as np
import datetime
import zipfile
import urllib.request
import os
import shutil


def get_confirmados_por_semana(file_path=None, activos=False):
    """Regresa la serie de tiempo con agregados y acumulados por municipio y por semana."""
    serie_municipios = pd.read_csv(file_path,
                                   dtype={'ENTIDAD_UM': str,
                                          'ENTIDAD_NAC': str,
                                          'ENTIDAD_RES': str,
                                          'MUNICIPIO_RES': str}, encoding='latin1')
    serie_municipios.loc[:, 'municipio_cvegeo'] = serie_municipios['ENTIDAD_RES'] + \
        serie_municipios['MUNICIPIO_RES']
    confirmados_municipios = serie_municipios.loc[serie_municipios['RESULTADO'] == 1, [
        'FECHA_SINTOMAS', 'FECHA_INGRESO', 'RESULTADO', 'municipio_cvegeo']].copy()
    confirmados_municipios.loc[:, 'FECHA_INGRESO'] = pd.to_datetime(
        confirmados_municipios['FECHA_INGRESO'], format="%Y-%m-%d")
    confirmados_municipios.loc[:, 'FECHA_SINTOMAS'] = pd.to_datetime(
        confirmados_municipios['FECHA_SINTOMAS'], format="%Y-%m-%d")
    if activos:
        print("Calculando casos activos")
        intervalo = pd.Timedelta('14 days')
        por_fecha = (confirmados_municipios.sort_values(by='FECHA_SINTOMAS')
                        .sort_values(by='FECHA_SINTOMAS')
                        .set_index('FECHA_SINTOMAS')
                        .groupby(['municipio_cvegeo', 'FECHA_INGRESO'])
                        .rolling(intervalo).sum()[['RESULTADO']]
                        .rename({'RESULTADO':'total'}, axis=1)
                        .reset_index()
                        .drop('FECHA_SINTOMAS', axis=1)
                    )
    else:
        por_fecha = (confirmados_municipios.groupby(['municipio_cvegeo', 'FECHA_INGRESO'])
                        .size()
                        .reset_index()
                        .rename({0: 'total'}, axis=1)
                    )
    confirmados_municipios_dia = (por_fecha
                                  .pivot_table("total", "FECHA_INGRESO", "municipio_cvegeo")
                                  .unstack()
                                  .reset_index()
                                  .fillna(0)
                                  .rename({0: 'total'}, axis=1)
                                  .set_index(['FECHA_INGRESO', 'municipio_cvegeo'])
                                  )
    por_semana = (confirmados_municipios_dia
                  .groupby(['municipio_cvegeo', pd.Grouper(level='FECHA_INGRESO', freq='W')])[['total']]
                  .sum()
                  )
    por_semana = (por_semana
                  .reset_index()
                  .set_index(['FECHA_INGRESO', 'municipio_cvegeo'])
                  )
    por_semana = por_semana.reset_index()
    por_semana = (por_semana
                  .set_index('FECHA_INGRESO')
                  .groupby('municipio_cvegeo')
                  .apply(lambda d: d.reindex(pd.date_range(min(por_semana.FECHA_INGRESO),
                                                           max(por_semana.FECHA_INGRESO),
                                                           freq='W')))
                  .drop('municipio_cvegeo', axis=1)
                  .fillna(method='ffill')
                  )
    por_semana.index.names = ['municipio_cvegeo', 'FECHA_INGRESO']
    por_semana.reset_index('municipio_cvegeo', inplace=True)
    por_semana['acumulados'] = por_semana.groupby('municipio_cvegeo').cumsum()
    return por_semana


def get_defunciones_por_semana(file_path=None):
    """Regresa la serie de tiempo con agregados y acumulados por municipio y por semana."""
    serie_municipios = pd.read_csv(file_path,
                                   dtype={'ENTIDAD_UM': str,
                                          'ENTIDAD_NAC': str,
                                          'ENTIDAD_RES': str,
                                          'MUNICIPIO_RES': str}, encoding='latin1')
    serie_municipios.loc[:, 'municipio_cvegeo'] = serie_municipios['ENTIDAD_RES'] + \
        serie_municipios['MUNICIPIO_RES']
    confirmados_municipios = serie_municipios.loc[(serie_municipios['RESULTADO'] == 1) & (serie_municipios['FECHA_DEF'] != '9999-99-99'), [
        'FECHA_SINTOMAS', 'FECHA_DEF', 'RESULTADO', 'municipio_cvegeo']].copy()
    confirmados_municipios.loc[:, 'FECHA_DEF'] = pd.to_datetime(
        confirmados_municipios['FECHA_DEF'], format="%Y-%m-%d")
    confirmados_municipios.loc[:, 'FECHA_SINTOMAS'] = pd.to_datetime(
        confirmados_municipios['FECHA_SINTOMAS'], format="%Y-%m-%d")
    por_fecha = (confirmados_municipios.groupby(['municipio_cvegeo', 'FECHA_DEF'])
                    .size()
                    .reset_index()
                    .rename({0: 'total'}, axis=1)
                )
    confirmados_municipios_dia = (por_fecha
                                  .pivot_table("total", "FECHA_DEF", "municipio_cvegeo")
                                  .unstack()
                                  .reset_index()
                                  .fillna(0)
                                  .rename({0: 'total'}, axis=1)
                                  .set_index(['FECHA_DEF', 'municipio_cvegeo'])
                                  )
    por_semana = (confirmados_municipios_dia
                  .groupby(['municipio_cvegeo', pd.Grouper(level='FECHA_DEF', freq='W')])[['total']]
                  .sum()
                  )
    por_semana = (por_semana
                  .reset_index()
                  .set_index(['FECHA_DEF', 'municipio_cvegeo'])
                  )
    por_semana = por_semana.reset_index()
    por_semana = (por_semana
                  .set_index('FECHA_DEF')
                  .groupby('municipio_cvegeo')
                  .apply(lambda d: d.reindex(pd.date_range(min(por_semana.FECHA_DEF),
                                                           max(por_semana.FECHA_DEF),
                                                           freq='W')))
                  .drop('municipio_cvegeo', axis=1)
                  .fillna(method='ffill')
                  )
    por_semana.index.names = ['municipio_cvegeo', 'FECHA_DEF']
    por_semana.reset_index('municipio_cvegeo', inplace=True)
    por_semana['acumulados'] = por_semana.groupby('municipio_cvegeo').cumsum()
    return por_semana


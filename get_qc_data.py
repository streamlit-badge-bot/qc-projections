import pandas as pd
import streamlit as st
import requests
from io import StringIO


@st.cache
def load_qc_data():
    qc_data = pd.read_csv(
        'https://www.dropbox.com/s/ud7r3l20mzyllvm/qc-covid-stats.csv?dl=1')
    qc_data.date = pd.to_datetime(qc_data.date)
    qc_data.total_cases = pd.to_numeric(
        qc_data.total_cases, errors='coerce')
    qc_data.total_deaths = pd.to_numeric(
        qc_data.total_deaths, errors='coerce')
    qc_data.hospitalizations = pd.to_numeric(
        qc_data.hospitalizations, errors='coerce')
    qc_data.icu = pd.to_numeric(qc_data.icu, errors='coerce')
    qc_data.total_recovered = pd.to_numeric(
        qc_data.total_recovered, errors='coerce')
    qc_data.under_investigation = pd.to_numeric(
        qc_data.under_investigation, errors='coerce')

    region_data_df = pd.read_csv(
        'https://raw.githubusercontent.com/pboardman/covid19-data-quebec/master/csv/region.csv')
    region_data_df.date = pd.to_datetime(region_data_df.date)
    region_data_df.total_case = pd.to_numeric(
        region_data_df.total_case, errors='coerce')
    region_data_df.new_case = pd.to_numeric(
        region_data_df.new_case, errors='coerce')

    mtl_data_df = pd.read_csv(
        'https://raw.githubusercontent.com/pboardman/covid19-data-quebec/master/csv/montreal.csv')
    mtl_data_df.date = pd.to_datetime(mtl_data_df.date)
    mtl_data_df.total_case = pd.to_numeric(
        mtl_data_df.total_case, errors='coerce')

    mtl_ed_df = pd.read_csv(
        'https://www.dropbox.com/s/w7n297w7pnapezn/dailyMontrealEdStats.csv?dl=1')
    mtl_ed_df.date = pd.to_datetime(mtl_ed_df.date)
    # mtl_ed_df = mtl_ed_df[mtl_ed_df.date >= "2020-03-01"]

    qc_ed_stretcher_df = pd.read_csv(
        'https://www.dropbox.com/s/7idv6buofuqru5z/hourlyQuebecEDStats.csv?dl=1')
    qc_ed_stretcher_df.rename(columns={"Nom_etablissement": "etablissement", "Nom_installation": "installation",
                                       "Nombre_de_civieres_occupees": "occupied", "Heure_de_l'extraction_(image)": "timestamp"}, inplace=True)
    qc_ed_stretcher_df.timestamp = pd.to_datetime(
        qc_ed_stretcher_df.timestamp)

    # death_predictions = pd.read_csv('deaths.csv')
    # death_predictions.date = pd.to_datetime(death_predictions.date)

    # target_date = qc_data.set_index('date').iloc[-1].name
    # severity_index = (qc_data.set_index('date').iloc[-1].total_death-death_predictions.set_index('date').loc[target_date].optimistic)/(
    #     death_predictions.set_index('date').loc[target_date].pessimistic-death_predictions.set_index('date').loc[target_date].optimistic)

    # death_predictions['current'] = severity_index * \
    #     (death_predictions.pessimistic-death_predictions.optimistic) + \
    #     death_predictions.optimistic

    # return qc_data
    return qc_data, region_data_df, mtl_data_df, mtl_ed_df, qc_ed_stretcher_df


@st.cache
def load_arrondissement_data():
    arrondissement_df = pd.read_csv(
        'https://www.dropbox.com/s/n6xfww9zfk670l3/arrondissement-covid.csv?dl=1')
    arrondissement_df.date = pd.to_datetime(arrondissement_df.date)
    return arrondissement_df


@st.cache
def load_mtl_courbe():

    url = "https://santemontreal.qc.ca/fileadmin/fichiers/Campagnes/coronavirus/situation-montreal/courbe.csv"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
    req = requests.get(url, headers=headers)
    data = StringIO(req.text)

    mtl_courbe_df = pd.read_csv(
        data, sep=';', encoding="ISO-8859-1", engine='python')
    mtl_courbe_df.Date = pd.to_datetime(mtl_courbe_df.Date)
    mtl_courbe_df = mtl_courbe_df[['Date', 'Nouveaux cas', 'Cumulatif de cas']]
    mtl_courbe_df = mtl_courbe_df.dropna()
    mtl_courbe_df = mtl_courbe_df.rename(columns={
                                         'Date': 'date', 'Nouveaux cas': 'new_cases', 'Cumulatif de cas': 'total_cases'})
    return mtl_courbe_df

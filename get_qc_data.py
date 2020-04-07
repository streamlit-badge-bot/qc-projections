import pandas as pd


def load_qc_data():
    qc_data_df = pd.read_csv(
        'https://raw.githubusercontent.com/pboardman/covid19-data-quebec/master/csv/total.csv')
    qc_data_df.date = pd.to_datetime(qc_data_df.date)
    qc_data_df.total_case = pd.to_numeric(
        qc_data_df.total_case, errors='coerce')
    qc_data_df.total_death = pd.to_numeric(
        qc_data_df.total_death, errors='coerce')
    qc_data_df.total_recovered = pd.to_numeric(
        qc_data_df.total_recovered, errors='coerce')
    qc_data_df.hospitalisations = pd.to_numeric(
        qc_data_df.hospitalisations, errors='coerce')
    qc_data_df.ICU = pd.to_numeric(qc_data_df.ICU, errors='coerce')

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
    mtl_ed_df = mtl_ed_df[mtl_ed_df.date >= "2020-03-01"]

    qc_ed_stretcher_df = pd.read_csv(
        'https://www.dropbox.com/s/7idv6buofuqru5z/hourlyQuebecEDStats.csv?dl=1')
    qc_ed_stretcher_df.rename(columns={"Nom_etablissement": "etablissement", "Nom_installation": "installation",
                                       "Nombre_de_civieres_occupees": "occupied", "Heure_de_l'extraction_(image)": "timestamp"}, inplace=True)
    qc_ed_stretcher_df.timestamp = pd.to_datetime(
        qc_ed_stretcher_df.timestamp)

    # return qc_data_df
    return qc_data_df, region_data_df, mtl_data_df, mtl_ed_df, qc_ed_stretcher_df

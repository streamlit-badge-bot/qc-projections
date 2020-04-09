import pandas as pd


def load_qc_projections():
    optimistic = pd.read_csv(
        'https://www.dropbox.com/s/8jytc10m2s79y1f/forecast_optimistic.csv?dl=1')
    optimistic.date = pd.to_datetime(optimistic.date)

    pessimistic = pd.read_csv(
        'https://www.dropbox.com/s/14lxuoatjdcscov/forecast_pessimistic.csv?dl=1')
    pessimistic.date = pd.to_datetime(pessimistic.date)

    realistic = pd.read_csv(
        'https://www.dropbox.com/s/ln24925c8ffvpxr/forecast_realistic.csv?dl=1')
    realistic.date = pd.to_datetime(realistic.date)

    total_cases_projections = optimistic.rename({'total_cases': 'optimistic'}, axis=1).merge(realistic.rename(
        {'total_cases': 'realistic'}, axis=1), on='date').merge(pessimistic.rename({'total_cases': 'pessimistic'}, axis=1), on='date')

    total_deaths_projections = pd.read_csv(
        'https://www.dropbox.com/s/7kf3ge312j3czrw/projected_deaths.csv?dl=1')
    total_deaths_projections.date = pd.to_datetime(
        total_deaths_projections.date)

    return total_cases_projections, total_deaths_projections

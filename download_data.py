import os
import pandas as pd
import numpy as np
import dateutil.relativedelta as dtr
import datetime as dt

def dl_one_csv(stn, year, mth):
    url = 'https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={}&Year={}&Month={}&Day=14&timeframe=1&submit=Download+Data'.format(
        stn, year, mth)
    return pd.read_csv(url)

def get_stn_data(stn=31688, fr=dt.datetime(2002,6,1), to=dt.datetime.now()):
    out = []
    cur = fr
    while cur < to:
        print(stn, cur.year, cur.month)
        out.append(dl_one_csv(stn, cur.year, cur.month))
        cur += dtr.relativedelta(months=1)
    df = pd.concat(out)
    df.to_csv('{}_weather_data.csv'.format(stn))

if __name__ == '__main__':
    get_stn_data()

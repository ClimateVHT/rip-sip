"""Utility functions"""

import datetime
import numpy as np
import pandas as pd
import xarray as xr


def lat_index_to_value(lat_index):
    """Convert metric file latitude index to value"""

    lat_values = np.round(np.arange(-10, -44.51, -0.05), 2)
    lat_value = lat_values[lat_index]

    return lat_value


def lon_index_to_value(lon_index):
    """Convert metric file latitude index to value"""

    lon_values = np.round(np.arange(112, 156.26, 0.05), 2)
    lon_value = lon_values[lon_index]

    return lon_value
    
v_lat_index_to_value = np.vectorize(lat_index_to_value)
v_lon_index_to_value = np.vectorize(lon_index_to_value)


def read_metric_data(infile):
    """Read metric data into an xarray data array"""
    
    df = pd.read_csv(infile)
    df_indexed = df.set_index(['latitude', 'longitude'])
    da_list = []
    for year in df['date'].unique():
        df_year = df_indexed[df_indexed['date'] == year]
        da_year = df_year['out'].to_xarray()
        da_year['time'] = datetime.datetime(year, 7, 1)
        da_list.append(da_year)
    da = xr.concat(da_list, dim='time')
    da['latitude'] = v_lat_index_to_value(da['latitude'])
    da['longitude'] = v_lon_index_to_value(da['longitude'])
    da = da.rename({'latitude': 'lat', 'longitude': 'lon'})

    return da


def select_region(da, region):
    """Select a given region."""
    
    mask = region.mask_3D(da)
    mask = mask.squeeze()
    da_region = da.where(mask)

    return da_region


def regional_mean(da, region):
    """Calculate the spatial mean for a given region."""
    
    da_region = select_region(da, region)
    weights = np.cos(np.deg2rad(da['lat']))
    da_region_mean = da_region.weighted(weights).mean(dim=("lat", "lon"))
    da_region_mean = da_region_mean.drop_vars(['region', 'abbrevs', 'names'])

    return da_region_mean


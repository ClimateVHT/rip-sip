'''Command line program for spatial aggregation of metric files.'''

import glob
import argparse
import datetime
import random

import numpy as np
import pandas as pd
import xarray as xr
import cmdline_provenance as cmdprov

import definitions

# Example file location:
# /datasets/work/af-ag2050-climate/reference/ag2050_extension_metrics_outputs/100_2025-may_cdx_cs_a-e5_h_ccam-2203_q-agcd/annRain.csv


def lat_index_to_value(lat_index):
    """Convert latitude index to value"""

    lat_values = np.round(np.arange(-10, -44.51, -0.05), 2)
    lat_value = lat_values[lat_index]

    return lat_value


def lon_index_to_value(lon_index):
    """Convert latitude index to value"""

    lon_values = np.round(np.arange(112, 156.26, 0.05), 2)
    lon_value = lon_values[lon_index]

    return lon_value
    
v_lat_index_to_value = np.vectorize(lat_index_to_value)
v_lon_index_to_value = np.vectorize(lon_index_to_value)


def read_data(infile):
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


def spatial_mean(da, region):
    """Calculate the spatial mean for a given region."""
    
    mask = region.mask_3D(da)
    mask = mask.squeeze()
    da_region = da.where(mask)
    weights = np.cos(np.deg2rad(da['lat']))
    da_region_mean = da_region.weighted(weights).mean(dim=("lat", "lon"))
    da_region_mean = da_region_mean.drop_vars(['region', 'abbrevs', 'names'])

    return da_region_mean


def add_metadata(ds, metric_name, rcm_name, region_abbrev):
    """Add metadata to the output dataset"""
   
    ds = ds.rename({'out': metric_name})
    ds[metric_name].attrs = definitions.METRIC_ATTRS[metric_name]
    ds['experiment'].attrs['long_name'] = 'Emission scenario'
    ds['gcm'].attrs['long_name'] = 'Global Climate Model'
    ds['gcm'].attrs['format'] = 'gcm_run'
    ds['bc'].attrs['long_name'] = 'Bias correction method'
    ds['time'].attrs['long_name'] = 'time'
    ds['time'].attrs['standard_name'] = 'time'
    ds['time'].attrs['axis'] = 'T'
    
    ds.attrs['history'] = cmdprov.new_log(code_url='https://github.com/ClimateVHT/rip-sip')
    region_name = definitions.REGION_NAME[region_abbrev]
    region_source = definitions.REGION_SOURCE[region_abbrev]
    ds.attrs['rcm'] = rcm_name
    ds.attrs['processing'] = f'Area-weighted spatial average over the {region_name} (shapefiles at {region_source})'

    encoding = {}
    encoding['time'] = {}
    encoding['time']['units'] = 'days since 1850-01-01'
    
    return ds, encoding
    
    
def main(args):
    '''Run the program.'''

    gcms = definitions.GCM_NAME[args.rcm].keys()
    exps = definitions.EXPERIMENT_NAME.keys()
    biases = list(definitions.BIAS_NAME.keys())
    if args.shuffle:
        random.shuffle(biases)
    dir_start = '/datasets/work/af-ag2050-climate/reference/ag2050_extension_metrics_outputs'
    region = definitions.REGION_FUNC[args.region](args.region)
    rcm_name = definitions.RCM_NAME[args.rcm]
    exp_dict = {}
    for exp in exps:
        exp_name = definitions.EXPERIMENT_NAME[exp]
        gcm_list = []
        for gcm in gcms:
            gcm_name = definitions.GCM_NAME[args.rcm][gcm]
            bc_list = []
            for bias in biases:
                bias_name = definitions.BIAS_NAME[bias]
                fpattern = f'{dir_start}/*_{gcm}_{exp}_{args.rcm}_{bias}/{args.metric}.csv'
                infile = glob.glob(fpattern)
                if len(infile) == 1:
                    try:
                        print(infile[0])
                        da = read_data(infile[0])
                        da_region_mean = spatial_mean(da, region)
                    except ValueError:
                        print(f'problem processing metric file: {infile[0]}. Skipping.')
                        da_region_mean = bc_list[-1] * np.nan
                else:
                    print(f'no metric file at {fpattern}')
                    da_region_mean = bc_list[-1] * np.nan
                da_region_mean['bc'] = bias_name
                bc_list.append(da_region_mean)
            da_bias = xr.concat(bc_list, dim='bc')
            run = definitions.RUN[(gcm, args.rcm)]  
            da_bias['gcm'] = f'{gcm_name}_{run}' 
            gcm_list.append(da_bias)
        da_gcm = xr.concat(gcm_list, dim='gcm')
        exp_dict[exp_name] = da_gcm

    ds_ssp126 = xr.combine_by_coords([exp_dict['historical'], exp_dict['ssp126']])
    ds_ssp126['experiment'] = 'ssp126'
    ds_ssp370 = xr.combine_by_coords([exp_dict['historical'], exp_dict['ssp370']])
    ds_ssp370['experiment'] = 'ssp370'
    ds_ssp = xr.concat([ds_ssp126, ds_ssp370], dim='experiment')
    ds_out, encoding = add_metadata(ds_ssp, args.metric, rcm_name, args.region)
    ds_out.to_netcdf(args.outfile, encoding=encoding)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    metrics = list(definitions.METRIC_ATTRS.keys())
    rcms = list(definitions.RCM_NAME.keys())
    regions = list(definitions.REGION_NAME.keys())
    parser.add_argument('metric', type=str, choices=metrics, help='input variable')
    parser.add_argument('rcm', type=str, choices=rcms, help='rcm to process')
    parser.add_argument('region', type=str, choices=regions, help='region for spatial aggregation')
    parser.add_argument('outfile', type=str, help='output file')
    parser.add_argument('--shuffle', action='store_true', default=False, help='shuffle bias order to avoid error')
    args = parser.parse_args()
    main(args)

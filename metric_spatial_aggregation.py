'''Command line program for spatial aggregation of metric files.'''

import glob
import argparse
import datetime

import numpy as np
import pandas as pd
import xarray as xr
import geopandas as gp
import regionmask
import cmdline_provenance as cmdprov

import definitions

##output files:
#- BOM
#- CSIRO
#- NSW Government
#- UQ (CCAMoc-v2112)
#- UQ (CCAM-v2112)
#- UQ (CCAM-v210)

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


def read_region(region_name):
    """Read shapefile for a given broadacre region"""
        
    broadacre_gdf = gp.read_file('aagis_asgs16v1_g5a.shp_/aagis_asgs16v1_g5a.shp')
    if region_name == 'aus-wheatbelt':
        wheatbelt_gdf = broadacre_gdf[broadacre_gdf.zone == 'Wheat Sheep']
        wheatbelt = wheatbelt_gdf.dissolve()
        wheatbelt = wheatbelt.drop(columns=['aagis', 'class', 'name'])
        region = regionmask.from_geopandas(
            wheatbelt, names="zone", name="aus-wheatbelt"
        )
    else:
        raise ValueError(f'{region_name} is not a recognised region')
    
    return region


def spatial_mean(da, region):
    """Calculate the spatial mean for a given region."""
    
    mask = region.mask_3D(da)
    mask = mask.squeeze()
    da_region = da.where(mask)
    weights = np.cos(np.deg2rad(da['lat']))
    da_region_mean = da_region.weighted(weights).mean(dim=("lat", "lon"))
    da_region_mean = da_region_mean.drop_vars(['region', 'abbrevs', 'names'])

    return da_region_mean


def add_metadata(ds, metric_name, region_name):
    """Add metadata to the output dataset"""
   
    ds = ds.rename({'out': metric_name})
    ds[metric_name].attrs = definitions.METRIC_ATTRS[metric_name]
    ds['experiment'].attrs['long_name'] = 'Emission scenario'
    ds['rcm'].attrs['long_name'] = 'Regional Climate Model'
    ds['gcm'].attrs['long_name'] = 'Global Climate Model'
    ds['gcm'].attrs['format'] = 'gcm_run'
    ds['bc'].attrs['long_name'] = 'Bias correction method'
    ds['time'].attrs['long_name'] = 'time'
    ds['time'].attrs['standard_name'] = 'time'
    ds['time'].attrs['axis'] = 'T'
    
    ds.attrs['history'] = cmdprov.new_log(code_url='https://github.com/DamienIrving/rip-sip')
    ds.attrs['processing'] = f'Area-weighted average over the {region_name} spatial region'
    
    encoding = {}
    encoding['time'] = {}
    encoding['time']['units'] = 'days since 1850-01-01'
    
    return ds, encoding
    
    
def main(args):
    '''Run the program.'''

    gcms = definitions.GCM_NAMES[args.institution].keys()
    rcms = definitions.RCM_NAMES[args.institution].keys()
    exps = definitions.EXPERIMENT_NAMES.keys()
    biases = definitions.BIAS_NAMES.keys()
    dir_start = '/datasets/work/af-ag2050-climate/reference/ag2050_extension_metrics_outputs'
    region = read_region(args.region)
    exp_dict = {}
    for exp in exps:
        exp_name = definitions.EXPERIMENT_NAMES[exp]
        gcm_list = []
        for gcm in gcms:
            gcm_name = definitions.GCM_NAMES[args.institution][gcm]
            rcm_list = []
            for rcm in rcms:
                rcm_name = definitions.RCM_NAMES[args.institution][rcm]
                bc_list = []
                for bias in biases:
                    bias_name = definitions.BIAS_NAMES[bias]
                    fpattern = f'{dir_start}/*_{gcm}_{exp}_{rcm}_{bias}/{args.metric}.csv'
                    infile = glob.glob(fpattern)
                    assert len(infile) == 1, f'problem locating metric file at {fpattern}'
                    print(infile[0])
                    da = read_data(infile[0])
                    da_region_mean = spatial_mean(da, region)
                    da_region_mean['bc'] = bias_name
                    bc_list.append(da_region_mean)
                da_bias = xr.concat(bc_list, dim='bc')
                da_bias['rcm'] = rcm_name
                rcm_list.append(da_bias)
            da_rcm = xr.concat(rcm_list, dim='rcm')
            run = definitions.RUNS[(gcm_name, rcm_name)]
            da_rcm['gcm'] = f'{gcm_name}_{run}'
            gcm_list.append(da_rcm)
        da_gcm = xr.concat(gcm_list, dim='gcm')     
        exp_dict[exp_name] = da_gcm
    
    ds_ssp126 = xr.combine_by_coords([exp_dict['historical'], exp_dict['ssp126']])
    ds_ssp126['experiment'] = 'ssp126'
    ds_ssp370 = xr.combine_by_coords([exp_dict['historical'], exp_dict['ssp370']])
    ds_ssp370['experiment'] = 'ssp370'
    ds_ssp = xr.concat([ds_ssp126, ds_ssp370], dim='experiment')
    ds_out, encoding = add_metadata(ds_ssp, args.metric, args.region)
    ds_out.to_netcdf(args.outfile, encoding=encoding)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    metrics = list(definitions.METRIC_ATTRS.keys())
    institutions = list(definitions.INSTITUTION_NAMES.keys())
    parser.add_argument('metric', type=str, choices=metrics, help='input variable')
    parser.add_argument('institution', type=str, choices=institutions, help='institution to process')
    parser.add_argument('region', type=str, choices=('aus-wheatbelt',), help='region for spatial aggregation')
    parser.add_argument('outfile', type=str, help='output file')
    args = parser.parse_args()
    main(args)

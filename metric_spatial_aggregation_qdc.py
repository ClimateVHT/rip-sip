'''Command line program for spatial aggregation of QDC metric files.'''

import glob
import argparse
import random

import numpy as np
import xarray as xr
import cmdline_provenance as cmdprov

import utils
import definitions

# Example file location:
# /datasets/work/af-ag2050-climate/reference/ag2050_extension_metrics_outputs/477_2026-march_qdc_cs_a-e5_s585_qdc_agcd_2035-2064/annRain.csv


def add_metadata(da, metric_name, region_abbrev):
    """Add metadata to the output dataset"""
   
    ds = da.to_dataset(name=metric_name)
    ds[metric_name].attrs = definitions.METRIC_ATTRS[metric_name]
    ds['experiment'].attrs['long_name'] = 'Emission scenario'
    ds['gcm'].attrs['long_name'] = 'Global Climate Model'
    ds['gcm'].attrs['format'] = 'gcm_run'
    ds['obs'].attrs['long_name'] = 'Observations that were scaled'
    ds['time'].attrs['long_name'] = 'time'
    ds['time'].attrs['standard_name'] = 'time'
    ds['time'].attrs['axis'] = 'T'
    
    ds.attrs['history'] = cmdprov.new_log(code_url='https://github.com/ClimateVHT/rip-sip')
    region_name = definitions.REGION_NAME[region_abbrev]
    region_source = definitions.REGION_SOURCE[region_abbrev]
    ds.attrs['scaling_method'] = 'Quantile Delta Change (https://doi.org/10.25919/03by-9y62)'
    ds.attrs['processing'] = f'Area-weighted spatial average over the {region_name} (shapefiles at {region_source})'

    encoding = {}
    encoding['time'] = {}
    encoding['time']['units'] = 'days since 1850-01-01'
    
    return ds, encoding
    
    
def main(args):
    '''Run the program.'''

    dir_start = '/datasets/work/af-ag2050-climate/reference/ag2050_extension_metrics_outputs'
    obs_file = {}
    obs_file['agcd'] = f'{dir_start}/469_2025-june_qdc_bom_raw_h_raw_agcd/{args.metric}.csv'
    obs_file['barra'] = f'{dir_start}/470_2025-june_qdc_bom_raw_h_raw_barra/{args.metric}.csv'

    gcms = definitions.GCM_NAME['qdc'].keys()
    exps = ['s126' , 's245', 's370', 's585']
    dir_start = '/datasets/work/af-ag2050-climate/reference/ag2050_extension_metrics_outputs'
    region = definitions.REGION_FUNC[args.region](args.region)

    dummy_arrays = {}
    exp_list = []
    for exp in exps:
        exp_name = definitions.EXPERIMENT_NAME[exp]
        gcm_list = []
        for number, gcm in enumerate(gcms):
            gcm_name = definitions.GCM_NAME['qdc'][gcm]
            obs_list = []
            for obs in ['agcd', 'barra']:
                obs_name = definitions.OBS_NAME[obs]
                fpattern = f'{dir_start}/*_{gcm}_{exp}_qdc_{obs}_*/{args.metric}.csv'
                infiles = sorted(glob.glob(fpattern))
                if len(infiles) == 2:
                    try:
                        print(infiles)
                        da0 = utils.read_metric_data(obs_file[obs])
                        da1 = utils.read_metric_data(infiles[0])
                        da2 = utils.read_metric_data(infiles[1])
                        da = xr.concat([da0, da1, da2], dim='time')
                        da_region_mean = utils.regional_mean(da, region)
                    except ValueError:
                        print(f'problem processing metric files: {infiles}. Skipping.')
                        da_region_mean = dummy_arrays[obs]
                else:
                    print(f'no metric files at {fpattern}')
                    da_region_mean = dummy_arrays[obs] 
                da_region_mean['obs'] = obs_name
                if number == 0:
                    dummy_arrays[obs] = da_region_mean * np.nan
                obs_list.append(da_region_mean)
            da_obs = xr.concat(obs_list, dim='obs')
            run = definitions.RUN[(gcm, 'qdc')]  
            da_obs['gcm'] = f'{gcm_name}_{run}' 
            gcm_list.append(da_obs)
        da_gcm = xr.concat(gcm_list, dim='gcm')
        da_gcm['experiment'] = exp_name
        exp_list.append(da_gcm)
    da_exp = xr.concat(exp_list, dim='experiment')

    ds_out, encoding = add_metadata(da_exp, args.metric, args.region)
    ds_out.to_netcdf(args.outfile, encoding=encoding)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    metrics = list(definitions.METRIC_ATTRS.keys())
    regions = list(definitions.REGION_NAME.keys())
    parser.add_argument('metric', type=str, choices=metrics, help='input variable')
    parser.add_argument('region', type=str, choices=regions, help='region for spatial aggregation')
    parser.add_argument('outfile', type=str, help='output file')
    args = parser.parse_args()
    main(args)

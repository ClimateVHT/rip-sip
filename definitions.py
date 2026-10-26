"""Module containing various abbreviations and file attributes"""

import geopandas as gp
import regionmask


# Data reference syntax for metric files

OBS_NAME = {'agcd': 'AGCD', 'barra': 'BARRA-R2'}

EXPERIMENT_NAME = {
    'h': 'historical',
    's126': 'ssp126',
    's245': 'ssp245',
    's370': 'ssp370',
    's585': 'ssp585',
}

BIAS_NAME = {
    'm-agcd': 'v1-r1-ACS-MRNBC-AGCDv1-1960-2022',
    'q-agcd': 'v1-r1-ACS-QME-AGCDv1-1960-2022',
    'm-barra': 'v1-r1-ACS-MRNBC-BARRAR2-1980-2022',
    'q-barra': 'v1-r1-ACS-QME-BARRAR2-1980-2022',
}

RCM_NAME = {
    'bar': 'BARPA-R',
    'ccam-2203': 'CCAM-v2203-SN',
    'nar-r3': 'NARCliM2-0-WRF412R3',
    'nar-r5': 'NARCliM2-0-WRF412R5',
    'ccamo-2112': 'CCAMoc-v2112',
    'ccamo-2112-r4': 'CCAMoc-v2112',
    'ccamo-2112-r2': 'CCAMoc-v2112',
    'ccam-2112': 'CCAM-v2112',
    'ccam-2105': 'CCAM-v2105',
    'ccam-2105-r6': 'CCAM-v2105',
}

GCM_NAME = {}
GCM_NAME['bar'] = {
    'a-cm2': 'ACCESS-CM2',
    'a-e5': 'ACCESS-ESM1-5',
    'ce2': 'CESM2',
    'cm-e2': 'CMCC-ESM2',
    'ea-3': 'EC-Earth3',
    'mpi-2h': 'MPI-ESM1-2-HR', 
    'nor-mm': 'NorESM2-MM',
}
GCM_NAME['ccam-2203'] = {
    'a-cm2': 'ACCESS-CM2',
    'a-e5': 'ACCESS-ESM1-5',
    'ce2': 'CESM2',
    'cm-e2': 'CMCC-ESM2',
    'cn-e21': 'CNRM-ESM2-1',
    'ea-3': 'EC-Earth3',
    'nor-mm': 'NorESM2-MM',
}
GCM_NAME['nar-r3'] = {
    'a-e5': 'ACCESS-ESM1-5',
    'ea-3v': 'EC-Earth3-Veg',
    'mpi-2h': 'MPI-ESM1-2-HR', 
    'nor-mm': 'NorESM2-MM',
    'uk-0ll': 'UKESM1-0-LL' 
}
GCM_NAME['nar-r5'] = {
    'a-e5': 'ACCESS-ESM1-5',
    'ea-3v': 'EC-Earth3-Veg',
    'mpi-2h': 'MPI-ESM1-2-HR', 
    'nor-mm': 'NorESM2-MM',
    'uk-0ll': 'UKESM1-0-LL' 
} 
GCM_NAME['ccamo-2112'] = {
    'a-cm2': 'ACCESS-CM2',
    'cn-c61': 'CNRM-CM6-1-HR',
    'nor-mm': 'NorESM2-MM',
}
GCM_NAME['ccamo-2112-r2'] = {
    'a-e5': 'ACCESS-ESM1-5',
}
GCM_NAME['ccamo-2112-r4'] = {
    'a-e5': 'ACCESS-ESM1-5',
}
GCM_NAME['ccam-2112'] = {
    'cn-c61': 'CNRM-CM6-1-HR',
    'nor-mm': 'NorESM2-MM',
}
GCM_NAME['ccam-2105'] = {
    'cm-e2': 'CMCC-ESM2',
    'ea-3': 'EC-Earth3',
    'fg-3': 'FGOALS-g3',
    'gf-e4': 'GFDL-ESM4',
    'gi-e2g': 'GISS-E2-1-G',
    'mpi-2l': 'MPI-ESM1-2-LR',
    'mri-e0': 'MRI-ESM2-0', 
}
GCM_NAME['ccam-2105-r6'] = {
    'a-e5': 'ACCESS-ESM1-5',
}
GCM_NAME['qdc'] = {
    'a-cm2': 'ACCESS-CM2',
    'a-e5': 'ACCESS-ESM1-5',
    'ce2': 'CESM2',
    'cm-e2': 'CMCC-ESM2',
    'cn-e21': 'CNRM-ESM2-1',
    'ea-3': 'EC-Earth3',
    'mpi-2h': 'MPI-ESM1-2-HR', 
    'nor-mm': 'NorESM2-MM',
    'uk-0ll': 'UKESM1-0-LL' 
}

RUN = {
    ('a-cm2', 'ccamo-2112'): 'r2i1p1f1',
    ('a-cm2', 'bar'): 'r4i1p1f1',
    ('a-cm2', 'ccam-2203'): 'r4i1p1f1',
    ('a-cm2', 'qdc'): 'r4i1p1f1',
    ('a-e5', 'bar'): 'r6i1p1f1',
    ('a-e5', 'ccam-2105-r6'): 'r6i1p1f1',
    ('a-e5', 'ccam-2203'): 'r6i1p1f1',
    ('a-e5', 'nar-r3'): 'r6i1p1f1',
    ('a-e5', 'nar-r5'): 'r6i1p1f1',
    ('a-e5', 'qdc'): 'r6i1p1f1',
    ('a-e5', 'ccamo-2112-r2'): 'r20i1p1f1',
    ('a-e5', 'ccamo-2112-r4'): 'r40i1p1f1',
    ('ce2', 'bar'): 'r11i1p1f1',
    ('ce2', 'ccam-2203'): 'r11i1p1f1',
    ('ce2', 'qdc'): 'r11i1p1f1',
    ('cm-e2', 'bar'): 'r1i1p1f1',
    ('cm-e2', 'ccam-2105'): 'r1i1p1f1',
    ('cm-e2', 'ccam-2203'): 'r1i1p1f1',
    ('cm-e2', 'qdc'): 'r1i1p1f1',
    ('cn-c61', 'ccamo-2112'): 'r1i1p1f2',
    ('cn-c61', 'ccam-2112'): 'r1i1p1f2',
    ('cn-e21', 'ccam-2203'): 'r1i1p1f2',
    ('cn-e21', 'qdc'): 'r1i1p1f2',
    ('ea-3', 'bar'): 'r1i1p1f1',
    ('ea-3', 'ccam-2105'): 'r1i1p1f1',
    ('ea-3', 'ccam-2203'): 'r1i1p1f1',
    ('ea-3', 'qdc'): 'r1i1p1f1',
    ('ea-3v', 'nar-r3'): 'r1i1p1f1',
    ('ea-3v', 'nar-r5'): 'r1i1p1f1',
    ('fg-3', 'ccam-2105'): 'r4i1p1f1',
    ('gf-e4', 'ccam-2105'): 'r1i1p1f1',
    ('gi-e2g', 'ccam-2105'): 'r2i1p1f2',
    ('mpi-2h', 'bar'): 'r1i1p1f1',
    ('mpi-2h', 'qdc'): 'r1i1p1f1',
    ('mpi-2h', 'nar-r3'): 'r1i1p1f1',
    ('mpi-2h', 'nar-r5'): 'r1i1p1f1',
    ('mpi-2l', 'ccam-2105'): 'r9i1p1f1',
    ('mri-e0', 'ccam-2105'): 'r1i1p1f1',
    ('nor-mm', 'bar'): 'r1i1p1f1',
    ('nor-mm', 'ccamo-2112'): 'r1i1p1f1',
    ('nor-mm', 'ccam-2112'): 'r1i1p1f1',
    ('nor-mm', 'ccam-2203'): 'r1i1p1f1',
    ('nor-mm', 'nar-r3'): 'r1i1p1f1',
    ('nor-mm', 'nar-r5'): 'r1i1p1f1',
    ('nor-mm', 'qdc'): 'r1i1p1f1',
    ('uk-0ll', 'nar-r3'): 'r1i1p1f2',
    ('uk-0ll', 'nar-r5'): 'r1i1p1f2',
    ('uk-0ll', 'qdc'): 'r1i1p1f2',
}


# Metric attributes

METRIC_ATTRS = {} 
METRIC_ATTRS['livestockFSunaltered'] = {
    'long_name': 'livestock farm stocking rate unaltered',
    'units': 'dse/ha',
}
METRIC_ATTRS['livestockFS50CC'] = {
    'long_name': 'livestock farm stocking rate with carrying capacity reduced by 50%',
    'units': 'dse/ha',
}
METRIC_ATTRS['livestockFSgrowingseasonSTH'] = {
    'long_name': 'livestock farm stocking rate during the southern Australia growing season (Apr-Oct)',
    'units': 'dse/ha',
}
METRIC_ATTRS['livestockFSgrowingseasonNTH'] = {
    'long_name': 'livestock farm stocking rate during the northern Australia growing season (Oct-Apr)',  # which months?
    'units': 'dse/ha',
}
METRIC_ATTRS['croppingFS'] = {
    'long_name': 'Estimated crop yield using the French-Schultz potential yield calculation',
    'units': 't/ha',
}
METRIC_ATTRS['THItemperate'] = {
    'long_name': 'Temperature-humidity index calibrated for a temperate climate',
    'units': 'ndays',
}
METRIC_ATTRS['THItropical'] = {
    'long_name': 'Temperature-humidity index calibrated for a tropical climate',
    'units': 'ndays',
}
METRIC_ATTRS['annRain'] = {
    'long_name': 'Total annual rainfall',
    'units': 'mm',
}
METRIC_ATTRS['annAveTmax'] = {
    'long_name': 'Annual average daily maximum temperature',
    'units': 'degC',
}
METRIC_ATTRS['annAveTmin'] = {
    'long_name': 'Annual average daily minimum temperature',
    'units': 'degC',
}
METRIC_ATTRS['summerPR'] = {
    'long_name': 'Total summer precipitation (DJF)',
    'units': 'mm',
}
METRIC_ATTRS['autummPR'] = {
    'long_name': 'Total autumn precipitation (MAM)',
    'units': 'mm',
}
METRIC_ATTRS['winterPR'] = {
    'long_name': 'Total winter precipitation (JJA)',
    'units': 'mm',
}
METRIC_ATTRS['springPR'] = {
    'long_name': 'Total spring precipitation (SON)',
    'units': 'mm',
}
METRIC_ATTRS['drySeasonPR'] = {
    'long_name': 'Total dry season precipitation (May-Aug)',
    'units': 'mm',
}
METRIC_ATTRS['wetSeasonPR'] = {
    'long_name': 'Total wet season precipitation (Oct-Apr)',
    'units': 'mm',
}
METRIC_ATTRS['annHotdays'] = {
    'long_name': 'Annual number of hot days', #threshold for hot??
    'units': 'ndays',
}
METRIC_ATTRS['springFrostdays'] = {
    'long_name': 'Number of frost days in spring (SON)',
    'units': 'ndays',
}


# Regions

def get_broadacre_region(region_name):
    """Read shapefile for a given broadacre region"""
        
    broadacre_gdf = gp.read_file('shapefiles/aagis_asgs16v1_g5a.shp')
    if region_name == 'wheatbelt':
        gdf = broadacre_gdf[broadacre_gdf.zone == 'Wheat Sheep']
    elif region_name == 'cropping':
        gdf = broadacre_gdf[broadacre_gdf.zone != 'Pastoral']
    else:
        raise ValueError(f'{region_name} is not a recognised broadacre region')
    
    gdf = gdf.dissolve()
    gdf = gdf.drop(columns=['aagis', 'class', 'name'])
    region = regionmask.from_geopandas(
        gdf, names="zone", name=region_name
    )

    return region


def get_ncra_region(region_name):
    """Read shapefile for a given NCRA region"""
    
    ncra_gdf = gp.read_file(f'shapefiles/{region_name}_shp_processed.shp')
    region = regionmask.from_geopandas(ncra_gdf, names="region", name=region_name)
    
    return region


REGION_FUNC = {
    'wheatbelt': get_broadacre_region,
    'cropping': get_broadacre_region,
    'ncra_sth': get_ncra_region,
    'ncra_nth': get_ncra_region,
    'mod_ncra_nth': get_ncra_region,
    'wine': get_ncra_region,
    'forestry': get_ncra_region,
    'summer_cropping': get_ncra_region,
        
}

REGION_NAME = {
    'wheatbelt': 'ABARES wheat sheep broadacre zone',
    'cropping': 'ABARES wheat sheep and high rainfall broadacre zones combined',
    'ncra_sth': 'NCRA southern Australia region',
    'ncra_nth': 'NCRA northern Australia region',
    'mod_ncra_nth': 'modified NCRA northern Australia region',
    'wine': 'NCRA Australian wine region',
    'forestry': 'NCRA Australian forestry region',  
    'summer_cropping': 'NCRA Australian summer cropping region', 
}

REGION_SOURCE = {
    'wheatbelt': 'https://www.agriculture.gov.au/abares/research-topics/surveys/farm-survey-data',
    'cropping': 'https://www.agriculture.gov.au/abares/research-topics/surveys/farm-survey-data',
    'ncra_sth': 'https://doi.org/10.25919/8tqq-0007',
    'ncra_nth': 'https://doi.org/10.25919/8tqq-0007',
    'mod_ncra_nth': 'https://doi.org/10.25919/8tqq-0007',
    'wine': 'https://doi.org/10.25919/8tqq-0007',
    'forestry': 'https://doi.org/10.25919/8tqq-0007',
    'summer_cropping': 'https://doi.org/10.25919/8tqq-0007',
}



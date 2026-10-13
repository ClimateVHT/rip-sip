"""Module containing various abbreviations and file attributes"""

# Data reference syntax for metric files

EXPERIMENT_NAME = {
    'h': 'historical',
    's126': 'ssp126',
    's370': 'ssp370',
}

BIAS_NAME = {
    'm-agcd': 'v1-r1-ACS-MRNBC-AGCDv1-1960-2022',
    'q-agcd': 'v1-r1-ACS-QME-AGCDv1-1960-2022',
    'm-barra': 'v1-r1-ACS-MRNBC-BARRAR2-1980-2022',
    'q-barra': 'v1-r1-ACS-QME-BARRAR2-1980-2022',
}

INSTITUTION_NAME = {
    'bom': 'BOM',
    'cs': 'CSIRO',
    'nsw': 'NSW-Government',
    'uq-ccamo-2112': 'UQ-DEC',
    'uq-ccam-2112': 'UQ-DEC',
    'uq-ccam-2105': 'UQ-DEC',
}

GCM_NAME = {}
GCM_NAME['bom'] = {
    'a-cm2': 'ACCESS-CM2',
    'a-e5': 'ACCESS-ESM1-5',
    'ce2': 'CESM2',
    'cm-e2': 'CMCC-ESM2',
    'ea-3': 'EC-Earth3',
    'mpi-2h': 'MPI-ESM1-2-HR', 
    'nor-mm': 'NorESM2-MM',
}
GCM_NAME['cs'] = {
    'a-cm2': 'ACCESS-CM2',
    'a-e5': 'ACCESS-ESM1-5',
    'ce2': 'CESM2',
    'cm-e2': 'CMCC-ESM2',
    'cn-c61': 'CNRM-CM6-1-HR',
    'ea-3': 'EC-Earth3',
    'nor-mm': 'NorESM2-MM',
}
GCM_NAME['nsw'] = {
    'a-e5': 'ACCESS-ESM1-5',
    'ea-3v': 'EC-Earth3-Veg',
    'mpi-2h': 'MPI-ESM1-2-HR', 
    'nor-mm': 'NorESM2-MM',
    'uk-0ll': 'UKESM1-0-LL' 
} 
GCM_NAME['uq-ccamo-2112'] = {
    'a-cm2': 'ACCESS-CM2',
    'a-e5': 'ACCESS-ESM1-5',
    'cn-c61': 'CNRM-CM6-1-HR',
    'nor-mm': 'NorESM2-MM',
}
GCM_NAME['uq-ccam-2112'] = {
    'cn-c61': 'CNRM-CM6-1-HR',
    'nor-mm': 'NorESM2-MM',
}
GCM_NAME['uq-ccam-2105'] = {
    'a-e5': 'ACCESS-ESM1-5',
    'cm-e2': 'CMCC-ESM2',
    'ea-3': 'EC-Earth3',
    'fg-3': 'FGOALS-g3',
    'gf-e4': 'GFDL-ESM4',
    'gi-e2g': 'GISS-E2-1-G',
    'mpi-2l': 'MPI-ESM1-2-LR',
    'mri-e0': 'MRI-ESM2-0', 
}

RCM_NAME = {}
RCM_NAME['bom'] = {'bar': 'BARPA-R'}
RCM_NAME['cs'] = {'ccam-2203': 'CCAM-v2203-SN'}
RCM_NAME['nsw'] = {'nar-r3': 'NARCliM2-0-WRF412R3', 'nar-r5': 'NARCliM2-0-WRF412R5'}
RCM_NAME['uq-ccamo-2112'] = {'ccamo-2112': 'CCAMoc-v2112'}
RCM_NAME['uq-ccam-2112'] = {'ccam-2112': 'CCAM-v2112'}
RCM_NAME['uq-ccam-2105'] = {'ccam-2105-r6': 'CCAM-v2105_r6i1p1f1'}
RCM_NAME['uq-ccamo-2112-r4'] = {'ccamo-2112-r4': 'CCAMoc-v2112_r40i1p1f1'}
RCM_NAME['uq-ccamo-2112-r2'] = {'ccamo-2112-r2': 'CCAMoc-v2112_r20i1p1f1'}

RUN = {
    ('ACCESS-CM2', 'CCAMoc-v2112'): 'r2i1p1f1',
    ('ACCESS-CM2', 'BARPA-R'): 'r4i1p1f1',
    ('ACCESS-CM2', 'CCAM-v2203-SN'): 'r4i1p1f1',
    ('ACCESS-ESM1-5', 'BARPA-R'): 'r6i1p1f1',
    ('ACCESS-ESM1-5', 'CCAM-v2105'): 'r6i1p1f1',
    ('ACCESS-ESM1-5', 'CCAM-v2203-SN'): 'r6i1p1f1',
    ('ACCESS-ESM1-5', 'NARCliM2-0-WRF412R3'): 'r6i1p1f1',
    ('ACCESS-ESM1-5', 'NARCliM2-0-WRF412R5'): 'r6i1p1f1',
    ('ACCESS-ESM1-5', 'CCAMoc-v2112'): 'r20i1p1f1',
    ('ACCESS-ESM1-5', 'CCAMoc-v2112'): 'r40i1p1f1',
    ('CESM2', 'BARPA-R'): 'r11i1p1f1',
    ('CESM2', 'CCAM-v2203-SN'): 'r11i1p1f1',
    ('CMCC-ESM2', 'BARPA-R'): 'r1i1p1f1',
    ('CMCC-ESM2', 'CCAM-v2105'): 'r1i1p1f1',
    ('CMCC-ESM2', 'CCAM-v2203-SN'): 'r1i1p1f1',
    ('CNRM-CM6-1-HR', 'CCAMoc-v2112'): 'r1i1p1f2',
    ('CNRM-CM6-1-HR', 'CCAM-v2112'): 'r1i1p1f2',
    ('CNRM-ESM2-1', 'CCAM-v2203-SN'): 'r1i1p1f2',
    ('EC-Earth3', 'BARPA-R'): 'r1i1p1f1',
    ('EC-Earth3', 'CCAM-v2105'): 'r1i1p1f1',
    ('EC-Earth3', 'CCAM-v2203-SN'): 'r1i1p1f1',
    ('EC-Earth3-Veg', 'NARCliM2-0-WRF412R3'): 'r1i1p1f1',
    ('EC-Earth3-Veg', 'NARCliM2-0-WRF412R5'): 'r1i1p1f1',
    ('FGOALS-g3', 'CCAM-v2105'): 'r4i1p1f1',
    ('GFDL-ESM4', 'CCAM-v2105'): 'r1i1p1f1',
    ('GISS-E2-1-G', 'CCAM-v2105'): 'r2i1p1f2',
    ('MPI-ESM1-2-HR', 'BARPA-R'): 'r1i1p1f1',
    ('MPI-ESM1-2-LR', 'CCAM-v2105'): 'r9i1p1f1',
    ('MPI-ESM1-2-HR', 'NARCliM2-0-WRF412R3'): 'r1i1p1f1',
    ('MPI-ESM1-2-HR', 'NARCliM2-0-WRF412R5'): 'r1i1p1f1',
    ('MRI-ESM2-0', 'CCAM-v2105'): 'r1i1p1f1',
    ('NorESM2-MM', 'BARPA-R'): 'r1i1p1f1',
    ('NorESM2-MM', 'CCAMoc-v2112'): 'r1i1p1f1',
    ('NorESM2-MM', 'CCAM-v2112'): 'r1i1p1f1',
    ('NorESM2-MM', 'CCAM-v2203-SN'): 'r1i1p1f1',
    ('NorESM2-MM', 'NARCliM2-0-WRF412R3'): 'r1i1p1f1',
    ('NorESM2-MM', 'NARCliM2-0-WRF412R5'): 'r1i1p1f1',
    ('UKESM1-0-LL', 'NARCliM2-0-WRF412R3'): 'r1i1p1f2',
    ('UKESM1-0-LL', 'NARCliM2-0-WRF412R5'): 'r1i1p1f2',
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
    'units': 'days', #???
}
METRIC_ATTRS['THItropical'] = {
    'long_name': 'Temperature-humidity index calibrated for a tropical climate',
    'units': 'days',  #???
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
    'units': 'days',
}
METRIC_ATTRS['springFrostdays'] = {
    'long_name': 'Number of frost days in spring (SON)',
    'units': 'days',
}


# Regions

def get_broadacre_region(region_name):
    """Read shapefile for a given broadacre region"""
        
    broadacre_gdf = gp.read_file('shapefiles/aagis_asgs16v1_g5a.shp')
    if region_name == 'wheatbelt':
        wheatbelt_gdf = broadacre_gdf[broadacre_gdf.zone == 'Wheat Sheep']
        wheatbelt = wheatbelt_gdf.dissolve()
        wheatbelt = wheatbelt.drop(columns=['aagis', 'class', 'name'])
        region = regionmask.from_geopandas(
            wheatbelt, names="zone", name="wheatbelt"
        )
    else:
        raise ValueError(f'{region_name} is not a recognised broadacre region')
    
    return region

def get_ncra_region(region_name):
    """Read shapefile for a given NCRA region"""
    
    ncra_gdf = gp.read_file(f'shapefiles/{region_name}_shp_processed.shp')
    region = regionmask.from_geopandas(ncra_gdf, names="region", name=region_name)
    
    return region

REGION_FUNC = {
    'wheatbelt': get_broadacre_region,
    'ncra_sth': get_ncra_region,
    'ncra_nth': get_ncra_region,
    'mod_ncra_nth': get_ncra_region,
    'wine': get_ncra_region,
    'forestry': get_ncra_region,
    'summer_cropping': get_ncra_region,
        
}

REGION_NAME = {
    'wheatbelt': 'ABARES wheat sheep broadacre zone',
    'ncra_sth': 'NCRA southern Australia region',
    'ncra_nth': 'NCRA northern Australia region',
    'mod_ncra_nth': 'modified NCRA northern Australia region',
    'wine': 'NCRA Australian wine region',
    'forestry': 'NCRA Australian forestry region',  
    'summer_cropping': 'NCRA Australian summer cropping region', 
}

REGION_SOURCE = {
    'wheatbelt': 'https://www.agriculture.gov.au/abares/research-topics/surveys/farm-survey-data',
    'ncra_sth': 'https://doi.org/10.25919/8tqq-0007',
    'ncra_nth': 'https://doi.org/10.25919/8tqq-0007',
    'mod_ncra_nth': 'https://doi.org/10.25919/8tqq-0007',
    'wine': 'https://doi.org/10.25919/8tqq-0007',
    'forestry': 'https://doi.org/10.25919/8tqq-0007',
    'summer_cropping': 'https://doi.org/10.25919/8tqq-0007',
}



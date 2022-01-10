#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   Haversine Formula
#   Created: June, 2016
#   Updated: Jan, 2022
#
#------------------------------------------------------------------------------+


from ctypes import c_double, CDLL
from glob import glob
from os import path
from .utils import conversion_dict


# initialize
so_path = glob(path.dirname(__file__) + "/haversine_c*")[0]
haversine_c = CDLL(so_path)

# specify signtures
haversine_c.haversine.argtypes = [c_double, c_double, c_double, c_double]
haversine_c.haversine.restype = c_double


def haversine(lnglat1, lnglat2, units='m'):
    '''
    use the haversine function to calculate the distance between
    two lon/lat coordnate pairs.

    output distance available in meters, kilometers, miles, yards, and feet.
    '''
    
    lng1, lat1 = lnglat1
    lng2, lat2 = lnglat2
        
    dist_m = haversine_c.haversine(lng1, lat1, lng2, lat2)
    
    if units == 'm': return dist_m
    return conversion_dict[units](dist_m)

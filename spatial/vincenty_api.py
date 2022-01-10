#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   Vincenty Inverse formula
#   Created: 2016-SEP-30
#   Updated: 2022-JAN
#   
#------------------------------------------------------------------------------+


from ctypes import c_double, c_uint, CDLL
from glob import glob
from os import path
from .utils import conversion_dict


# initialize
so_path = glob(path.dirname(__file__) + "/vincenty_c*")[0]
vincenty_c = CDLL(so_path)

# specify signtures
vincenty_c.vincenty_inv.restype = c_double
vincenty_c.vincenty_inv.argtypes = [c_double, c_double, c_double, c_double, 
    c_uint, c_double]


def vincenty_inverse(lnglat1, lnglat2, units='m', maxIter=200, tol=1E-12):
    '''
    use the vincenty inverse function to calculate the distance between
    two lon/lat coordnate pairs.

    output distance available in meters, kilometers, miles, yards, and feet.
    '''
    
    lng1, lat1 = lnglat1
    lng2, lat2 = lnglat2
        
    dist_m = vincenty_c.vincenty_inv(lng1, lat1, lng2, lat2, maxIter, tol)
    
    if units == 'm': return dist_m
    return conversion_dict[units](dist_m)

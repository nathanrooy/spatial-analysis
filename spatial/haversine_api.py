#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   Haversine Formula
#   Created: June, 2016
#   Updated: Jan, 2022
#
#------------------------------------------------------------------------------+


from ctypes import CDLL
from ctypes import c_double
from .utils import conversion_dict


# initialize
haversine_c = CDLL("/home/nathan/Public/venvs/venv_py3.10/lib64/python3.10/site-packages/spatial/haversine_c.cpython-310-x86_64-linux-gnu.so")

# specify signtures
haversine_c.haversine.argtypes = [c_double, c_double, c_double, c_double]
haversine_c.haversine.restype = c_double


def haversine(lnglat1, lnglat2, units='m'):
    '''
    use the haversine class to calculate the distance between
    two lon/lat coordnate pairs.

    output distance available in meters, kilometers, miles, yards, and feet.

    example usage: haversine([lon1,lat1],[lon2,lat2]).ft

    '''
    
    lng1, lat1 = lnglat1
    lng2, lat2 = lnglat2
        
    dist_m = haversine_c.haversine(lng1, lat1, lng2, lat2)
    
    if units == 'm': return dist_m
    return conversion_dict[units](dist_m)

#------------------------------------------------------------------------------
#
#   Nathan A. Rooy
#   Haversine Formula
#   Created: June, 2016
#   Updated: Jan, 2022
#
#------------------------------------------------------------------------------


from _spatial import haversine as h
from .utils import conversion_dict


def haversine(lnglat1, lnglat2, units='m'):
    '''> Haversine Distance
    
    Calculate the distance between two points of longitude/latitude using the
    Haversine approach.
    
    Parameters
    ----------
    lnglat1 : array_like
        Point #1 which can be either a list of length 2 or a tuple. Follow the 
        convention of (x, y) or (longitude, latitude).
        
    lnglat2 : array_like
        Point #2, specify in the same manner as point #1.
        
    units : str, optional (default = 'm')
        The units for which the distance is to be returned. By default, this is
        set at 'm' for meters, however additional units are available.
            'km' -> kilometers
            'mi' -> miles
            'nm' -> nautical miles
            'yd' -> yards
            'ft' -> feet
            
    Returns
    -------
    dist : float
        distance between the two input points in the units specified.
    '''

    lng1, lat1 = lnglat1
    lng2, lat2 = lnglat2

    dist_m = h(lng1, lat1, lng2, lat2)

    if units == 'm': return dist_m
    return conversion_dict[units](dist_m)

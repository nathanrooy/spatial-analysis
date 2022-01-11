#------------------------------------------------------------------------------
#
#   Nathan A. Rooy
#   Vincenty Inverse formula
#   Created: 2016-SEP-30
#   Updated: 2022-JAN
#
#------------------------------------------------------------------------------


from ctypes import c_double, c_uint, CDLL
from glob import glob
from os import path
from .utils import conversion_dict


# initialize
so_path = glob(path.dirname(__file__) + "/vincenty_c*")[0]
vincenty_c = CDLL(so_path)

# specify signtures
vincenty_c.vincenty_inv.restype = c_double
vincenty_c.vincenty_inv.argtypes = [
    c_double, c_double, c_double, c_double,  c_uint, c_double
]


def vincenty_inverse(lnglat1, lnglat2, units='m', maxIter=200, tol=1E-12):
    '''> Vincenty Distance

    Calculate the distance between two points of longitude/latitude using the
    Vincenty inverse approach. This is more accurate than the Haversine
    method, however because of its iterative nature, it carries with it an 
    increased computational cost.

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

    maxIter : int, optional (default = 250)
        The maximum number of iterations to perform before exiting.

    tol : float, optional (default = 1E-12)
        Tolerance for early exit. When the iteration-to-iteration difference
        in distance residual drops below this level, the iteration loop is
        terminated. When using 'tol' as the primary stopping criteria, make
        sure to increase maxIter to a sufficiently high level so as to not
        force an early exit.

    Returns
    -------
    dist : float
        distance between the two input points in the units specified.
    '''

    lng1, lat1 = lnglat1
    lng2, lat2 = lnglat2

    dist_m = vincenty_c.vincenty_inv(lng1, lat1, lng2, lat2, maxIter, tol)

    if units == 'm': return dist_m
    return conversion_dict[units](dist_m)

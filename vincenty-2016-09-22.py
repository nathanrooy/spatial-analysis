#------------------------------------------------------------------------------+
#
#   Solve the inverse Vincenty's formulae
#   https://en.wikipedia.org/wiki/Vincenty%27s_formulae
#
#
#
#------------------------------------------------------------------------------+


#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from __future__ import division


#--- CONSTANTS ----------------------------------------------------------------+

a=6378137.0                                         # radius at equator in meters (WGS-84)
f=1/298.257223563                                   # flattening of the ellipsoid (WGS-84)
b=(1-f)*a                                           # radius at the poles in meters (WGS-84)



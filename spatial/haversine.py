#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   Haversine Formula
#   Created: June, 2016
#   Updated: Nov, 2019
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from __future__ import division

from math import atan2
from math import cos
from math import radians
from math import sin
from math import sqrt

#--- MAIN ---------------------------------------------------------------------+

class Haversine:
    '''
    use the haversine class to calculate the distance between
    two lon/lat coordnate pairs.

    output distance available in meters, kilometers, miles, yards, and feet.

    example usage: haversine([lon1,lat1],[lon2,lat2]).ft

    '''
    def __init__(self,coord1,coord2):
        lon1,lat1=coord1
        lon2,lat2=coord2

        R=6371000   # radius of Earth in meters
        phi_1=radians(lat1)
        phi_2=radians(lat2)

        delta_phi=radians(lat2-lat1)
        delta_lambda=radians(lon2-lon1)

        a=(sin(delta_phi/2.0)**2 +
            cos(phi_1)*cos(phi_2) *
            sin(delta_lambda/2.0)**2)

        c=2*atan2(sqrt(a),sqrt(1-a))

        self.R = R
        self.c = c

    #--- OUTPUT OPTIONS -----------------------------------+
    
    def m(self):
        return self.R*self.c                # output distance in meters

    def km(self):
        return self.m() / 1000.0            # output distance in kilometers

    def mi(self):
        return self.m() * 0.000621371       # output distance in miles

    def nm(self):
        return self.m() / 1852.0  			# output distance in nautical miles

    def yd(self):
        return self.m() * 1.0936132983      # output distance in yards

    def ft(self):
        return self.mi() * 5280.0           # output distance in feet

#--- END ----------------------------------------------------------------------+

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
from math import atan
from math import atan2
from math import cos
from math import radians
from math import sin
from math import sqrt
from math import tan

#--- MAIN ---------------------------------------------------------------------+

class vincenty_inverse:

    def __init__(self,coord1,coord2,maxIter=200,tol=10**-12):

        #--- CONSTANTS ------------------------------------+
        
        a=6378137.0                             # radius at equator in meters (WGS-84)
        f=1/298.257223563                       # flattening of the ellipsoid (WGS-84)
        b=(1-f)*a

        phi_1,L_1,=coord1                        # (lat=L_?,lon=phi_?)
        phi_2,L_2,=coord2                  

        U_1=atan((1-f)*tan(radians(phi_1)))
        U_2=atan((1-f)*tan(radians(phi_2)))

        L=radians(L_2-L_1)

        Lambda=L                                # set initial value of lambda to L

        sinU1=sin(U_1)
        cosU1=cos(U_1)
        sinU2=sin(U_2)
        cosU2=cos(U_2)

##        if lon1==lon2 and lat1==lat2:
##            return 0.0

        #--- BEGIN ITERATIONS -----------------------------+

        for i in range(0,maxIter):
            cosLambda=cos(Lambda)
            
            sinLambda=sin(Lambda)
            
            sinSigma=sqrt((cosU2*sin(Lambda))**2 +
                          (cosU1*sinU2-sinU1*cosU2*cosLambda)**2)
            
            cosSigma=sinU1*sinU2+cosU1*cosU2*cosLambda

            sigma=atan2(sinSigma,cosSigma)

            sin_alpha=(cosU1*cosU2*sinLambda)/sinSigma

            cosSq_alpha=1-sin_alpha**2

            cos2Sig_m=cosSigma-((2*sinU1*sinU2)/cosSq_alpha)

            C=(f/16)*cosSq_alpha*(4+f*(4-3*cosSq_alpha))
            
            Lambda_prev=Lambda
            Lambda=L+(1-C)*f*sin_alpha*(sigma+C*sinSigma*(cos2Sig_m+C*cosSigma*(-1+2*cos2Sig_m**2)))

            # successful convergence
            diff=abs(Lambda_prev-Lambda)
            if diff<=tol:
                break

        uSq=cosSq_alpha*((a**2-b**2)/b**2)
        A=1+(uSq/16384)*(4096+uSq*(-768+uSq*(320-175*uSq)))
        B=(uSq/1024)*(256+uSq*(-128+uSq*(74-47*uSq)))
        deltaSig=B*sinSigma*(cos2Sig_m+0.25*B*(cosSigma*(-1+2*cos2Sig_m**2)-(1/6)*B*cos2Sig_m*(-3+4*sinSigma**2)*(-3+4*cos2Sig_m**2)))

        self.meters=b*A*(sigma-deltaSig)            # output distance in meters     
        self.km=self.meters/1000                    # output distance in kilometers
        self.mm=self.meters*1000                    # output distance in millimeters
        self.miles=self.meters*0.000621371          # output distance in miles
        self.n_miles=self.miles*(6080.20/5280)      # output distance in nautical miles
        self.feet=self.miles*5280                   # output distance in feet
        self.inches=self.feet*12                    # output distance in inches
        self.yards=self.feet/3                      # output distance in yards

if __name__ == "__vincenty_inverse__":
    main()

#--- EXAMPLES -----------------------------------------------------------------+
        
print vincenty_inverse([39.152501,-84.412977],[39.152505,-84.412946]).meters
##print Haversine((-84.412977,39.152501),(-84.412946,39.152505)).feet
##print Haversine((-84.412977,39.152501),(-84.412946,39.152505)).km
##print Haversine((-84.412977,39.152501),(-84.412946,39.152505)).miles        
      
#--- END ----------------------------------------------------------------------+



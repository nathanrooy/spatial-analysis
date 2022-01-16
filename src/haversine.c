#define _USE_MATH_DEFINES
#include <math.h>
#include "haversine.h"

double DTOR = M_PI / 180.0;       // degrees -> radians
long R = 6371000;

double haversine(double lng1, double lat1, double lng2, double lat2){
    double phi_1, phi_2;
    double delta_phi, delta_lambda;
    double a, c;
    
    phi_1 = lat1 * DTOR;
    phi_2 = lat2 * DTOR;

    delta_phi    = (lat2 - lat1) * DTOR;
    delta_lambda = (lng2 - lng1) * DTOR;
        
    a = (
        pow(sin(delta_phi / 2.0), 2) + 
        cos(phi_1) * 
        cos(phi_2) * 
        pow(sin(delta_lambda / 2.0), 2)
     );
    
    c = 2 * atan2(sqrt(a), sqrt(1-a));
    return R * c;
}

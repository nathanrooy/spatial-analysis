#ifndef CONSTANTS_H
#define CONSTANTS_H

/* shared constants */
extern const double DTOR = M_PI / 180.0;       // degrees -> radians

/* haversine specific */
extern const long R = 6371000;

/*vincenty specific */
extern const double a = 6378137.0;             // radius at equator in meters (WGS-84)
extern const double f = 1.0 / 298.257223563;   // flattening of the ellipsoid (WGS-84)
extern const double b = (1 - f) * a;           // length of semi-minor axis   (WGS-84)

#endif

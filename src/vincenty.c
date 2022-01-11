#define _USE_MATH_DEFINES
#include <math.h>


const double a = 6378137.0;             // radius at equator in meters (WGS-84)
const double f = 1.0 / 298.257223563;   // flattening of the ellipsoid (WGS-84)
const double b = (1 - f) * a;           // length of semi-minor axis   (WGS-84)
const double DTOR = M_PI / 180.0;       // degrees -> radians

// https://en.wikipedia.org/wiki/Vincenty%27s_formulae#Inverse_problem


double vincenty_inv(double l_1, double phi_1, double l_2, double phi_2,
    unsigned int maxIter, double tol) {
    
    double u_1, u_2, sin_u1, cos_u1, sin_u2, cos_u2, cos_lambda, sin_lambda;
    double sin_sigma, cos_sigma, sigma, sin_alpha, cos_sq_alpha, cos2_sigma_m;
    double lambda, lambda_prev, l, diff, C, u_sq, A, B, delta_sig;
    unsigned int i;
    
    u_1 = atan((1 - f) * tan(phi_1 * DTOR));
    u_2 = atan((1 - f) * tan(phi_2 * DTOR));

    l = (l_2 - l_1) * DTOR;
    lambda = l;                         // set initial value of lambda to l

    sin_u1 = sin(u_1);
    cos_u1 = cos(u_1);
    sin_u2 = sin(u_2);
    cos_u2 = cos(u_2);

    // begin iterations    
    for (i = 1; i <= maxIter; ++i) {
        cos_lambda = cos(lambda);
        sin_lambda = sin(lambda);
        sin_sigma = sqrt(
            pow(cos_u2 * sin(lambda), 2) + 
            pow(cos_u1 * sin_u2 - sin_u1 * cos_u2 * cos_lambda, 2)
        ); 
        cos_sigma = sin_u1 * sin_u2 + cos_u1 * cos_u2 * cos_lambda;
        sigma = atan2(sin_sigma, cos_sigma);
        sin_alpha = (cos_u1 * cos_u2 * sin_lambda) / sin_sigma;
        cos_sq_alpha = 1 - pow(sin_alpha, 2);
        cos2_sigma_m = cos_sigma - ((2 * sin_u1 * sin_u2) / cos_sq_alpha);
        C = (f / 16.0) * cos_sq_alpha * (4 + f * (4 - 3 * cos_sq_alpha));
        lambda_prev = lambda;
        lambda = l +(1 - C) * f * sin_alpha * (
            sigma + C * sin_sigma * (
                cos2_sigma_m + C * cos_sigma * (-1 + 2 * pow(cos2_sigma_m, 2))
                )
        );
        
        // successful convergence
        diff = fabs(lambda_prev - lambda);
        if(diff <= tol) {
            break;
        }
    }

    u_sq = cos_sq_alpha * ((pow(a, 2) - pow(b, 2)) / pow(b, 2));
    A = 1.0 + ( u_sq / 16384.0) * (
        4096.0 + u_sq * (-768.0 + u_sq * (320.0 - 175.0 * u_sq))
    );
    B = (u_sq / 1024.0) * (
        256.0 + u_sq * (-128.0 + u_sq * (74.0 - 47.0 * u_sq))
    );
    delta_sig = (
        B * sin_sigma * (
            cos2_sigma_m + 
            0.25 * B * (
                cos_sigma * 
                (-1.0 + 2.0 * pow(cos2_sigma_m, 2)) - 
                (B / 6.0)   * cos2_sigma_m * 
                (-3.0 + 4.0 * pow(sin_sigma, 2)) * 
                (-3.0 + 4.0 * pow(cos2_sigma_m, 2))
            )
        )
    );

    // return distance in meters
    return b * A * (sigma - delta_sig);
}

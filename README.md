# spatial-analysis
[![ci](https://github.com/nathanrooy/spatial-analysis/actions/workflows/ci.yaml/badge.svg)](https://github.com/nathanrooy/spatial-analysis/actions/workflows/ci.yaml)
[![GitHub license](https://img.shields.io/github/license/nathanrooy/spatial-analysis)](https://github.com/nathanrooy/spatial-analysis/blob/master/LICENSE)
[![codecov](https://img.shields.io/codecov/c/github/nathanrooy/spatial-analysis.svg)](https://codecov.io/gh/nathanrooy/spatial-analysis)

Python scripts I use for the analysis of spatial data

## Installation
You can either download/clone this repo and use as is, or you can pip install it with the following command:
```sh
pip install git+https://github.com/nathanrooy/spatial-analysis
```
## Usage

### Haversine
Calculate the distance between two longitude/latitude pairs using the
<a target="_blank" href="https://en.wikipedia.org/wiki/Haversine_formula">Haversine formula</a>. For more information on the math/implementation details, see this blog post [<a target="_blank" href="https://nathanrooy.github.io/posts/2016-09-07/haversine-with-python/">here</a>].

```py
>>> from spatial import haversine
>>> p1 = [-84.4941318, 39.113223]     # p1=[longitude_1, latitude_1]
>>> p2 = [-81.4061265, 41.250386]     # p2=[longitude_2, latitude_2]
>>> haversine(p1, p2)                 # meters (default)
353922.9402484654
```
By default, the distance returned is in meters (`m`), however additional units can be specified as follows:

```py
>>> haversine(p1, p2, units='km')  # kilometers
353.9229402484654
>>> haversine(p1, p2, units='mi')  # miles
219.9174513051292
>>> haversine(p1, p2, units='nm')  # nautical miles
191.10309948621241
>>> haversine(p1, p2, units='yd')  # yards
387054.83402915805
>>> haversine(p1, p2, units='ft')  # feet
1161164.1428910822
>>> haversine(p1, p2, units='m')   # meters
353922.9402484654
```

### Vincenty Inverse

If more accuracy is needed than what the Haversine formula can provide, a good option is <a target="_blank" href="https://en.wikipedia.org/wiki/Vincenty%27s_formulae">Vincenty's Inverse formulae</a>. For more information on the math/implementation details, see this blog post [<a target="_blank" href="https://nathanrooy.github.io/posts/2016-12-18/vincenty-formula-with-python/">here</a>].

```py
>>> from spatial import vincenty_inverse as vi
>>> p1 = [-84.4941318, 39.113223]     # p1=[longitude_1, latitude_1]
>>> p2 = [-81.4061265, 41.250386]     # p2=[longitude_2, latitude_2]
>>> vi(p1, p2)                        # meters (default)
354188.01859971555
```

Just like the `haversine` method, `vincenty_inverse` supports `meters`,`kilometers`,`miles`,`nautical miles`,`yards`, and `feet` as seen below:

```py
>>> vi(p1, p2, units='km')  # kilometers
354.1880185997156
>>> vi(p1, p2, units='mi')  # miles
220.08216330532386
>>> vi(p1, p2, units='nm')  # nautical miles
191.24623034541875
>>> vi(p1, p2, units='yd')  # yards
387344.7272391767
>>> vi(p1, p2, units='ft')  # feet
1162033.8222521099
>>> vi(p1, p2, units='m')   # meters
354188.01859971555
```
Since Vincenty's inverse formulae is an iterative approach, it employs two methods for stopping. The first is to simply specify a maximum number of iterations using `maxIter` as seen below:
```py
>>> vi(p1, p2, maxIter=500)
```
The default value for `maxIter` is 250 iterations. The second stopping method is specified using `tol`. When the iteration-to-iteration difference in distance residual drops below the value specified by `tol`, the iteration loop terminates. By default, this value is 1E-12.
```py
>>> vi(p1, p2, tol=1E-10)
```
When using `tol` as the primary stopping criteria, make sure to increase `maxIter` to a sufficiently high level so as to not force an early exit.

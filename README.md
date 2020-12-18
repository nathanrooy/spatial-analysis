# spatial-analysis
Python scripts I use for the analysis of spatial data

## Installation
You can either download/clone this repo and use as is, or you can pip install it with the following command:
```sh
pip install git+https://github.com/nathanrooy/spatial-analysis
```
## Usage

### Haversine
Calculate the distance between two longitude/latitude pairs using the
<a target="_blank" href="https://en.wikipedia.org/wiki/Haversine_formula">Haversine formula</a>. For more information on the math/implementation details, see this blog post here: https://nathanrooy.github.io/posts/2016-09-07/haversine-with-python/

```py
>>> from spatial import haversine
>>> p1 = [-84.4941318, 39.113223]     # p1=[longitude_1, latitude_1]
>>> p2 = [-81.4061265, 41.250386]     # p2=[longitude_2, latitude_2]
>>> haversine(p1, p2).m()             # meters
353922.9402484654
```
In addition to `meters`, the following units can be specified:
- `kilometers`
- `miles`
- `nautical miles`
- `yards`
- `feet`

Example usage:
```py
>>> haversine(p1, p2).km()  # kilometers
353.9229402484654
>>> haversine(p1, p2).mi()  # miles
219.9174513051292
>>> haversine(p1, p2).nm()  # nautical miles
191.10309948621241
>>> haversine(p1, p2).yd()  # yards
387054.83402915805
>>> haversine(p1, p2).ft()  # feet
1161164.1428910822
```
### Vincenty Inverse

If more accuracy is needed than what the Haversine formula can provide, a good option is <a target="_blank" href="https://en.wikipedia.org/wiki/Vincenty%27s_formulae">Vincenty's Inverse formulae</a>. For more information on the math/implementation details, see this blog post here: https://nathanrooy.github.io/posts/2016-12-18/vincenty-formula-with-python/

```py
>>> from spatial import vincenty_inverse as vi
>>> p1 = [-84.4941318, 39.113223]     # p1=[longitude_1, latitude_1]
>>> p2 = [-81.4061265, 41.250386]     # p2=[longitude_2, latitude_2]
>>> vi(p1, p2).m()                    # meters
354188.01859971555
```

Just like the `haversine` method, `vincenty_inverse` supports `meters`,`kilometers`,`miles`,`nautical miles`,`yards`, and `feet` as seen below:

```py
>>> vi(p1, p2).km()         # kilometers
354.1880185997156
>>> vi(p1, p2).mi()         # miles
220.08216330532386
>>> vi(p1, p2).nm()         # nautical miles
253.4362820698921
>>> vi(p1, p2).yd()         # yards
387344.7272391767
>>> vi(p1, p2).ft()         # feet
1162033.8222521099
```
Since Vincenty's inverse formulae is an iterative approach, it employs two methods for stopping. The first is to simply specify a maximum number of iterations using `maxIter` as seen below:
```py
>>> vi(p1, p2, maxIter=500).m()           # meters
```
The default value for `maxIter` is 250 iterations. The second stopping method is specified using `tol`. When the iteration-to-iteration difference in distance residual drops below the value specified by `tol`, the iteration loop terminates. By default, this value is 10^-12.
```py
>>> vi(p1, p2, tol=10**-10).m()           # meters
```
When using `tol` as the primary stopping criteria, make sure to increase `maxIter` to a sufficiently high level so as to not force an early exit.

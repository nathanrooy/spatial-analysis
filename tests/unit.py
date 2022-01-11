import unittest

from spatial import haversine as h
from spatial import vincenty_inverse as vi


TOL = 1E-8
P1 = [-84.4941318, 39.113223]
P2 = [-81.4061265, 41.250386]


class test_everything(unittest.TestCase):

    def test_haversine(self):
        self.assertLess(abs(353922.9402484654  - h(P1, P2, units='m')),  TOL)
        self.assertLess(abs(353.9229402484654  - h(P1, P2, units='km')), TOL)
        self.assertLess(abs(219.9174513051292  - h(P1, P2, units='mi')), TOL)
        self.assertLess(abs(191.10309948621241 - h(P1, P2, units='nm')), TOL)
        self.assertLess(abs(387054.83402915805 - h(P1, P2, units='yd')), TOL)
        self.assertLess(abs(1161164.1428910822 - h(P1, P2, units='ft')), TOL)

    def test_vincenty(self):
        self.assertLess(abs(354188.01859971555 - vi(P1, P2, units='m')),  TOL)
        self.assertLess(abs(354.1880185997156  - vi(P1, P2, units='km')), TOL)
        self.assertLess(abs(220.08216330532386 - vi(P1, P2, units='mi')), TOL)
        self.assertLess(abs(191.24623034541875 - vi(P1, P2, units='nm')), TOL)
        self.assertLess(abs(387344.7272391767  - vi(P1, P2, units='yd')), TOL)
        self.assertLess(abs(1162033.8222521099 - vi(P1, P2, units='ft')), TOL)


if __name__ == '__main__':
    unittest.main()

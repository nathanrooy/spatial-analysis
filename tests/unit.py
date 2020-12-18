import unittest

from spatial import haversine
from spatial import vincenty_inverse as vi


P1 = [-84.4941318, 39.113223]
P2 = [-81.4061265, 41.250386]


class test_everything(unittest.TestCase):

    def test_haversine(self):
        self.assertEqual(haversine(P1, P2).m(), 353922.9402484654)
        self.assertEqual(haversine(P1, P2).km(), 353.9229402484654)
        self.assertEqual(haversine(P1, P2).mi(), 219.9174513051292)
        self.assertEqual(haversine(P1, P2).nm(), 191.10309948621241)
        self.assertEqual(haversine(P1, P2).yd(), 387054.83402915805)
        self.assertEqual(haversine(P1, P2).ft(), 1161164.1428910822)
        
    def test_vincenty(self):
        self.assertEqual(vi(P1, P2).m(), 354188.01859971555)
        self.assertEqual(vi(P1, P2).km(), 354.1880185997156)
        self.assertEqual(vi(P1, P2).mi(), 220.08216330532386)
        self.assertEqual(vi(P1, P2).nm(), 191.24623034541875)
        self.assertEqual(vi(P1, P2).yd(), 387344.7272391767)
        self.assertEqual(vi(P1, P2).ft(), 1162033.8222521099)
        

if __name__ == '__main__':
    unittest.main()

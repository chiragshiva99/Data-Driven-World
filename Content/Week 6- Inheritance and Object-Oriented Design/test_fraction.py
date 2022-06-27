import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
    
    def setUp(self):
        # create object instances
        self.f = Fraction(1, 2)
        self.g = Fraction(2, 3)

    ########
    # CS1
    ########
        
    def test_init(self):
        # test if numerator is initialized
        self.assertEqual(self.f.num, 1)
        self.assertEqual(self.g.num, 2)
    
        # test if denominator is initialized
        self.assertEqual(self.f.den, 2)
        self.assertEqual(self.g.den, 3)
        
    def test_num(self):
        # test if you can set the numerator
        self.f.num = 3
        self.g.num = 7
        self.assertEqual(self.f.num, 3)
        self.assertEqual(self.g.num, 7)
        
        # test if the type is an integer
        self.assertIsInstance(self.f.num, int)
        self.assertIsInstance(self.g.num, int)
    
    def test_den(self):
        # test if you can set the denominator
        # normal case
        self.f.den = 5
        self.g.den = 7
        self.assertEqual(self.f.den, 5)
        self.assertEqual(self.g.den, 7)
        
        # test if the denominator type is int
        self.assertIsInstance(self.f.den, int)
        self.assertIsInstance(self.g.den, int)
    
        # test when zero is assigned to denominator, it should be set as 1
        self.f.den = 0
        self.assertEqual(self.f.den, 1)
    
    def test_str(self):
        # test if str() output is num/den
        out = str(self.f)
        self.assertEqual(out, "1/2")
        out = str(self.g)
        self.assertEqual(out, "2/3")
    
    #######
    # CS2
    #######
    
    def test_simplify(self):
        # test simplify to return a new Fraction object with lowest terms
        h = Fraction(2, 4)
        g = h.simplify()
        self.assertIsInstance(g, Fraction)
        self.assertEqual(g.num, 1)
        self.assertEqual(g.den, 2)
    
    def test_add(self):

        # test if you can use + operator
        h = self.f + self.g
        self.assertIsInstance(h, Fraction)
        self.assertEqual(h.num, 7)
        self.assertEqual(h.den, 6)
        
        h = Fraction(1, 3)
        g = Fraction(1,6)
        result = h + g
        self.assertEqual(result.num, 1)
        self.assertEqual(result.den, 2)
    
    def test_eq(self):
        # test if can use == operator
        h = Fraction(2, 4)
        self.assertEqual(self.f, h, "Implement __eq__.")
        self.assertNotEqual(self.f, self.g)
        
if __name__ == "__main__":
    unittest.main()
        
        
    

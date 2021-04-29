import unittest
import calculator

class SimpleTest(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(calculator.add(4, 2), 6) 
        
    def test_calculator0(self):
        self.assertEqual(calculator.sub(4, 2), 2)
    
    def test_calculator1(self):
        self.assertEqual(calculator.mul(4, 2), 8)

    def test_calculator2(self):
        self.assertEqual(calculator.div(4, 2), 2.0)
    
    def test_calculator3(self):
        self.assertEqual(calculator.add(4, -2), 2) 
        
    def test_calculator4(self):
        self.assertEqual(calculator.sub(4.5, 2), 2.5)
    
    def test_calculator5(self):
        self.assertEqual(calculator.mul(4, -2.5), -10)

    def test_calculator6(self):
        self.assertEqual(calculator.div(4, -2), -2.0)
    
    def test_calculator7(self):
        self.assertEqual(calculator.div(4, 0), "0 can't be the divisor")

    def test_calculator8(self):
        self.assertEqual(calculator.add('4', 2), "Numbers only")
    
    def test_calculator9(self):
        self.assertEqual(calculator.sub(4, 2), 10)

    def test_calculator10(self):
        self.assertEqual(calculator.mul(5, 6), -2.3)
    
    def test_calculator11(self):
        self.assertEqual(calculator.div('4', 2), 2)

if __name__ == '__main__':
	unittest.main()

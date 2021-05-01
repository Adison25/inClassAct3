import unittest
import calc

class TestCase(unittest.TestCase):
    def test_Add(self):
        self.assertEqual(calc.addition(2, 1),3)
    #Fail Add
    #def test_2(self):
        #self.assertEqual(calc.addition(2, 1),4)
    def test_Sub(self):
        self.assertEqual(calc.subtraction(2, 1),1)
    #Fail Sub
    #def test_4(self):
        #self.assertEqual(calc.subtraction(2, 1),3)
    def test_Mult(self):
        self.assertEqual(calc.multiplication(2, 1),2)
    #Fail multiplication
    #ef test_6(self):
        #self.assertEqual(calc.multiplication(2, 1),3)
    def test_Div(self):
        self.assertEqual(calc.division(2, 1),2)
    #Fail division
    #def test_8(self):
        #self.assertEqual(calc.division(2, 1),3)

if __name__ == '__main__':
    unittest.main()
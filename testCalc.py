import unittest
import calc

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc.addition(2, 1),3)
    #Fail Add
    #def test2(self):
        #self.assertEqual(calc.addition(2, 1),4)
    def test3(self):
        self.assertEqual(calc.subtraction(2, 1),1)
    #Fail Sub
    #def test4(self):
        #self.assertEqual(calc.subtraction(2, 1),3)
    def test5(self):
        self.assertEqual(calc.multiplication(2, 1),2)
    #Fail multiplication
    #ef test6(self):
        #self.assertEqual(calc.multiplication(2, 1),3)
    def test7(self):
        self.assertEqual(calc.division(2, 1),2)
    #Fail division
    #def test8(self):
        #self.assertEqual(calc.division(2, 1),3)

if __name__ == '__main__':
    unittest.main()
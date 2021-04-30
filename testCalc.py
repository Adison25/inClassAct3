import unittest
import calc

class TestCase(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(calc.addition(2, 1),3)
    #Fail Add
    #def test2(self):
        #self.assertEqual(calc.addition(2, 1),4)
    def testSub(self):
        self.assertEqual(calc.subtraction(2, 1),1)
    #Fail Sub
    #def test4(self):
        #self.assertEqual(calc.subtraction(2, 1),3)
    def testMult(self):
        self.assertEqual(calc.multiplication(2, 1),2)
    #Fail multiplication
    #ef test6(self):
        #self.assertEqual(calc.multiplication(2, 1),3)
    def testDiv(self):
        self.assertEqual(calc.division(2, 1),2)
    #Fail division
    #def test8(self):
        #self.assertEqual(calc.division(2, 1),3)

if __name__ == '__main__':
    unittest.main()
import unittest
import MyMathLib
class DivisionTest(unittest.TestCase):
    def testSumPositiveNumbersOneAndOne(self):
        division = MyMathLib.Division()
        self.assertEqual(2,division.execute(4,2))
    

if __name__ == '__main__':
    unittest.main()


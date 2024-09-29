import unittest
import calculator

class BasicTest(unittest.TestCase):
    def test_result(self):
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.multiply(10, 3), 30)


    def test_divide(self):
        self.assertEqual(calculator.divide(5, 2), 2.5)
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(100, 0),'На ноль делить нельзя')



if __name__ == '__main__':
    unittest.main()

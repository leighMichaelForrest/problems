import unittest
import functools

from leibniz import leibniz

class LeibnizTest(unittest.TestCase):
    def test_leibniz_4(self):
        terms = [1, -1/3, 1/5, -1/7]
        pi = functools.reduce(lambda x, y: x + y, terms) * 4
        pi_dict = leibniz(4)
        self.assertSequenceEqual(terms, pi_dict['terms'])
        self.assertAlmostEqual(pi_dict['pi'], pi)

if __name__ == '__main__':
    unittest.main()

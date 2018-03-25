import unittest

from bounce import bounce

class TestBounce(unittest.TestCase):
    def test_bounce(self):
        height = 10
        bounces = 2
        self.assertAlmostEqual(bounce(10, 2), 25.6, places=1)

if __name__ == '__main__':
    unittest.main()

import unittest

from sphere import diameter, circumference, surface_area, volume

class SphereTests(unittest.TestCase):
    def setUp(self):
        self.radius = 6

    def test_diameter(self):
        self.assertEqual(diameter(self.radius), 12)
        self.assertEqual(diameter('bleen'), 0)

    def test_circumference(self):
        self.assertAlmostEqual(circumference(self.radius), 37.6991, places=4)
        self.assertEqual(circumference('bleen'), 0)

    def test_surface_area(self):
        self.assertAlmostEqual(surface_area(self.radius), 452.39, places=2)
        self.assertEqual(surface_area('bleen'), 0)

    def test_volume(self):
        self.assertAlmostEqual(volume(self.radius), 904.78, places=2)
        self.assertEqual(volume('bleen'), 0)

if __name__ == '__main__':
    unittest.main()

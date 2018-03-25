import unittest

from payroll import payroll

class PayrollTest(unittest.TestCase):
    def test_payroll_regular_hours(self):
        self.assertEqual(payroll(20, 40), 800)

    def test_payroll_part_time(self):
        self.assertEqual(payroll(20, 10), 200.0)

    def test_payroll_overtime(self):
        self.assertEqual(payroll(20, 60), 1400)

if __name__ == '__main__':
    unittest.main()

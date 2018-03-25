import unittest

from loan import loan

class TestLoan(unittest.TestCase):
    def setUp(self):
        self.results = loan(1000)

    def test_loan_payments(self):
        self.assertEqual(len(self.results), 23)

    def test_first_payment(self):
        payment = self.results[0]

        self.assertEqual(payment['payment'], 45)
        self.assertEqual(payment['month'], 1)
        self.assertEqual(payment['remaining_balance'], 864)
        self.assertEqual(payment['interest_owed'], 9.0)
        self.assertEqual(payment['principal_owed'], 36)
        self.assertEqual(payment['payment'], 45)

    def test_last_payment(self):
        # 22 is the index of the last payment
        payment = self.results[22]

        self.assertLess(payment['payment'], 45)
        self.assertEqual(payment['month'], 23)
        self.assertEqual(payment['remaining_balance'], 0)
        self.assertLess(payment['interest_owed'], 9.0)
        self.assertLess(payment['principal_owed'], 36)
        self.assertLess(payment['payment'], 45)


if __name__ == '__main__':
    unittest.main()

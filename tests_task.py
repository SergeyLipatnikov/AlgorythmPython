import unittest
from TankRush import TankRush

class TestTasks(unittest.TestCase):

    def test_right(self):
        H1 = 3
        W1 = 4
        S1 = '1234 2345 0987'
        H2 = 2
        W2 = 2
        S2 = '34 98'

        self.assertTrue(TankRush(H1,W1,S1,H2,W2,S2))

    def test_right2(self):
        H1 = 3
        W1 = 4
        S1 = '1234 2345 0987'
        H2 = 3
        W2 = 2
        S2 = '23 34 98'

        self.assertTrue(TankRush(H1,W1,S1,H2,W2,S2))

    def test_right3(self):
        H1 = 3
        W1 = 4
        S1 = '1234 2345 0987'
        H2 = 3
        W2 = 2
        S2 = '23 34 96'

        self.assertFalse(TankRush(H1,W1,S1,H2,W2,S2))

    def test_right4(self):
        H1 = 3
        W1 = 4
        S1 = '1234 2345 0987'
        H2 = 2
        W2 = 2
        S2 = '23 34'

        self.assertTrue(TankRush(H1,W1,S1,H2,W2,S2))

    def test_zero(self):
        H1 = 1
        W1 = 1
        S1 = '0'
        H2 = 1
        W2 = 1
        S2 = '0'

        self.assertTrue(TankRush(H1,W1,S1,H2,W2,S2))

    def test_False(self):
        H1 = 3
        W1 = 3
        S1 = '321 694 798'
        H2 = 2
        W2 = 2
        S2 = '69 98'

        self.assertFalse(TankRush(H1,W1,S1,H2,W2,S2))
        



if __name__ == '__main__':
    unittest.main()
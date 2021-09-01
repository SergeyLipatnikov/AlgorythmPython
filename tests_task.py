import unittest
from TankRush import TankRush
from MaximumDiscount import MaximumDiscount
from white_walkers import white_walkers
from Football import Football

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
            
    def test_A(self):
        N = 3
        price = [400,300,250]
        self.assertEqual(MaximumDiscount(N,price),250)

    def test_B(self):
        N = 7
        price = [100,150,400,200,250,300,350]
        self.assertEqual(MaximumDiscount(N,price),450)
    
    def test_C(self):
        N = 2
        price = [1000,400]
        self.assertEqual(MaximumDiscount(N,price),0)
        
    def test_D(self):
        N = 7
        price = [200,200,200,100,100,100,100]
        self.assertEqual(MaximumDiscount(N,price),300)
        
    def test_E(self):
        N = 5
        price = [400,300,300,300,300]
        self.assertEqual(MaximumDiscount(N,price),300)

    def test_StringA(self):
        String = "axxb6===4xaf5===eee5"
        self.assertTrue(white_walkers(String))

    def test_StringB(self):
        String = "5==ooooooo=5=5"
        self.assertFalse(white_walkers(String))

    def test_StringC(self):
        String = "abc=7==hdjs=3gg1=======5"
        self.assertTrue(white_walkers(String))

    def test_StringD(self):
        String = "aaS=8"
        self.assertFalse(white_walkers(String))

    def test_StringE(self):
        String = "9===1===9===1===9"
        self.assertTrue(white_walkers(String))

    def test_ArrayA(self):
        Array = [1,3,2]
        self.assertTrue(Football(Array,3))

    def test_ArrayB(self):
        Array = [3,2,1]
        self.assertTrue(Football(Array,3))
        
    def test_ArrayC(self):
        Array = [1,7,5,3,9]
        self.assertTrue(Football(Array,5))

    def test_ArrayD(self):
        Array = [9,5,3,7,1]
        self.assertTrue(Football(Array,5))

    def test_ArrayE(self):
        Array = [1,4,3,2,5]
        self.assertTrue(Football(Array,5))

if __name__ == '__main__':
    unittest.main()
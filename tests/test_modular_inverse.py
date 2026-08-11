import unittest
from maths.modular_inverse import modular_inverse

class TestModulatInverse(unittest.TestCase):
    def test_inverse_of_5_mod_26(self):
        self.assertEqual(modular_inverse(5, 26), 21)

    
    def test_inverse_of_3_mod_26(self):
        self.assertEqual(modular_inverse(3,26), 9)
        
    
    def test_inverse_of_7_mod_26(self):
        self.assertEqual(modular_inverse(7, 26), 15)
        
        
    def test_inverse_of_11_mod_26(self):
        self.assertEqual(modular_inverse(11, 26), 19)
        
        
    def test_no_inverse(self):
        with self.assertRaises(ValueError):
            modular_inverse(2, 26)
            

if __name__ == "__main__":
    unittest.main()
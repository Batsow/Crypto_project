import unittest
from maths.totient import totient

class TestTotient(unittest.TestCase):
    def test_totient_of_8(self):
        self.assertEqual(
            totient(8), 4
        )
        
        
    def test_totient_9(self):
        self.assertEqual(
            totient(9), 6
        )
        
    
if __name__ == "__main__":
    unittest.main()
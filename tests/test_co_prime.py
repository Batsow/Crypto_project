from maths.co_prime import is_coprime

class TestCoprime(unittest.TestCase):
    def test_coprime_numbers(self):
        self.assertTrue(is_coprime(5,26))
        
import unittest

from maths.affine_keys import validate_affine_key


class TestAffineKeyValidation(unittest.TestCase):

    def test_valid_key(self):
        self.assertEqual(
            validate_affine_key(5, 8),
            (5, 8)
        )

    def test_invalid_a(self):
        with self.assertRaises(ValueError):
            validate_affine_key(2, 8)

    def test_large_b_is_normalised(self):
        self.assertEqual(
            validate_affine_key(5, 30),
            (5, 4)
        )

    def test_negative_b_is_normalised(self):
        self.assertEqual(
            validate_affine_key(5, -3),
            (5, 23)
        )

    def test_large_a_is_normalised(self):
        self.assertEqual(
            validate_affine_key(31, 8),
            (5, 8)
        )


if __name__ == "__main__":
    unittest.main()
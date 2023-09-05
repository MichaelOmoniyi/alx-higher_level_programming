import unittest
add_integer = __import__('0-add_integer').add_integer

class TestAdd(unittest.TestCase):
    def test_add_integer(self):
        """Works for integers"""
        self.assertEqual(add_integer(2, 98), 100)
        self.assertEqual(add_integer(-2, 100), 98)
        self.assertEqual(add_integer(-98, -98), -196)
        """Works for floats"""
        self.assertEqual(add_integer(1.5, 99), 100.5)
        self.assertEqual(add_integer(-15.5, 31), 15.5)
        self.assertEqual(add_integer(-15.5, -15.5), -31)
        """Only works for integers and floats"""
        self.assertRaises(TypeError, add_integer, "two", 2)
        self.assertRaises(TypeError, add_integer, 2, "two")
        self.assertRaises(TypeError, add_integer, "two", "two")

if __name__ == '__main__':
    unittest.main()

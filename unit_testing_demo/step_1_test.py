import unittest

from step_1 import get_array_product

class TestGetArrayProduct(unittest.TestCase):
    def test_get_array_product(self):
        self.assertEqual(get_array_product([1,2]), 2)
        self.assertEqual(get_array_product([2,2]), 4)
        self.assertEqual(get_array_product([2]), 2)
        
        try:
            get_array_product([])
        except ValueError:
            pass
        else:
            self.fail("An empty array has no product, should raise a ValueError")
        print("TestGetArrayProduct tests passed")


if __name__ == "__main__":
    unittest.main()

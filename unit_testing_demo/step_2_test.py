import unittest
import os
from step_2 import CsvNumberManipulator

class TestCsvNumberManipulator(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("Running setUpClass")
        number_file = open("numbers.csv", "w")
        number_file.write("1,2,3,4,5\n")
        number_file.close()
        
    def setUp(self):
        print("Running setUp")
        self.csv_number_manipulator = CsvNumberManipulator("numbers.csv")        
        self.csv_number_manipulator.read_infile()
    
    def tearDown(self):
        print("Running tearDown")
        pass
    
    def test_get_csv_product(self):
        print("Running test_get_csv_product")
        computed_product = self.csv_number_manipulator.get_csv_product()
        expected_product = 120
        self.assertEqual(computed_product, expected_product)
        
    def test_get_csv_quotient(self):
        print("Running test_get_csv_quotient")
        computed_quotient = self.csv_number_manipulator.get_csv_quotient()
        expected_quotient = 1./2/3/4/5
        self.assertEqual(computed_quotient, expected_quotient)

    
    @classmethod
    def tearDownClass(self):
        print("Running tearDownClass")
        os.remove("numbers.csv")


if __name__ == "__main__":
    unittest.main()

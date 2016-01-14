import csv
import operator

class CsvNumberManipulator:
    def __init__(self, infile_path):
        self.infile_path = infile_path
        
    def read_infile(self):
        try:
            infile = open(self.infile_path, "r")
            self.numbers_to_manipulate = [float(value) for row in csv.reader(infile) for value in row]
        except Exception as e:
            print("Got an exception ")
            print(e)
            raise
            
    def get_csv_product(self):
        return reduce(operator.mul, self.numbers_to_manipulate)
    
    def get_csv_quotient(self):
        return reduce(operator.div, self.numbers_to_manipulate)


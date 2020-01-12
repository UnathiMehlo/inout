import unittest, csv
from datetime import datetime

from in_and_out import read_write


class Test(unittest.TestCase):
    
    def setUp(self):
        self.value_arr_output = {
            "Name":["Joe","Jane","John"],
            "Surname":["Soap","Doe","Smith"],
            "Age":["25","45","80"],
            "Parsed":["2019 14:06:42","2019 14:06:42","2019 14:06:42"]
        }
        
        self.value_arr_input = {
            "Name":["Joe","Jane","John"],
            "Surname":["Soap","Doe","Smith"],
            "Age":["25","45","80"],
        }
    
# testing for parsed    
    def test_read_write_parsed(self):
        test_code = read_write(self.value_arr_input,self.value_arr_output)
        self.assertIn(self.value_arr_output,test_code)
            
            
# # testing for date and time
#     def test_read_write_date(self):
#         with open('new_output.csv', 'r') as new_file:
#             inandout_reader = csv.reader(new_file)
#             arr = [i for i in inandout_reader]
#             now = datetime.now()
#             restval = now.strftime("%b %d %Y %H:%M:%S")
#             test_arr = arr[1][3]
#             self.assertEqual(test_arr,restval)
        
if __name__ == '__main__':
    unittest.main()

    # parser = argparse.ArgumentParser()
    # parser.add_argument("input_file",help="Place input file here")
    # parser.add_argument("output_file",help="Place output file here")

    # args = parser.parse_args()
    # test_read_write_parsed(args.input_file,args.output_file)
    

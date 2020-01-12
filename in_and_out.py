# import necessary modules
import argparse
import csv
import sys
from datetime import datetime



def read_write(read_file,write_file):
    
    with open(read_file, 'r') as csv_file:
        # create a variable that reads the file
        inandout_reader = csv.DictReader(csv_file) 
        
        # writing a new file
        with open(write_file, 'w') as new_file:
            
            # state headers
            fieldnames = ['Name', 'Surname', 'Age', 'Parsed']
            # use csv writer method, and conditions
            now = datetime.now()
            now.strftime("%b %d %Y %H:%M:%S")
            inandout_writer =  csv.DictWriter(new_file, fieldnames=fieldnames, restval=now.strftime("%b %d %Y %H:%M:%S"), delimiter=',')   
            
            inandout_writer.writeheader()
        
            for line in inandout_reader:
                inandout_writer.writerow(line)
                
        return inandout_writer
        
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file",help="Place input file here")
    parser.add_argument("output_file",help="Place output file here")

    args = parser.parse_args()
    read_write(args.input_file,args.output_file)
    
    
    


        
    

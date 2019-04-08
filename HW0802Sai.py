'''
@author Sai
File name: HW0802Sai.py
Date created: 3/27/2019
Date last modified: 3/27/2019
Python Version: 3.1
This program checks for delimiters and displays the values using generator
'''

import unittest


def file_reader(path, num_fields,sep,header):
    '''
    This function throws 
    a) FileNotFoundException => file is not found
    b) ValueError => if a line has more than num_fields after splitting the line with sep
    '''
    try:
        fp = open(path, 'r', encoding='utf-8')
        with fp:
            if header:
                next(fp)
 
            for i, line in enumerate(fp,1):
                array=list(line.strip().split(sep))
                if len(array) == num_fields:
                    yield tuple(array)
                else:
                    raise ValueError(f"ValueError: '{path}' has {len(array)} fields on line {i} but expected {num_fields}")
    except FileNotFoundError:
        raise FileNotFoundError(f"could not open file {path}")


class FileReaderTest(unittest.TestCase):
    
    
    def test_with_headers(self):
        file_name = 'test_with_headers.csv'
        value=list(file_reader(file_name, num_fields=3, sep=',', header=True))
        print(value)
        self.assertEqual(value,
        [('Sai', '10444910', 'Majors in software Engineering'),
         ('Sai1', '10555910', 'Majors in Electrical Engineering'), 
         ('Sai2', '10666910', 'Majors in Engineering Management'), ('Sai3', '10666910', 'Majors in Enviromental sciences')])

        

    def test_with_no_headers(self):
        file_name = 'test_with_no_headers.csv'
        value=list(file_reader(file_name, num_fields=3, sep=',', header=False))
        self.assertEqual(value,
         [('Sai', '10444910', 'Majors in software Engineering'),
         ('Sai1', '10555910', 'Majors in Electrical Engineering'), 
         ('Sai2', '10666910', 'Majors in Engineering Management'), ('Sai3', '10666910', 'Majors in Enviromental sciences')])
        
                        
    
    def test_file_not_found_exception(self):
        file_name = 'test1.csv'
        with self.assertRaises(FileNotFoundError) as context:
            list(file_reader(file_name, num_fields=3, sep=',', header=True))
        self.assertEqual(str(context.exception), f"could not open file {file_name}")    
        
    def test_value_error_with_headers(self):
        file_name = 'test_with_headers.csv'
        with self.assertRaises(ValueError) as context:
            list(file_reader(file_name, num_fields=4, sep=',', header=True))
        self.assertEqual(str(context.exception), f"ValueError: '{file_name}' has 3 fields on line 1 but expected 4")

    def test_value_error_with_no_headers(self):
        file_name = 'test_with_no_headers.csv'
        with self.assertRaises(ValueError) as context:
            list(file_reader(file_name, num_fields=2, sep=',', header=False))
        self.assertEqual(str(context.exception), f"ValueError: '{file_name}' has 3 fields on line 1 but expected 2")

    def test_value_errors(self):
        file_name = 'validation1.csv'
        with self.assertRaises(ValueError) as context:
            list(file_reader(file_name, num_fields=3, sep=',', header=True))
        self.assertEqual(str(context.exception), f"ValueError: '{file_name}' has 4 fields on line 2 but expected 3")
    

if __name__ == '__main__':
    path= "test_with_headers.csv"
    for cwid, name, major in file_reader(path, 3, sep=',', header=True):
        print("name: {} cwid: {} major: {}".format(name, cwid, major))

    unittest.main(exit=False, verbosity=2)
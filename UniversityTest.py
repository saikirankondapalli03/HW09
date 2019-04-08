from University import University
import unittest

class BookIndexTest(unittest.TestCase):

    def setUp(self):
        self.univ= University("stanford\\")

    def test_student_summary(self):
        self.univ.print_instructor_summary()
        self.univ.print_majors_summary()
        self.univ.print_student_summary()
        student_list = []     
        for eachstudent in self.univ.student_list.values():
            student_list.append(eachstudent.details())
        self.assertEqual(student_list,[['10103', 'Sai', 'SFEN', ['SSW 540', 'SSW 555', 'SSW 564A', 'SSW 810'], {'SSW 564', 'SSW 567'}, None], ['10115', 'Mark', 'SFEN', ['SSW 540', 'SSW 564A', 'SSW 810'], {'SSW 564', 'SSW 555', 'SSW 567'}, None], ['10172', 'Tobi', 'SFEN', ['SSW 540', 'SSW 810'], {'SSW 564', 'SSW 555', 'SSW 567'}, None]])


    def test_major_summary(self):
        self.univ.print_instructor_summary()
        self.univ.print_majors_summary()
        self.univ.print_student_summary()
        majors_list = []     
        for major in self.univ.majors_list.values():
            majors_list.append(major.details())
        print(majors_list)
        self.assertEqual(student_list,[['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']], ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]])
     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)           

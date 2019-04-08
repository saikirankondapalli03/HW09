'''
@author Sai
File name: Main.py
Date created: 4/3/2019
Date last modified: 4/3/2019
Python Version: 3.1
class Repository binds data of grades.txt
'''


import os

import unittest

from prettytable import PrettyTable
from HW0802Sai import file_reader

from Student import Student
from Instructor import Instructor
from Major import Major


class University: 

    def __init__(self, path):
        '''
        takes path as input and reads all the files, transforms   
        a) students.txt to list of student objects
        b) instructors.txt to list of instructor objects
        c) grades.txt to list of repository objects
        '''
        self.path= path; 
        self.student_list= dict()
        self.instructor_list= dict()
        self.majors_list= dict()
        self.read_majors(os.path.join(path+"\\majors.txt"))
        self.read_students(os.path.join(path+"\\students.txt"))
        self.read_instructors(os.path.join(path+"\\instructors.txt"))
        self.read_grades(os.path.join(path+"\\grades.txt"))
        

    def read_majors(self,path):
        '''
        this reads majors.txt with help of file_reader() from HW0802.py
        '''
        try:
            for dept,course_required ,course_name in file_reader(path, num_fields=3, sep='\t', header=False):
                if not dept in self.majors_list:
                    m= Major(dept)
                    m.add_course(course_required,course_name)
                    self.majors_list[dept]=m
                else:
                    self.majors_list[dept].add_course(course_required,course_name)
                    
        except ValueError as e: 
            print(f"Exception while reading majors data : {e}")
        except FileNotFoundError as e:
            print(f"Exception while reading majors data : {e}") 
            
    def read_students(self,path):
        '''
        this reads students.txt with help of file_reader() from HW0802.py
            '''
        student_list = list()
        try:
            for cwid, name, major in file_reader(path, num_fields=3, sep='\t', header=False):
                self.student_list[cwid]= Student(cwid,name,major)
        except ValueError as e: 
                print(f"Exception while reading students data : {e}")
        except FileNotFoundError as e:
                print(f"Exception while reading students data : {e}")
        return student_list


    def read_instructors(self,path):
        '''
        this reads instructors.txt with help of file_reader() from HW0802.py
        '''
        instructor_list = list()
        try:
            for cwid, name, department in file_reader(path, num_fields=3, sep='\t', header=False):
                self.instructor_list[cwid]= Instructor(cwid,name,department)
        except ValueError as e: 
            print(f"Exception while reading instructors data : {e}")
        except FileNotFoundError as e:
                print(f"Exception while reading instructors data : {e}")
        return instructor_list

    def read_grades(self,path):
        '''
        this reads grades.txt with help of file_reader() from HW0802.py
        '''
        try:
            for scwid,course,grade,icwid in file_reader(path, num_fields=4,sep="\t",header=False):
                if scwid in self.student_list:
                    st=self.student_list[scwid]
                    st.add_grade(course,grade,self.majors_list[st.major]) 

                if icwid in self.instructor_list:
                    self.instructor_list[icwid].add_student(course)
        except FileNotFoundError as e:
                print(f"Exception while reading grades data : {e}")
        except ValueError as e:
            print(e) 

    def print_student_summary(self):
        '''
        prints pretty table of student summary that has student id , name, courses he enrolled in 
        '''
        table= PrettyTable()
        table.field_names = ["CWID","Student name","Major","Completed courses","remaining courses","electives"]

        for student in self.student_list.values():
            table.add_row(student.details())

        print(f"Student Summary: \n {table}")


    def print_instructor_summary(self):
        '''
        prints pretty table of student summary that has student id , name, courses he enrolled in 
        '''
        table= PrettyTable()
        table.field_names = ["CWID","Name", "Department","Course","Students"]
        instructor_list = self.instructor_list.values()
        for eachinstructor in instructor_list:
            for row in eachinstructor.details():
                table.add_row(row)
        
        print(f"Instructor Summary: \n {table}")
        
    def print_majors_summary(self):
        '''
        prints pretty table of student summary that has student id , name, courses he enrolled in 
        '''
        table= PrettyTable()
        table.field_names = ["Dept","Required","electives"]

        for department in self.majors_list.values():
            table.add_row(department.details())

        print(f"Major Summary: \n {table}")


if __name__ == '__main__':
    path = input("please enter the path of repository: ")
    university = University(path)
    university.print_student_summary()
    university.print_instructor_summary()
    university.print_majors_summary()
    
    unittest.main(exit=False, verbosity=2)
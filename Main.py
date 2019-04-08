'''
@author Sai
File name: Main.py
Date created: 4/3/2019
Date last modified: 4/3/2019
Python Version: 3.1
class Repository binds data of grades.txt
'''


import os
import errno
import unittest

from prettytable import PrettyTable
from HW0802Sai import file_reader
from collections import defaultdict
from Student import Student
from Instructor import Instructor
from Repository import Repository

class University: 

    def __init__(self, path):
        '''
        takes path as input and reads all the files, transforms   
        a) students.txt to list of student objects
        b) instructors.txt to list of instructor objects
        c) grades.txt to list of repository objects
        '''
        self.student_list= read_students(path)
        self.instructor_list= read_instructors(path)
        self.grade_list = read_grades(path)

    def print_all_students(self):
        '''
        prints pretty table of students
        '''
        table = PrettyTable()
        table.field_names = ["CWID","Student name","Major"]
        for student in self.student_list:
            table.add_row([student.cwid,student.name,student.major])
        print(f"Student File Data: \n {table}")

    def print_all_instructors(self):
        '''
        prints pretty table of instructors
        '''
        table = PrettyTable()
        table.field_names = ["CWID","Instructor name","Department"]
        for instructor in self.instructor_list:
            table.add_row([instructor.cwid,instructor.name,instructor.department])
        print(f"Instructor File Data: \n {table}")

    def print_all_grades(self):
        '''
        prints pretty table of repository
        '''
        table = PrettyTable()
        table.field_names = ["Student CWID","Course","Grade","instructor CWID"]
        for grade in self.grade_list:
            table.add_row([grade.scwid,grade.course,grade.sgrade,grade.icwid])
        print(f"Repository File Data: \n {table}")
                
    def print_student_summary(self):
        '''
        prints pretty table of student summary that has student id , name, courses he enrolled in 
        '''
        student_course_grade= defaultdict(list);
        for grade in self.grade_list:
            student_course_grade[grade.scwid].append((grade.course,grade.sgrade))
          
        for student in self.student_list:
            #access student_course_grade by unique identity => cwid as shown below
            course_grade= dict(student_course_grade[student.cwid])
            for course,grade in course_grade.items():
               student.add_grade(course,grade)

        table = PrettyTable()
        table.field_names = ["CWID","Student name","Completed courses"]

        for student in self.student_list:
            table.add_row([student.cwid,student.name,sorted(student.courses.keys())])

        print(f"Student Summary: \n {table}")
        return self.student_list

    def print_instructor_summary(self):
        '''
        prints pretty table of Instructor summary that has instructor id , name, branch and no of students enrolled in his course
        '''
        instructor_course = [] ;
        for grade in self.grade_list:
            instructor_course.append((grade.icwid, grade.course))

        instructor_map = defaultdict(int)
        for instructor in self.instructor_list:
            instructor_map[instructor.cwid] = instructor
                
        for cwid, course_name in instructor_course:
            instructor= instructor_map[cwid]
            instructor.add_student(course_name)
               
        table = PrettyTable()
        table.field_names = ["CWID","Name", "Department","Course","Students"]

        for instructor in self.instructor_list:
            for key,value in instructor.course_students.items():
                table.add_row([instructor.cwid,instructor.name,instructor.department,key, value])

        print(f"Instructor Summary: \n {table}")
        return self.instructor_list

def read_students(path):
    '''
    this reads students.txt with help of file_reader() from HW0802.py
    '''
    student_list = list()
    try:
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                 if file == "students.txt" :
                    completepath=os.path.join(path+"\\"+file)
                    for value in file_reader(completepath, num_fields=3, sep='\t', header=False):
                        student_list.append(Student(value[0],value[1],value[2]))
    except Exception as e: 
            print(f"Exception while reading students data : {e}")
            return list()   
    return student_list


def read_instructors(path):
    '''
    this reads instructors.txt with help of file_reader() from HW0802.py
    '''
    instructor_list = list()
    try:
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                if file == "instructors.txt" :
                    completepath=os.path.join(path+"\\"+file)
                    for value in file_reader(completepath, num_fields=3, sep='\t', header=False):
                        instructor_list.append(Instructor(value[0],value[1],value[2]))
    except Exception as e: 
        print(f"Exception while reading instructors data : {e}")
        return list()    
    return instructor_list

def read_grades(path):
    '''
    this reads grades.txt with help of file_reader() from HW0802.py
    '''
    grade_list = list()
    try:
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                if file == "grades.txt" :
                    completepath=os.path.join(path+"\\"+file)
                    for value in file_reader(completepath, num_fields=4, sep='\t', header=False):
                        grade_list.append(Repository(value[0],value[1],value[2],value[3]))
    except Exception as e: 
        print(f"Exception while reading grades data: {e}")
        return list()    
    return grade_list       


class UniversityTest(unittest.TestCase):

    def test_student_summary(self):
        university= University(os.curdir+"/stanford/")
        student_list= university.print_student_summary()
        for student in student_list:
            if student.name=="Sai":
                self.assertEqual(3,len(student.courses.keys()))
            if student.name=="Mark":
                self.assertEqual(3,len(student.courses.keys()))
            if student.name=="Tobi":
                self.assertEqual(2,len(student.courses.keys()))

    def test_Instructor_summary(self):
        university= University(os.curdir+"/stanford/")
        instructor_list= university.print_instructor_summary()
        for instructor in instructor_list:
            if instructor.name=="Roland":
                self.assertEqual({'SSW 810': 3},instructor.course_students)
            if instructor.name=="Cohen":
                self.assertEqual({'SSW 540':  3}, instructor.course_students)
            if instructor.name=="Sanjeev":
                self.assertEqual({'SSW 564A': 2},instructor.course_students)
                 
        print("University test")




if __name__ == '__main__':
    path = input("please enter the path of repository: ")
    university = University(path)
    university.print_all_students()
    university.print_all_instructors()
    university.print_all_grades()
    university.print_student_summary()
    university.print_instructor_summary()
    
    unittest.main(exit=False, verbosity=2)
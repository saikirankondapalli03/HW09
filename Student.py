'''
@author Sai
File name: Student.py
Date created: 4/3/2019
Date last modified: 4/3/2019
Python Version: 3.1
class Student binds data of students.txt
'''

from collections import defaultdict

class Student: 
    def __init__(self, cwid , name, major):
        '''
        constructor for setting values
        '''
        self.cwid= cwid
        self.name= name
        self.major = major
        self.completed_courses= dict()
        self.remaining_courses= set()
        self.elective_courses= dict()
        #defaultdict of course and grade {'810':'A' , '564':'A-'} or for this problem ['564','810']
            
    def __str__(self):
        return (f"student name: {self.name}  cwid: {self.cwid}  major: {self.major}")
    
    def details(self):
        cwid= self.cwid
        name =self.name
        completed_courses = sorted(self.completed_courses.keys())
        elective_courses= None if len(set(self.elective_courses.keys())) ==0 else set(self.elective_courses.keys())
        remaining_courses = None if len(self.remaining_courses) ==0 else self.remaining_courses
        return [self.cwid,self.name,self.major,completed_courses,remaining_courses,elective_courses]

    def add_grade(self,course, grade , major):
        if course in major.electives:
            self.elective_courses[course] = grade
        else:
            self.completed_courses[course] = grade
            self.remaining_courses= set(major.required)-set(self.completed_courses.keys())

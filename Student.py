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
        self.courses= defaultdict(str) 
        #defaultdict of course and grade {'810':'A' , '564':'A-'} or for this problem ['564','810']
            
    def __str__(self):
        return (f"student name: {self.name}  cwid: {self.cwid}  major: {self.major}")

    def add_grade(self,course, grade):
        self.courses[course] = grade

if __name__ == '__main__':
    #path = input("please enter the path of repository: ")
    #read_students(path)
    s1= Student(1010,"sai","MS in CE")
    s1.add_grade('810','a')
    s1.add_grade('564','a-')
    print(s1.courses)
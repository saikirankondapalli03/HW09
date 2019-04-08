'''
@author Sai
File name: Instructor.py
Date created: 4/3/2019
Date last modified: 4/3/2019
Python Version: 3.1
class Insturctor binds data of instructors.txt
'''


from collections import defaultdict

class Instructor: 
    def __init__(self, cwid , name, department):
        '''
        constructor for setting values
        '''
        self.cwid= cwid
        self.name= name
        self.department = department
        self.course_students= defaultdict(int)
        #defaultdict of course and no of students {'810':'5' , '564':'6'} or for this problem ['564','810']
    
    def __str__(self):
        return (f"Instructor name: {self.name}  Instructor CWID: {self.cwid}  department: {self.department}")

    def add_student(self,student):
        self.course_students[student] += 1

if __name__ == '__main__':
    #path = input("please enter the path of repository: ")
    #read_students(path)
    i1= Instructor(1010,"inst1","SWE")
    i1.add_student("SSW 564")
    i1.add_student("SSW 564")
    i1.add_student("SSW 540")
    print(i1.course_students)
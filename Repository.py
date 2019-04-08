'''
@author Sai
File name: Repository.py
Date created: 4/3/2019
Date last modified: 4/3/2019
Python Version: 3.1
class Repository binds data of grades.txt
'''

class Repository: 
    def __init__(self, scwid , course, sgrade , icwid):
        '''
        constructor for setting values
        '''
        self.scwid= scwid
        self.course= course
        self.sgrade = sgrade
        self.icwid = icwid
    
    def __str__(self):
        return (f"student CWID: {self.scwid}  course: {self.course}  student grade: {self.sgrade} instructor CWID: {self.icwid}")





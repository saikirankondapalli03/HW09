'''
@author Sai
File name: DB_queries.py
Date created: 4/16/2019
Date last modified: 4/16/2019
Python Version: 3.1
This file connects to sql3 db and prints instructor summary
'''

import sqlite3
from prettytable import PrettyTable
DB_File= "db/810_startup.db"

try:
    db = sqlite3.connect(DB_File)

    table= PrettyTable()
    table.field_names = ["CWID","Name", "Department","Course","Students"]

    for row in db.execute("SELECT  ins.CWID,ins.NAME, ins.DEPT , gd.course, count(*) as number_of_students from HW11_instructors ins inner join HW11_grades gd    on gd.INSTRUCTOR_CWID=ins.CWID group by  ins.CWID,ins.NAME, ins.DEPT"):
        table.add_row([row[0],row[1],row[2],row[3],row[4]])

    print(f"Instructor Summary: \n {table}")
except Exception as e:
    print(f"Exception while trying to connect . root cause is {e}")
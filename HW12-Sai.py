'''
@author Sai
File name: HW12-Sai.py
Date created: 4/16/2019
Date last modified: 4/16/2019
Python Version: 3.1
This file connects to sql3 db and displays instructor table in html
'''

import sqlite3
DB_File= "db/810_startup.db"

from flask import Flask , render_template

app = Flask(__name__)

@app.route('/instructor_courses')
def template_demo():
    query="SELECT  ins.CWID,ins.NAME, ins.DEPT , gd.course, count(*) as number_of_students from HW11_instructors ins inner join HW11_grades gd    on gd.INSTRUCTOR_CWID=ins.CWID group by  gd.course order by ins.CWID desc";
    db= sqlite3.connect(DB_File)
    results= db.execute(query)
    data = [{
        'cwid': cwid, 
        'name': name,
        'dept': dept,
        'course': course,
        'number_of_students':number_of_students} for cwid, name, dept, course, number_of_students in results]
    return render_template('instructors.html',my_header="Stevens Repository",title="Number of students by course and instructor",instructors= data)

app.run(debug=True)
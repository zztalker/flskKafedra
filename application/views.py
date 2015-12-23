from flask import render_template, request
import json

from application import app, SessionSQL
from application.models import *


@app.route('/')
@app.route('/index')
def board():
    # from application.controllers import board
    # board.print_lecturers()
    return render_template('board.html', 
        lecturers = Lecturer.query.all(), disciplines = Discipline.query.all(),)

@app.route('/test', methods=['POST'])
def test():
    # print(request.form['Command'])
    # d = request.form['Data']
    # j = json.loads(d)
    # print(d)
    # print(j)
    # return 'test'
    if request.form['Command'] == 'UpdateTeachers':
        d = request.form['Data']
        j = json.loads(d)
        s = SessionSQL()
        # print(s.query(Lecturer.second_name).all())
        # with SessionContext() as session:
        lecturers = s.query(Lecturer.second_name).all()
        for lecturer in j.items():
            last_name = lecturer[1]["Name"].split(" ")[1]
            if last_name not in lecturers:
                print("kek")

    return 'test'   

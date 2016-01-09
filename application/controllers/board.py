# coding=utf8
from application.controllers import *

from application.models import board

def __return__():
    return render_template('board/board.html', 
        lecturers = board.Lecturer.query.all(), disciplines = board.Discipline.query.all())

def __return_modal__(id):
    lecturer = board.Lecturer.query.get(id)
    print("esdasd"+lecturer.description)
    return render_template("board/modal.html", lecturer = lecturer)
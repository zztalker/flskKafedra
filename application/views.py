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
    if request.form['Command'] == 'UpdateTeachers':
        lecturers_update()
    return 'test'

def lecturers_update():
    d = request.form['Data']
    j = json.loads(d)
    s = SessionSQL()

    lecturers_sname = s.query(Lecturer.second_name).all()
    for i in range(0, len(lecturers_sname)):
        #каждый из sname - массив с одним элементом, поэтому его нужно превратить строку:
        lecturers_sname[i] = lecturers_sname[i][0]

    for lecturer in j.items():
        # lecturer - это массив. В [0] нах-ся название папки лектора на сервере, в [1] - его данные
        second_name = lecturer[1]["Name"].split(" ")[0]
        if (second_name not in lecturers_sname):
            first_name = lecturer[1]["Name"].split(" ")[1]
            middle_name = lecturer[1]["Name"].split(" ")[2]
            description = lecturer[1]["Descr"]

            img_url = lecturer[1]["Photo"]["FileName"]
            img_url = lecturer_img(lecturer[0], img_url)

            lecturer_model = Lecturer(first_name = first_name, second_name = second_name,
                middle_name = middle_name, description = description, img_url = img_url)
            s.add(lecturer_model)
    s.commit()
    s.close()

def lecturer_img(dir_name, img_url):
    import shutil, os
    try:
        os.mkdir("application/static/img/lecturers/"+dir_name)
    except FileExistsError:
        pass
    shutil.copy(img_url, "application/static/img/lecturers/"+dir_name+"/photo.jpg")
    new_url = "static/img/lecturers/"+dir_name+"/photo.jpg"
    return new_url
from application import SessionSQL
from application.controllers import *
from application.models import board

from flask import request
import json

def __return__():
    if request.form['Command'] == 'UpdateTeachers':
            lecturers_update()
    return 'test'

def lecturers_update():
    d = request.form['Data']
    j = json.loads(d)
    s = SessionSQL()

    lecturers_sname = s.query(board.Lecturer.second_name).all()
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

            lecturer_model = board.Lecturer(first_name = first_name, second_name = second_name,
                middle_name = middle_name, description = description, img_url = img_url)
            s.add(lecturer_model)
    s.commit()
    s.close()

def lecturer_img(dir_name, img_url):
    import shutil, os
    from trans import trans
    dir_name = trans(dir_name)
    try:
        os.mkdir("application/static/img/lecturers/"+dir_name)
    except FileExistsError:
        pass
    shutil.copy(img_url, "application/static/img/lecturers/"+dir_name+"/photo.jpg")
    new_url = "static/img/lecturers/"+dir_name+"/photo.jpg"
    return new_url
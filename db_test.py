# Мой файл для тестирования sqlite3-базы

from application import SessionSQL
from application.models import *
s = SessionSQL()

# Удаление лекторов:
lecturers = s.query(Lecturer).all()
for lecturer in lecturers:
	s.delete(lecturer)

s.commit()
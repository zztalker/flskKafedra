#!flask/bin/python
'''
Скрипт выглядит сложным, но на самом деле он делает немного. 
Способ создания миграции SQLAlchemy-migrate состоит в сравнении структуры нашей базы данных 
(полученной из файла app.db) и структуры нашей модели (полученной из файла models.py). 
Различия между ними записываются как скрипт миграции внутри репозитория. Скрипт миграции знает 
как применить миграцию или отменить ее, таким образом всегда будет возможно обновить или 
«откатить» формат базы данных.

Пока у меня не было проблем с автоматической генерацией миграций вышеупомянутым скриптом, я мог 
наблюдать, что временами трудно определить, просто сравнивая старый и новый формат, какие 
изменения были сделаны. Для упрощения работы SQLAlchemy-migrate в определении изменений, я никогда 
не переименовываю существующие поля, ограничивая изменения добавлением/удалением моделей или 
полей, меняю типы созданных полей. И я всегда осматриваю сгенерированный скрипт миграции, чтобы 
удостовериться в его правильности.
'''
import imp
from migrate.versioning import api
from application import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))
tmp_module = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec(old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
open(migration, "wt").write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('New migration saved as ' + migration)
print('Current database version: ' + str(v))
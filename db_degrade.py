#!flask/bin/python
# Этот скрипт понизит базу данных на одну ревизию. 
# Вы можете запускать его множество раз, чтобы откатиться на несколько ревизий.
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
confirm = input("Are you sure you want to degrade base? [Y for Yes]: ")
if (confirm == 'Y') or (confirm == 'y'):
	v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
	api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
	print( 'Current database version: ' + 
		str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)) )
else: print( 'Okay then.' )
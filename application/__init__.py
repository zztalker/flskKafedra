from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.lesscss import lesscss

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionSQL = sessionmaker()
SessionSQL.configure(bind=engine)

#lesscss(app)

from application import views, models
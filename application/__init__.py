from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.assets import Environment, Bundle

#from flask.ext.lesscss import lesscss
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionSQL = sessionmaker()
SessionSQL.configure(bind=engine)

assets = Environment(app)
# assets.url = ; 
# assets.directory = app.static_folder; 
# assets.append_path('assets')
print(app.static_url_path)
scss = Bundle('../assets/scss/*.scss', filters='scss', output='css/scss-packed.css')
coffee = Bundle('../assets/coffee/*.coffee', filters='coffeescript', output='js/coffee-packed.js')
assets.register('scss_all', scss)
assets.register('coffee_all', coffee)

#lesscss(app)

from application import routes
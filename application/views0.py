from application import app
from flask import render_template, request
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
	# сделана с помощью включения.

@app.route('/info')
def info():
    return render_template('info.html')
	# переопределение футера

@app.route('/offers')
def offers():
    return render_template('offers.html')
	# дополнение контента

@app.route('/test', methods=['POST'])
def test():
    print(request.form['Command'])
    d = request.form['Data']
    j = json.loads(d)
    print(d)
    print(j)
    return 'test'

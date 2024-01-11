from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
# from flask_mysqlbd import MySQL

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'prueba'

# db = SQLAlchemy(app)
# app.secret_key = "mysecretkey"

# INDEX

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secundaria')
def secundaria():
    return render_template('forms/secundaria.html')

# @app.route('/consulta')
# def home():
#     #return 'Bienvenidos'
#     #return render_template('pruebauno.html')
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM usuarios')
#     data = cur.fetchall()
#     cur.close()
#     return render_template('pruebauno.html', usuarios = data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
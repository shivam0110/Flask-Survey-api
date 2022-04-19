from flask import Blueprint
from flask_mysqldb import MySQL


survey_api = Blueprint('survey_api', __name__)

survey_api.current_app.config['MYSQL_HOST'] = 'localhost'
survey_api.current_app.config['MYSQL_USER'] = 'root'
survey_api.current_app.config['MYSQL_PASSWORD'] = 'PASS1234'
survey_api.current_app.config['MYSQL_DB'] = 'survey'
mysql = MySQL(survey_api)

cursor = mysql.connection.cursor()

@survey_api.route('/surveys', methods = ['POST', 'GET'])
def surveys():
    if request.method == 'GET':
        cursor.execute("SELECT * FROM survey;")
        return cursor.fetchall()
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return "Done!!"

@survey_api.route('/surveys/<id>', methods = ['POST', 'GET'])
def surveyid(id):
    if request.method == 'GET':
        return "Login via the login Form"
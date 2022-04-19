from flask import Blueprint

question_api = Blueprint('question_api', __name__)

ques = {"question" : "bsfh djvsdf kv", "options" : "1. sdcc 2.fvs 3.vds 4.vds"}

@question_api.route('/question', methods = ['POST', 'GET'])
def question():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return "Done!!"

@question_api.route('/login/<id>', methods = ['POST', 'GET'])
def questionid(id):
    if request.method == 'GET':
        return "Login via the login Form"
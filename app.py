from flask import Flask,render_template, request
import json
from flask_mysqldb import MySQL
# from question import question_api
# from survey import survey_api
 
app = Flask(__name__)

# app.register_blueprint(question_api)
# app.register_blueprint(survey_api)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'PASS1234'
app.config['MYSQL_DB'] = 'survey'
 
mysql = MySQL(app)

@app.route('/')
def mainfun():
    return "Survey API"


#########################################  Survey API  #########################################
@app.route('/surveys', methods = ['POST', 'GET'])
def surveys():
    # Get all surveys
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM survey;")
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
    
    # Insert a new survey
    if request.method == 'POST':
        try:
            sid = request.json['id']
            question = request.json['question']
            options = request.json['options']

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO survey VALUES(%s,%s,%s)",(sid,question,options))
            mysql.connection.commit()
            cursor.close()
            return "Values inserted"
        except Exception as e:
            return(str(e))

@app.route('/surveys/<id>', methods = ['PUT', 'GET', 'DELETE'])
def surveyid(id):
    # Get a particular survey details from id
    if request.method == 'GET':
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM survey where id = %s;", (id))
            row_headers=[x[0] for x in cursor.description] #this will extract row headers
            rv = cursor.fetchall()
            json_data=[]
            for result in rv:
                    json_data.append(dict(zip(row_headers,result)))
            return json.dumps(json_data)
        except Exception as e:
            return(str(e))

    # Update values of a particular survey from id
    if request.method == 'PUT':
        try:
            question = request.json['question']
            options = request.json['options']

            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE survey set question = %s, options = %s WHERE id = %s",(question,options,id))
            mysql.connection.commit()
            cursor.close()
            return "Values Updated"
        except Exception as e:
            return(str(e))
    
    # DELETE values of a particular survey from id
    if request.method == 'DELETE':
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM survey WHERE id = %s",(id))
            mysql.connection.commit()
            cursor.close()
            return "Values DELETED"
        except Exception as e:
            return(str(e))





#########################################  QUESTION API  #########################################

@app.route('/question', methods = ['POST', 'GET'])
def question():
    # Get all questions
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM question;")
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
    
    # Insert a new question
    if request.method == 'POST':
        try:
            sid = request.json['id']
            question = request.json['question']
            options = request.json['options']
            survey_ref = request.json['survey_ref']

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO question VALUES(%s,%s,%s, %s)",(sid,question,options, survey_ref))
            mysql.connection.commit()
            cursor.close()
            return "Values inserted"
        except Exception as e:
            return(str(e))

@app.route('/question/<id>', methods = ['PUT', 'GET', 'DELETE'])
def questionid(id):
    # Get a particular question details from id
    if request.method == 'GET':
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM question where id = %s;", (id))
            row_headers=[x[0] for x in cursor.description] #this will extract row headers
            rv = cursor.fetchall()
            json_data=[]
            for result in rv:
                    json_data.append(dict(zip(row_headers,result)))
            return json.dumps(json_data)
        except Exception as e:
            return(str(e))

    # Update values of a particular question from id
    if request.method == 'PUT':
        try:
            question = request.json['question']
            options = request.json['options']
            survey_ref = request.json['survey_ref']

            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE question set question = %s, options = %s, survey_ref= %s WHERE id = %s",(question,options,survey_ref,id))
            mysql.connection.commit()
            cursor.close()
            return "Values Updated"
        except Exception as e:
            return(str(e))
    
    # DELETE values of a particular question from id
    if request.method == 'DELETE':
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM question WHERE id = %s",(id))
            mysql.connection.commit()
            cursor.close()
            return "Values DELETED"
        except Exception as e:
            return(str(e))






#########################################  RESPONSE API  #########################################

@app.route('/response', methods = ['POST', 'GET'])
def response():
    # Get all response
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM response;")
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
    
    # Insert a new response
    if request.method == 'POST':
        try:
            rid = request.json['id']
            response = request.json['response']
            ques_ref = request.json['ques_ref']

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO response VALUES(%s,%s,%s)",(rid,response,ques_ref))
            mysql.connection.commit()
            cursor.close()
            return "Values inserted"
        except Exception as e:
            return(str(e))

@app.route('/response/<id>', methods = ['PUT', 'GET', 'DELETE'])
def responseid(id):
    # Get a particular response details from id
    if request.method == 'GET':
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM response where id = %s;", (id))
            row_headers=[x[0] for x in cursor.description] #this will extract row headers
            rv = cursor.fetchall()
            json_data=[]
            for result in rv:
                    json_data.append(dict(zip(row_headers,result)))
            return json.dumps(json_data)
        except Exception as e:
            return(str(e))

    # Update values of a particular response from id
    if request.method == 'PUT':
        try:
            response = request.json['response']
            ques_ref = request.json['ques_ref']

            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE response set response = %s, ques_ref = %s WHERE id = %s",(response,ques_ref,id))
            mysql.connection.commit()
            cursor.close()
            return "Values Updated"
        except Exception as e:
            return(str(e))
    
    # DELETE values of a particular response from id
    if request.method == 'DELETE':
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM response WHERE id = %s",(id))
            mysql.connection.commit()
            cursor.close()
            return "Values DELETED"
        except Exception as e:
            return(str(e))



# TO DO: Implement auth

@app.route('/login', methods = ['POST', 'GET'])
def login():
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

@app.route('/login/<id>', methods = ['POST', 'GET'])
def loginid(id):
    if request.method == 'GET':
        return "Login via the login Form"

 
app.run(host='localhost', port=5000)
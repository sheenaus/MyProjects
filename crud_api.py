import os
from flask import Flask, render_template, request,jsonify
from flask import flash
import pypyodbc
import json
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")
@app.route("/upload", methods=['POST'])
def upload():
    print(APP_ROOT)
    target = os.path.join(APP_ROOT, 'json/')
    print("hello")

    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print('iam herr'+destination)
        file.save(destination)
    cwd =os.getcwd()
    print(cwd)
    json_file_path= destination###'%s/%s' %(cwd,'Emp.json')
    print(json_file_path)
    with open(json_file_path) as jfile:
        emp_j=jfile.read()
        emp_j='\''+emp_j+'\''
        query = 'insert into json_emp_1 values ('+emp_j + ')'
        print (query)
        conn = pypyodbc.connect('Driver={SQL Server};Server=<DbServername>;Database=testdb;uid=testuser;pwd=test123'),
        cursor = conn.cursor()
        jobj=cursor.execute("delete from  json_emp_1")
        cursor.execute(query)
        cursor.commit()
        squery = 'insert into EmployeesDetails (userID,firstName,lastName,jobTitleName,Ecode,region,phoneNumber,emailAddress)select userId,firstName,lastName,jobTitleName,employeeCode,region,phoneNumber,emailAddress from json_emp_1 t cross apply OPENJSON (t.json_Data, N\'$.Employees\')with (firstName varchar(100) N\'$.firstName\', jobTitleName varchar(100) N\'$.jobTitleName\',userId  varchar(100) N\'$.userId\',lastName  varchar(100) N\'$.lastName\',employeeCode  varchar(100) N\'$.employeeCode\',region  varchar(100) N\'$.region\',phoneNumber varchar(100) N\'$.phoneNumber\',emailAddress varchar(100) N\'$.emailAddress\')'
        print (squery)
        cursor.execute(squery)
        cursor.commit()
        rquery='select * from EmployeesDetails'
        all_emps = cursor.execute(rquery).fetchall()
        print(all_emps)
        conn.close()
        return (render_template("complete.html"))

@app.route("/Add", methods=['GET'])
def add_user():
    try:
        conn = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-SMNIM6O;Database=testdb;uid=testuser;pwd=test123')
        query_parameters = request.args
        UserID = query_parameters.get('UserID')
        Firstname = query_parameters.get('Firstname')
        Lastname = query_parameters.get('Lastname')
        cursor = conn.cursor()
        sql = 'INSERT INTO EmployeesDetails (userID,firstName,lastName) VALUES('
        sql=sql+str(UserID)+','+str(Firstname)+','+str(Lastname)+')'
        print(sql)
        cursor.execute(sql)
        conn.commit()
        resp = jsonify('User added successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/users', methods=['GET'])
def users():
	try:
		conn = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-SMNIM6O;Database=testdb;uid=testuser;pwd=test123')
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM EmployeesDetails")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
@app.route("/user/", methods=['GET'])
def user():
    try:
        conn = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-SMNIM6O;Database=testdb;uid=testuser;pwd=test123')
        query_parameters = request.args
        UserID = query_parameters.get('UserID')
        cursor = conn.cursor()
        sql = 'select * from EmployeesDetails where userID='
        sql=sql+str(UserID)
        print(sql)
        cursor.execute(sql)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
@app.route("/update/", methods=['GET'])
def update_user():
    try:
        conn = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-SMNIM6O;Database=testdb;uid=testuser;pwd=test123')
        query_parameters = request.args
        UserID = query_parameters.get('UserID')
        Firstname = query_parameters.get('Firstname')
        cursor = conn.cursor()
        sql = 'update EmployeesDetails set firstName = '+ str(Firstname)+' where  userID='+ str(UserID)
        print(sql)
        cursor.execute(sql)
        cursor.commit()
        resp = jsonify('User updated successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/delete/", methods=['GET'])
def delete_user():
    try:
        conn = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-SMNIM6O;Database=testdb;uid=testuser;pwd=test123')
        query_parameters = request.args
        UserID = query_parameters.get('UserID')
        Firstname = query_parameters.get('Firstname')
        cursor = conn.cursor()
        sql = 'delete from EmployeesDetails where userID='
        sql = sql + str(UserID)
        print(sql)
        cursor.execute(sql)
        cursor.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug='True')
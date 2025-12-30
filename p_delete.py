#!C:/python3/python
print("Content-type: text/html")
print()
import cgi

form=cgi.FieldStorage()

studentID=form.getvalue("student_id")

import mysql.connector

conn=mysql.connector.connect(user='root', password='', host='localhost', database='mystudent_db')
cursor=conn.cursor()
cursor.execute('DELETE FROM mystudent_tbl  WHERE student_id= '+studentID)
conn.commit()

cursor.close()
conn.close()

print(f'''
            <html>
                <head>
                    <title>
                        SMK Hua Lian E-Evaluation
                    </title>
                    <link rel="stylesheet" href="css/body.css">
                    <link rel="stylesheet" href="css/button.css">
                </head>
                <body>
                    <h1>Student Result has been Deleted Successfully!</h1>
                    <div style="margin-top: 20px;">
                        <a href="index.html">
                            <button>
                                Back To Home
                            </button>
                        </a>
                    </div>
                </body>
            </html>
          ''')
 
#!C:/python3/python
print("Content-type: text/html")
print()

import cgi

form=cgi.FieldStorage()

studentID=form.getvalue("student_id")

import mysql.connector

conn=mysql.connector.connect(user='root', password='', host='localhost', database='mystudent_db')
cursor=conn.cursor()
 
cursor.execute('''SELECT student_name, student_year_of_born, coursework_mark, examination_mark 
                FROM mystudent_tbl WHERE student_id=%s''', (studentID,))

row=cursor.fetchone()


def calculateMark():
    return int(row[2]) + int(row[3])
    
totalMark = calculateMark()
    
def defineGrade(totalMark):
    if totalMark >= 80:
        return "A"
    elif 70 <= totalMark <= 79:
        return "B"
    elif 60 <= totalMark <= 69:
        return "C"
    elif 50 <= totalMark <= 59:
        return "D"
    elif totalMark <= 49:
        return "F"
        
def defineComment(totalMark):
    if totalMark >= 80:
        return "Excellent"
    elif 70 <= totalMark <= 79:
        return "Well Done"
    elif 60 <= totalMark <= 69:
        return "Try Harder"
    elif 50 <= totalMark <= 59:
        return "Don't Give Up"
    elif totalMark <= 49:
        return "Repeat Again"

print(f'''
            <html>
                <head>
                    <title>
                        SMK Hua Lian E-Evaluation
                    </title>
                    <link rel="stylesheet" href="css/body.css">
                    <link rel="stylesheet" href="css/table.css">
                    <link rel="stylesheet" href="css/button.css">
                </head>
                <body>
                    <h1>Student Result has been Found!</h1>
                    <div class="student-table">
                        <div class="student-title">
                            Student ID
                        </div>
                        <div class="student-title">
                            Student Name
                        </div>
                        <div class="student-title">
                            Student Year of Born
                        </div>
                        <div class="student-title">
                            Evaluation Mark(%)
                        </div>
                        <div class="student-title">
                            Examination Mark(%)
                        </div>
                        <div class="student-title">
                            Total(%)
                        </div>
                        <div class="student-title">
                            Grade
                        </div>
                        <div class="student-title">
                            Comment
                        </div>
                        <div class="student-content">
                        {studentID}
                        </div>
                        <div class="student-content">
                            {row[0]}
                        </div>
                        <div class="student-content">
                            {row[1]}
                        </div>
                        <div class="student-content">
                            {row[2]}
                        </div>
                        <div class="student-content">
                            {row[3]}
                        </div>
                        <div class="student-content">
                            {totalMark}
                        </div>
                        <div class="student-content">
                            {defineGrade(totalMark)}
                        </div>
                        <div class="student-content">
                            {defineComment(totalMark)}
                        </div>
                    </div>
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

conn.commit()        
cursor.close()
conn.close()

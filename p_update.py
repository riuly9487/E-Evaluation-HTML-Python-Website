#!C:/python3/python
print("Content-type: text/html")
print()

import cgi

form=cgi.FieldStorage()

studentID=form.getvalue("student_id")
courseworkMark=form.getvalue("coursework_mark")
examinationMark=form.getvalue("examination_mark")

errorReturn = 0
isError = False

if courseworkMark > "60" and examinationMark > "40":
    errorReturn = 1001
    isError = True
elif courseworkMark < "0" and examinationMark < "0":
    errorReturn = 1002
    isError = True
elif courseworkMark > "60":
    errorReturn = 1003
    isError = True
elif examinationMark > "40":
    errorReturn = 1004
    isError = True
elif courseworkMark < "0":
    errorReturn = 1005
    isError = True
elif examinationMark < "0":
    errorReturn = 1006
    isError = True

def websiteGenerate(value):
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
                    <h1>Student Result has been Updated Successfully!</h1>
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
                        {value}
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

generateHTML = ''

def errorCode(value):
    if value == 1001:
        return '''<h1>Error code 1001, Coursework Mark and Examination Mark has exceeded its limits values.</h1>
                <a href="form_input.html">
                    <button>
                        Return
                    </button>
                </a>
                '''
    elif value == 1002:
        return '''<h1>Error code 1002, Coursework Mark and Examination Mark are negative values</h1>
                <a href="form_input.html">
                    <button>
                        Return
                    </button>
                </a>
                '''
    elif value == 1003:
        return '''<h1>Error code 1003, Coursework Mark has exceeded its limits values.</h1>
                <a href="form_input.html">
                    <button>
                        Return
                    </button>
                </a>
                '''
    elif value == 1004:
        return '''<h1>Error code 1004, Examination Mark has exceeded its limits values.</h1>
                <a href="form_input.html">
                    <button>
                        Return
                    </button>
                </a>
                '''
    elif value == 1005:
        return '''<h1>Error code 1005, Coursework Mark and Examination Mark are negative values.</h1>
                <a href="form_input.html">
                    <button>
                        Return
                    </button>
                </a>
                '''
    elif value == 1006:
        return '''<h1>Error code 1006, Coursework Mark and Examination Mark are negative values.</h1>
                <a href="form_input.html">
                    <button>
                        Return
                    </button>
                </a>
                '''
    elif value == 1007:
        return '''<h1>Error code 1007, Coursework Mark or Examination Mark consists of non-digits.</h1>
                <a href="form_input.html">
                    <button>
                        Return
                    </button>
                </a>
                '''

if isError:
    websiteGenerate(errorCode)
else:
    import mysql.connector

    conn=mysql.connector.connect(user='root', password='', host='localhost', database='mystudent_db')
    cursor=conn.cursor()
    
    conn.commit()

    cursor.execute('''UPDATE mystudent_tbl
                SET coursework_mark=%s,examination_mark=%s WHERE student_id=%s''',
                    (courseworkMark, examinationMark, studentID)
                )
    conn.commit()

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
    
    generateHTML += f'''
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
    '''

    websiteGenerate(generateHTML)
    
    cursor.close()
    conn.close()

 
 
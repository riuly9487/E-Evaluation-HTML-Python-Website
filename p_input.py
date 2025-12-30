#!C:/python3/python
print("Content-type: text/html")
print()

import cgi

form=cgi.FieldStorage()

studentName=form.getvalue("student_name")
studentYOB=form.getvalue("student_year_of_born")
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
    print(f'''<html>
                    <head>
                        <title>
                            SMK Hua Lian E-Evaluation
                        </title>
                        <link rel="stylesheet" href="css/body.css">
                        <link rel="stylesheet" href="css/button.css">
                    </head>
                    <body>
                        {value}
                    </body>
                </html>
                ''')
                
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
        
uploadSuccess='''
            <h1>Data Uploaded Successfully</h1>
            <a href="index.html">
                <button>
                    Back To Home
                </button>
            </a>
            '''


if isError:
    websiteGenerate(errorCode(errorReturn))
else:
    import mysql.connector

    conn=mysql.connector.connect(user='root', password='', host='localhost', database='mystudent_db')
    cursor=conn.cursor()
    cursor.execute('''Insert into mystudent_tbl 
                (student_name, student_year_of_born, coursework_mark, examination_mark) values(%s,%s,%s,%s)'''
                ,(studentName,studentYOB,courseworkMark,examinationMark)
                )
    conn.commit()

    cursor.close()
    conn.close()
    
    websiteGenerate(uploadSuccess)
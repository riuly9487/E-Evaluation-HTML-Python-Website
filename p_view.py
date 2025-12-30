#!C:/python3/python
print("Content-type: text/html")
print()

import mysql.connector

conn=mysql.connector.connect(user='root', password='', host='localhost', database='mystudent_db')
cursor=conn.cursor()
 
conn.commit()

cursor.execute('SELECT * FROM mystudent_tbl')

data = cursor.fetchall()

generateHTML = ''

a = 1
for row in data:
    
    def calculateMark():
        return int(row[3]) + int(row[4])
    
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
                {row[4]}
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
    a += 1

def generateWebsite(value):
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
                    <h1>All Student Data Displayed Successfully</h1>
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
                    <h1>Number of Records: {a-1}</h1>
                    <a href="index.html">
                        <button>
                            Back To Home
                        </button>
                    </a>
                </body>
            </html>
          ''')

cursor.close()
conn.close()

generateWebsite(generateHTML)
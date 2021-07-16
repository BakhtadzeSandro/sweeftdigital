# -------------------1--------------------

def my_function(str):
    str = input("Enter any string: ")
    return str == str[::-1]

result = my_function(str)
print(result)

# -------------------2--------------------


import math

x = int(input("Enter the sum of coins: "))
coins=[50,20,10,5,1]
coins.sort(reverse=True)

def findanswer(x):
    result = 0
    for i in range(len(coins)):
        quantity = math.floor(x/coins[i])
        reminder = x % coins[i]
        x = reminder
        result = result + quantity
        if reminder == 0:
            break
    print(result)

if __name__ == '__main__':
    findanswer(x)


# ------------------3-------------------


x = input('enter: ')

def findanswer(x):
    counter = 0
    for i in x:
        if i == '(':
            counter = counter + 1
        elif i == ')':
            counter = counter - 1
        if counter<0:
            break
    if counter==0:
        print("Yes",counter)
    else:
        print("No", counter)


if __name__ == '__main__':
    findanswer(x)


# ------------------5-------------------


import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS teacher(teacherID INTEGER,name TEXT, lastname TEXT, age INTEGER, subject TEXT,PRIMARY KEY(teacherID))")
cursor.execute("CREATE TABLE IF NOT EXISTS pupil(teacherID INTEGER,name TEXT, lastname TEXT, age INTEGER, grade INTEGER,PRIMARY KEY(teacherID))")
cursor.execute("INSERT INTO main.teacher VALUES( 15 ,'Beqa', 'Tsikarishvili' ,22, 'Liberalism')")
cursor.execute("INSERT INTO main.pupil VALUES( 15 ,'Giorgi', 'Mechiauri' ,20, 12 )")
connection.commit()
cursor.execute("SELECT teacher.name FROM teacher INNER JOIN pupil ON teacher.teacherID = pupil.teacherID WHERE pupil.name = 'Giorgi'")
for i in cursor:
    print(i)


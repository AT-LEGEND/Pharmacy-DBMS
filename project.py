from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

'''mydb = mysql.connect(
  host="localhost",
  user="root",
  password="LETSdoDBMS8"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
mycursor.commit()
mycursor.close()'''

con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="mydatabase"
    )

cursor = con.cursor()

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
cursor.execute("drop table Login")
cursor.execute("CREATE TABLE IF NOT EXISTS Login(Login_username varchar(20) primary key, Login_password varchar(20))")
sql = "INSERT INTO Login (Login_username, Login_password) VALUES (%s, %s)"
val = ("a", "b")
cursor.execute(sql, val)
cursor.execute("commit")
con.close()
print("mysql is closed")

def submit():

    username=e_username.get()
    password=e_password.get()
    print(username)
    if(username=="" or password==""):
        MessageBox.showinfo("Insert Status","All Field are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="LETSdoDBMS8", database="mydatabase")
        cursor = con.cursor()        
        cursor.execute("select * from login where Login_username=\'"+username+"\'")
        result = cursor.fetchall()
        for row in result:
            print(row)
            if row==password:
                print("Entry granted")
        con.close()

root= Tk()

root.geometry('500x500')

root.title("Python+Tkinter+Mysql")

username= Label( root,text='Enter Username', font=('bold', 10))
username.place(x=30, y=100)

password = Label (root, text='Enter Password', font=('bold',10))
password.place(x=30, y=140)

e_username= Entry()
e_username.place(x=150, y=100)

e_password= Entry()
e_password.place(x=150, y=140)

submit = Button(root, text="Submit", command=submit)
submit.place(x=100, y=180)
root.mainloop()
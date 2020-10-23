from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def addmed():

    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )

    cursor = con.cursor()
    cursor.execute("DELETE FROM medicine WHERE medicine_id='1003'")
    cursor.execute("INSERT INTO medicine VALUES ('"+med_id_adder.get()+"', '"+med_name_adder.get()+"', '"+med_cost_adder.get()+"', '"+med_brand_adder.get()+"')")
    con.commit()
    con.close()
    med_id_adder.delete(0,END)
    med_name_adder.delete(0,END)
    med_cost_adder.delete(0,END)
    med_brand_adder.delete(0,END)

def addbatch():

    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )

    cursor = con.cursor()
    cursor.execute("INSERT INTO batch VALUES ('"+batch_no_adder.get()+"', '"+batch_med_stock_adder.get()+"', '"+batch_mfg_adder.get()+"', '"+batch_expdate_adder.get()+"')")
    con.commit()
    con.close()

    batch_no_adder.delete(0,END)
    batch_med_stock_adder.delete(0,END)
    batch_mfg_adder.delete(0,END)
    batch_expdate_adder.delete(0,END)

def addorg():
    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )

    cursor = con.cursor()
    cursor.execute("INSERT INTO organisation VALUES ('"+org_id_adder.get()+"', '"+org_name_adder.get()+"', '"+org_type_adder.get()+"', '"+org_contact_adder.get()+"')")
    con.commit()
    con.close()

    org_id_adder.delete(0,END)
    org_name_adder.delete(0,END)
    org_type_adder.delete(0,END)
    org_contact_adder.delete(0,END)

def adduser():

    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )

    cursor = con.cursor()
    cursor.execute("INSERT INTO user VALUES ('"+username_adder.get()+"', '"+user_phone_adder.get()+"', '"+user_email_adder.get()+"', '"+user_street_adder.get()+"', '"+user_city_adder.get()+"', '"+user_state_adder.get()+"', '"+user_pincode_adder.get()+"')")
    con.commit()
    con.close()

    username_adder.delete(0,END)
    user_phone_adder.delete(0,END)
    user_email_adder.delete(0,END)
    user_street_adder.delete(0,END)
    user_city_adder.delete(0,END)
    user_state_adder.delete(0,END)
    user_pincode_adder.delete(0,END)


def addsaledetails():
    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )

    cursor = con.cursor()
    cursor.execute("INSERT INTO sale_details VALUES ('"+sale_date_adder.get()+"', '"+sale_id_adder.get()+"', '"+sale_user_id_adder.get()+"', '"+sale_org_id_adder.get()+"', '"+user_city_adder.get()+"', '"+user_state_adder.get()+"', '"+user_pincode_adder.get()+"')")
    con.commit()
    con.close()

    sale_date_adder.delete(0,END)
    sale_id_adder.delete(0,END)
    sale_user_id_adder.delete(0,END)
    sale_org_id_adder.delete(0,END)

'''def addsales():

    sale_id_adder.delete(0,END)
    sale_med_id_adder.delete(0,END)
    #med_cost_adder
    sale_amount_adder.delete(0,END)
    sale_batch_no_adder.delete(0,END)
    sale_quantity_adder.delete(0,END)
    
'''

'''def var1():
    return var.get()
def activateCheck(var):
    #global sale_org_id
    
    sale_org_id= Entry(adder,width=30)
    sale_org_id.grid(row=18, column=1)
    if var1() == 1:          #whenever checked
        sale_org_id.config(state=NORMAL)
    elif var1() == 0:        #whenever unchecked
        sale_org_id.config(state=DISABLED)'''

def add():
    global adder
    adder=Tk()
    adder.title("Add a record")
    adder.geometry("600x700")
    '''v = Scrollbar(adder)
    t = Text(adder, width = 15, height = 15, wrap = NONE, yscrollcommand = v.set)
    v.config(command=t.yview)
    v.grid(sticky=E, row = 0, rowspan =10, column = 20, ipady = 1000)'''


    med_id_label_adder= Label(adder,text='Enter med_id', font=('bold', 10))
    med_id_label_adder.grid(row=0, column=0)
    med_name_label_adder = Label (adder, text='Enter med_name', font=('bold',10))
    med_name_label_adder.grid(row=1, column=0)
    med_cost_label_adder= Label( adder,text='Enter med_cost', font=('bold', 10))
    med_cost_label_adder.grid(row=2, column=0)
    med_brand_label_adder = Label (adder, text='Enter med_brand', font=('bold',10))
    med_brand_label_adder.grid(row=3, column=0)
    
    global med_id_adder,med_name_adder,med_cost_adder,med_brand_adder
    med_id_adder= Entry(adder,width=30)
    med_id_adder.grid(row=0, column=1)
    med_name_adder= Entry(adder,width=30)
    med_name_adder.grid(row=1, column=1)
    med_cost_adder= Entry(adder,width=30)
    med_cost_adder.grid(row=2, column=1)
    med_brand_adder= Entry(adder,width=30)
    med_brand_adder.grid(row=3, column=1)
    addmed1 = Button(adder, text="Add Medicine Data", command=addmed)
    addmed1.grid(row=4,column=0)

    batch_no_label_adder= Label( adder,text='Enter batch_no', font=('bold', 10))
    batch_no_label_adder.grid(row=5, column=0,pady=(10,0))
    batch_med_stock_label_adder = Label (adder, text='Enter batch_med_stock', font=('bold',10))
    batch_med_stock_label_adder.grid(row=6, column=0)
    batch_mfg_label_adder= Label( adder,text='Enter batch_mfg', font=('bold', 10))
    batch_mfg_label_adder.grid(row=7, column=0)
    batch_expdate_label_adder = Label (adder, text='Enter batch_expdate', font=('bold',10))
    batch_expdate_label_adder.grid(row=8, column=0)
    
    global batch_no_adder,batch_med_stock_adder,batch_mfg_adder,batch_expdate_adder
    batch_no_adder= Entry(adder,width=30)
    batch_no_adder.grid(row=5, column=1, pady=(10,0))
    batch_med_stock_adder= Entry(adder,width=30)
    batch_med_stock_adder.grid(row=6, column=1)
    batch_mfg_adder= Entry(adder,width=30)
    batch_mfg_adder.grid(row=7, column=1)
    batch_expdate_adder= Entry(adder,width=30)
    batch_expdate_adder.grid(row=8, column=1)
    addbatch1 = Button(adder, text="Add Batch Data", command=addbatch)
    addbatch1.grid(row=9, column=0)
    
    org_id_label_adder= Label(adder,text='Enter org_id', font=('bold', 10))
    org_id_label_adder.grid(row=10, column=0)
    org_name_label_adder = Label (adder, text='Enter org_name', font=('bold',10))
    org_name_label_adder.grid(row=11, column=0)
    org_type_label_adder= Label( adder,text='Enter org_type', font=('bold', 10))
    org_type_label_adder.grid(row=12, column=0)
    org_contact_label_adder = Label (adder, text='Enter org_contact', font=('bold',10))
    org_contact_label_adder.grid(row=13, column=0)
    
    global org_id_adder,org_name_adder,org_type_adder,org_contact_adder
    org_id_adder= Entry(adder,width=30)
    org_id_adder.grid(row=10, column=1)
    org_name_adder= Entry(adder,width=30)
    org_name_adder.grid(row=11, column=1)
    org_type_adder= Entry(adder,width=30)
    org_type_adder.grid(row=12, column=1)
    org_contact_adder= Entry(adder,width=30)
    org_contact_adder.grid(row=13, column=1)
    addorg1 = Button(adder, text="Add Org Data", command=addorg)
    addorg1.grid(row=14,column=0)

    '''global var
    var= IntVar()
    global check
    check=Checkbutton(adder,text="Use same org_id",variable=var,command=lambda: activateCheck(var))
    check.grid(row=15,column=2)'''

    sale_date_label_adder= Label(adder,text='Enter sale_date', font=('bold', 10))
    sale_date_label_adder.grid(row=15, column=0)
    sale_id_label_adder = Label (adder, text='Enter sale_id', font=('bold',10))
    sale_id_label_adder.grid(row=16, column=0)
    sale_user_id_label_adder= Label( adder,text='Enter sale_user_id', font=('bold', 10))
    sale_user_id_label_adder.grid(row=17, column=0)
    sale_org_id_label_adder = Label (adder, text='Enter sale_org_id', font=('bold',10))
    sale_org_id_label_adder.grid(row=18, column=0)
    
    global sale_date_adder,sale_id_adder,sale_user_id_adder,sale_org_id_adder
    sale_date_adder= Entry(adder,width=30)
    sale_date_adder.grid(row=15, column=1)
    sale_id_adder= Entry(adder,width=30)
    sale_id_adder.grid(row=16, column=1)
    sale_user_id_adder= Entry(adder,width=30)
    sale_user_id_adder.grid(row=17, column=1)
    sale_org_id_adder= Entry(adder,width=30)
    sale_org_id_adder.grid(row=18, column=1)
    
    addsaledet1 = Button(adder, text="Add sale details Data", command=addsaledetails)
    addsaledet1.grid(row=19,column=0)

    username_label_adder= Label(adder,text='Enter username', font=('bold', 10))
    username_label_adder.grid(row=20, column=0)
    user_phone_label_adder = Label (adder, text='Enter user_phone', font=('bold',10))
    user_phone_label_adder.grid(row=21, column=0)
    user_email_label_adder= Label( adder,text='Enter user_email', font=('bold', 10))
    user_email_label_adder.grid(row=22, column=0)
    user_street_label_adder = Label (adder, text='Enter user_street', font=('bold',10))
    user_street_label_adder.grid(row=23, column=0)
    user_city_label_adder= Label(adder,text='Enter user_city', font=('bold', 10))
    user_city_label_adder.grid(row=24, column=0)
    user_state_label_adder = Label (adder, text='Enter user_state', font=('bold',10))
    user_state_label_adder.grid(row=25, column=0)
    user_pincode_label_adder= Label( adder,text='Enter user_pincode', font=('bold', 10))
    user_pincode_label_adder.grid(row=26, column=0)
    
    global username_adder,user_phone_adder,user_email_adder,user_street_adder,user_city_adder,user_state_adder,user_pincode_adder
    username_adder= Entry(adder,width=30)
    username_adder.grid(row=20, column=1)
    user_phone_adder= Entry(adder,width=30)
    user_phone_adder.grid(row=21, column=1)
    user_email_adder= Entry(adder,width=30)
    user_email_adder.grid(row=22, column=1)
    user_street_adder= Entry(adder,width=30)
    user_street_adder.grid(row=23, column=1)
    user_city_adder= Entry(adder,width=30)
    user_city_adder.grid(row=24, column=1)
    user_state_adder= Entry(adder,width=30)
    user_state_adder.grid(row=25, column=1)
    user_pincode_adder= Entry(adder,width=30)
    user_pincode_adder.grid(row=26, column=1)
    adduser1 = Button(adder, text="Add User Data", command=adduser)
    adduser1.grid(row=27,column=0)
    
    adder.mainloop()
def update():
    global updater
    updater=Tk()
    updater.title("Update a record")
    updater.geometry("600x700")
    '''v = Scrollbar(updater)
    t = Text(updater, width = 15, height = 15, wrap = NONE, yscrollcommand = v.set)
    v.config(command=t.yview)
    v.grid(sticky=E, row = 0, rowspan =10, column = 20, ipady = 1000)'''

    med_id_label_updater= Label(updater,text='Enter med_id', font=('bold', 10))
    med_id_label_updater.grid(row=0, column=0)
    med_name_label_updater = Label (updater, text='Enter med_name', font=('bold',10))
    med_name_label_updater.grid(row=1, column=0)
    med_cost_label_updater= Label( updater,text='Enter med_cost', font=('bold', 10))
    med_cost_label_updater.grid(row=2, column=0)
    med_brand_label_updater = Label (updater, text='Enter med_brand', font=('bold',10))
    med_brand_label_updater.grid(row=3, column=0)
    
    global med_id_updater,med_name_updater,med_cost_updater,med_brand_updater
    med_id_updater= Entry(updater,width=30)
    med_id_updater.grid(row=0, column=1)
    med_name_updater= Entry(updater,width=30)
    med_name_updater.grid(row=1, column=1)
    med_cost_updater= Entry(updater,width=30)
    med_cost_updater.grid(row=2, column=1)
    med_brand_updater= Entry(updater,width=30)
    med_brand_updater.grid(row=3, column=1)
    updatemed1 = Button(updater, text="Update Medicine Data", command=updatemed)
    updatemed1.grid(row=4,column=0)

    batch_no_label_updater= Label( updater,text='Enter batch_no', font=('bold', 10))
    batch_no_label_updater.grid(row=5, column=0,pady=(10,0))
    batch_med_stock_label_updater = Label (updater, text='Enter batch_med_stock', font=('bold',10))
    batch_med_stock_label_updater.grid(row=6, column=0)
    batch_mfg_label_updater= Label( updater,text='Enter batch_mfg', font=('bold', 10))
    batch_mfg_label_updater.grid(row=7, column=0)
    batch_expdate_label_updater = Label (updater, text='Enter batch_expdate', font=('bold',10))
    batch_expdate_label_updater.grid(row=8, column=0)
    
    global batch_no_updater,batch_med_stock_updater,batch_mfg_updater,batch_expdate_updater
    batch_no_updater= Entry(updater,width=30)
    batch_no_updater.grid(row=5, column=1, pady=(10,0))
    batch_med_stock_updater= Entry(updater,width=30)
    batch_med_stock_updater.grid(row=6, column=1)
    batch_mfg_updater= Entry(updater,width=30)
    batch_mfg_updater.grid(row=7, column=1)
    batch_expdate_updater= Entry(updater,width=30)
    batch_expdate_updater.grid(row=8, column=1)
    updatebatch1 = Button(updater, text="Update Batch Data", command=updatebatch)
    updatebatch1.grid(row=9, column=0)
    
    org_id_label_updater= Label(updater,text='Enter org_id', font=('bold', 10))
    org_id_label_updater.grid(row=10, column=0)
    org_name_label_updater = Label (updater, text='Enter org_name', font=('bold',10))
    org_name_label_updater.grid(row=11, column=0)
    org_type_label_updater= Label( updater,text='Enter org_type', font=('bold', 10))
    org_type_label_updater.grid(row=12, column=0)
    org_contact_label_updater = Label (updater, text='Enter org_contact', font=('bold',10))
    org_contact_label_updater.grid(row=13, column=0)
    
    global org_id_updater,org_name_updater,org_type_updater,org_contact_updater
    org_id_updater= Entry(updater,width=30)
    org_id_updater.grid(row=10, column=1)
    org_name_updater= Entry(updater,width=30)
    org_name_updater.grid(row=11, column=1)
    org_type_updater= Entry(updater,width=30)
    org_type_updater.grid(row=12, column=1)
    org_contact_updater= Entry(updater,width=30)
    org_contact_updater.grid(row=13, column=1)
    updateorg1 = Button(updater, text="Update Org Data", command=updateorg)
    updateorg1.grid(row=14,column=0)

    '''global var
    var= IntVar()
    global check
    check=Checkbutton(updater,text="Use same org_id",variable=var,command=lambda: activateCheck(var))
    check.grid(row=15,column=2)'''

    sale_date_label_updater= Label(updater,text='Enter sale_date', font=('bold', 10))
    sale_date_label_updater.grid(row=15, column=0)
    sale_id_label_updater = Label (updater, text='Enter sale_id', font=('bold',10))
    sale_id_label_updater.grid(row=16, column=0)
    sale_user_id_label_updater= Label( updater,text='Enter sale_user_id', font=('bold', 10))
    sale_user_id_label_updater.grid(row=17, column=0)
    sale_org_id_label_updater = Label (updater, text='Enter sale_org_id', font=('bold',10))
    sale_org_id_label_updater.grid(row=18, column=0)
    
    global sale_date_updater,sale_id_updater,sale_user_id_updater,sale_org_id_updater
    sale_date_updater= Entry(updater,width=30)
    sale_date_updater.grid(row=15, column=1)
    sale_id_updater= Entry(updater,width=30)
    sale_id_updater.grid(row=16, column=1)
    sale_user_id_updater= Entry(updater,width=30)
    sale_user_id_updater.grid(row=17, column=1)
    sale_org_id_updater= Entry(updater,width=30)
    sale_org_id_updater.grid(row=18, column=1)
    
    updatesaledet1 = Button(updater, text="Update sale details Data", command=updatesaledetails)
    updatesaledet1.grid(row=19,column=0)

    username_label_updater= Label(updater,text='Enter username', font=('bold', 10))
    username_label_updater.grid(row=20, column=0)
    user_phone_label_updater = Label (updater, text='Enter user_phone', font=('bold',10))
    user_phone_label_updater.grid(row=21, column=0)
    user_email_label_updater= Label( updater,text='Enter user_email', font=('bold', 10))
    user_email_label_updater.grid(row=22, column=0)
    user_street_label_updater = Label (updater, text='Enter user_street', font=('bold',10))
    user_street_label_updater.grid(row=23, column=0)
    user_city_label_updater= Label(updater,text='Enter user_city', font=('bold', 10))
    user_city_label_updater.grid(row=24, column=0)
    user_state_label_updater = Label (updater, text='Enter user_state', font=('bold',10))
    user_state_label_updater.grid(row=25, column=0)
    user_pincode_label_updater= Label( updater,text='Enter user_pincode', font=('bold', 10))
    user_pincode_label_updater.grid(row=26, column=0)
    
    global username_updater,user_phone_updater,user_email_updater,user_street_updater,user_city_updater,user_state_updater,user_pincode_updater
    username_updater= Entry(updater,width=30)
    username_updater.grid(row=20, column=1)
    user_phone_updater= Entry(updater,width=30)
    user_phone_updater.grid(row=21, column=1)
    user_email_updater= Entry(updater,width=30)
    user_email_updater.grid(row=22, column=1)
    user_street_updater= Entry(updater,width=30)
    user_street_updater.grid(row=23, column=1)
    user_city_updater= Entry(updater,width=30)
    user_city_updater.grid(row=24, column=1)
    user_state_updater= Entry(updater,width=30)
    user_state_updater.grid(row=25, column=1)
    user_pincode_updater= Entry(updater,width=30)
    user_pincode_updater.grid(row=26, column=1)
    updateuser1 = Button(updater, text="Update User Data", command=updateuser)
    updateuser1.grid(row=27,column=0)
    
    updater.mainloop()

def delete():
    print('a')

root=Tk()
root.title("DBMS")
root.geometry("600x300")

id=Label(root)

con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )

add = Button(root, text="Add New Data", command=add)
add.place(x=100, y=180)
add.pack()
#update and delete function main page
med_id_label= Label(root,text='Enter med_id', font=('bold', 10))
med_id_label.place(x=100, y=40)
#med_id_label.pack()
med_id= Entry(root,width=30)
med_id.place(x=200, y=40)
#med_id.pack()

batch_no_label= Label( root,text='Enter batch_no', font=('bold', 10))
batch_no_label.place(x=100, y=60)
#batch_no_label.pack()
batch_no= Entry(root,width=30)
batch_no.place(x=200, y=60)
#batch_no.pack()

sale_id_label = Label (root, text='Enter sale_id', font=('bold',10))
sale_id_label.place(x=100, y=80)
#sale_id_label.pack()
sale_id= Entry(root,width=30)
sale_id.place(x=200, y=80)
#sale_id.pack()

org_id_label= Label(root,text='Enter org_id', font=('bold', 10))
org_id_label.place(x=100, y=100)
#org_id_label.pack()
org_id= Entry(root,width=30)
org_id.place(x=200, y=100)
#org_id.pack()

username_label= Label(root,text='Enter username', font=('bold', 10))
username_label.place(x=100, y=120)
#username_label.pack()
username= Entry(root,width=30)
username.place(x=200, y=120)
#username.pack()

update = Button(root, text="Update Data", command=update)
update.place(x=250, y=150)

delete = Button(root, text="Delete Data", command=delete)
delete.place(x=250, y=190)



print("in")
cursor = con.cursor()
con.close()
root.mainloop()

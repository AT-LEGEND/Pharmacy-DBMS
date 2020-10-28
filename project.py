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
def updatemed():
    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )
    batch_no_updater.config(state=DISABLED)
    cursor = con.cursor()
    cursor.execute("UPDATE medicine SET MEDICINE_NAME='"+med_name_updater.get()+"', medicine_cost='"+med_cost_updater.get()+"', medicine_brand= '"+med_brand_updater.get()+"' where medicine_id='"+med_id_updater.get()+"'")
    con.commit()
    con.close()

def updatebatch():
    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )
    batch_no_updater.config(state=DISABLED)
    cursor = con.cursor()
    cursor.execute("UPDATE batch SET MEDICINE_STOCK='"+batch_med_stock_updater.get()+"', MANUFACTURE_DATE='"+batch_mfg_updater.get()+"', EXPIRY_DATE= '"+batch_expdate_updater.get()+"' where BATCH_NO='"+batch_no_updater.get()+"'")
    con.commit()
    con.close()

def updateorg():
    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )
    cursor = con.cursor()
    cursor.execute("UPDATE organisation SET org_name='"+org_name_updater.get()+"', org_type='"+org_type_updater.get()+"', contact_no= '"+org_contact_updater.get()+"' where org_id='"+org_id_updater.get()+"'")
    con.commit()
    con.close()

def updatesaledetails():
    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )
    cursor = con.cursor()
    cursor.execute("UPDATE sale_details SET org_id='"+sale_org_id_updater.get()+"', user_id='"+sale_user_id_updater.get()+"'where sale_id='"+sale_id_updater.get()+"'")
    con.commit()
    con.close()

def updateuser():
    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )
    cursor = con.cursor()
    cursor.execute("UPDATE user_info SET phone_number='"+user_phone_updater.get()+"', email='"+user_email_updater.get()+"', street_user='"+user_street_updater.get()+"', user_city='"+user_city_updater.get()+"', user_state='"+user_state_updater.get()+"', pincode='"+user_pincode_updater.get()+"'where username='"+username_updater.get()+"'")
    con.commit()
    con.close()
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
def updater():
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
    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )

    cursor = con.cursor()
    cursor.execute("SELECT * FROM medicine WHERE medicine_id='"+ med_id.get()+"'")
    med_records = cursor.fetchall()
    for med_record in med_records:
        med_id_updater.insert(0, med_record[0])
        med_name_updater.insert(0, med_record[1])
        med_cost_updater.insert(0, med_record[2])
        med_brand_updater.insert(0, med_record[3])
    med_id_updater.config(state=DISABLED)
	

    cursor.execute("SELECT * FROM batch WHERE batch_no='"+ batch_no.get()+"'")
    batch_records = cursor.fetchall()
    for batch_record in batch_records:
        batch_no_updater.insert(0, batch_record[0])
        batch_med_stock_updater.insert(0, batch_record[1])
        batch_mfg_updater.insert(0, batch_record[2])
        batch_expdate_updater.insert(0, batch_record[3])
    batch_no_updater.config(state=DISABLED)
    
    cursor.execute("SELECT * FROM organisation WHERE org_id='"+ org_id.get()+"'")
    org_records = cursor.fetchall()
    for org_record in org_records:
        org_id_updater.insert(0, org_record[0])
        org_name_updater.insert(0, org_record[1])
        org_type_updater.insert(0, org_record[2])
        org_contact_updater.insert(0, org_record[3])
    org_id_updater.config(state=DISABLED)

    cursor.execute("SELECT * FROM sale_details WHERE sale_id='"+ sale_id.get()+"'")
    sale_det_records = cursor.fetchall()
    for sale_det_record in sale_det_records:
        sale_date_updater.insert(0, sale_det_record[0])
        sale_id_updater.insert(0, sale_det_record[1])
        sale_user_id_updater.insert(0, sale_det_record[2])
        sale_org_id_updater.insert(0, sale_det_record[3])

    sale_id_updater.config(state=DISABLED)
    sale_date_updater.config(state=DISABLED)

    cursor.execute("SELECT * FROM user_info WHERE username='"+ username.get()+"'")
    user_records = cursor.fetchall()
    for user_record in user_records:
        username_updater.insert(0, user_record[0])
        user_phone_updater.insert(0, user_record[1])
        user_email_updater.insert(0, user_record[2])
        user_street_updater.insert(0, user_record[3])
        user_city_updater.insert(0, user_record[4])
        user_state_updater.insert(0, user_record[5])
        user_pincode_updater.insert(0, user_record[6])


    username_updater.config(state=DISABLED)

    updater.mainloop()

def update():
    update=Tk()
    update.geometry("600x300")
    global med_id, batch_no, sale_id, org_id, username
    med_id_label= Label(update,text='Enter med_id', font=('bold', 10))
    med_id_label.place(x=100, y=40)
    #med_id_label.pack()
    med_id= Entry(update,width=30)
    med_id.place(x=200, y=40)
    #med_id.pack()

    batch_no_label= Label( update,text='Enter batch_no', font=('bold', 10))
    batch_no_label.place(x=100, y=60)
    #batch_no_label.pack()
    batch_no= Entry(update,width=30)
    batch_no.place(x=200, y=60)
    #batch_no.pack()

    sale_id_label = Label (update, text='Enter sale_id', font=('bold',10))
    sale_id_label.place(x=100, y=80)
    #sale_id_label.pack()
    sale_id= Entry(update,width=30)
    sale_id.place(x=200, y=80)
    #sale_id.pack()

    org_id_label= Label(update,text='Enter org_id', font=('bold', 10))
    org_id_label.place(x=100, y=100)
    #org_id_label.pack()
    org_id= Entry(update,width=30)
    org_id.place(x=200, y=100)
    #org_id.pack()

    username_label= Label(update,text='Enter username', font=('bold', 10))
    username_label.place(x=100, y=120)
    #username_label.pack()
    username= Entry(update,width=30)
    username.place(x=200, y=120)
    #username.pack()
    update = Button(update, text="Update Data", command=updater)
    update.place(x=250, y=150)

def deli():
    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine")
    cursor = con.cursor()
    tabn=tab.get()
    colname=""
    var=delid1.get()
    if(tabn=="batch"):
        colname="batch_no"
    elif(tabn=="login"):
        colname="Login_id"
    elif(tabn=="medicine"):
        colname="medicine_id"
    elif(tabn=="organisation"):
        colname="org_id"
    elif(tabn=="role"):
        colname="Role_id"
    elif(tabn=="sale_details"):
        if(var[0]=='S'):
            colname="sale_id"
        elif(var[0]=='O'):
            colname="org_id"
        elif(var[0]=='^[0-9]'):
            colname="sale_date"
        else:
            colname="user_id"
    elif(tabn=="sales"):
        colname="sale_id"
    else:
        colname="username"
    cursor.execute("DELETE FROM `dbms_medicine`.`"+tabn+"` WHERE (`"+colname+"` = '"+var+"');")
    cursor.execute("commit")
    MessageBox.showinfo("Delete Status","Record deleted")
    con.close()
	

def delete():
	top = Toplevel()
	top.title("Delete")
	top.geometry("300x200")
	global delid1
	col=["batch","login","medicine","organisation","role","sale_details","sales","user_info"]
	global tab
	tab = StringVar()
	tab.set("batch")
	dropcol=OptionMenu(top,tab,*col)
	dropcol.pack()
	delb1=Label(top,text='Enter id :')
	delb1.pack()
	delid1=Entry(top)
	delid1.pack()
	delogin_label=Button(top, text="Delete", command= deli)
	delogin_label.pack()


def Sale():
    global top
    top = Toplevel()
    top.geometry('500x200')

    billstr="Enter type to retrieve data according to"
    blabel=Label( top,text=billstr)
    blabel.pack()
    col=["Sale id","Date","Organisation","Medicine Name","User"]
    global tab
    tab = StringVar()
    tab.set("Sale id")
    dropcol=OptionMenu(top,tab,*col)
    dropcol.pack()
    billsort="Sort by:"
    billsort_label=Label(top, text=billsort)
    billsort_label.pack()
    global tab1
    tab1= StringVar()
    tab1.set("Date")
    dropcol1=OptionMenu(top,tab1,*col)
    dropcol1.pack()

    top.title("Enter Sale Id")
    salelb=Label( top,text='Enter details for which you want details for')
    salelb.place(x=10,y=120)
    global saleid
    saleid= Entry(top)
    saleid.place(x=300, y=120)
    sale = Button(top, text="Get Sale details", command=submit_sale)
    sale.place(x=200, y=170)

def submit_sale():
    global sid
    sid = saleid.get()
    sort_id= tab1.get()
    print(sort_id)
    top.destroy()
    con = mysql.connect(host="localhost", user="root", password="LETSdoDBMS8", database="dbms_medicine")
    cursor = con.cursor()   
    if(tab.get()=="Sale id"):
        cursor.execute("select sale_date from sale_details where sale_id =\'"+sid+"\';") 
        sdate=cursor.fetchall()
        sd=str(sdate[0][0])

    if(tab.get()=="Sale id"):
        colname="sales.sale_id"
    elif(tab.get()=="Date"):
        colname="sale_details.sale_date"
    elif(tab.get()=="Organisation"):
        colname="sale_details.org_id"
    elif(tab.get()=="Medicine Name"):
        colname="medicine.medicine_name"
    else:
        colname="sale_details.user_id"

    if(tab1.get()=="Sale id"):
        colname1="sales.sale_id"
    elif(tab1.get()=="Date"):
        colname1="sale_details.sale_date"
    elif(tab1.get()=="Organisation"):
        colname1="sale_details.org_id"
    elif(tab1.get()=="Medicine Name"):
        colname1="medicine.medicine_name"
    else:
        colname1="sale_details.user_id"

    cursor.execute("select sale_details.sale_date,sales.medicine_id,medicine.medicine_name,sales.batch_id,sales.quantity,medicine.medicine_cost,(sales.quantity*medicine.medicine_cost) as \"Amount\" from sales join medicine on sales.medicine_id=medicine.medicine_id join sale_details on sales.sale_id=sale_details.sale_id join organisation  on sale_details.org_id=organisation.org_id where "+colname+"=\'"+sid+"\' order by "+colname1+" desc;")
    bill = cursor.fetchall()
    top2=Toplevel()
    if(tab.get()=="Sale id"):
        billstr="Bill id: "+sid+"\t\t\t Date:"+str(sd)
        blabel=Label( top2,text=billstr)
        blabel.pack()
    list=Listbox(top2,width=100)
    list.pack()
    list.insert(END,"sale date  medicine id   medicine name  batch id   quantity   medicine cost   amount")
    sum=0
    for row in bill:
        sum=sum+row[6]
        insert=str(row[0])+'                 '+str(row[1])+'             '+str(row[2])+'          '+str(row[3])+'            '+str(row[4])+'                        '+str(row[5])+'                    '+str(row[6])
        list.insert(END,insert)
    con.close()
    amount="Total Amount: "+str(sum)
    alabel=Label(top2,text=amount)
    alabel.pack()

def Med():
    global top
    top = Toplevel()
    top.geometry('500x200')

    billstr="Enter type to retrieve data according to"
    blabel=Label( top,text=billstr)
    blabel.pack()
    col=["Medicine Name","Batch id","Brand","Medicine Id"]
    global tab2
    tab2 = StringVar()
    tab2.set("Medicine Name")
    dropcol=OptionMenu(top,tab2,*col)
    dropcol.pack()

    top.title("Enter Med Id")
    medlb=Label( top,text='Enter Medicine details for which you want details for')
    medlb.place(x=10,y=70)
    global medn
    medn= Entry(top)
    medn.place(x=300, y=70)
    med = Button(top, text="Get Medicine details", command=Med_det)
    med.place(x=200, y=120)

def Med_det():
    mn = medn.get()
    top.destroy()
    con = mysql.connect(host="localhost", user="root", password="LETSdoDBMS8", database="dbms_medicine")
    cursor = con.cursor() 

    if(tab2.get()=="Medicine Name"):
        colname="medicine.medicine_name"
    elif(tab2.get()=="Batch id"):
        colname="batch.batch_no"
    elif(tab2.get()=="Brand"):
        colname="medicine.medicine_brand"
    elif(tab2.get()=="Medicine Id"):
        colname="medicine.medicine_id"
    else:
        colname=""

    cursor.execute("select medicine.medicine_id,batch.batch_no,medicine.medicine_name,medicine.medicine_brand,medicine.medicine_cost,batch.medicine_stock,batch.manufacture_date,batch.expiry_date from medicine inner join batch on medicine_id=batch.med_id where "+colname+"=\'"+mn+"\' order by expiry_date;")
    med_d = cursor.fetchall()
    top2=Toplevel()
    list=Listbox(top2,width=100)
    list.pack()
    list.insert(END,"Med id        batch id     name         brand         cost        stock          manufature date          expiry date")
    for row in med_d:
    	insert=str(row[0])+'            '+str(row[1])+'           '+str(row[2])+'     '+str(row[3])+'      '+str(row[4])+'          '+str(row[5])+'               '+str(row[6])+'                '+str(row[7])
    	list.insert(END,insert)
    con.close()

def show():
    show=Tk()
    show.geometry("300x300")
    sale = Button(show, text="Get Sale details", command=lambda : Sale())
    sale.place(x=100, y=75)

    medicine = Button(show,text="Get medicine Details",command=lambda : Med())
    medicine.place(x=85,y=125)

def manager():
    login.destroy()
    manager=Tk()
    manager.title("Hi Manager!")
    manager.geometry("600x300")

    id=Label(manager)

    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )
    global add, update, delete, show
    add = Button(manager, text="Add New Data", command=add)
    add.place(x=100, y=180)
    add.pack(padx=10,pady=10)

    update = Button(manager, text="Update Data", command=update)
    update.place(x=250, y=150)
    update.pack(padx=10,pady=10)

    delete = Button(manager, text="Delete Data", command=delete)
    delete.place(x=250, y=190)
    delete.pack(padx=10,pady=10)

    show= Button(manager, text="View Data", command=show)
    show.place(x=250, y=230)
    show.pack(padx=10,pady=10)

    Back1 = Button(manager,text="Signout",command=lambda:[manager.destroy(),mainpage()]).pack()

    print("in")
    cursor = con.cursor()
    con.close()
    manager.mainloop()

def employee():
    login.destroy()
    employee=Tk()
    employee.title("Hi Employee!")
    employee.geometry("600x300")

    id=Label(employee)

    con = mysql.connect(
    host="localhost",
    user="root",
    password="LETSdoDBMS8",
    database="dbms_medicine"
    )
    
    show1= Button(employee, text="View Data", command=show)
    show1.place(x=250, y=230)
    show1.pack(padx=10,pady=10)
    Back2 = Button(employee,text="Signout",command=lambda:[employee.destroy(),mainpage()]).pack()
    print("in")
    cursor = con.cursor()
    con.close()
    employee.mainloop()

def denied():
    MessageBox.showinfo("Login","Access Denied!")

def submit():
    print(username)
    if(username.get()=="" or password.get()==""):
        MessageBox.showinfo("Insert Status","All Field are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="LETSdoDBMS8", database="dbms_medicine")
        cursor = con.cursor()       
        cursor.execute("SELECT EXISTS(SELECT * from login WHERE Login_username='"+username.get()+"');") 
        result1=cursor.fetchall()
        #print(result1[0])
        if(result1[0][0]==0):
            denied()
        cursor.execute("select login_password,role_type from login inner join role on role_user_id=login_id where Login_username=\'"+username.get()+"\'")
        result = cursor.fetchall()
        global access
        access = StringVar()
        for row in result:
            if row[0]==password.get():
                if row[1]=='Manager':
                    manager()
                elif row[1]=='Employee':
                    employee()
            else:
                denied()
        
        con.close()

def login():
    global username, login, password, username_label, password_label
    flag = "pat_login"
    main.destroy()
    login = Tk()
    login.title("Login Page")
    login.geometry("700x500")
    username_label = Label(login,text="Enter your name below: ")
    password_label = Label(login,text="Enter your password below: ")
    username_label.pack()
    username = Entry(login)
    username.pack()
    password_label.pack()
    password = Entry(login,show="*")
    password.pack()
    Sign_in = Button(login,text="Sign in",command=submit).pack()
    Back = Button(login,text="back to Mainpage",command=lambda:[login.destroy(),mainpage()]).pack()
    login.mainloop()
def mainpage():
    global main
    main=Tk()
    main.title("Main Page")
    main.geometry("300x300")
    main_login_btn= Button(main, text="Login", command=login)
    main_login_btn.pack(padx=10,pady=10)
    main.mainloop()

mainpage()
import tkinter as tk
from tkinter import ttk
#from csv import DictWriter
#import os
import psycopg2

win = tk.Tk()
win.title('gui_1')

# create label

name_label = ttk.Label( win , text = 'enter your name :',foreground = 'Red', background = 'blue')
name_label.grid(row = 0, column = 0 , sticky = tk.W)

email_label = ttk.Label( win , text = 'enter your email :')
email_label.grid(row = 1, column = 0 , sticky = tk.W)

age_label = ttk.Label( win , text = 'enter your age :')
age_label.grid(row = 2, column = 0 , sticky = tk.W)

gender_label = ttk.Label( win , text = 'enter your gender :')
gender_label.grid(row = 3, column = 0 , sticky = tk.W)

# create entrybox

name_var = tk.StringVar()
name_entrybox = ttk.Entry( win , width = 16 , textvariable = name_var)
name_entrybox.grid(row =0 , column = 1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry( win , width = 16 , textvariable = email_var)
email_entrybox.grid(row =1 , column = 1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry( win , width = 16 , textvariable = age_var)
age_entrybox.grid(row =2 , column = 1)

# create combobox

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox( win, width = 14 , textvariable = gender_var , state = 'readonly' )
gender_combobox ['values'] = ('male' , 'female' ,'other')
gender_combobox.current(0)
gender_combobox.grid(row = 3,column =1)


# create radio button
usertype = tk.StringVar()
radiobtn_1 = ttk.Radiobutton( win , text = 'student' , value = 'student', variable = usertype)
radiobtn_1.grid(row = 4 ,column = 0)


radiobtn_2 = ttk.Radiobutton( win , text = 'taecher' , value = 'teacher', variable = usertype)
radiobtn_2.grid(row = 4 ,column = 1)


# create check button

checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton( win , text = 'check if u want to subscribed' , variable = checkbtn_var)
checkbtn.grid( row = 5 ,columnspan = 2 , sticky = tk.W)

DB_NAME="try1"
DB_USER="postgres"
DB_PASSWORD="password"
DB_PORT="5432"


conn=psycopg2.connect(database=DB_NAME,  user=DB_USER,  password=DB_PASSWORD,  port=DB_PORT)
my_cursor = conn.cursor()


# create button

def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    
   
    query_1 = "create table student(name char(20), email varchar(20), age char(20), gender char(20), type char(20) )"
    
    my_cursor.execute(query_1)

    query = "insert into student values(%s,%s,%s,%s,%s)"
    values = (user_name,user_email,user_age,user_gender,user_type)
    my_cursor.execute(query,values)

    conn.commit()
    

    name_entrybox.delete(0, tk.END)
    email_entrybox.delete(0 , tk.END)
    age_entrybox.delete(0 , tk.END)

    # to change or configure the color of label

    name_label.configure(foreground = 'black')


submit_button = ttk.Button( win , text = 'submit', command = action )
submit_button.grid( row = 6 , column = 1)


win.mainloop()
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
from tkinter import messagebox as m_box
win=tk.Tk()
#change heading
win.title('GUI app')
#create notebook
nb=ttk.Notebook(win)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text='one')
nb.add(page2,text='two')
nb.pack(expand=True, fill='both')

#create labels
name_label=ttk.Label(page1,text='Enter your name')
name_label.grid(row=0,column=0,sticky=tk.W)
age_label=ttk.Label(page1,text='Enter age')
age_label.grid(row=1,column=0,sticky=tk.W)
email_label=ttk.Label(page1,text='Enter your email')
email_label.grid(row=2,column=0,sticky=tk.W)
gender_label=ttk.Label(page2,text='gender')
gender_label.grid(row=3,column=0,sticky=tk.W)
#create entrybox
name_var=tk.StringVar()
name_entrybox=ttk.Entry(page1,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()
age_var=tk.StringVar()
age_entrybox=ttk.Entry(page1,width=16,textvariable=age_var)
age_entrybox.grid(row=1,column=1)
email_var=tk.StringVar()
email_entrybox=ttk.Entry(page1,width=16,textvariable=email_var)
email_entrybox.grid(row=2,column=1)
#create combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(page2,width=13,textvariable=gender_var)
gender_combobox['values']=('select','Male','Female','Others')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)
#create radio button
user_var=tk.StringVar()
user_type=ttk.Radiobutton(page2,text='Student',valu='Student',variable=user_var)
user_type.grid(row=4,column=0)
user_type1=ttk.Radiobutton(page2,text='Teacher',value='Teacher',variable=user_var)
user_type1.grid(row=4,column=1)
#create check button
check_var=tk.StringVar()
checkbtn=ttk.Checkbutton(page2,text='I agree for all T&C of the union',variable=check_var)
checkbtn.grid(row=5,columnspan=5)
#create menubar
def func():
    pass
main_menu=tk.Menu(win)

file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New File',command=func)
file_menu.add_command(label='New Window',command=func)
file_menu.add_separator()
file_menu.add_command(label='Open File',command=func)
file_menu.add_command(label='Open Folder',command=func)

edit_menu=tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Undo',command=func)
edit_menu.add_command(label='Redo',command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Cut',command=func)
edit_menu.add_command(label='Copy',command=func)
edit_menu.add_command(label='Paste',command=func)

main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
win.configure(menu=main_menu)
# #create button
def submit():
    name=name_var.get()
    age=age_var.get()
    email=email_var.get()
    gender=gender_var.get()
    user_type=user_var.get()
    if check_var.get()==0:
        subscribed='No'
    else:
        subscribed='Yes'
    name_entrybox.focus()
    
    
    if name=='' or age=='':
        m_box.showerror('Error','Some inputs must be given')
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showerror('Error','age must be integer')
        else:
            if age<18:
                m_box.showwarning('warning','You are below 18')
            print(f'{name}, {age}, {email}, {gender}, {user_type}, {subscribed}\n')
            m_box.showinfo('application','Successful\t\t\t\t')
    with open('file.txt','a') as wf:
        wf.write(f'{name}, {age}, {email}, {gender}, {user_type}, {subscribed}\n')
    with open('file.csv','a',newline='') as f:
        dict_writer=DictWriter(f,fieldnames=['name','age','email','gender','type','subscribed'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'name':name,
            'age':age,
            'email':email,
            'gender':gender,
            'type':user_type,
            'subscribed':subscribed
        })
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    gender_combobox.delete(0,tk.END)
submit=ttk.Button(page2,text='Submit',command=submit)
submit.grid(row=6,column=0)
win.mainloop()

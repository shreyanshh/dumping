#taking user inpuut and write in csv file using tkinter gui

import tkinter as tk
import os, sys
from csv import DictWriter
from tkinter import ttk
win= tk.Tk()
win.title('GUI')

# leveling
name_lable=ttk.Label(win,text  = 'custmer name : ')
name_lable.grid(row = 0, column = 0, sticky = tk.W)

mob_lable= ttk.Label(win,text = 'your mobile no. : ')
mob_lable.grid(row=1,column = 0, sticky = tk.W)

gender_lable= ttk.Label(win,text = 'select your gender : ')
gender_lable.grid(row=2,column = 0, sticky = tk.W)


# entrybox
name_var=tk.StringVar()
name_box = ttk.Entry(win,width= 15, textvariable= name_var)
name_box.grid(row= 0, column = 2)
name_box.focus()

mob_var=tk.StringVar()
mob_box = ttk.Entry(win, width = 15, textvariable= mob_var)
mob_box.grid(row= 1, column = 2)

# combobox
gender_var= tk.StringVar()
gender_combo = ttk.Combobox(win, width = 12, values = ['male','female','other'], textvariable = gender_var, state= 'readonly')
gender_combo.grid(row = 2,column= 2)
'''gender_combobox current state set to values[0] position
txtvariable is used for text entry type box otherwise only variable is used like in radio and check btn'''
gender_combo.current(0)


# check_btn
'''defining variable type is intiger'''
subscribe_var= tk.IntVar()
check_btn = ttk.Checkbutton(win, text= 'check if you have subscribed our team', variable= subscribe_var)
check_btn.grid(row = 3, columnspan= 3, sticky= tk.W)

# radio_btn
radio_var =tk.StringVar()
radio_btn= ttk.Radiobutton(win, text='student', value= 'student', variable= radio_var)
radio_btn.grid(row= 4,column= 2)

radio_btn2= ttk.Radiobutton(win, text='professor', value= 'professor', variable= radio_var)
radio_btn2.grid(row= 4,column= 3)

# submit btn
def action():
    user_name=name_var.get()
    user_mob =mob_var.get()
    user_gender=gender_var.get()
    user_type=radio_var.get()
    user_subscription=''
    if subscribe_var.get()== 1:
        user_subscription= 'yes'
    else:
        user_subscription='no'
    
    with open('file.csv','a',newline='')as f:
        dicwriter= DictWriter(f,fieldnames=['name','mob','gender','type','subscription'])
        dicwriter.writeheader()
        dicwriter.writerows({
            'name': user_name,
            'mob':user_mob,
            'gender': user_gender,
            'type':user_type,
            'subscription': user_subscription
        })

    name_box.delete(0,tk.END)
    mob_box.delete(0,tk.END)
    name_lable.configure(foreground= 'Blue')
    name_box.configure(background = 'Red')

    
    # with open('file1', 'a')as f:
    #     f.write(user_name+ '\n'+user_mob+'\n'+user_gender+'\n'+user_type+'\n'+user_subscription+'\n' )

    # print(f'name is {name_var.get()}, mob number is {mob_var.get()}, gender is {gender_var.get()}, person profession is {radio_var.get()}, person subscribe {subscribe_var.get()}')


def action2():
    sys.exit()

# use tk.button(win,text='submit',command=action  for using configure option for submit btn)
submitbtn= ttk.Button(win, text='submit1', command= action)
submitbtn.grid(row= 5, column=1)

cancel_btn = ttk.Button(win,text='cancel',command= action2)
cancel_btn.grid(row= 5, column = 2)

win.mainloop()

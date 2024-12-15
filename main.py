from tkinter import *
root=Tk()
root.title('Login app')
root.geometry('400x400')

frame=Frame(root,height=200,width=360,bg='#d0efff')
lb1=Label(frame,text='Full Name',bg='#3895d3',fg='white',width=12)
lb2=Label(frame,text='Email Id',bg='#3895d3',fg='white',width=12)
lb3=Label(frame,text='Enter Password',bg='#3895d3',fg='white',width=12)

name_entry=Entry(frame)
email_entry=Entry(frame)
password_entry=Entry(frame, show='*')
pass_entry=Button(root,text='Submit')

def display():
    name=name_entry.get()
    greet='Hey '+name
    message='\nCongratulations for your new account!'
    textbox.insert(END,greet)
    textbox.insert(END,message)

textbox=Text(bg='#BEBEBE',fg='black')
btn=Button(text='Create Account',command=display,bg='red')
frame.place(x=20,y=0)
lb1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lb2.place(x=20,y=80)
email_entry.place(x=150,y=80)
lb3.place(x=20,y=140)
password_entry.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)
root.mainloop()
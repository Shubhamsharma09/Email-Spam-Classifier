from Classifier import *
from tkinter import *
import tkinter.messagebox
def show():
    a=Mail.get()
    lis=[]
    print(a)
    if(a!=''):
        lis.append(a)
        b=checkingmail(lis)
        print(lis,b)
        a=b[0]
        if(a=='ham'):
            tkinter.messagebox.showinfo('ham',"The message is not spam")
            Mail.delete(0,END)
            lis.clear()
        else:
            tkinter.messagebox.showerror('spam','It is a spam')  
            Mail.delete(0,END)  
            lis.clear()
        

root=Tk()
root.title('Email-Classifier')
logo=PhotoImage(file='F:/project/logo.png')
lab=Label(root,image=logo,compound=CENTER).place(x=0,y=0)
Mail= Entry(root, bd=0, bg="lightblue",width="29",  font="Arial", fg='red')
Mail.place(x=0,y=250)
a=Mail.get()
print(a)
lab1=Label(root , text="Enter String" , fg="orange",font=7)
Check=Button(root, font=30, text="Check",fg='red', bg='orange',command =show)
                     
Check.place(x=0,y=275)                    
lab1.place(x=0,y=220)

root.geometry('280x310')
root.resizable(width=False,height=False)

root.mainloop()
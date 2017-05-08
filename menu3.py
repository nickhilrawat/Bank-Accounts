from tkinter import Tk,Button,Label
root=Tk()
b1=Button(root,text="1.Sign up(new customer)")
b2=Button(root,text="2.sign In (existing customer)")
b3=Button(root,text="3.Admin Sign In")
b4=Button(root,text="4.Quit")
l=Label(root,text="Main Menu")
l.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
def try_login():

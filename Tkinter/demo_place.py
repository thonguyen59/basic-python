from tkinter import *

form = Tk()
form.geometry("300x150")

lbLogin = Label(master=form, text='LOGIN')
lbLogin.place(x=20, y=10)

lbUser = Label(master=form, text='User')
lbUser.place(x=20, y=30)

etUser = Entry(master=form)
etUser.place(x=20, y=50)

btClick = Button(master=form, text='Click')
btClick.place(x=20, y=80)
form.mainloop()



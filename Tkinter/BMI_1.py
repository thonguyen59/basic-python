from tkinter import *


def btn_click(event):
    heightTemp = float(height.get()) / 100
    bmi = float(weight.get()) / (heightTemp * heightTemp)
    print(bmi)

    kq.config(text=f'Kết quả {bmi}')

root = Tk()
root.geometry('250x100')

heightLabel = Label(master=root, text="Chiều cao")
heightLabel.grid(row=0, column=0)

weightLabel = Label(master=root, text="Cân nặng")
weightLabel.grid(row=1, column=0)

height = Entry(master=root)
height.grid(row=0, column=1)

weight = Entry(master=root)
weight.grid(row=1, column=1)

button = Button(root, text="Click me")
button.grid(row=2, column=1)
button.bind("<Button-1>", btn_click)

kq = Label(master=root)
kq.grid(row=3, column=1)

root.mainloop()

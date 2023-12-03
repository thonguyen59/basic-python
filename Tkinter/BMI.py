from tkinter import *


class BMI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('250x100')
        # Label
        self.heightLabel = Label(master=self, text='Chiều cao')
        self.heightLabel.grid(row=0, column=0)
        self.weightLabel = Label(master=self, text='Cân nặng')
        self.weightLabel.grid(row=1, column=0)

        # Input text
        self.height = Entry(master=self)
        self.height.grid(row=0, column=1)
        self.weight = Entry(master=self)
        self.weight.grid(row=1, column=1)

        # Button
        button = Button(self, text="Nhập")
        button.grid(row=2, column=1)
        button.bind("<Button-1>", lambda event: self.calculate())

        # Result
        self.result = Label(master=self)
        self.result.grid(row=3, column=1)

    def calculate(self):
        heightTemp = float(self.height.get()) / 100
        bmi = round(float(self.weight.get()) / (heightTemp * heightTemp), 2)
        self.result.config(text=f'Kết quả {bmi}')

    def show(self):
        self.mainloop()


if __name__ == '__main__':
    f = BMI()
    f.show()
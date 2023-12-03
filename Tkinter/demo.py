import tkinter as tk
import tkinter.ttk as ttk


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(background="#c0c0c0", height=100, width=250)
        label1 = ttk.Label(toplevel1)
        label1.configure(compound="top", text='Chiều cao')
        label1.grid(column=0, row=2)
        label2 = ttk.Label(toplevel1)
        label2.configure(text='Cân nặng')
        label2.grid(column=0, row=1)
        self.height = ttk.Entry(toplevel1)
        self.height.grid(column=1, row=1)
        self.weight = ttk.Entry(toplevel1)
        self.weight.grid(column=1, row=2)
        self.result = tk.Message(toplevel1)
        self.result.configure(background="#c0c0c0", text='Kết quả')
        self.result.grid(column=1, row=4)
        message2 = tk.Message(toplevel1)
        message2.configure(background="#c0c0c0", text='TÍNH BMI', width=100)
        message2.grid(column=0, columnspan=2, row=0)
        self.submitBtn = tk.Button(toplevel1)
        self.submitBtn.configure(
            default="normal",
            justify="left",
            takefocus=False,
            text='Nhập',
            width=10)
        self.submitBtn.grid(column=1, row=3)
        self.submitBtn.configure(command=self.onSubmit)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def onSubmit(self):
        pass


if __name__ == "__main__":
    app = NewprojectApp()
    app.run()


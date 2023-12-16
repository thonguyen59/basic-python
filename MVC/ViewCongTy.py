import tkinter as tk
from tkinter import ttk

class ViewCongTy(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý công ty")
        self.geometry("350x150")

        self.buttons = {
            "Nhập": tk.Button(self, text="Nhập"),
            "Tính Lương": tk.Button(self, text="Tính lương"),
            "Cập Nhật": tk.Button(self, text="Cập nhật")
        }

        self.buttons["Nhập"].grid(row=1, column=0)
        self.buttons["Tính Lương"].grid(row=2, column=0)
        self.buttons["Cập Nhật"].grid(row=3, column=0)

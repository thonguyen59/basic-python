import tkinter as tk
import tkinter.ttk as ttk
from Model import CongTy, VanPhong, BanHang, NhanVienQL, NhanVien


class GUI(tk.Tk):
    def __init__(self, cty: CongTy):
        super().__init__()
        self.geometry("800x600")
        self.cty = cty

        # build ui
        frame = ttk.Frame(self)
        frame.configure(height=600, width=800)
        header_label = ttk.Label(frame)
        header_label.configure(text='Quản Lý Nhân Viên')
        header_label.place(anchor="nw", relx=0.45, x=0, y=0)
        ma_nv_label = ttk.Label(frame)
        ma_nv_label.configure(text='Mã NV')
        ma_nv_label.place(anchor="nw", relx=0.05, rely=0.1, x=0, y=0)
        ho_ten_label = ttk.Label(frame)
        ho_ten_label.configure(text='Họ Tên')
        ho_ten_label.place(anchor="nw", relx=0.05, rely=0.15, x=0, y=0)
        loai_nv_label = ttk.Label(frame)
        loai_nv_label.configure(text='Loại NV')
        loai_nv_label.place(anchor="nw", relx=0.45, rely=0.15, x=0, y=0)

        self.loai_nv_cbb = ttk.Combobox(frame)
        self.loai_nv_cbb.place(
            anchor="nw",
            relwidth=0.24,
            relx=0.52,
            rely=0.15,
            x=0,
            y=0)
        self.loai_nv_cbb['values'] = [row[0] for row in self.cty.load_loaiNV()]

        self.ho_ten_entry = ttk.Entry(frame)
        self.ho_ten_entry.place(
            anchor="nw",
            relwidth=0.24,
            relx=0.12,
            rely=0.15,
            x=0,
            y=0)

        self.ma_nv_entry = ttk.Entry(frame)
        self.ma_nv_entry.place(
            anchor="nw",
            relwidth=0.24,
            relx=0.12,
            rely=0.1,
            x=0,
            y=0)
        luong_cb_label = ttk.Label(frame)
        luong_cb_label.configure(text='Lương CB')
        luong_cb_label.place(anchor="nw", relx=0.45, rely=0.1, x=0, y=0)

        self.luong_cb_entry = ttk.Entry(frame)
        self.luong_cb_entry.place(
            anchor="nw",
            relwidth=0.24,
            relx=0.52,
            rely=0.1,
            x=0,
            y=0)
        self.them_btn = ttk.Button(frame, text='Thêm nhân viên', command=self.them_nv)
        self.them_btn.place(anchor="nw", relx=0.45, rely=0.3, x=0, y=0)

        self.tinh_luong_btn = ttk.Button(frame, text='Tính lương', command=self.tinh_luong)
        self.tinh_luong_btn.place(anchor="nw", relx=0.3, rely=0.3, x=0, y=0)

        self.load_btn = ttk.Button(frame, text='Load', command=self.load)
        self.load_btn.place(anchor="nw", relx=0.15, rely=0.3, x=0, y=0)

        self.treeview = ttk.Treeview(frame)
        self.treeview.configure(selectmode="extended")

        self.treeview["columns"] = ("c1", "c2", "c3", "c4", "c5")

        self.treeview["show"] = "headings"
        self.treeview.column("c1", width=50)
        self.treeview.column("c2", width=60)
        self.treeview.column("c3", width=100)
        self.treeview.column("c4", width=100)
        self.treeview.column("c5", width=160)
        self.treeview.heading("c1", text="STT")
        self.treeview.heading("c2", text="Mã NV")
        self.treeview.heading("c3", text="Họ tên")
        self.treeview.heading("c4", text="Lương CB")
        self.treeview.heading("c5", text="Lương HT")

        self.treeview.place(
            anchor="nw",
            relwidth=1.0,
            relx=0.0,
            rely=0.4,
            x=0,
            y=0)
        frame.place(anchor="nw", x=0, y=0)

        self.message = tk.Message(frame)
        self.message.place(
            anchor="nw",
            relwidth=0.16,
            relx=0.8,
            rely=0.1,
            x=0,
            y=0)
        frame.place(anchor="nw", x=0, y=0)

        # Main widget
        self.main_window = frame

    def load(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for i, nv in enumerate(self.cty.dsNV, start=1):
            self.treeview.insert('', 'end', values=nv.row(i))

    def them_nv(self):
        try:
            maNV = self.ma_nv_entry.get()
            hoTen = self.ho_ten_entry.get()
            luongCB = self.luong_cb_entry.get()
            loaiNV = self.loai_nv_cbb.get()

            if not maNV or not hoTen or not luongCB or not loaiNV:
                raise ValueError("All fields must be filled.")

            try:
                luongCB = float(luongCB)
            except ValueError:
                raise ValueError("luongCB must be a number.")

            if self.cty.tim_nv_by_maNV(maNV) is not None:
                raise ValueError(f"A NhanVien with maNV {maNV} already exists.")

            nv = NhanVien(maNV=maNV, hoTen=hoTen, luonngCB=luongCB, loaiNV=loaiNV)
            print(nv)

            self.cty.them_nv(nv)
            self.load()
            self.ma_nv_entry.delete(0, 'end')
            self.ho_ten_entry.delete(0, 'end')
            self.luong_cb_entry.delete(0, 'end')
            self.loai_nv_cbb.set('')

        except Exception as e:
            self.message.config(text=str(e))

    def tinh_luong(self):
        try:
            self.cty.tinh_luong_hang_thang()
            self.load()
        except Exception as e:
            self.message.config(text=str(e))

    def run(self):
        self.main_window.mainloop()

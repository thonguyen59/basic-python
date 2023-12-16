class ControllerCongTy:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.buttons["Nhập"].config(command=self.load_nhan_vien, text="Nhập lại")
        self.view.buttons["Tính Lương"].config(command=self.tinh_luong_nv)
        self.view.buttons["Cập Nhật"].config(command=self.cap_nhat_nv)

    def load_nhan_vien(self):
        print("Click load")
        self.model.load_data()

    def tinh_luong_nv(self):
        print("click tinh luong")

    def cap_nhat_nv(self):
        print("click Cap nhat")

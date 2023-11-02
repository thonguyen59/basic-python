class NhanVien:
    def __init__(self, maNV, **kwargs):
        self.maNV = maNV
        self.hoTen = kwargs.get("hoTen")
        self.luongCB = kwargs.get("luongCB")

    def inThongTin(self, ):
        print("Thông tin nhân viên: ")
        print("\t+ Mã nhân viên: ", self.maNV)
        print("\t+ Tên nhân viên: ", self.hoTen)
        print("\t+ Lương căn bản: ", self.luongCB)


nv = NhanVien("123", hoTen = "Nghĩa thúi", luongCB = 100_000_000)

NhanVien.inThongTin(nv)
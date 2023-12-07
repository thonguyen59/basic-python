import tkinter as tk
from tkinter import ttk
from tkinter import *
from abc import ABC, abstractmethod
from ODBC import ODBC


class CongTy:
    soNV = 0

    def __init__(self, ma: int, **kwargs):
        self.__maCongTy = kwargs.get('maCongTy', '')
        self.__tenCongTy = kwargs.get('tenCongTy', '')
        self.__dsNV = []

        CongTy.soNV += 1

    def tim_nhan_vien(self, maNV: int):
        return [nv for nv in self.dsNV if nv.maNhanVien == maNV]

    def tim_NV_BH_luong_thap_nhat(self):
        nv_bh = [nv for nv in self.__dsNV if isinstance(nv, NVBanHang)]
        return min(nv_bh, key=lambda nv: nv.luongThang)

    def nv_co_luong_cao_nhat(self):
        if not self.__dsNV:
            return None

        return max(self.__dsNV, key=lambda nv: nv._luongThang)

    def tinh_luong_thang_NV(self):
        for nv in self.__dsNV:
            nv.tinh_luong()

    def them_nhan_vien(self, ds_nv):
        self.__dsNV.extend(ds_nv)

    def xuat_tat_ca_nhan_vien(self):
        for nv in self.__dsNV:
            print(nv)

    def hien_thi(self):
        window = tk.Tk()

        tree = ttk.Treeview(window)

        tree["columns"] = ("c1", "c2", "c3")

        tree.heading("c1", text="Cột 1")
        tree.heading("c2", text="Cột 2")
        tree.heading("c3", text="Cột 3")

        for nv in self.__dsNV:
            tree.insert("", tk.END, text="Dòng 1", values=nv.__str__())

        tree.pack()

        window.mainloop()

    def luu_luong_hang_thang(self):
        db = ODBC(driver='SQL Server', server='GROOO0030', database='qlnv', username='', password='')
        db.connect()

        query = """
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'LuongThangNV')
        BEGIN
            CREATE TABLE LuongThangNV (
                MaNhanVien VARCHAR(255) PRIMARY KEY,
                luongThang DECIMAL(10, 2),
                FOREIGN KEY (MaNhanVien) REFERENCES NhanVien(MaNhanVien)
            );
        END
        """
        db.execute_query(query)

        for nv in self.__dsNV:
            luongThang = nv._luongThang

            query = f"""IF EXISTS (SELECT 1 FROM LuongThangNV WHERE MaNhanVien = '{nv._maNhanVien}')
                        BEGIN
                            UPDATE LuongThangNV SET luongThang = {luongThang} WHERE MaNhanVien = '{nv._maNhanVien}';
                        END
                        ELSE
                        BEGIN
                            INSERT INTO LuongThangNV (MaNhanVien, luongThang) VALUES ('{nv._maNhanVien}', {luongThang});
                        END"""
            db.execute_query(query)

        db.conn.commit()

    def loadDatabase(self):
        db = ODBC(driver='SQL Server', server='GROOO0030', database='qlnv', username='', password='')
        db.connect()

        query = """SELECT * FROM NhanVien;"""
        db.execute_query(query)
        nhan_vien_records = db.fetch_all()

        # Truy vấn dữ liệu từ bảng ChamCongTongHop
        query = """SELECT * FROM ChamCongTongHop;"""
        db.execute_query(query)
        cham_cong_records = db.fetch_all()

        # Tạo đối tượng BanHang hoặc VanPhong hoặc NhanVienQL cho mỗi bản ghi và thêm vào danh sách
        for nhan_vien_record in nhan_vien_records:

            for cham_cong_record in cham_cong_records:

                if nhan_vien_record[0] == cham_cong_record[0]:  # So sánh MaNhanVien

                    if cham_cong_record[1] == 'Bán Hàng':
                        nv = NVBanHang(maNhanVien=nhan_vien_record[0], hoTen=nhan_vien_record[1], luonngCB=float(nhan_vien_record[2]),
                                     SoNG=cham_cong_record[2], soSP=cham_cong_record[3])

                    else:
                        nv = NVVanPhong(maNhanVien=nhan_vien_record[0], hoTen=nhan_vien_record[1], luonngCB=float(nhan_vien_record[2]),
                                      soNG=cham_cong_record[2])

                    self.__dsNV.append(nv)

class NhanVienTruuTuong(ABC):
    @abstractmethod
    def xuat(self):
        pass

    @abstractmethod
    def tinh_luong(self):
        pass


class NhanVien(NhanVienTruuTuong):
    def __init__(self, maNhanVien: int, **kwargs):
        self._maNhanVien = maNhanVien
        self._hoTen = kwargs.get('hoTen', '')
        self._luongCB = kwargs.get('luongCB', 0)
        self._luongThang = kwargs.get('luongThang', 0)
        self.__name = kwargs.get('name', '')

    @property
    def name(self):
        return self.__name

    def print(self):
        print(self.name)

    @name.setter
    def name(self, name):
        self.__name = name

    def xuat(self):
        print("Mã nhân viên: ", self._maNhanVien)
        print("Họ và tên: ", self._hoTen)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self._luongCB))

    def __str__(self):
        return str([self.maNhanVien, self.hoTen, self.luongCB, self.luongThang])


class NVBanHang(NhanVien):
    def __init__(self, maNhanVien: int, **kwargs):
        super().__init__(maNhanVien, **kwargs)
        self.__soSP = kwargs.get('soSP', 0)

    def tinh_luong(self):
        self.luongThang = self._luongCB + (self.__soSP * 18_000)

    def xuat(self):
        super().xuat()
        print("Số sản phẩm bán được: ", self.__soSP)
        print("Lương tháng: {:,.0f} VNĐ".format(self.luongThang))

    def __str__(self):
        return str([self._maNhanVien, self._hoTen, self._luongCB, self.__soSP, self._luongThang])


class NVVanPhong(NhanVien):

    def __init__(self, maNhanVien: int, **kwargs):
        super().__init__(maNhanVien, **kwargs)
        self.__soNgayLam = kwargs.get('soNgayLam', 0)

    def tinh_luong(self):
        self.luongThang = self._luongCB + (self.__soNgayLam * 150_000)

    def xuat(self):
        super().xuat()
        print("Số ngày làm việc: ", self.__soNgayLam)
        print("Lương tháng: {:,.0f} VNĐ".format(self.luongThang))

    def __str__(self):
        return str([self._maNhanVien, self._hoTen, self._luongCB, self.__soNgayLam, self._luongThang])


if __name__ == '__main__':
    congTy = CongTy(ma='CT1', ten='Cong Ty 1')
    congTy.loadDatabase()
    congTy.tinh_luong_thang_NV()
    congTy.xuat_tat_ca_nhan_vien()
    congTy.luu_luong_hang_thang()
    congTy.hien_thi()

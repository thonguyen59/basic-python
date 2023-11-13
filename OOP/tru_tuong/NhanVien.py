import random
from abc import ABC, abstractmethod


class CongTy:
    def __init__(self, **kwargs):
        self.__maCongTy = kwargs.get('maCongTy', '')
        self.__tenCongTy = kwargs.get('tenCongTy', '')
        self.__dsNV = []

    def them_nhan_vien(self, ds_nv):
        self.__dsNV.extend(ds_nv)

    def tinh_luong_thang_NV(self):
        for nv in self.__dsNV:
            nv.tinh_luong()

    def xuat_tat_ca_nhan_vien(self):
        print("Danh sách nhân viên:")
        for nv in self.__dsNV:
            nv.xuat()
            print("----------")

    def tim_NV_luong_cao_nhat(self):
        return max(self.__dsNV, key=lambda nv: nv.luongThang)

    def tim_NV_BH_luong_thap_nhat(self):
        nv_bh = [nv for nv in self.__dsNV if isinstance(nv, nvBanHang)]
        return min(nv_bh, key=lambda nv: nv.luongThang)

    def print(self):
        for nv in self.dsNV:
            print(nv)

    def tim_nv(self, maNV: int):
        for nv in self.__dsNV:
            if maNV == nv._maNhanVien:
                return nv

    def print_nv_bh(self):
        for nv in self.dsNV:
            if isinstance(nv, nvBanHang):
                print(nv)

    def print_nv_vp(self):
        for nv in self.dsNV:
            if isinstance(nv, nvVanPhong):
                print(nv)

    def __str__(self):
        return str([self.maNhanVien, self.hoTen, self.luongCB, self.luongThang])


class NhanVienTruuTuong(ABC):
    @abstractmethod
    def xuat(self):
        pass

    @abstractmethod
    def tinhLuong(self):
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


class nvVanPhong(NhanVien):

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


class nvBanHang(NhanVien):

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
        return str([self.maNhanVien, self.hoTen, self.luongCB, self.soSP, self.luongThang])


# Bắt đầu tạo data
dsNhanVien = [nvVanPhong(i, hoTen=f'Van Phong {i}', luongCB=random.randint(10_000_000, 45_000_000),
                         soNgayLam=random.randint(20, 30)) for i in range(1, 6)]

dsNhanVien.append(nvVanPhong(59, hoTen='Nguyễn Trường Thọ', luongCB=random.randint(10_000_000, 45_000_000),
                             soNgayLam=random.randint(20, 30)))

dsNhanVien.extend([nvBanHang(i, hoTen=f'Ban Hang {i+100}', luongCB=random.randint(7_500_000, 25_000_000),
                             soSP=random.randint(100, 500)) for i in range(1, 6)])
# Kết thúc tạo data


if __name__ == '__main__':
    cty = CongTy(maCongTy='CT1', tenCongTy='Cong Ty 1')
    cty.them_nhan_vien(dsNhanVien)

    cty.tinh_luong_thang_NV()
    cty.xuat_tat_ca_nhan_vien()

    nv_luong_cao_nhat = cty.tim_NV_luong_cao_nhat()
    if nv_luong_cao_nhat is not None:
        print('Nhân viên có lương cao nhất:', nv_luong_cao_nhat._hoTen)
    else:
        print('Không có nhân viên')

    nv_bh_co_luong_thap_nhat = cty.tim_NV_BH_luong_thap_nhat()
    if nv_bh_co_luong_thap_nhat is not None:
        print('Nhân viên kinh doanh có lương thấp nhất:', nv_bh_co_luong_thap_nhat._hoTen)
    else:
        print('Không có nhân viên bán hàng')

    print('Tên nhân viên có mã 59:', cty.tim_nv(59))



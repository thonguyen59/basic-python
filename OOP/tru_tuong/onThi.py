from abc import ABC, abstractmethod

class NhanVienAbstract(ABC):
    @abstractmethod
    def tinhLuongHT(self):
        pass


class NhanVien(NhanVienAbstract):
    def __init__(self, maNV: int, **kwargs):
        self._maNV = maNV
        self._hoTen = kwargs.get('hoTen', '')
        self._luongCB = kwargs.get('luongCB', 0)
        self._luongHT = kwargs.get('luongHT', 0)

    def __str__(self):
        return str([self._maNV, self._hoTen, self._luongCB, self._luongHT])


class NVVanPhong(NhanVien):
    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__soGioLam = kwargs.get('soGioLam', 0)

    def tinhLuongHT(self):
        self._luongHT = self._luongCB + (self.__soGioLam * 220_000)
        if self.__soGioLam > 100:
            self._luongHT = self._luongHT + 5_000_000

    def xuat(self):
        print(super().__str__())


class NVSanXuat(NhanVien):
    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__soSanPham = kwargs.get('soSanPham')

    def tinhLuongHT(self):
        self._luongHT = self._luongCB + (self.__soSanPham * 170_000)
        if self.__soSanPham > 150:
            self._luongHT = self._luongHT * 1.2


class NVQuanLy(NhanVien):
    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__heSoChucVu = kwargs.get('heSoChucVu')
        self.__thuong = kwargs.get('thuong')

    def tinhLuongHT(self):
        self._luongHT = self._luongCB * self.__heSoChucVu + self.__thuong


class DaiLy:
    def __init__(self, maDL: int):
        self.__maDL = maDL
        self.__dsNhanVien = []

    def loadNV(self):
        '''Cau 1'''
        vp1 = NVVanPhong(100, hoTen='Nguyen A', luongCB=4_500_00, soGioLam=200)
        vp2 = NVVanPhong(101, hoTen='Nguyen B', luongCB=5_600_00, soGioLam=100)
        # vp2 = NVVanPhong(103, hoTen = 'Nguyen C', luongCB = 8_900_00, soGioLam = 90)

        self.__dsNhanVien.extend([vp1, vp2])

    def xuat(self):
        print(len(self.__dsNhanVien))
        for item in self.__dsNhanVien:
            item.xuat()


if __name__ == '__main__':
    dl = DaiLy('madL')
    dl.loadNV()
    dl.xuat()



import random


class CongTy:
    def __init__(self, **kwargs):
        self.maCongTy = kwargs.get('maCongTy', '')
        self.tenCongTy = kwargs.get('tenCongTy', '')
        self.dsNV = []

    def them_nhan_vien(self, ds_nv):
        self.dsNV.extend(ds_nv)

    def tinh_luong_thang_NV(self):
        for nv in self.dsNV:
            nv.tinh_luong()

    def xuat_tat_ca_nhan_vien(self):
        print("Danh sách nhân viên:")
        for nv in self.dsNV:
            nv.xuat()
            print("----------")

    def tim_nhan_vien(self, maNhanVien):
        return [nv for nv in self.dsNV if nv.maNhanVien == maNhanVien]

    def tim_NV_luong_cao_nhat(self):
        return max(self.dsNV, key=lambda nv: nv.luongThang)

    def tim_NV_BH_luong_thap_nhat(self):
        nv_bh = [nv for nv in self.dsNV if isinstance(nv, nvBanHang)]
        return min(nv_bh, key=lambda nv: nv.luongThang)

    def print(self):
        for nv in self.dsNV:
            print(nv)

    def tim_nv(self, maNV: int):
        for nv in self.dsNV:
            if maNV == nv.maNhanVien:
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
        return str([self.maNhanVien, self.hoTen, self.luonngCB, self.luongThang])


class nvVanPhong:
    soNV = 0

    def __init__(self, maNhanVien: int, **kwargs):
        self.maNhanVien = maNhanVien
        self.hoTen = kwargs.get('hoTen', '')
        self.luonngCB = kwargs.get('luonngCB', 0)
        self.soNgayLam = kwargs.get('soNgayLam', 0)
        self.luongThang = kwargs.get('luongThang', 0)
        nvVanPhong.soNV = nvVanPhong.soNV + 1;

    def tinh_luong(self):
        self.luongThang = self.luonngCB + (self.soNgayLam * 150_000)

    def xuat(self):
        print("Mã nhân viên Văn Phòng: ", self.maNhanVien)
        print("Họ và tên: ", self.hoTen)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self.luonngCB))
        print("Số ngày làm việc: ", self.soNgayLam)
        print("Lương tháng: {:,.0f} VNĐ".format(self.luongThang))

    def __str__(self):
        return str([self.maNhanVien, self.hoTen, self.luonngCB, self.luongThang])


class nvBanHang:
    soNV = 0

    def __init__(self, maNhanVien: int, **kwargs):
        self.maNhanVien = maNhanVien
        self.hoTen = kwargs.get('hoTen', '')
        self.luonngCB = kwargs.get('luonngCB', 0)
        self.soSP = kwargs.get('soSP', 0)
        self.luongThang = kwargs.get('luongThang', 0)
        nvBanHang.soNV = nvBanHang.soNV + 1;

    def tinh_luong(self):
        self.luongThang = self.luonngCB + (self.soSP * 18_000)

    def xuat(self):
        print("Mã nhân viên Bán Hàng: ", self.maNhanVien)
        print("Họ và tên nhân viên: ", self.hoTen)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self.luonngCB))
        print("Số sản phẩm bán được: ", self.soSP)
        print("Lương tháng: {:,.0f} VNĐ".format(self.luongThang))

    def __str__(self):
        return str([self.maNhanVien, self.hoTen, self.luonngCB, self.luongThang])


# Bắt đầu tạo data
dsNhanVien = [nvVanPhong(i, hoTen=f'Van Phong {i}', luonngCB=random.randint(10_000_000, 45_000_000),
                         soNgayLam=random.randint(20, 30)) for i in range(1, 6)]

dsNhanVien.append(nvVanPhong(59, hoTen='Nguyễn Trường Thọ', luonngCB=random.randint(10_000_000, 45_000_000),
                             soNgayLam=random.randint(20, 30)))

dsNhanVien.extend([nvBanHang(i, hoTen=f'Ban Hang {i}', luonngCB=random.randint(7_500_000, 25_000_000),
                             soSP=random.randint(100, 500)) for i in range(1, 6)])
# Kết thúc tạo data


if __name__ == '__main__':
    cty = CongTy(maCongTy='CT1', tenCongTy='Cong Ty 1')
    cty.them_nhan_vien(dsNhanVien)

    cty.tinh_luong_thang_NV()
    cty.xuat_tat_ca_nhan_vien()

    nv_luong_cao_nhat = cty.tim_NV_luong_cao_nhat()
    if nv_luong_cao_nhat is not None:
        print('Nhân viên có lương cao nhất:', nv_luong_cao_nhat.hoTen)
    else:
        print('Không có nhân viên')

    nv_bh_co_luong_thap_nhat = cty.tim_NV_BH_luong_thap_nhat()
    if nv_bh_co_luong_thap_nhat is not None:
        print('Nhân viên kinh doanh có lương thấp nhất:', nv_bh_co_luong_thap_nhat.hoTen)
    else:
        print('Không có nhân viên bán hàng')

    timNV = cty.tim_nhan_vien(59)
    print('Tên nhân viên có mã 59:', cty.tim_nv(59))

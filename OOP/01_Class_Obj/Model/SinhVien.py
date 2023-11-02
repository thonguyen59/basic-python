#!/usr/bin/python
# -*- coding: utf-8 -*-

class SinhVien:
    def __init__(self, maSV, hoTen, diemTB, diemRL):
        self.maSV = maSV
        self.hoTen = hoTen
        self.diemTB = diemTB
        self.diemRL = diemRL

    def inThongTin(self, ):
        print("Thông tin sinh viên: ")
        print("\t+ Mã sinh viên: ", self.maSV)
        print("\t+ Tên sinh viên: ", self.hoTen)
        print("\t+ Điểm trung bình: ", self.diemTB)
        print("\t+ Điểm rèn luyện: ", self.diemRL)


sv = SinhVien("123", "Nghĩa thúi", "10", "22")

SinhVien.inThongTin(sv)

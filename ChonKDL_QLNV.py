nvbh1 = {'maNV': 123, 'hoTen': 'Nguyễn Trường Thọ', 'luongCB': 50_000_000, 'luongHT': 0, 'soSP': 105}
nvbh2 = {'maNV': 124, 'hoTen': 'Nguyễn Trường Thịnh', 'luongCB': 20_000_000, 'luongHT': 0, 'soSP': 45}
nvbh3 = {'maNV': 125, 'hoTen': 'Nguyễn Viết Huy', 'luongCB': 30_000_000, 'luongHT': 0, 'soSP': 142}
nvbh4 = {'maNV': 126, 'hoTen': 'Nguyễn Trọng Nghĩa', 'luongCB': 40_000_000, 'luongHT': 0, 'soSP': 89}
nvbh5 = {'maNV': 127, 'hoTen': 'Trần Duy Tân', 'luongCB': 50_000_000, 'luongHT': 0, 'soSP': 97}
nvvp1 = {'maNV': 128, 'hoTen': 'Trần Ngọc Lãm', 'luongCB': 15_000_000, 'luongHT': 0, 'soNL': 500}
nvvp2 = {'maNV': 129, 'hoTen': 'Phạm Thị Thu Thủy', 'luongCB': 20_000_000, 'luongHT': 0, 'soNL': 600}
nvvp3 = {'maNV': 130, 'hoTen': 'Mai Quốc Khánh', 'luongCB': 34_000_000, 'luongHT': 0, 'soNL': 456}
nvvp4 = {'maNV': 131, 'hoTen': 'Đỗ Vắn Trung', 'luongCB': 23_000_000, 'luongHT': 0, 'soNL': 654}
nvvp5 = {'maNV': 132, 'hoTen': 'Thái Ngọc Bảo', 'luongCB': 10_000_000, 'luongHT': 0, 'soNL': 356}
nvvp6 = {'maNV': 133, 'hoTen': 'Mai Thị Ngoan', 'luongCB': 24_000_000, 'luongHT': 0, 'soNL': 567}

dsNV = []
dsNV.append(nvbh1)
dsNV.append(nvbh2)
dsNV.append(nvvp1)


def displayNV(dsNV):
    for nv in dsNV:
        temp = list(nv.values())
        print(temp)
    return 1, 2, 3, 4


def tinh(a: int, b: float = 3) -> int:
    """Test"""
    cong = a + b
    tru = a - b
    nhan = a * b
    chia = a / b
    return cong


if __name__ == '__main__':
    cong = tinh(8.5)

    cong = (lambda x: 12 * x + 1)(5)

    print(cong)

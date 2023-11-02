def tao_nv(*args, **kwargs) -> dict:
    nv = {}
    if kwargs.get('so_ngay_lv'):
        nv = {
            'ma_nv': args[0],
            'ho_ten': args[1],
            'luong_cb': args[2],
            'so_ngay_lv': kwargs.get('so_ngay_lv'),
            'luong_ht': 0
        }
    elif kwargs.get('so_sp'):
        nv = {
            'ma_nv': args[0],
            'ho_ten': args[1],
            'luong_cb': args[2],
            'so_sp': kwargs.get('so_sp'),
            'luong_ht': 0
        }
    return nv


# Khởi tạo nhân viên
def khoi_tao(ds_nv: list):
    ds_nv.append(tao_nv(23, 'Nguyễn Trường Thọ', 50_000_000, so_ngay_lv=105))
    ds_nv.append(tao_nv(24, 'Nguyễn Trường Thịnh', 20_000_000, so_ngay_lv=45))
    ds_nv.append(tao_nv(26, 'Nguyễn Trọng Nghĩa', 40_000_000, so_ngay_lv=89))
    ds_nv.append(tao_nv(27, 'Trần Duy Tân', 50_000_000, so_ngay_lv=97))
    ds_nv.append(tao_nv(28, 'Trần Ngọc Lãm', 15_000_000, so_ngay_lv=500))
    ds_nv.append(tao_nv(29, 'Phạm Thị Thu Thủy', 20_000_000, so_sp=600))
    ds_nv.append(tao_nv(30, 'Mai Quốc Khánh', 34_000_000, so_sp=456))
    ds_nv.append(tao_nv(31, 'Đỗ Vắn Trung', 23_000_000, so_sp=654))
    ds_nv.append(tao_nv(32, 'Thái Ngọc Bảo', 10_000_000, so_sp=356))
    ds_nv.append(tao_nv(33, 'Mai Thị Ngoan', 24_000_000, so_sp=0))


# Xuất các nhân viên
def print_vn(dsNV: list):
    for nv in dsNV:
        if nv.get('so_sp'):
            print('Nhan vien ban hang: {}'.format(nv.values()))
        elif nv.get('so_ngay_lv'):
            print('Nhan vien van phong: {}'.format(nv.values()))


# Tính lương hằng tháng các nhân viên
def tinh_luong_ht(ds_nv: list):
    for nv in ds_nv:
        if nv.get('so_sp', 0) > 1:
            nv['luong_ht'] = 1
        elif nv.get('so_ngay_lv', 0) > 0:
            nv['luong_ht'] = 2


if __name__ == '__main__':
    ds = []
    khoi_tao(ds)
    tinh_luong_ht(ds)
    print_vn(ds)

import random
import string

nguoi_thang = '*Người thắng vòng này !!'
may_thang = '*Máy thắng vòng này :(('
hoa = "*Hòa ^.^"
keo = 'kéo'
bua = 'búa'
bao = 'bao'
lua_chon = [keo, bua, bao]
diem_may = 0
diem_nguoi = 0

print("Nhập các lựa chọn sau: " + str(lua_chon))

while (abs(diem_may - diem_nguoi) != 2):
    nguoi = input('Người ra: ')
    while (nguoi not in lua_chon):
        print("Vui lòng chọn các lựa chọn sau: " + str(lua_chon))
        nguoi = input('Người ra: ')

    may = random.choice(lua_chon)
    print("Máy ra: " + may)
    if (may == keo):
        if (nguoi == bua):
            diem_nguoi += 1
            print(nguoi_thang)
        elif (nguoi == bao):
            diem_may += 1
            print(may_thang)
        else:
            print(hoa)
    elif (may == bua):
        if (nguoi == bao):
            diem_nguoi += 1
            print(nguoi_thang)
        elif (nguoi == keo):
            diem_may += 1
            print(may_thang)
        else:
            print(hoa)
    else:
        if (nguoi == keo):
            diem_nguoi += 1
            print(nguoi_thang)
        elif (nguoi == bua):
            diem_may += 1
            print(may_thang)
        else:
            print(hoa)

    print("*Người được: " + str(diem_nguoi) + " điểm - Máy được: " + str(diem_may) + " điểm")
    print("==========")

if (diem_may > diem_nguoi): print("CON NGƯỜI ĐÃ THUA NGƯỜI MÁY T.T")
else: print("CON NGƯỜI ĐÃ CHIẾN THẮNG NGƯỜI MÁY ^.^")

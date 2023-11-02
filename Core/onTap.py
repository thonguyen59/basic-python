s = "Nghia oi"
print("Nghia" in s)

ds = [1, 2, 3, 4]

ds[ds.index(4)] = 5

print(ds)

ds1 = [1, 1, 2, 3, 4]

mySet = set(ds1)
myList = list(mySet)

print(myList)

tuoi = 18
bia = 1

if tuoi >= 18 :
    if bia == 0:
        print("Duoc phep lai xe!")
    else:
        print("Khong duoc phep lai xe")
else:
    print("Khong duoc phep lai xe")


ds = [3, 6, 9]
num = 0

while num not in ds:
    num = int(input("Nhap lai nhe: "))
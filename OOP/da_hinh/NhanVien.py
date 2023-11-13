class NhanVien:
    def __init__(self, name = ''):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def print(self):
        print(self.name)

    @name.setter
    def name(self, name):
        self.__name = name

class NVVP(NhanVien):
    def __init__(self, name, days = 0):
        super().__init__(name)
        self.days = days

    def printNVVP(self):
        print(self.name, self.days)


class NVBH(NhanVien):
    def __init__(self, name, sales = 0):
        super().__init__(name)
        self.sales = sales

    def printNVBH(self):
        print(self.name, self.sales)


if __name__ == '__main__':
    nv1 = NVVP('Nguyễn Văn A', 22)
    nv2 = NVBH('Nguyễn Văn B', 13)

    # nv1.printNVVP()
    # nv2.printNVBH()

    ds = [nv1, nv2]

    for nv in ds:
        if isinstance(nv, NVVP):
            nv.printNVVP()
        else: nv.printNVBH()

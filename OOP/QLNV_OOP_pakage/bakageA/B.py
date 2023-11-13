class B:
    def __init__(self, a: int, b, c) -> None:
        self._a = a
        self.__b = b
        self.c = c

    def _methodA(self):
        print("Phương thức _a(): Protected")

    def __methodB(self):
        print("Phương thức __b(): Private")

    def methodC(self):
        print("Phương thức c(): Public")


if __name__ == '__main__':



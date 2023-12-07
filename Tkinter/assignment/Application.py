from Model import CongTy
from GUI import GUI

if __name__ == '__main__':
    cong_ty = CongTy('CT1', tenCty='Cong Ty 1')
    cong_ty.loadDatabase()
    gui = GUI(cong_ty)
    gui.run()
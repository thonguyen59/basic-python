from ViewCongTy import ViewCongTy
from ModelCongTy import ModelCongTy
from ControllerCongTy import ControllerCongTy

view = ViewCongTy()
model = ModelCongTy()
controller = ControllerCongTy(view, model)

view.mainloop()
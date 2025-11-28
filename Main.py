
from View.CTKView import View
from Controller.Controller import Controller
from Model.Model import Model

if __name__ == "__main__":
    model = Model()
    controller = Controller(model)
    view = View(controller)
    
    
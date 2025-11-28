
from View.View import View
from Controller.Controller import Controller
from Model.Model import Model

if __name__ == "__main__":
    view = View()
    model = Model()
    controller = Controller(view, model)
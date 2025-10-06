
from View import View
from Controller import Controller
from Model import Model

if __name__ == "__main__":
    view = View()
    model = Model()
    controller = Controller(view, model)
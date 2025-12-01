
class MyObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.secret = "hiddenValue"

obj = MyObject("Alice", 30)


obj_dict_1 = obj.__dict__
print(obj_dict_1)

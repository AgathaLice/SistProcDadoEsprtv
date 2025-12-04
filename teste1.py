
from Model.Chain import Link

class EloUm(Link):
    
    def run(self, **kwargs):

        print(kwargs)
        print(1)

        if self.next != None:
            return self.next.run(kwargs=kwargs)
        else:
            return self.last(kwargs=kwargs)
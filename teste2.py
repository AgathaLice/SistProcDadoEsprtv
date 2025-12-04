
from Model.Chain import Link

class EloDois(Link):
    
    def run(self, **kwargs):

        print(kwargs)
        print(2)

        if self.next != None:
            return self.next.run(kwargs=kwargs['kwargs'])
        else:
            return self.last(kwargs=kwargs['kwargs'])
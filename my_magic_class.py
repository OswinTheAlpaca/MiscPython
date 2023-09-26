


class Dummy(object):
    def __init__(self, *args, a = 0, b = 0, unicorn = "", desc = "instance magic", ** kwargs):  
        self.desc = desc
        self.kwargs = kwargs
        self.args = args
        self.a = a
        self.b = b
        self.unicorn = unicorn
        
    def __str__(self):
        dm = self.Dummy
        print(dm)
        
    def __setitem__(self, index, item1):
        self.item[index] = item1

    def __getitem__(self, index):
        return self.args[index]
    
    def __len__(self):
        return len(self.args)
    
    
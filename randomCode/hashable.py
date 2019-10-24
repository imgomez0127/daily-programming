class Hashable(type):
    def __new__(cls,name,base,dct):
        if "__hash__" not in dct:
            dct["__hash__"] = lambda x: hash(id(x))
        new_class = super().__new__(cls,name,base,dct) 
        return new_class

class hashable_list(list,metaclass = Hashable):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

test = hashable_list([1,2,3,4,5])
print(test)
print(test.__hash__)
print(hash(test))

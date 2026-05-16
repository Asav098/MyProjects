class bob:
    def __init__(self,name,age):
        self.name  = name
        self.age = age

    def __gt__(self,other):
        return True if self.age>other.age else False

bobin = bob("bobin", 20)
bobby = bob("bobby", 30)

print(bobin > bobby)
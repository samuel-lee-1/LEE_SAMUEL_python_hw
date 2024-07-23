class Pet:
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        print ("hello, I am", self.name)


# the errors were init(self, name) and introduce()
pet = Pet("Perry")
pet.introduce()
pet1 = Pet("Matt")
pet1.introduce()
pet2 = Pet("Nicholas")
pet2.introduce()
pet3 = Pet("James")
pet3.introduce()
pet4 = Pet("Sasha")
pet4.introduce()


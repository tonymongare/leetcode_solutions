class Dogs:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark !!")

    def info(self):
        print(f'My name is {self.name} and i\'m ages {self.age}')


ozzy = Dogs('simba', 25)
obby = Dogs('Saddam', 90)

#calling the methods
ozzy.bark()
ozzy.info()

#calling the methods
obby.bark()
obby.info()
//

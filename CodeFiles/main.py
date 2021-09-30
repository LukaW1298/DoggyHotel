


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'says "WOOF WOOF"')
        else:
            print(self.name, 'says "woof woof"')

    def humanYears(self):
        humanAge = self.age * 7
        return humanAge

    def __str__(self):
        return "I'm a dog named " + self.name



class ServiceDog(Dog):
    def __init__(self, name, age, weight,handler, isWorking):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.isWorking = False

    def walk(self):
        print(self.name, "is helping its handler",self.handler, "walk")

    def bark(self):
        if self.isWorking:
            print(self.name, 'says "I can\'t bark, I\'m working"')
        else:
            Dog.bark(self)

ravioli = ServiceDog("Ravioli",5,38,"Luka",False)

print(ravioli)
ravioli.bark()
ravioli.isWorking = True
ravioli.bark()

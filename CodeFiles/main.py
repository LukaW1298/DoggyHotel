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

    def walk(self):
        print(self.name, 'is walking')

    def humanYears(self):
        humanAge = self.age * 7
        return humanAge

    def __str__(self):
        return "I'm a dog named " + self.name
class ServiceDog(Dog):
    def __init__(self, name, age, weight,handler):
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
class Frisbee:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "Im a " + self.color + " frisbee"
class FrisbeeDog(Dog):

    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        # if he has a frisbee
        if self.frisbee is not None:
            print(self.name, 'says, "I can\'t bark, I have a frisbee in my mouth"')
        else:
            Dog.bark(self)

    def walk(self):
        if self.frisbee is not None:
            print(self.name, 'says, "I can\'t walk, I have a frisbee in my mouth"')
        else:
            Dog.walk(self)

    def catch(self, frisbee):
        # assign the frisbee variable to the frisbee attribute
        self.frisbee = frisbee
        print(self.name, 'caught a', frisbee.color, 'frisbee')

    def give(self):
        frisbee = self.frisbee
        # remove the value of the frisbee attribute
        self.frisbee = None
        return frisbee

    def __str__(self):
        if self.frisbee is not None:
            return "I'm a dog named " + self.name + " and I have a frisbee"
        else:
            return Dog.__str__(self)
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name, 'says, "Meow"')
class HotDog:
    def __init__(self, calories):
        self.calories = calories

    def cook(self):
        pass

    def eat(self):
        pass

'''-------------------------------Hotel and TestCode---------------------------------'''


class Hotel:
    def __init__(self, name):
        self.name = name
        self.kennel = {}

    def check_in(self, dog):
        # if: 'dog' is an instance of Dog, check him in. else: reject the request
        if isinstance(dog, Dog):
            self.kennel[dog.name] = dog
            print(dog.name, 'is checked into', self.name)
        else:
            print('Sorry only Dogs are allowed in', self.name)

    def check_out(self, name):
        # if dog is checked in, check him out
        if name in self.kennel:
            dog = self.kennel[name]
            print(dog.name, 'is checked out of', self.name)
            del self.kennel[dog.name]
            return dog
        else:
            print('Sorry', name, 'is not boarding at', self.name)
            return None

    def barktime(self):
        # call the bark() method of each dog checked in
        for dog_name in self.kennel:
            dog = self.kennel[dog_name]
            dog.bark()

    def walking_service(self):
        if self.walker is not None:
            self.walker.walk_the_dogs(self.kennel)
        else:
            # call the walk() method of each dog checked in
            for dog_name in self.kennel:
                dog = self.kennel[dog_name]
                dog.walk()

    def hire_walker(self, walker):
        # if walker is an instance of DogWalker, assign walker
        if isinstance(walker, DogWalker):
            self.walker = walker
        else:
            print('Sorry,', walker.name, 'is not a Dog Walker')


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "I'm a person and my name is " + self.name
class DogWalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)

    def walk_the_dogs(self, dogs):
        # call the walk() method of each dog checked in
        for dog_name in dogs:
            dogs[dog_name].walk()

def test_code():
    ravioli = ServiceDog("Ravioli",5,38,"Luka")
    codie = Dog('Codie', 12, 38)
    jackson = Dog('Jackson', 9, 12)
    sparky = Dog('Sparky', 2, 14)
    rody = ServiceDog('Rody', 8, 38, 'Joseph')
    rody.bark()
    rody.isWorking = True
    rody.bark()

    red_frisbee = Frisbee('red')
    dude = FrisbeeDog('Dude', 5, 20)
    print(dude)
    dude.bark()
    dude.catch(red_frisbee)
    dude.bark()
    print(dude)
    frisbee = dude.give()
    print(frisbee)
    print(dude)
    kitty = Cat('Kitty')
    joe = DogWalker('Joe')

    # is checking the dogs into the new opened Hotel named "Doggy Hotel"
    hotel = Hotel('Doggy Hotel')
    hotel.check_in(codie)
    hotel.check_in(jackson)
    hotel.check_in(rody)
    hotel.check_in(dude)
    hotel.check_in(kitty)

    hotel.barktime()

    hotel.hire_walker(joe)

    hotel.walking_service()




if __name__ == '__main__':
    test_code()



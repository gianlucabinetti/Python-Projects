class animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f" {self.name} is currently eating")
        
    def sleep(self):
        print(f" {self.name} is currently sleeping")


class prey(animal):
    def flee(self):
        print(f" {self.name}is fleeing")

class predator(animal):
    def hunt(self):
        print(f" {self.name} is hunting")


class Rabbit(prey):
    pass

class Shark(predator):
    pass

class Fish(prey, predator):
    pass

class hawk(predator):
    pass

rabbit = Rabbit ('Bugs')
fish = Fish ('nemo')
shark = Shark ('rick')
hawk = hawk ('balding eagle')
    
hawk.hunt()
fish.hunt()
fish.flee()
fish.eat()
fish.sleep()
rabbit.flee()
rabbit.eat()
rabbit.sleep()
hawk.sleep()
hawk.hunt()
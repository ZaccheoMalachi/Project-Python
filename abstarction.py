from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def eat(self,food):
        pass
class Mamalia(Animal):
    def __init__(self,name,weight):
        self.__name=name
        self.weight=weight
    def move(self):
        print(self.__name,'is running')
    def eat(self, food):
        print(self.__name,'is eating',food)
class Fish(Animal):
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def move(self):
        print(self.color,self.name,'is swimming')
    def eat(self):
        print(self.color,self.name,'is eating')
cow=Mamalia('Cow','1000kg')
cow.move()
cow.eat('grass')
print(cow.weight)
clownFish=Fish('Clown Fish','Orange')
clownFish.move()
clownFish.eat()
clownFish.name='Gold fish'
clownFish.eat()
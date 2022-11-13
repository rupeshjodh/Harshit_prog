# raise errors example 1
# NotImplimentedError
# abstract method

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplementedError('you have to define this method in subclasses')


class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'bhow bhow'

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'moew moew'

doggy = Dog('boony','pug')
cat = Cat('boony','pug')
print(doggy.sound())
print(cat.sound())
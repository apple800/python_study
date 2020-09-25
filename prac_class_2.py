class Pets():
    animals = []
    def init(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def init(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Jovy(Cat):
    def sing(self, sounds):
        return f'{sound}'

#1 Add another Cat

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon(), Sally(), Jovy()]
print(my_cats)

#3 Instantiate the Pet class with all your cats use variable my_pets

#4 Output all of the cats walking using the my_pets instance
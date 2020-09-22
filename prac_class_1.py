#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('cathy', 23)
cat2 = Cat('Tom', 30)
cat3 = Cat('Lue', 13)


# 2 Create a function that finds the oldest cat
def oldest(c1,c2,c3):
    max = c1.age if c1.age > c2.age else c2.age
    max = max if max > c3.age else c3.age
    return max


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'"The oldest cat is {oldest(cat1, cat2, cat3)} years old."')
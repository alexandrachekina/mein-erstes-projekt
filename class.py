class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def vorstellen(self):
        return f"name: {self.name}, age: {self.age}, grade: {self.grade}"

    def prüfen(self):
        if self.grade >= 10:
            return True
        return False


s1 = Student("Alex", 19, 12)

print(s1.prüfen())
print(s1.vorstellen())

class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

def makeSpeak(animal):
    animal.speak()

animals = [Dog(), Cat()]
for animal in animals:
        animal.makeSpeak(animal)    

       
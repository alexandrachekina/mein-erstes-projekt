class Student:
            def __init__(self,name, age, beruf):
                self.name = name
                self.age = age
                self.beruf = beruf

class Lehrer:
            def __init__(self,name, age, beruf):
                self.name = name
                self.age = age
                self.beruf = beruf
def prüfen():
    name = input("Geben Sie die name")
    age = input("geben Sie den age")
    beruf = input("geben sie den Beruf")

    if beruf == "Lehrer":
        lehr1 = Lehrer(name,age,beruf)
        return f"Ich bin Student --name : {name}, alter: {age}, beruf:{beruf}"

    elif beruf == "Student":
        stu1 = Student(name,age,beruf)
        return f"Ich bin Student --name : {name}, alter: {age}, beruf:{beruf}"
        
    else:
        return "Dieser beruf ist nicht gültig"


print(prüfen())
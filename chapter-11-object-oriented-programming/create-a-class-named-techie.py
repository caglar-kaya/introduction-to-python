'''
Write a class Techie that has four global attributes (part of self) name (str), age (int), profession (str), and location (str). 
Additionally, write four methods that print one of the global attributes respectively named get_name, get_age, get_profession, and get_location.
'''

class Techie:  
    def __init__(self, name, age, profession, location):
        self.name = name
        self.age = age
        self.profession = profession
        self.location = location

    def get_name(self):
        print("Name:", self.name)

    def get_age(self):
        print("Age:", self.age) 

    def get_profession(self):
        print("Profession:", self.profession) 

    def get_location(self):
        print("Location:", self.location)

techie = Techie("Caglar", 34, "Software Developer", "Rotterdam")

techie.get_name()
techie.get_age()
techie.get_profession()
techie.get_location()

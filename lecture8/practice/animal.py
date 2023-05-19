class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def set_animal_name(self):
        animal_name = input("set the animal name: ")
        self.name = animal_name
    
    def get_animal_name(self):
        return self.name

    def set_animal_species(self, species):
        animal_species = input("Witch is that animal species? ")
        self.species = animal_species

    def get_animal_species(self):
        return self.species

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("Canine", name)
        self.breed = breed
    
    def set_dog_species(self, species):
        self.species = "Canine"

    def get_dog_breed(self):
        return self.breed

    def set_dog_breed(self):
        dog_breed = input("What breed is that dog? ")
        self.breed = dog_breed


dog = Dog(name="?", breed="?")
print(dog.get_animal_species())
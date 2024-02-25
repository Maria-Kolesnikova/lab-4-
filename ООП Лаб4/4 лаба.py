
class Animal:
    def __init__(self, species: str, sound: str):
        self.species = species
        self.sound = sound

    def make_sound(self) -> str:
        """Make the sound specific to the animal"""
        return self.sound

    def __str__(self) -> str:
        return f"A {self.species}"

    def __repr__(self) -> str:
        return f"Animal(species={self.species}, sound={self.sound})"


class Dog(Animal):
    def __init__(self, species: str, sound: str, breed: str):
        super().__init__(species, sound)
        self.breed = breed

    def bark(self) -> str:
        """Make the specific sound of barking for a dog"""
        return "Woof! Woof!"

    def __str__(self) -> str:
        return f"A {self.breed} dog"

    def __repr__(self) -> str:
        return f"Dog(species={self.species}, sound={self.sound}, breed={self.breed})"


if __name__ == "__main__":
    animal = Animal("Mammal", "Generic animal sound")
    print(animal)  # Output: A Mammal
    print(repr(animal))  # Output: Animal(species=Mammal, sound=Generic animal sound)

    dog = Dog("Mammal", "Bark", "Golden Retriever")
    print(dog)  # Output: A Golden Retriever dog
    print(repr(dog))  # Output: Dog(species=Mammal, sound=Bark, breed=Golden Retriever)
    print(dog.make_sound())  # Output: Bark
    print(dog.bark())  # Output: Woof! Woof!

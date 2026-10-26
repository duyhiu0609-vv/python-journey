"""Exercise 03: one clear basic inheritance example."""


class Animal:
    """A general animal with a name."""

    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    """A dog is an animal and can make a dog sound."""

    def speak(self) -> str:
        return f"{self.name}: woof"


if __name__ == "__main__":
    animal = Animal("Animal")
    dog = Dog("Milo")

    print(animal.name)
    print(dog.speak())
    print(f"Dog is an Animal: {isinstance(dog, Animal)}")

    # Dog "is an" Animal because Dog inherits from Animal.

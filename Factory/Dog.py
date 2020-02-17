class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "This is dog named " + self.name

def get_pet(pet="dog"):
    """factory to create objects"""
    pets = dict(dog=Dog("Hope"))
    return pets[pet]

print (get_pet())
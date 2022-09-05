from pet import Pet

class Ninja():

    def __init__(self ,first_name, last_name, treats, pet_food, Pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet
        self.treats = treats 
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        print(f"Yay! {self.first_name}'s health is now {self.pet.health}")
        return self

    def feed(self):
        self.pet.eat()
        print(f"Yay! {self.first_name}'s health is now {self.pet.health} and energy is {self.pet.energy}")
        return self

    def bathe(self):
        self.pet.noise()
        return self



dog = Pet("Chedar", "husky", "roll")
me = Ninja("Paul", "Kim", "candy", "meat", dog)

me.walk().feed().bathe()

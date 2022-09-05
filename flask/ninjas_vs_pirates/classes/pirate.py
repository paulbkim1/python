class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.is_blocking = False
        self.speed_count = 0

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nSpeed Count: {self.speed_count}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        #is target currently blocking
        if ninja.is_blocking:
            ninja.health += (self.strength - self.strength/2)
            ninja.is_blocking = False
        return self
    
    def block( self ):
        self.is_blocking = True
        return self
    
    def calculate_count (self):
        self.speed_count += self.speed
        return self
    
    def show_count(self):
        print(f"Jack Sparrow Speed Count: {self.speed_count}\n")


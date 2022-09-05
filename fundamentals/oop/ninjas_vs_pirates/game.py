from classes.ninja import Ninja
from classes.pirate import Pirate

speed = 6

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")
michelangelo.show_stats()
jack_sparrow.show_stats()

while(michelangelo.health > 0 and jack_sparrow.health > 0):
        michelangelo.calculate_count()
        jack_sparrow.calculate_count()
        
        if michelangelo.speed_count >= 10:
            michelangelo.speed_count = 0
            
            response_ninja = input("You are a ninja what do you want to do? \n 1) Attack 2) Block\n")
            if response_ninja == '1':
                michelangelo.attack(jack_sparrow)
            elif response_ninja == '2':
                michelangelo.block() #invokes block method
            # elif response_ninja == '2':
            #     print("both parties blocked, start fighting ninja.")
            else:
                while(response_ninja != '1' and response_ninja != 2):
                    print("Please pick a valid response")
                    response = input("You are a ninja what do you want to do? \n 1) Attack 2) Block\n") 
            michelangelo.show_stats()
            jack_sparrow.show_stats()
            
        if jack_sparrow.speed_count >= 10:
            jack_sparrow.speed_count = 0 
                   
            response_pirate = input("You are a pirate what do you want to do? argh \n 1) Attack 2) Block\n")
            if response_pirate == '1':
                jack_sparrow.attack(michelangelo)
            elif response_pirate == '2':
                jack_sparrow.block()
            # elif response_pirate == '2' and response_ninja == '2':
            #     print("both parties blocked, start fighting matey")
            else:
                while(response_pirate != '1' and response_pirate != 2):
                    print("Please pick a valid response")
                    response_pirate = input("You are a ninja what do you want to do? \n 1) Attack 2) Block\n")
            michelangelo.show_stats()
            jack_sparrow.show_stats()
            
        else: 
            michelangelo.show_count()
            jack_sparrow.show_count()
            
        
        





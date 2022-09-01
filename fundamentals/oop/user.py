class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.reward_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(f"{self.first_name} {self.last_name} {self.email} {self.age} {self.reward_member} {self.gold_card_points} points")
    def enroll(self):
        if self.reward_member == True:
            print("User already a member")
        else:
            self.reward_member = True
            self.gold_card_points += 200
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not enough points")
        else:
            self.gold_card_points -= amount

user1 = User("John", "Kim", "p@gmail.com", 27)
user2 = User("Paul", "Kim", "pk@gmail.com", 27)

user1.spend_points(50)
user1.enroll()
user2.enroll()
user2.spend_points(80)
user1.display_info()
user2.display_info()
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]


class Player():
    player_list = []
    def __init__(self, players_data):
        self.name = players_data['name']
        self.age = players_data['age']
        self.position = players_data['position']
        self.team = players_data['team']
        Player.player_list.append(self)

    def __repr__(self):
        return f"name : {self.name} age : {self.age} position : {self.position} team : {self.team}"

    @classmethod
    def get_team(cls, team_list):
        for i in team_list:
            Player(i)
        print(cls.player_list)
        


Player.get_team(players)

player1 = Player(kevin)
player2 = Player(jason)
player3 = Player(kyrie)


new_team = []
for i in players:
    player = Player(i)
    new_team.append(player)

print(new_team)
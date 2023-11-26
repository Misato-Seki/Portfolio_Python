class Player:
    """Player-class: stores data on team colors and points. """
    def __init__(self):
        self.color = input("What color do I get?:")
        self.__points = 0
	
    def tellscore(self):
        print('I am', self.color, ', we have', self.__points, 'points!')
	
    def goal(self):
        self.__points += 1

def main():
    player_1 = Player()
    player_2 = Player()
    
    player_1.goal()
    player_1.goal()
    player_2.goal()
	
    player_1.tellscore()
    player_2.tellscore()
	
if __name__ == "__main__":
    main()

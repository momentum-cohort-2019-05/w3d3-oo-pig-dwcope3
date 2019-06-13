import random 
from player_classes import ComputerPlayer
from player_classes import HumanPlayer


def roll_die():
    return random.randint(1,6)


class Game:
    """
    Game class
    """
    def __init__(self, die, player1, player2):
        self.die = die
        self.players = [player1, player2]
        self.current_player = None
        self.reset_scores()

    def reset_scores(self):
        self.scores = [0,0]
        self.round_score = 0

    def decide_first_player(self):
        self.current_player = random.randint(0,1)
        print(f"Player {self.current_player + 1} starts")

    def getcurrent_player(self):
        return self.players[self.current_player]

    def switch_player(self):
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0
        print(f"It is player {self.current_player + 1}'s turn.")

    def game_ends(self):
        return self.scores[0] >= 100 or self.scores[1] >= 100

    def start_game(self):
        self.welcome()
        self.reset_scores()
        self.decide_first_player()
        
        while not self.game_ends():
            self.run_game()
            if not self.game_ends():
                self.switch_player()

        # play_again = True
        # while play_again:
        #     self.run_game()
        #     play_again = input("Play Again? (Y/N) ")
        #     play_again = play_again.lower().startswith("y")

        
    
        print(f"Player {self.current_player + 1} Wins!")

    def run_game(self):
        turn_score = 0
        player = self.getcurrent_player()
        player.start_of_game()
       
        roll = self.die()
        player.roll(roll)
        print(f"Roll: {roll}")

        while roll != 1:
            turn_score += roll
            if not player.roll_again():
                break
            roll = self.die()
            player.roll(roll)
            print(f"Roll: {roll}")

        if roll == 1:
            turn_score = 0

        print (f"Turn score: {turn_score}")
        self.scores[self.current_player] += turn_score
        print(f"Current score for player {self.current_player + 1}: {self.scores[self.current_player]}")

    def welcome(self):
        print("*"*70)
        print("Welcome to Pig Dice".center(70))
        print("The first to reach 100 points wins".center(70))
        print("*"*70)
# breakpoint()
if __name__ == "__main__":
    game = Game(roll_die, HumanPlayer(), ComputerPlayer())
    game.start_game()


    
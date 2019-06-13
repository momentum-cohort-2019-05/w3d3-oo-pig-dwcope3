import random

def roll_die():
    return random.randit(1,6)
    
class ComputerPlayer:
    """
    computer player class
    """
    

    def __init__(self):
        self.current_score = 0 

    def start_of_game(self):
        self.current_score = 0

    def roll(self, number):
        self.current_score += number

    def roll_again(self):
        return self.current_score < 20

class HumanPlayer:
    """
    Human Player Class
    """
        


    def __init__(self):
        self.current_score = 0

    def start_of_game(self):
        self.current_score = 0

    def roll(self, number):
        self.curent_score += number

    def roll_again(self):
        decision = None
        while decision is None or decision.lower()[0] not in ['r','h']:
            decision = input("(R)oll again or (H)old? ").lower()
        return decision[0] == "r"

class Game:
    """
    Game class
    """


    def __init__(self, die, player1, player2):
        self.die = die
        self.players = [player1, player2]
        self._current_player = None
        self.reset_scores()

    def start_game(self):
        self.print_instructions()
        play_again = True
        while play_again:
            self.run_game()
            play_again = input("Play Again? (Y/N) ")
            play_again = play_again.lower().startswith("y")

    def reset_scores(self):
        self.scores = [0,0]
        self.round_score = 0

    def decide_first_player(self):


    

    



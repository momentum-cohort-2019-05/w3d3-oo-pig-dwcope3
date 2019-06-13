

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
        self.current_score += number

    def roll_again(self):
        decision = None
        while decision is None or decision.lower()[0] not in ['r','h']:
            decision = input("(R)oll again or (H)old? ").lower()
        return decision[0] == "r"
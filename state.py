class GameState:
    def __init__(self):

        self.deck = []

        self.player_hand = []
        self.computer_hand = []

        self.player_played = []
        self.computer_played = []

        self.running_cards = []
        self.running_values = []

        self.player_score = 0
        self.computer_score = 0

        self.dealer = None

        self.messages = []

        self.phase = "START"
        self.begin = "STARTED"
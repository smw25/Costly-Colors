class GameState:
    def __init__(self):

        self.deck = []
        self.top = ''

        self.player_hand = []
        self.computer_hand = []

        self.player_played = []
        self.computer_played = []

        self.running_cards = []
        self.running_values = []

        self.player_score = 0
        self.computer_score = 0

        self.player_rsco = 0
        self.comp_rsco = 0

        self.dealer = None
        self.card_choice = ''

        self.messages = []

        self.phase = "NOT"
        self.begin = "NO"
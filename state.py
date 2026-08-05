class GameState:
    def __init__(self):

        self.reset()

        self.deck = []
        self.top = ''
        self.top_split = ''

        self.player_hand = []
        self.computer_hand = []

        self.player_played = []
        self.computer_played = []

        self.running_cards = []         #card value as string(8, or King)
        self.running_values = []        #numeric card value
        #self.running_suits = []         #suit's of cards  (suit, value)
        self.running_total = 0

        self.player_score = 0
        self.computer_score = 0

        self.player_rsco = 0
        self.comp_rsco = 0

        self.pp_score = 0    #player's hand score
        self.cp_score = 0    #computer's hand score
        
        self.dealer = None
        self.card_choice = ''   #for the computer during mogging

        self.messages = []
        self.handages = []
        self.wintags = []
        
        self.p_css_hand = []
        self.c_css_hand = []

        self.phase = "NOT"
        self.begin = "NO"
        self.go = "None"
        self.round = 1

        self.comp_pegs = []
        self.player_pegs = [] 
        self.comp_handscs = []
        self.player_handscs = []

        self.comp_p_avg = 0
        self.player_p_avg = 0
        self.comp_h_avg = 0
        self.player_h_avg = 0
        

    def reset(self):
        self.deck = []
        self.top = ''

        self.player_hand = []
        self.computer_hand = []

        self.player_played = []
        self.computer_played = []

        self.running_cards = []    #cards played with just name e.g. ['Jack', '7', 'Ace']
        self.running_values = []   #cards played as integers
        self.running_total = 0

        self.player_score = 0
        self.computer_score = 0

        self.player_rsco = 0
        self.comp_rsco = 0

        self.pp_score = 0    #player's hand score
        self.cp_score = 0    #computer's hand score
        
        self.dealer = None
        self.card_choice = ''   #for the computer during mogging

        self.messages = []
        self.handages = []
        self.wintags = []

        self.phase = "NOT"
        self.begin = "NO"
        self.go = "None"
        self.round = 1

        self.comp_pegs = []
        self.player_pegs = [] 
        self.comp_handscs = []
        self.player_handscs = [] 

        
        self.comp_p_avg = 0
        self.player_p_avg = 0
        self.comp_h_avg = 0
        self.player_h_avg = 0
import random



class Card():
    def __init__(self, suit, value):
       self.suit = suit
       self.value = value
       self.ptotal = 0
       self.dtotal = 0

    def showcard(self):
        print (f"{self.value} of {self.suit}")    

    
    def tot(self):
        self.ptotal += self.value 
        print(self.ptotal)

class Deck():
    def __init__(self):
        self.cards = []
        

    def build(self):
        for s in ['Diamonds','Hearts','Clubs','Spades']:
            for v in range(1, 14):
                self.cards.append(Card(s,v))
            
    def showdeck(self):
        for c in self.cards:
            c.showcard()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0,i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw(self):
        return self.cards.pop()
class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.playertotal = 0

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def dealershow(self, deck):
        print(self.hand[0])

    def showhand(self):
        for card in self.hand:
            card.showcard()


class UI():
    @classmethod
    def runUI(cls):
        while True:

            user_response = input("Welcome to the table!\nTo start enter 'y'  ").lower().strip()
            if user_response == 'y':
                deck = Deck()
                deck.build()
                deck.shuffle()
                house = Player("House")
                house.draw(deck).draw(deck)
                
                



UI.runUI()


#card = Card("clubs",5)
#deck = Deck()
#deck.build()
#card.showcard()


#newcard = deck.draw()
#newcard.show()

#jay = Player("Jayden")
#jay.draw(deck).draw(deck)
#jay.showhand()



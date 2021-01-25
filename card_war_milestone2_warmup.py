# #Milestone Warmup Project 2: Create the card game; War
# #For randomly generating a deck:
# import random
# #Global Variables:
# #Using dictionaries so that when a card is entered and it sees the rank, it will return the corresponding value
# card_values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,
#              'Nine':9,'Ten':10,'Jack':11,'Queen':12, 'King':13, 'Ace':14}
#
# ranks=('Two','Three','Four','Five','Six','Seven','Eight',
#              'Nine','Ten','Jack','Queen','King','Ace')
#
# suits=('Hearts','Diamond','Spades','Clubs')
#
#
# #Classes:
# #Card:
# #Contains info regarding SUIT of card
# #Contains info regarding RANK of card
# #Contains info regarding VALUE of card CORRESPONDING to the RANK of card
# class Card():
#     #Instantiation:
#     def __init__(self,suit,rank):
#         self.card_suit=suit
#         self.card_rank=rank
#         #This will correspond rank with its value:
#         self.card_value=card_values[rank]
#
#     def __str__(self):
#         return self.card_suit +' of '+ self.card_rank
#
# #Deck:
# class Deck():
#     #Instantiation:
#     def __init__(self):
#         #Creating a new deck of cards:
#         self.all_cards=[]
#         for i in range(len(suits)):
#             for j in range(len(ranks)):
#                 self.all_cards.append(Card(suits[i],ranks[j]))
#
#     #Will shuffle cards to ensure randomness:
#     def shuffle(self):
#         random.shuffle(self.all_cards)
#     #Will randomly deal a card:
#     def deal_card(self):
#         return self.all_cards.pop()
#
#     def __len__(self):
#         return self.all_cards
#
# #Player
# class Player():
#     def __init__(self,name):
#         self.player_name=name
#         #Player cards:
#         self.player_cards=[]
#
#     def remove_card(self):
#         #We're always gonna remove the first card of the deck:
#         return self.player_cards.pop(0)
#
#     def add_card(self,new_card):
#         #Checks if there are more than one cards being added to deck:
#         if type(new_card)==type([]):
#             #List of multiple card objects:
#             self.player_cards.extend(new_card)
#         else:
#             #For cases where there is only one card to be added into the deck:
#             self.player_cards.append(new_card)
#
#     def __str__(self):
#         return self.player_name + " has "+ str(len(self.player_cards)) + " cards."
#
#     def __len__(self):
#         return self.player_cards
#
# #Game Setup:
# #Creating Players:
# player_1=Player('One')
# player_2=Player('Two')
#
# #Creating a new deck shuffling it:
# new_deck=Deck()
# new_deck.shuffle()
#
# #Splitting deck between player 1 and player 2:
# def split():
#     for i in range(0,int(len(new_deck.all_cards)/2)):
#         player_1.add_card(new_deck.all_cards[i])
#     for j in range(26,len(new_deck.all_cards)):
#         player_2.add_card(new_deck.all_cards[j])
#     #Edit what to return later:
#
# def game():
#     game_on=True
#     round=0
#     while game_on:
#         round+=1
#         print('Current Round: '+str(round))
#         #Check for winner and loser:
#         if len(player_1.player_cards)==0:
#             return 'Player 1 has lost. Player 2 is the WINNER!!!'
#         if len(player_2.player_cards)==0:
#             return 'Player 2 has lost. Player 1 is the WINNER!!!'
#
#         #New Round: Append cards to compare
#         player_1_cards=[]
#         player_1_cards.append(player_1.remove_card())
#
#         print(player_1_cards)
#
#         player_2_cards = []
#         player_2_cards.append(player_2.remove_card())
#
#         at_war=True
#
#         while at_war:
#             #We use -1 index because as we're appending new cards and appending adds cards to the end
#             #we need want to compare our latest cards:
#             if player_1_cards[-1].value > player_2_cards[-1].value:
#                 player_1.add_card(player_1_cards)
#                 player_1.add_card(player_2_cards)
#                 at_war=False
#             elif player_1_cards[-1].value < player_2_cards[-1].value:
#                 player_2.add_card(player_2_cards)
#                 player_2.add_card(player_1_cards)
#                 at_war=False
#             else:
#                 print('WAR!!!')
#                 if len(player_1.player_cards)<5:
#                     print('Player 1 does not have enough cards')
#                     print('Player 2 is the WINNER')
#                     game_on=False
#                     break
#                 elif len(player_2.player_cards)<5:
#                     print('Player 2 does not have enough cards')
#                     print('Player 1 is the WINNER')
#                     game_on=False
#                     break
#                 else:
#                     for i in range(5):
#                         player_1_cards.append(player_1.remove_card())
#                         player_2_cards.append(player_2.remove_card())
#
#
#
#
# print(game())

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

def gameplay():
    player_one = Player("One")
    player_two = Player("Two")

    new_deck = Deck()
    new_deck.shuffle()

    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    game_on = True

    print(player_one.all_cards[0])
    print(player_one.all_cards[0].value)

    round_num = 0
    while game_on:

        round_num += 1
        print(f"Round {round_num}")

        # Check to see if a player is out of cards:
        if len(player_one.all_cards) == 0:
            print("Player One out of cards! Game Over")
            print("Player Two Wins!")
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print("Player Two out of cards! Game Over")
            print("Player One Wins!")
            game_on = False
            break

        # Otherwise, the game is still on!

        # Start a new round and reset current cards "on the table"
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True

        while at_war:

            if player_one_cards[-1].value > player_two_cards[-1].value:

                # Player One gets the cards
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                # No Longer at "war" , time for next round
                at_war = False

            # Player Two Has higher Card
            elif player_one_cards[-1].value < player_two_cards[-1].value:

                # Player Two gets the cards
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                # No Longer at "war" , time for next round
                at_war = False

            else:
                print('WAR!')
                # This occurs when the cards are equal.
                # We'll grab another card each and continue the current war.

                # First check to see if player has enough cards

                # Check to see if a player is out of cards:
                if len(player_one.all_cards) < 5:
                    print("Player One unable to play war! Game Over at War")
                    print("Player Two Wins! Player One Loses!")
                    game_on = False
                    break

                elif len(player_two.all_cards) < 5:
                    print("Player Two unable to play war! Game Over at War")
                    print("Player One Wins! Player One Loses!")
                    game_on = False
                    break
                # Otherwise, we're still at war, so we'll add the next cards
                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())


print(gameplay())


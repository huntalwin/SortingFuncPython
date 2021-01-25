#Milestone Project 2: Black Jack
#For randomly generating a hand:
import random
#Global Variables:
#Using dictionaries so that when a card is entered and it sees the rank, it will return the corresponding value
#Ace value ommited because in black jack Ace can be 11 or 1 depending on hand.
card_values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,
             'Nine':9,'Ten':10,'Jack':10,'Queen':10, 'King':10,'Ace':11}

ranks=('Two','Three','Four','Five','Six','Seven','Eight',
             'Nine','Ten','Jack','Queen','King','Ace')

suits=('Hearts','Diamond','Spades','Clubs')

#Classes:
class Card():
    def __init__(self,rank,suit):
        self.card_rank=rank
        self.card_suit=suit
        self.value = card_values[rank]

    def __str__(self):
        return self.card_rank+' of '+self.card_suit

class Deck():
    def __init__(self):
        self.all_cards=[]
        #Loop meant to append rank and suit together into all cards list:
        for i in range(len(suits)):
            for j in range(len(ranks)):
                self.all_cards.append(Card(ranks[j],suits[i]))

    def shuffle(self):
        return random.shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop()

class Hand(Deck):
    def __init__(self):
        Deck.__init__(self)
        #Player Hand:
        self.p_hand=[]
        #Dealer Hand:
        self.d_hand=[]
        self.p_hand_value=0
        self.d_hand_value=0

    #Find total value in a hand:
    #This function is used in the add_card function to find current value of hand.
    def find_total(self,hand):
        total_value=0
        for i in range(len(hand)):
            # if hand[i].value == 11:
            #     if total_value > 10:
            #         total_value += 1
            #     else:
            #         total_value += 11
            # else:
                total_value+=hand[i].value
        return total_value

    #Adding a card to the player hand:
    #card parameter will be for the deal card function call--> add_card(deal_card)
    def add_card(self,card):
        self.p_hand.append(card)
        #Checks for appropriate ace according to current value of player hand
        if self.p_hand[-1].value==11:
            total=self.find_total(self.p_hand)
            if total>11:
                self.p_hand_value+=1
            else:
                self.p_hand_value+=11
        else:
            self.p_hand_value+=self.p_hand[-1].value

    def add_card_dealer(self,card):
        self.d_hand.append(card)
        #Checks for appropriate ace according to current value of player hand
        if self.d_hand[-1].value==11:
            total=self.find_total(self.p_hand)
            if total>11:
                self.d_hand_value+=1
            else:
                self.d_hand_value+=11
        else:
            self.d_hand_value+=self.d_hand[-1].value



class Chip():
    def __init__(self):
        #100 is default for bet
        self.chip_total=100
        self.chip_bet=0

    #Will instantiate the number of chips the player wants for the game:
    def place_chips(self):
        while True:
            try:
                place_bet_ask = int(input('Please enter your buy-in amount: '))
            except:
                print('Whoops! That is not a number')
                continue
            else:
                self.chip_total=place_bet_ask
                return 'The value of your disposable chips is: '+ str(self.chip_total)

    def place_bet(self):
        while True:
            try:
                place_bet_ask=int(input('Please enter a bet: '))
            except:
                print('Whoops! That is not a number')
                continue
            else:
                if place_bet_ask<=self.chip_total:
                    self.chip_bet+=int(place_bet_ask)
                    self.chip_total-=self.chip_bet
                    return 'You have entered a bet of: '+str(place_bet_ask)+'\n'+ \
                           ' You have a total of '+str(self.chip_total)+' chips'
                else:
                    while place_bet_ask>self.chip_total:
                        place_bet_ask = int(input('Please enter a bet: '))
                        if place_bet_ask <= self.chip_total:
                            self.chip_bet += int(place_bet_ask)
                            self.chip_total -= self.chip_bet
                            return 'You have entered a bet of: ' + str(place_bet_ask) + '\n' + \
                                   ' You have a total of ' + str(self.chip_total) + ' chips'

    def raise_bet(self):
        print('Would you like to raise your bet?')
        print('   yes           no')
        raise_input = (input())
        if raise_input.lower() == 'yes':
            player_chip.place_bet()
            return True
        elif raise_input.lower() == 'no':
            print('Very well')
            return False
        else:
            while raise_input.lower()!='yes' or raise_input.lower()!='no':
                if raise_input.lower() == 'yes':
                    player_chip.place_bet()
                    return True
                elif raise_input.lower() == 'no':
                    print('Very well')
                    return False


    #Parameters will be *self.chip_total* and  *self.chip_bet*
    def win_bet(self,chip_total,chip_bet):
        chip_total+=(chip_bet*2)
        return 'You have WON this round and have gained '+str(chip_bet*2) + ' chips'+'\n'+ \
                   'Total Chips: '+str(chip_total)

    def lose_bet(self,chip_total,chip_bet):
        chip_total
        return 'You have LOST this round and have lost ' + str(chip_bet) + ' chips' + '\n' + \
               'Total Chips: ' + str(chip_total)

    #Will call function when value of dealer and player hand are equal:
    def push(self,chip_total,chip_bet):
        chip_total+=chip_bet
        return 'PUSH! Your bet has been returned'


#Game Logic:
#Class instantiation:
play_deck=Deck()
cpu_hand=Hand()
player_hand=Hand()
player_chip=Chip()
dealer_hand=Hand()

def intro():
    print('  ---Black Jack---')
    print('Would you like to play?')
    print('   yes           no')
    intro_input=(input())
    # print(intro_input)
    if intro_input.lower()=='yes':
        return True
    elif intro_input.lower()=='no':
        print('Maybe next time then')
        return False
    else:
        while intro_input.lower()!='yes' or intro_input.lower()!='no':
            intro_input = input(" Not a valid input, Please enter yes or no")
            if intro_input.lower() == 'yes':
                return True
            if intro_input.lower() == 'no':
                print('Maybe next time then')
                return False

def hit_card():
    print('Would the player like to hit?')
    print('   yes           no')
    hit_input=(input())
    if hit_input.lower() == 'yes':
        return True
    elif hit_input.lower() == 'no':
        return False
    else:
        while hit_input.lower() != 'yes' or hit_input.lower() != 'no':
            if hit_input.lower() == 'yes':
                return True
            if hit_input.lower() == 'no':
                return False

def game_on():
    player_chip.place_chips()
    play_deck.shuffle()
    true_check=True
    round=0
    #While there is no winner the loop will continue to run:
    while true_check:
        round+=1
        print('Round: '+str(round))
        print('Current Chips: '+ str(player_chip.chip_total))
        #May add a del dealer_hand and player_hand variable HERE OR BOTTOM: Thinking about it

        #Ask player to enter a bet:
        player_chip.place_bet()
        print('Current Chips: '+ str(player_chip.chip_total))

        print('===================================')

        #Dealer deals first card for themselves:
        dealer_hand1=play_deck.deal_card()
        dealer_hand.add_card_dealer(dealer_hand1)
        print('Dealer Hand 1: '+str(dealer_hand1))
        print('-----------------------------------')
        #Dealer deals first card for player:
        player_hand1=play_deck.deal_card()
        player_hand.add_card(player_hand1)
        print('Player Hand 1: '+str(player_hand1))

        print('===================================')

        #Game will ask player if they want to raise the bet:
        player_chip.raise_bet()

        print('===================================')

        #Dealer deals second card for themselves:
        dealer_hand2=play_deck.deal_card()
        dealer_hand.add_card_dealer(dealer_hand2)
        print('Dealer Hand 2: HIDDEN')
        print('-----------------------------------')
        #Dealer deals second card for player:
        player_hand2 = play_deck.deal_card()
        player_hand.add_card(player_hand2)
        print('Player Hand 2: ' + str(player_hand2))

        print('===================================')

        #Display cards for this round:
        print('Cards Dealt: ')
        print('Dealer Hand 1: '+str(dealer_hand1))
        print('Dealer Hand 2: '+str(dealer_hand2))
        print('-----------------------------------')
        print('Player Hand 1: '+str(player_hand1))
        print('Player Hand 2: ' + str(player_hand2))
        print('===================================')

        #Ask player if they want to hit:
        if hit_card():
            player_hand_hit=play_deck.deal_card()
            player_hand.add_card(player_hand_hit)
            print('Player Hand 3: ' + str(player_hand_hit))
            print('===================================')
            if player_hand.p_hand_value>21:
                print(player_chip.lose_bet(player_chip.chip_total,player_chip.chip_bet))
                continue

        #Dealer will deal card if their hand value is greater than or equal to 17:
        if dealer_hand.d_hand_value <17:
            dealer_hand_hit=(play_deck.deal_card())
            dealer_hand.add_card_dealer(dealer_hand_hit)
            print('Dealer Hand 3: '+str(dealer_hand_hit))
            print('===================================')
            if dealer_hand.d_hand_value>21:
                print(player_chip.win_bet(player_chip.chip_total,player_chip.chip_bet))
                continue

        #Check if player is a winner or loser of round:
        if player_hand.p_hand_value<=21 and player_hand.p_hand_value> dealer_hand.d_hand_value:
            print(player_chip.win_bet(player_chip.chip_total, player_chip.chip_bet))
        if player_hand.p_hand_value>21 or player_hand.p_hand_value< dealer_hand.d_hand_value and dealer_hand.d_hand_value<=21:
            print(player_chip.lose_bet(player_chip.chip_total,player_chip.chip_bet))
        if player_hand.p_hand_value == dealer_hand.d_hand_value:
            print(player_chip.push(player_chip.chip_total,player_chip.chip_bet))

        #Resets values for next round:
        dealer_hand.d_hand_value=0
        player_hand.p_hand_value=0

        dealer_hand.d_hand.clear()
        player_hand.p_hand.clear()


        #Will check if player chips is equal or less than 0, If so they lose:
        if player_chip.chip_total<=0:
            print('You are out of chips and can no longer continue')
            true_check=False
            break

#Play again?
def ask_play_again():
    print('Would you like to play again? ')
    print('Would you like to play?')
    print('   yes           no')
    play_again_input = input(input())
    if play_again_input.lower() == 'yes':
        return True
    elif play_again_input.lower() == 'no':
        print('Maybe next time then')
        return False
    else:
        while play_again_input.lower() != 'yes' or play_again_input.lower() != 'no':
            play_again_input = input(" Not a valid input, Please enter yes or no")
            if play_again_input.lower() == 'yes':
                return blackjack()
            if play_again_input.lower() == 'no':
                print('Maybe next time then')
                return 'Thank you for Playing'


def blackjack():
    if intro():
        game_on()
        ask_play_again()


print(blackjack())
# player_hand.add_card(play_deck.deal_card())
# print(player_hand.p_hand[-1].value)
# print(player_hand.p_hand[-1])
#
# player_hand.add_card(play_deck.deal_card())
# print(player_hand.p_hand[-1].value)
# print(player_hand.p_hand[-1])
#
# player_hand.add_card(play_deck.deal_card())
# print(player_hand.p_hand[-1].value)
# print(player_hand.p_hand[-1])

# print(player_hand.p_hand_value)


# print(player_hand.p_hand[0])














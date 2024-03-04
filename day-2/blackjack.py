"""
        BlackJack is a card game where players try to get to the wining number
    21 as possible.
        card values:
            - Kings, Queens and Jacks have 10 value
            - Aces have 1 or 11 value
            - cars 2 to 10 woth their value

    HIT to take a card
    STAND to stop laying the game    
    if there is a tie the bet will be returned back to the players
"""
import random, sys, time

HEARTS = chr(9829)  
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def blackjack():
    Money = 5000
    while True:
        if Money < 0:
            print("You do not have money")
            sys.exit()

        bet = make_bet(Money)
        deck = get_deck()
        dealer = [deck.pop(), deck.pop()]
        player = [deck.pop(), deck.pop()]
        print("Bet: ", bet)
        while True:
            displayHands(dealer, player, True)
            print()
            if getHandValue(player) > 21:
                break

            move = getMove(player, Money - bet)
            if move == 'D':
                additionalBet = make_bet(min(bet, (Money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                player.append(newCard)

                if getHandValue(player) > 21:
                    continue
                if move in ("S", "D"):
                    break

            if getHandValue(player) <= 21:
                while getHandValue(dealer) < 17:
                    print("Dealer Hits ... ")
                    time.sleep(2)
                    dealer.append(deck.pop())
                    displayHands(player, dealer, True)

                    if getHandValue(dealer) > 21:
                        break
                    input("Press enter to continue ...")
                    print("\n\n\n")
        displayHands(player, dealer, True)
        playervalue = getHandValue(player)
        dealervalue = getHandValue(dealer)

        if dealervalue > 21:
                print("you won ${}".format(bet))
                Money += bet 
        elif (playervalue > 21) or (playervalue < dealervalue):
                print("you lost ${}".format(bet))
                Money -= bet
        elif playervalue > dealervalue:
            print("You won {}".format(bet))
            Money += bet
        elif playervalue == dealervalue:
                print("It is a tie")
        input("Press enter to continue")
        print("\n\n")

def make_bet(maxBet):
    while True:
        print(F"How much would you like to bet? 1 - {maxBet} or QUIT") 
        bet = input().upper().strip()

        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 < bet < maxBet:
            return bet

def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(dealer, player, showDealer):
    print()
    if showDealer:
        print("DEALER: ", getHandValue(dealer))
        displayCard(dealer)
    else:
        print("DEALER: ? ? ?")
        displayCard([BACKSIDE] + dealer[1:])

    print("PLAYER: ", getHandValue(player))
    displayCard(player)

def getHandValue(cards):
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("J", "Q", "K"):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value

def displayCard(cards):
    rows = ['', '', '', '','']
    for i, card in enumerate(cards):
        rows[0] += ' ____  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{}  | '.format(rank.ljust(2))
            rows[2] += '| {}  | '.format(suit)
            rows[3] += '|__{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)

def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move 

if __name__ == "__main__":
    blackjack()
# Blackjack
import random

HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)


def play():
    # Create the deck of cards:
    deck = []
    for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        for suit in [HEARTS, DIAMONDS, SPADES, CLUBS]:
            deck.append([rank, suit])
    random.shuffle(deck)

    # Give the dealer and player two cards each:
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    # Handle player actions:
    # Keep looping until player stands or busts.
    while True:  
        displayHands(playerHand, [['??', '?']] + dealerHand[1:])
        print()

        if getHandValue(playerHand) > 21:
            break  # Player has busted.

        # Get the player's move, either 'Y' or 'N':
        print("\nType \"Y\" to get another card, type \"N\" to pass.")
        move = input('Y or N > ').upper()

        if move == 'Y':
            newCard = deck.pop()
            print('You drew a', newCard[0], 'of', newCard[1])
            playerHand.append(newCard)

            if getHandValue(playerHand) > 21:
                continue  # The player has busted.
        elif move == 'N':
            break  # Standing stops the player's turn.

    # Handle the dealer's actions:
    if getHandValue(playerHand) <= 21:
        while getHandValue(dealerHand) < 17:
            print('Dealer hits...')
            dealerHand.append(deck.pop())
            displayHands(playerHand, [['??', '?']] + dealerHand[1:])

            if getHandValue(dealerHand) > 21:
                break  # The dealer has busted.
            input('Press Enter to continue...\n\n')

    # Show the final hands:
    displayHands(playerHand, dealerHand)

    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)

    if dealerValue > 21:
        print('Dealer busts! You win!')
    elif (playerValue > 21) or (playerValue < dealerValue):
        print('You bust. Dealer wins.')
    elif playerValue > dealerValue:
        print('You win!')
    elif playerValue == dealerValue:
        print('It is a tie!')


def displayHands(playerHand, dealerHand):
    print('DEALER:')
    displayCards(dealerHand)
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(allCards):
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in allCards:
        # card is a list like [rank, suit]
        rank = card[0]  
        if rank == 'A':
            # Aces are worth at least 1
            numberOfAces += 1  
        elif rank in ['K', 'Q', 'J']:  
            # Face cards are worth 10.
            value += 10
        elif rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            # Numbered cards are worth their number.
            value += int(rank)  

    # Add the value for the aces:
    # Add 1 per ace.
    value += numberOfAces  

    for i in range(numberOfAces):
        # If another 10 can be added without busting, do so:
        if value + 10 <= 21:
            value += 10
    return value


def displayCards(allCards):
    # The text to display on each row.

    rows = ['', '', '', '', '']  
    for card in allCards:
        rank = card[0]
        suit = card[1]
        rows[0] += ' ___  '  # Print the top line of the card.
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for row in rows:
        print(row)


# Main loop[]:
play()

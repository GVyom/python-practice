import random

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']

while True:
    welcome = input('welcome to blackjack, are you ready for your shuffle?(Y/N): ').lower()

    if welcome == 'n':
        print('We are ready when you are! Just Type Y, and cards will be dealt.')

    elif welcome == 'y':
        print('Shuffling cards')
        break

    else:
        print('Please enter Y or N')

p_cards = random.sample(cards, k=2)
d_cards = random.sample(cards, k=2)


def convert_cards(cards):
    int_cards = []
    for x in cards:
        try:
            int_cards.append(int(x))
        except ValueError:
            if x in ['J', 'Q', 'K']:
                int_cards.append(10)
            elif x == 'A':
                int_cards.append(11)

    # Ace handling
    total = sum(int_cards)

    while total > 21 and 11 in int_cards:
        ace_index = int_cards.index(11)
        int_cards[ace_index] = 1
        total = sum(int_cards)

    return int_cards


current_score = sum(convert_cards(p_cards))
current_d_score = sum(convert_cards(d_cards))

print(f'Your cards are {p_cards} current score: {current_score}')
print(f'dealer got {d_cards[0]} card')


# Initial blackjack checks
if current_score == 21 and current_d_score == 21:
    print('Both got Blackjack! Draw!')

elif current_score == 21:
    print(f'You win! Your cards score is {current_score}')

elif current_d_score == 21:
    print(f'Dealer cards are {d_cards}')
    print('Dealer got Blackjack! You lose!')

else:
    while True:
        ask = input('Hit or stand?: ').lower()
        if ask == 'hit':

            new_card = random.choice(cards)
            p_cards.append(new_card)
            current_score = sum(convert_cards(p_cards))

            print(f'Your Cards are {p_cards} -> New card: {new_card}')
            print(f'Updated score: {current_score}')

            if current_score == 21:
                print(f'You win! Dealer cards were {d_cards}')
                break

            elif current_score > 21:
                print(f'This is a Bust! You lose, your score is {current_score}')
                break

        elif ask == 'stand':
            print(f'Dealers cards are: {d_cards}')
            dealer_sum = sum(convert_cards(d_cards))

            # Dealer keeps drawing until 17+
            while dealer_sum < 17:
                print(f'Dealer sum stands at {dealer_sum}, dealing another card!')
                d_cards.append(random.choice(cards))
                dealer_sum = sum(convert_cards(d_cards))
                print(f'Dealer Cards are {d_cards} -> Dealer Card Sum {dealer_sum}')

            # Final comparison
            if dealer_sum > 21:
                print('Dealer hit a Bust, you win!')

            elif dealer_sum > current_score:
                print(f'You lose, dealer score {dealer_sum} is closer to 21')

            elif current_score > dealer_sum:
                print(f'You win! Your score {current_score} is closer to 21')

            else:
                print('This is a draw!')

            break

        else:
            print('Invalid input. Please type hit or stand.')

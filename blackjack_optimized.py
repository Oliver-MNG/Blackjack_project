import random
def deal_card():
    """This function returns the dealed cards"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """This function returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 20:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_sum, computer_sum):
    if user_sum == computer_sum:
        return "Draw"
    elif computer_sum == 0:
        return "You lose, opponent has Blackjack"
    elif user_sum == 0:
        return "You win, you have Blackjack"
    elif user_sum > 21:
        return "You lose, you went over"
    elif computer_sum > 21:
        return "You win, opponent went over"
    elif user_sum > computer_sum:
        return "You win, your score is higher than opponent's!"
    else:
        return "You lose, opponent score is higher than yours"

user_cards = []
computer_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())



game_end = False
while not game_end:
    user_sum = calculate_score(user_cards)
    computer_sum = calculate_score(computer_cards)
    print(f"User cards: {user_cards} User score: {user_sum}\nComputer cards: [{computer_cards[0]}, *]")
    if user_sum == 0 or computer_sum == 0 or user_sum > 21:
        game_end = True
    else:
        user_should_deal = input("Type 'y' to get another card, or 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            game_end = True


while computer_sum != 0 and computer_sum < 17:
    computer_cards.append(deal_card())
    computer_sum = calculate_score(computer_cards)

print(f"{compare(user_sum,computer_sum)}\nThe scores are: \nUser cards: {user_cards} User score: {user_sum}\nComputer cards: {computer_cards} Computer score:{computer_sum}")




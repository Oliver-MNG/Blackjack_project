# In this project first I am going to finish the task by myself, then look for an optimal version.
import random

#Blackjack

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10]

play = input("Do you want to play Blackjack? 'y' or 'n': ")
user_start = []
computer_start = []
user_start = random.sample(cards,2)
computer_start = random.sample(cards,2)
print(f"{user_start} [{computer_start[1]}, * ]")
add = True
while add == True:
    another_card = input("Another card? 'y' or 'n': ")
    if another_card == 'y':
        user_start.append(random.choice(cards))
    elif another_card == 'n':
        add = False
    print(f"{user_start} [{computer_start[1]}, * ]")
#check
#print(user_start, computer_start)    check
for i in range(0,16):
    if sum(computer_start)<17:
        computer_start.append(random.choice(cards))
sum_user = sum(user_start)
sum_computer = sum(computer_start)
# sum_computer += computer_start[i]
# if sum_computer < 17:
# sum_computer += random.choice()
if sum_user > 21 and sum_computer > 21:
    print("Split")
elif sum_user > 21 and sum_computer < 21:
    print(f"Computer win.\nUser: {sum_user} \nComputer: {sum_computer}")
elif sum_user < 21 and sum_computer > 21:
    print(f"User win.\nUser: {sum_user} \nComputer: {sum_computer}")
elif sum_user == sum_computer:
    print(f"Draw!\nUser: {sum_user} \nComputer: {sum_computer}")
elif sum_user == 21:
    print(f"Blackjack for user\nUser: {sum_user} \nComputer: {sum_computer}")
elif sum_computer == 21:
    print(f"Blackjack for computer\nUser: {sum_user} \nComputer: {sum_computer}")
elif sum_user < 21 and sum_computer < 21:
    if (21 - sum_user) > (21 - sum_computer):
        print(f"Computer win.\nUser: {sum_user} \nComputer: {sum_computer}")
    else:
        print(f"User win.\nUser: {sum_user} \nComputer: {sum_computer}")

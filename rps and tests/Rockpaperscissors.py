import random


def get_choices():
    player_choice = input ("Enter a choice (rock, paper , scissors :)")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice , "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Tie"
    elif player == "rock" :
        if computer == "scissors":
         return "Rock beats up scissors,You win!"
        else:
         return "Paper covers rock, You lose!"
    elif player == "paper" :
        if computer == "scissors":
         return "scissors cut paper,You lose!"
        else:
         return "paper covers rock, You win!"
    elif player == "scissors" :
        if computer == "paper":
         return "scissors cut paper,You win!"
        else:
         return "rock beats down scissors, You lose!"
        
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
 
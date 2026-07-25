import random

print("===== Rock Paper Scissors Game =====")

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper or scissors: ").lower()

computer = random.choice(choices)

print("Your Choice:", user)
print("Computer Choice:", computer)

if user not in choices:
    print("Invalid Choice!")

elif user == computer:
    print("It's a Tie!")

elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("🎉 You Win!")

else:
    print("😢 Computer Wins!")

import random
options=("rock", "paper", "seasor")
computer=random.choice(options)
player=input("Enter your choice (rock, paper, seasor) : ")
print(f"you chose {player}")
print(f"computer chose {computer}")
if(computer==player):
    print("Its a tie!")
while player not in options:
    print("chose correct options ") 
if(computer=="rock" and player=="paper"):
    print("you win!")
elif(computer=="rock" and player=="seasor"):
    print("you lose!") 
elif(computer=="paper" and player=="rock"):
    print("you lose!")
elif(computer=="paper" and player=="seasor"):
    print("you win!")
elif(computer=="seasor" and player=="paper"):
    print("you lose!")
elif(computer=="seasor" and player=="rock"):
    print("you win!")
else:
    None

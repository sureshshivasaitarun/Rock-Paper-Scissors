#Rock Paper Scissors Game
import random
print("Rock Paper Scissors Game")
print("Winning Rules ") 
print("1st Rule (Rock defeats Scissors.)")
print("2nd Rule (Scissors defeats Paper.)")
print("3rd Rule (Paper defeats Rock.)")
print("4th Rule (If both players choose the same option, the round ends in a draw.)")
Rock=1
Paper=2
Scissors=3
Game_Items=[1,2,3]
Play_Again="yes"
user_count=0
computer_count=0
while Play_Again == "yes":
    User_Choice=int(input("Enter your choice:\n1. Rock \n2. Paper \n3. Scissors"))
    while User_Choice not in Game_Items:
        print("choose the correct choice and enter correct value")
        User_Choice=int(input("Enter your choice:\n1. Rock \n2. Paper \n3. Scissors"))
    else:
        print("You Choose Option ", User_Choice)
    Computer_Choice=random.randint(1,3)
    print("Computer Choose ",Computer_Choice)
    if User_Choice == Computer_Choice:
        print("Draw")
    elif User_Choice == Rock and Computer_Choice == Scissors:
        print("You Win")
        user_count+=1
    elif User_Choice == Scissors and Computer_Choice == Paper:
        print("You Win")
        user_count+=1
    elif User_Choice == Paper and Computer_Choice == Rock:
        print("You Win")
        user_count+=1
    else:
        print("Computer Win's")
        computer_count+=1
    Play_Again=input("Play again yes/no")
print("Your Score is ",user_count)
print("Computer Score is ",computer_count)
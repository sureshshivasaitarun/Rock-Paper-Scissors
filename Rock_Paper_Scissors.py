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
mode=int(input("option 1 for Best of 3\n option 2 for Best of 5"))
def play_mode(mode):
    if mode == 1:
        return 3
    elif mode == 2:
        return 5
    else:
        mode=int(input("Please enter option 1 or 2"))
        while not(mode ==1 or mode ==2):
            mode=int(input("Please enter option 1 or 2"))
rounds=play_mode(mode)
def play_rounds(rounds):
    if rounds == 3 or rounds == 5:
        global user_count
        global computer_count
        for i in range(rounds):
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
                if computer_count <= rounds: 
                    computer_count+=1
            if i <= rounds-2:
                Play_Again=input("Play again yes/no")
                if Play_Again == "y":
                    continue
                elif Play_Again == "n":
                    break
    # else:
    #     print("Please choose exact no of rounds as mentioned above")
    #     rounds=int(input("Choose Game Mode:\n 1. Best of 3 \n 2. Best of 5"))
    #     while not(rounds==3 or rounds==5):
    #         print("Please choose exact no of rounds as mentioned above")
    #         rounds=int(input("Choose Game Mode:\n 1. Best of 3 \n 2. Best of 5"))   
    #         play_rounds(rounds)
final_result=play_rounds(rounds)
def result(final_result):
    print("FINAL RESULT IS")
    print("Your Score ",user_count)
    print("Computer Score ",computer_count)
    if user_count == computer_count:
        print("DRAW MATCH")
    elif user_count < computer_count:
        print("COMPUTER WON")
    elif user_count > computer_count:
        print("YOU WON")
result(final_result)
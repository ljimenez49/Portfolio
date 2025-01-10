#liz Jimenez
#period 3
#1/6/25

#ROCK PAPER SCISSORS

#Init
import random


#functions
def RPS():
    while True: #uinfinite loop
        print("Welcome to Rock, Paper, Siccors")
        #Player's choice
        print("Please select one of the three options: Rock, Paper, Scissor")
        player = input("Selection: ")



        #Computer's Choice
        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("Computer chose rock")

        elif computer == 2:
            computer = "paper"
            print("Computer chose paper")

        else:
            computer = "scissor"
            print("Computer chose scissor")

        #Determine the outcome
        # = gets the value of
        # == is equal to

        if computer == "rock" and player == "rock":
            print("Computer and player tie!")

        elif computer == "rock" and player == "scissor":
            print("Computer wins this round!")

        elif computer == "rock" and player == "paper":
            print("Player wins this round!")


        elif computer == "paper" and player == "paper":
            print("Computer and player tie!")

        elif computer == "paper" and player == "rock":
            print("Computer wins this round!")

        elif computer == "paper" and player == "scissor":
            print("Player wins this round!")


        elif computer == "scissor" and player == "scissor":
            print("Computer and player tie!")

        elif computer == "scissor" and player == "paper":
            print("Computer wins this round!")

        else:
            computer == "scissor" and player == "rock"
            print("Player wins this round!")


        playagain = input("would you like to play again?")
        if playagain == "Yes":
            print("Restarting...")
        elif playagain == "No":
            break










#Main


RPS()

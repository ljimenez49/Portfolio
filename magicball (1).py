#Liz Jimenez
#Period



#INIT
responses = ["Yes", "Of Course!", "Yeah Sure", "Definitely", "No", "definitely not", "nah", "Gosh No", "Unsure", "Maybe", "Not really", "unknown"]
import random
import time

#Functions
def ballGame():
    print("Welcome to the Magic 8 Ball Game!")
    while True:
        answer = input("Please ask the Magic 8 Ball a yes-or-no question!")
        while answer.endswith("?") != True:
                print("Your answer must end with a question mark!")
                answer = input("Please ask the Magic 8 Ball a yes-or-no question!")

        print("Shake...")
        time.sleep(2)
        print("Shake...")
        time.sleep(2)
        print("Shake...")
        time.sleep(2)
        print(random.choice(responses))

        print("Do you wish to continue?")
        selection = input("(n or y) Selection: ")
        if selection == "y":
            print("Please ask the Magic 8 Ball Another yes-or-no question!")
            answer = input("Please ask the Magic 8 Ball a yes-or-no question!")
            print("Shake...")
            time.sleep(2)
            print("Shake...")
            time.sleep(2)
            print("Shake...")
            time.sleep(2)
            print(random.choice(responses))

        else:
            print("Thank you for playing The Magic 8 Ball, see you next time!")
            break




#main
ballGame()

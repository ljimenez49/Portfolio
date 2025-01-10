#Liz Jimenez
#Period 2
#11/19/24

#SImple Calcuclator

#Init
#Function

#Adds num1 and num2 and prints the result
#def add(num1,num2):
    #result = num1 + num2
    #print(result)


def SimpleCalc():
    print("Welcome Preschoolers to Simple Calculator")
    while True:
        print("Enter an operation: ")

        print ("""1. Addition
    2. Subtraction
    3. Division
    4. Multiplication
    5. Quit""")

        operation = input("(1-5) Operation: ")
        if operation == "1": #True
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            print(int1 + int2)

        if operation == "2": #True
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            print(int1 - int2)

        if operation == "3": #True
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            print(int1 / int2)

        if operation == "4": #True
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            print(int1 * int2)

        if operation == "5":
            print("Thank you for visiting Simple Calculator, see you next time!")
            break





#Main
SimpleCalc()

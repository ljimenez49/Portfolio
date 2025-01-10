#Liz Jimenez
#Period 3
#10/24/22

def bottles():
    milk = 99
    for i in range(99):
        milk = milk - 1
        if milk == 1:
            print(str(milk) +" bottle of milk on the wall, take one down pass it around")
        elif milk > 0:
            print(str(milk) +" bottles of milk on the wall")
            print(str(milk) +" bottles of milk")
            print("take one down pass it around")

        if milk == 0:
            print("No more bottles of milk on the wall, Boo Hoo!")


#Main
bottles()

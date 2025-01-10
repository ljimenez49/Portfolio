#Liz Jimenez
#Period 3
#10/17/24


print("Welcome to, whats color!")
print("Answer the questions to find out your color")
ans = input("candy (c) or chocolate (ch) ?")
if ans == "c":
    ans = input("sweet (se) or sour (so) ?")
    if ans == "se":
        ans = input("lollipop (lo) or cotton candy (cc) ?")
        if ans == "lo":
            print("Your color is pink")
        else:
            print("Your color is blue")
    if ans == "c":
        ans = input("sour patch kids (SPK) or skittles (sk) ?")
        if ans == "SPK":
            print("Your color is green")
        else:
            print("Your color is rainbow")
if ans == "ch":
    ans = input("milk (mi) or dark (d) ?")
    if ans == "mi":
        ans = input("nuts (n) or caramel (ca) ?")
        if ans == "n":
            print("Your color is white")
        else:
            print("Your color is ginger")
    if ans == "d":
        ans = input("salty (s) or bitter (bi) ?")
        if ans == "s":
            print("Your color is brown")
        else:
            print("Your color is black")


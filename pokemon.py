#Liz Jimenez
#11/19/24

#SQUIRTLE Pokemon evolution




#INIT
pokemon_level = 0 #Global
pokemon_name = "Squirtle"
day = 1
#FUNCTIONS

def train():
        print("Your Pokemon did 20 situps today, Squirtle is now level " + str(pokemon_level + 1))
def display_info():
        print(str(pokemon_name) + " is now resting!  " + str(pokemon_name) + " is currentley level " + str(pokemon_level))
def Gym_Battle():
        print("your " + str(pokemon_name) + " won a gym battle he is now level " + str(pokemon_level + 2))
def evolution():
        global pokemon_level
        global pokemon_name
        if pokemon_level < 5:
                pokemon_name = "Squirtle"
        if pokemon_level > 5:
                pokemon_name = "Wartle"
        if pokemon_level >= 10:
                pokemon_name = "Blastoise"



#Main
print("Welcome to Pokemon Evolution, Day: " + str(day))
while True:
        day = day + 1
        print("it is day " + str(day))
        print("Select an activity for the day")
        print("""1. Train
2. Gym Battle
3. Rest (Display info)
4. Quit""")
        activity = int(input("Avctivity: "))
        if activity == 1: #True
                train()
                pokemon_level = pokemon_level + 1
                evolution()
        if activity == 2:
                Gym_Battle()
                pokemon_level = pokemon_level + 2
                evolution()
        if activity == 3:
                display_info()
                evolution()
        if activity == 4:
                print("Thank you for playing, see you next time!")
                break




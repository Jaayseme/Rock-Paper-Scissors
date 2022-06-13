# [Rock-Paper-Scissors] Zuri Task
#Task Title: Creating and Using [Local] Python Packages
"""Game Rules
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
List
"R" for "rock", 
"P" for "paper", 
"S" for "scissors".
"""
#importing a random Module
import random
#Rules of the Game
print("GAME RULES: \n"+"Rock beats Scissors\n" +"Paper beats Rock\n" +"Scissors beats Paper \n" +"R for Rock \n" +"P for Paper \n" +"S for Scissors")
#A list to store all possible options:
Choice=['R', 'P', 'S']
not_Choice= None
CPU=random.choice(['R', 'P', 'S'])
#Player's Input
Player=input("Select an Option:rock, paper or scissors? ")
#Print Player VS CPU choice(moves) format
# looping until user enter invalid input
#CPU format
for i in CPU:
        if CPU==i[0]:
            CPU_format="Rock"
        elif CPU==i[1]:
            CPU_format="Paper"
        else:
            CPU_format="Scissors"
        #Player format
        if Player=='R':
            Player_format="Rock"
        elif Player=='S':
            Player_format="Scissors"
        elif Player=='P':
            Player_format="Paper"
        #Print both players move
        print(f"Player({Player_format}):CPU({CPU_format})")
        if Player_format == CPU_format:
            print(f"It's a Tie! computer and player picked  {Player_format}")
        elif Player_format == "Rock":
            if CPU_format =="Scissors":
                print("Rock beats scissors.. Player wins!!")
            else:
                print("CPU Wins!! paper covers rock")
        elif Player_format == "Paper":
            if CPU_format == "Rock":
                print("Paper beats Rock!")
            else:
                print("CPU Wins!! scissors cut paper")
        elif Player_format == "Scissors":
            if CPU_format == "Paper":
                print("Scissors beats Paper!!! Scissors cut paper")
        else:
            print("CPU Wins.. Rock beats scissors")

   



   


       
       
        
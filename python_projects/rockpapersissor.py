import random
object = ["Rock", "Paper", "Scissor"]
index = random.randint(0, 2)
computersign = object[index]
playersign = input("Rock Paper Scissor Shoot:").strip(" ").capitalize()
computerpoints = 0
playerpoints = 0
while (playersign != "Exit"):

    if (playersign not in object):
        if (playersign != ""):
            print("Error, Enter correct spelling")
        else:
            print("Nothing Entered")
        playersign = input(
            "Rock Paper Scissor Shoot (Exit to see the final score):").strip().capitalize()
        continue
    if (playersign in object):
        print(
            f"You chose {playersign} and the computer chose {computersign}")
        if (playersign == computersign):
            print("The game is tie")
        elif (playersign in object):
            if ((playersign == "Rock" and computersign == "Paper") or (playersign == "Paper" and computersign == "Scissor") or (playersign == "Scissor" and computersign == "Rock")):
                print("The computer has won")
                computerpoints += 1
            else:
                print("You have won!!!")
                playerpoints += 1

    playersign = input(
        "Rock Paper Scissor Shoot(Exit to see the final score):").strip().capitalize()
    index = random.randint(0, 2)
    computersign = object[index]
print("Your points :", playerpoints, "\nComputer points :", computerpoints)
if (playerpoints == computerpoints):
    print("The game is a tie")
else:
    if (playerpoints > computerpoints):
        print("You won the game!!!")
    else:
        print("Computer won the game")

#*************************************
#FILE NAME: Dicegames_oo.py
#PURPOSE: Program-1 for CS-524 Programming Languages-01.
#AUTHOR: Vani Krishna Raghu Vamsha Kokkula (vk0018).
#DATE: APRIL 8 2017
#VERSION: Python 3.6.1
#BRIEF DESCRIPTION: This Program is written based on Object Oriented Approach.
# Pig Game: The goal of Fifty is to be the first player to reach 50 points. You get points by rolling doubles.
# Fifty Game: The goal of Pig is to be the first player to reach 100 points. You get points by rolling
#             a single die multiple times and adding the value on each roll of the die to your current score.
#
#This Program is entirely my own work.
#*************************************


import random

print("----WELCOME TO CS-524 PROGRAM 1 Object Oriented Approach----")
print("WHICH GAME DO YOU WANT TO PLAY")
choice = float(input("PRESS 1 TO PLAY FIFTY or PRESS 2 TO PLAY PIG"))

if choice == 1:
    print("\n\n---WELCOME TO FIFTY GAME---")
    print("Goal: The goal of Fifty is to be the first player to reach 50 points. You get points by rolling doubles.\n")
    print("Play: A turn consists of a player rolling a pair of dice (with the goal of rolling doubles), \n"
          "and scoring the roll as described below. Play continues with each player taking one roll per turn. The\n"
          "first player to score 50 or more points is declared the winner.\n")
    print("Scoring: All doubles except 3s and 6s score 5 points. Double 6s are worth 25 points. Double 3s\n"
          "wipe out the player’s entire score, and the player must start again at 0. Non-double rolls are 0 points.\n")
    score = 0
    score1 = 0           #Initializing score variables here.
    score2 = 0
    dice1 = 0           #Initializing dice variables here.
    dice2 = 0

    class Roll():       #This is a seperate class for rolling dice and the functions in it are rolldice().

        def rolldice(self):     #In this function we roll the dice and decide what scores to return for different cases.
            global score        # Using global variables for score
            global dice1
            global dice2        # Using global variables for dice
            if 7 > 6:           #using an if statement which always should become true, to roll the dice.
                dice1 = random.randint(1, 6)        #importing random number and calling the random number--
                print("Dice1 = ", dice1)            # --function within range 1 and 6 included.
                dice2 = random.randint(1, 6)
                print("Dice2 = ", dice2)

                if dice1 == dice2:      # if both the dice are same then go into the if statement.
                    if dice1 == 3:      # if both the dice are 3 then return score=0.
                        score = 0

                    if dice1 == 6:      # if both the dice are 6 then return score=25
                        score = 25
                    elif dice1 == 1 or dice1 == 2 or dice1 == 4 or dice1 == 5:
                        score = 5           # for both same dices except 3 & 6, score=5.
                else:
                    score = 0           # for all other cases, i.e different dices, score=0.

                return score            # returning score.


    class Turns(Roll):          #This is seperate class for giving turns to players
                                #and the functions in it are rolldice().
        def turn(self):         #In this function we call the roll function and assign score to different players.
            global score
            global score1
            global score2           # Using global variables for score
            global dice1
            global dice2            # Using global variables for dice

            while 7 > 6:    # Using While statement which always should become true,
                                # to gives players chance to roll the dice.
                player1_chance = input("IS IT YOUR TURN PLAYER1, Press 'y' to continue")
                if player1_chance == "y":   # If we press "Y" we give player-1 chance to roll the dice and
                                            #  calculate his score.
                    player1 = Roll.rolldice(self);  #Here we call a function from different class,
                                                    #So we call using object.
                                                    # Calling rolldice function for player-1.
                    if dice1 == dice2:
                        if dice1 == 3:              # If 3 comes in both the dices we reset player-1 score to 0.
                            score1 = 0

                        if dice1 != 3:
                            score1 += score          # Otherwise we add to the cumulative score.
                    print("player 1 score = ", score1)
                    if score1 >= 50:                # if player-1 reaches 50 or more, he WINS!!
                        print("PLAYER-1 YOU WIN")
                        break                       # we break the loop if Player-1 Wins

                player2_chance = input("IS IT YOUR TURN PLAYER2, Press 'y' to continue")
                if player2_chance == "y":
                    player2 = Roll.rolldice(self);      #Here we call a function from different class,
                                                        # So we call using object.
                                                        # Calling rolldice function for player-2.
                    if dice1 == dice2:
                        if dice1 == 3:              # If 3 comes in both the dices we reset player-1 score to 0.
                            score2 = 0
                            print("player score is zero")
                        if dice1 != 3:
                            score2 += score         # Otherwise we add to the cumulative score.
                    print("player 2 score = ", score2)
                    if score2 >= 50:                # if plater-1 reaches 50 or more, he WINS!!
                        print("PLAYER-2 YOU WIN")
                        break                   # we break the loop if Player-1 Wins.

            return

    x = Turns()         #Here we create an object for Turns() class.
    x.turn()            #Here we use the object to call the turn() function.

else:

    print("\n\n---WELCOME TO PIG GAME---")
    print("Goal: The goal of Pig is to be the first player to reach 100 points. You get points by rolling a \n"
          "single die multiple times and adding the value on each roll of the die to your current score.\n")
    print("Play: The first player rolls the die as many times as they want. The value of each throw is added\n "
          "onto the score until the player decides to end his turn and passes the die to the next player. Play\n"
          "continues until one player reaches 100.\n")
    print("Scoring: The value of each throw is added to the current player’s score. If the player rolls a 1, the\n"
          "player’s score goes back to 0, and their turn ends.\n")
    score = 0
    player_score = 0        #Initializing score and player_score variables here.

    class RollPig():        #This is a seperate class for rolling dice and the functions in it are roll().
        def roll(self):     #This function is used to roll the die, and return the player's score
            global score        # Using global variable for score
            global player_score     # Using global variables for player_score

            dice_rolling = input("DO YOU WANT TO ROLL THE DICE?, press 'y' to continue.")
            dice_rolling = "y"  #If we press "Y" we roll the dice and calculate the player_score

            if dice_rolling == "y":
                dice = random.randint(1, 6)     #importing random number and calling the random number--
                print("dice = ", dice)      # --function within range 1 and 6 included.

                if dice != 1:           # If  the rolled die is not 1, then score is equal to the dice number.
                    player_score = dice

                elif dice == 1:         # If the rolled die is 1, then score is zero.
                    player_score = 0
            return player_score             # Return the player's score.

    class TurnsPig(RollPig):        #This is seperate class for giving turns to players
        def player1_turn(self):     #This function allows the user to play as player1, and returns player1_score

            global score            #Using global varible for score.
            player1_score = 0       #player1_score is initialized.
            play1 = input("PLAYER-1 GAME STARTS, press 'y' to continue")
            play1 = "y"
            score = RollPig.roll(self);     #Here we call a function from different class,
                                            # So we call using object.
                                            # Calling rollPig function for player-1.
            if score == 0:              #If score is zero on the first turn then player loses and other player wins.
                print("YOU LOSE!!!\n Player-2 Wins!!!")
                return "true"
            else:
                player1_score = score           #else, the score of the player is the same as die.
                print("player1_score = ", player1_score)

            while play1 == "1":             #If the player1 game is going on then it enters the while loop.

                score = RollPig.roll(self);     #Here we call a function from different class,
                                                # So we call using object.
                                                # Calling rollPig function for player-2.
                player1_score += score          # Here we add the player1's score cumulatively.
                print("player1 score = ", player1_score)
                if score == 0:                  #If the score of the player1 is zero---
                    print("YOUR CHANCE IS ENDED")   #---other than first chance then the chance is ended.
                    break                           #If your chance is ended then the while loop will break.

                elif player1_score >= 100:          #If the score reaches 100 or greater than 100 then the player wins.
                    print("PLAYER-1 YOU WIN")
                    return "true"               #If player1 wins it returns "true".
            return player1_score

        def player2_turn(self):         #This function allows the user to play as player2, and returns player2_score

            global score                #Using global varible for score.
            player2_score = 0           #player2_score is initialized.

            play2 = input("PLAYER-2 GAME STARTS, press 'y' to continue")
            play2 = "2"
            score = RollPig.roll(self);         #Here we call a function from different class,
                                                # So we call using object.
                                                # Calling rollPig function for player-1.
            if score == 0:                 #If score is zero on the first turn then player loses and other player wins.
                print("YOU LOSE!!!")
                return "true"
            else:
                player2_score = score            #else, the score of the player is the same as die.
                print("player2_score = ", player2_score)

            while play2 == "y":              #If the player2 game is going on then it enters the while loop.
                score = RollPig.roll(self);         #Here we call a function from different class,
                                                # So we call using object.
                                                # Calling rollPig function for player-2.
                player2_score += score              # Here we add the player2's score cumulatively.
                print("player2 score = ", player2_score)
                if score == 0:                  #If the score of the player2 is zero---
                    print("YOUR CHANCE IS ENDED")           #---other than first chance then the chance is ended.
                    break                           #If your chance is ended then the while loop will break.

                elif player2_score >= 100:           #If the score reaches 100 or greater than 100 then the player wins.
                    print("PLAYER-2 YOU WIN")
                    return "true"                   #If player2 wins it returns "true".
            return player2_score

        def game(self):                             #This function will call the player1_turn and player2_turn,
                                      #  they will be called alternatively so that they get chance one after the other.
            player1 = TurnsPig.player1_turn(self);          #Here we call a function from different class,
                                                # So we call using object.
                                                # Calling player1_turn function for player-1.
            while 7 > 6:                        #Here we use while loop which always becomes true,
                                                # so that each player gets chance alternatively.

                if player1 == "true":          #If player1_turn returns true then it has won then the loop will break.
                    break
                else:
                    player2 = TurnsPig.player2_turn(self);
                if player2 == "true":           #If player2_turn returns true then it has won then the loop will break.
                    break
                else:
                    player1 = TurnsPig.player1_turn(self);      #Like this the loop will continue,
                                        #until one of the player wins and the loop breaks.


    x = TurnsPig()           #Here we create an object for TurnsPig() class.
    x.game();               #Here we use the object to call the game() function.

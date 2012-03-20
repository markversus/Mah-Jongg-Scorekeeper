#-------------------------------------------------------------------------------
# Name:        MahjonggScorer
# Version:     0.0
# Purpose:     This module is an payment calculator for Mah Jongg hands. It is
#              designed to be a Python learning tool for me and should get
#              incrementally more complex as I (hopefully) improve.
#
# Author:      Mark Johnson
#
# Created:     23/09/2011
# Copyright:   (c) Mark Johnson 2011
# Licence:     Apache License 2.0 http://www.apache.org/licenses/
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Define Player Class
class Player():
    def __init__(self, name, starting_chips):
        self.name = name
        self.total_score = starting_chips
        self.hand_score = 0
        self.is_hand_winner = False

# Start the game
print("Welcome to the MarkVersus Mah Jongg Scorekeeper")
starting_chips = int(input("Please enter the initial chip balance: "))
running = True

# Instantiate the four players
player1 = Player(input("Player 1 Name:"), starting_chips)
player2 = Player(input("Player 2 Name:"), starting_chips)
player3 = Player(input("Player 3 Name:"), starting_chips)
player4 = Player(input("Player 4 Name:"), starting_chips)
playerlist = [player1, player2, player3, player4]

# Collecting the hand scores
sorted_pl = []
temp_list = []

while running == True:
    winner = input("Who won this hand {} {} {} or {}?".format(player1.name,
                                                              player2.name,
                                                              player3.name,
                                                              player4.name,))
    print("Please enter the scores:")
    for player in playerlist:
        player.hand_score = int(input(player.name))
        if player.name == winner:
            player.is_hand_winner = True
            winning_score = player.hand_score
            sorted_pl.append(player)
        else:
            temp_list.append(player)
            temp_list.sort(key=lambda x: x.hand_score, reverse=True)
    sorted_pl.extend(temp_list)
    print("{} won this hand with a winning score of {}".format(winner,
                                                               winning_score,))

    # The transactions.
    # Works but is ugly as hell. Needs review to tidy it up both programatically
    # and in syntax.
    x = (sorted_pl[0].hand_score - sorted_pl[3].hand_score)*2
    if x < 0:
        x = 0
    else:
        pass
    sorted_pl[3].total_score -= x
    sorted_pl[0].total_score += x

    y = (sorted_pl[0].hand_score - sorted_pl[2].hand_score)*2
    if y < 0:
        y = 0
    else:
        pass
    sorted_pl[2].total_score -= y
    sorted_pl[0].total_score += y
    z = (sorted_pl[0].hand_score - sorted_pl[1].hand_score)*2
    if z < 0:
        z = 0
    else:
        pass
    sorted_pl[1].total_score -= z
    sorted_pl[0].total_score += z

    sorted_pl[3].total_score -= (sorted_pl[2].hand_score -
                                         sorted_pl[3].hand_score)
    sorted_pl[2].total_score += (sorted_pl[2].hand_score -
                                         sorted_pl[3].hand_score)
    sorted_pl[3].total_score -= (sorted_pl[1].hand_score -
                                         sorted_pl[3].hand_score)
    sorted_pl[1].total_score += (sorted_pl[1].hand_score -
                                         sorted_pl[3].hand_score)
    sorted_pl[2].total_score -= (sorted_pl[1].hand_score -
                                         sorted_pl[2].hand_score)
    sorted_pl[1].total_score += (sorted_pl[1].hand_score -
                                         sorted_pl[2].hand_score)

    #Display the scores
    print("The current scores are:")
    for player in playerlist:
        print(player.name+" : "+str(player.total_score))

    play_again = input("Play another hand? (y/n)")

    # End the game
    if play_again == "n":
        print("The final scores are:")
        for player in playerlist:
            print(player.name+" : "+str(player.total_score))
        running = False
    else:
        pass


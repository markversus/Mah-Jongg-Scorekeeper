#-------------------------------------------------------------------------------
# Name:        MahjonggScorer
# Version:     0.1
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
#!/usr/bin/python3.2

# Define Game Class
class Game():
    def __init__(self):
        self.start_game()
        self.run_game()

    def start_game(self):
        print("Welcome to the MarkVersus Mah Jongg Scorekeeper")
        self.starting_chips = int(input("Please enter the initial chip balance: "))
        self.running = True
        # Instantiate the four players
        self.player1 = Player(input("Player 1 Name:"), self.starting_chips)
        self.player2 = Player(input("Player 2 Name:"), self.starting_chips)
        self.player3 = Player(input("Player 3 Name:"), self.starting_chips)
        self.player4 = Player(input("Player 4 Name:"), self.starting_chips)
        self.playerlist = [self.player1, self.player2, self.player3, self.player4]

    def run_game(self):
        # Collecting the hand scores
        self.sorted_pl = []
        self.temp_list = []

        while self.running == True:
            self.winner = input("Who won this hand {} {} {} or {}?".format(self.player1.name,
                                                                      self.player2.name,
                                                                      self.player3.name,
                                                                      self.player4.name,))
            print("Please enter the scores:")
            for self.player in self.playerlist:
                self.player.hand_score = int(input(self.player.name))
                if self.player.name == self.winner:
                    self.player.is_hand_winner = True
                    self.winning_score = self.player.hand_score
                    self.sorted_pl.append(self.player)
                else:
                    self.temp_list.append(self.player)
                    self.temp_list.sort(key=lambda x: x.hand_score, reverse=True)
            self.sorted_pl.extend(self.temp_list)
            print("{} won this hand with a winning score of {}".format(self.winner,
                                                                       self.winning_score,))

            # The transactions.
            # Works but is ugly as hell. Needs review to tidy it up both programatically
            # and in syntax.
            x = (self.sorted_pl[0].hand_score - self.sorted_pl[3].hand_score)*2
            if x < 0:
                x = 0
            else:
                pass
            self.sorted_pl[3].total_score -= x
            self.sorted_pl[0].total_score += x

            y = (self.sorted_pl[0].hand_score - self.sorted_pl[2].hand_score)*2
            if y < 0:
                y = 0
            else:
                pass
            self.sorted_pl[2].total_score -= y
            self.sorted_pl[0].total_score += y
            z = (self.sorted_pl[0].hand_score - self.sorted_pl[1].hand_score)*2
            if z < 0:
                z = 0
            else:
                pass
            self.sorted_pl[1].total_score -= z
            self.sorted_pl[0].total_score += z

            self.sorted_pl[3].total_score -= (self.sorted_pl[2].hand_score -
                                                 self.sorted_pl[3].hand_score)
            self.sorted_pl[2].total_score += (self.sorted_pl[2].hand_score -
                                                 self.sorted_pl[3].hand_score)
            self.sorted_pl[3].total_score -= (self.sorted_pl[1].hand_score -
                                                 self.sorted_pl[3].hand_score)
            self.sorted_pl[1].total_score += (self.sorted_pl[1].hand_score -
                                                 self.sorted_pl[3].hand_score)
            self.sorted_pl[2].total_score -= (self.sorted_pl[1].hand_score -
                                                 self.sorted_pl[2].hand_score)
            self.sorted_pl[1].total_score += (self.sorted_pl[1].hand_score -
                                                 self.sorted_pl[2].hand_score)

            #Display the scores
            print("The current scores are:")
            for self.player in self.playerlist:
                print(self.player.name+" : "+str(self.player.total_score))

            self.play_again = input("Play another hand? (y/n)")

            # End the game
            if self.play_again == "n":
                print("The final scores are:")
                for self.player in self.playerlist:
                    print(self.player.name+" : "+str(self.player.total_score))
                self.running = False
            else:
                pass

# Define Player Class
class Player():
    def __init__(self, name, starting_chips):
        self.name = name
        self.total_score = starting_chips
        self.hand_score = 0
        self.is_hand_winner = False

def main():
    game = Game()

if __name__ == '__main__':
    main()

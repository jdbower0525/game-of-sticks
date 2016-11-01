class UserInteraction:
    def game_start(self):
        self.players = input("Would you like to play against a friend or the computer? ")
        return self.players
    def stick_start(self):
        self.stick_start = input("How many sticks between 10 and 100 would you like to start with? ")
        return self.stick_start

class GamePlay:
    def __init__(self, stick_count=0, players=0, turn_count = 0):
        print("The player to pick up the last stick is the loser")
        self.players = UserInteraction.game_start(self)
        self.stick_count = UserInteraction.stick_start(self)
        print(self.players)
        print(self.stick_count)

    def display(self, stick_count, players, turn_count):
        turn_count = 2
        player = 'Player 1'
        print("There are {} sticks remaining. ".format(self.stick_count))
        print("It is {}'s turn. ".format(self.players))

    def turn(self, stick_count, players, turn_count):
        GamePlay.display


def main():
    game1 = GamePlay()


main()
#
# class game_status:
#     def __init__(self, stick_count=20, players=2, turn_count=0):
#         self.stick_count = stick_count
#         self.players = players
#         self.turn_count = turn_count
#         #stick_count = int(input("How many sticks would you like to start with? "))
#
#     def display(self, stick_count, players, turn_count):
#         turn_count = 2
#         player = 'Player 1'
#         print("The player to pick up the last stick is the loser")
#         print("There are {} sticks remaining. ".format(self.stick_count))
#         print("It is {}'s turn. ".format(self.players))
#
#     def turn(self, stick_count):
#         game_status.display()
#
# def main():
#     game_status.turn()
#
# main()






#
# def game_start():
#      game_mode = input("Would you like to play against the computer or a friend? ")
#      if game_mode == "friend":
#          return game_mode
#
# def number_of_sticks():
#     stick_number = input("How many sticks (between 10 and 100) would you like to start with? ")
#     return int(stick_number)
#
# def friend_mode(stick_number):
#     count = 2
#     player = 'Player 1'
#     print("The player to pick up the last stick is the loser")
#     while stick_number >1:
#         count += 1
#         if count % 2 == 1:
#             player = "Player 1"
#         else:
#             player = "Player 2"
#         print("There are {} sticks on the board.".format(stick_number))
#         remove_sticks = int(input("{}: How many sticks would you like to take off the board? ".format(player)))
#         stick_number = stick_number - remove_sticks
#         if stick_number == 1:
#             print ("GAME OVER!!!")
#             print ("{} is the winner".format(player))
#
# def main():
#     if game_start() == "friend":
#         stick_number = number_of_sticks()
#         friend_mode(stick_number)
#
# if __name__ == '__main__':
#     main()

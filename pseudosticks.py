"""
Actors:
    Player 1 (chooses to play against AI or another player)
    Player 2 (replicates player 1 actions, another human user)
    AI (interacts with program when user selects AI opponent)

Program:
    Program include 3 classes and a main() function.

3 Classes:
    UserInteraction()
    GamePlay()
    AI()

UserInteraction()
    game_start(self):
        ("Would you like to play against a friend or against the computer? ")
        checks for invalid input
        returns (friend/computer)

    stick_count(self):
        ("How many sticks would you like to start with? ")
        checks for stick_count within range 10-100
        checks for invalid input
        returns (stick_count) (between 10-100)

    stick_remove(self):
        ("How many sticks (1-3) would you like to remove from pile? ")
        checks for stick_remove > stick_count
        checks for stick_remove being between 1-3
        returns (stick_remove)

    game_replay(self)
        ("Would you like to play again? ")
        checks for invalid input
        returns Yes/No

GamePlay()
    __init__(self, stick_count = 0, player=0)
    game_start(self, player)
    (calls UserInteraction prompt for game_start)
    stick_count(self, stick_count)
    (calls UserInteraction prompt for stick_count)
    turn_count:
        turn = 0
        each turn will increase turn_count by 1
    game_display(self, stick_count, turn_count, players)
    (prints at the beginning of each turn, necessary information)
        stick_count
        Player_turn (based on turn_count % 2)
    game_turn(self, stick_count, turn_count, players)
    (meat of the program, contains loop for game until stick_count == 0)
        player = ""
        turn_count += 1
        if turn_count % 2 == 1:
            player = "Player 1"
        else:
            player = "Player 2"
        while True:
        stick_remove (calls UserInteraction for how many sticks to remove)
        print turn_count
        if stick_count = 0:
            winner = player
            run (end_game(winner))


    end_game(self, winner)
        print (Player 1 won the game! (based on turn_count/player))
        game_replay(self) (calls UserInteraction for yes/no to play game again)


AI() (makes a random choice based on stick_count, and weighs winning choices heavily)
    AI = [[1,2,3],[1,2,3],[1,2,3]...]
    computer_turns = []
    computer_guesses = []
    if turn_count % 2 == 1:
        if len(AI[stick_count-1]) == 1
            stick_remove = random.choice(AI[stick_count-1])
        else:
            stick_remove = pop.random.choice(AI[stick_count-1])
            computer_turns.append(stick_count-1)
            computer_guesses.append(stick_remove)
    else:
        continue
    if winner = "Player 2"
        for each turn in computer_turns:
            AI.append(computer_guesses[computer_turns]*2)
    return(stick_count, stick_remove)



User Experience:
    At first, the user will load up the program, looking to play the stick game
    either against a computer AI or against one of their friends.  Loading the
    program will bring about an input prompt to see if they would like to play
    against AI or a friend.

    After this choice, the program would ask the user how many sticks they would
    like to start with, ranging from 10-100.  If input is outside of that range,
    the user will be prompted to enter a number inside the range.  After the
    amount of sticks is decided, the program will either continue vs. a friend
    vs. an AI.

    Against a friend, the program will begin to count turns, and letting the
    users know which player's turn it is.  Each player will take a turn inputting
    how many sticks they would like to take out of the pile.  These turns will
    repeat until the stick count goes down to zero, at which point the program
    will tell the players which one of them won based on who was forced to pick
    up the last stick.

    Against an AI, the program will basically run the same, where the user will
    be prompted for how many sticks to take out of the pile, and the AI will
    make a random choice to do the same.  Again, at the end of the program, the
    user will be told who the winner was.  The only caveat to the AI part of the
    program will be how the AI chooses how many sticks to pick up.  As the
    AI continues to play the game, it will put more weight on the choice that
    led to it's victory, thus making it more and more difficult to defeat.

    At the end of the program, the user will be prompted as to whether or not
    they want to play again.

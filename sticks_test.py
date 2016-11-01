from sticks import *

def test_creation():
    type_of_game = game_type(players=2)

def test_type_of_game():
    player_options = ['friend', 'computer']
    assert type_of_game in player_options

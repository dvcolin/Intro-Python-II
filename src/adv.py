from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms
room['outside'].items = [
    Item('Shotgun', 'A short-ranged weapon used for killing mortal beings.'), Item('Rock', 'A natural weapon.')]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    def direction_error():
        print('INVALID DIRECTION!')

    def print_room_items():
        print('Available Items:')
        for item in player.current_room.items:
            print(item)

    def print_player_items():
        print('Current Items:')
        for item in player.items:
            print(item)

    def add_item(item_name):
        for item in player.current_room.items:
            if item.name == item_name:
                player.items.append(item)
                player.current_room.items.remove(item)
                return
        print('Item not available.')

    def drop_item(item_name):
        for item in player.items:
            if item.name == item_name:
                player.items.remove(item)
                player.current_room.items.append(item)
                return
        print('Item not available.')

    print(
        f"****************************\nCurrent Room: {player.current_room.name}\n{player.current_room.description}\n****************************\n")

    if len(player.current_room.items) != 0:
        print_room_items()

    if len(player.items) != 0:
        print_player_items()

    player_input = input(
        'Please enter a command. (move: n, s, e, w) (take ITEM_NAME, drop ITEM_NAME) (quit: q): ').split(' ')

    if len(player_input) == 1 and player_input[0] != '':
        if player_input[0] == 'n':
            try:
                player.current_room = player.current_room.n_to
            except:
                direction_error()
        elif player_input[0] == 's':
            try:
                player.current_room = player.current_room.s_to
            except:
                direction_error()
        elif player_input[0] == 'e':
            try:
                player.current_room = player.current_room.e_to
            except:
                direction_error()
        elif player_input[0] == 'w':
            try:
                player.current_room = player.current_room.w_to
            except:
                direction_error()
        elif player_input[0] == 'q':
            break
    elif len(player_input) == 2 and player_input[0] != '' and player_input[1] != '':
        if player_input[0] == 'take':
            add_item(player_input[1])
        elif player_input[0] == 'drop':
            drop_item(player_input[1])
    else:
        print('Please enter a valid command.')

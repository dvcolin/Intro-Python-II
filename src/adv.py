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
    Item('Shotgun', 'A short-ranged weapon used for killing mortal beings. Gotta good spread.'), Item('Rock', 'A natural weapon.')]

room['foyer'].items = [
    Item('Candle', 'A common light source of the 1800s.'), Item('FatMan', 'Launches mini nukes all day, every day.')]
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

    def take_item(item_name):
        for item in player.current_room.items:
            if item.name == item_name or item.name.lower() == item_name:
                player.items.append(item)
                player.current_room.items.remove(item)
                print(item.on_take())
                return
        print('Item not in current room.')

    def drop_item(item_name):
        for item in player.items:
            if item.name == item_name or item.name.lower() == item_name:
                player.items.remove(item)
                player.current_room.items.append(item)
                print(item.on_drop())
                return
        print('Item not in inventory.')

    print(
        f"****************************\nCurrent Room: {player.current_room.name}\n{player.current_room.description}\n****************************\n")

    if len(player.current_room.items) != 0:
        print_room_items()

    if len(player.items) != 0:
        print_player_items()

    player_input = input(
        'Please enter a command. (move: n, s, e, w) (take ITEM_NAME, drop ITEM_NAME) (inventory: "i" or "inventory") (quit: q): ').split(' ')

    if len(player_input) == 1 and player_input[0] != '':
        if player_input[0] == 'n':
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to
            else:
                direction_error()
        elif player_input[0] == 's':
            if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to
            else:
                direction_error()
        elif player_input[0] == 'e':
            if player.current_room.e_to != None:
                player.current_room = player.current_room.e_to
            else:
                direction_error()
        elif player_input[0] == 'w':
            if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to
            else:
                direction_error()
        elif player_input[0] == 'i' or player_input[0] == 'inventory':
            if len(player.items) != 0:
                print_player_items()
            else:
                print('You have no items in your inventory.')
        elif player_input[0] == 'q':
            break
    elif len(player_input) == 2 and player_input[0] != '' and player_input[1] != '':
        if player_input[0] == 'get' or player_input[0] == 'take':
            take_item(player_input[1])
        elif player_input[0] == 'drop':
            drop_item(player_input[1])
    else:
        print('Please enter a valid command.')

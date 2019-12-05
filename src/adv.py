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


# Declare all items
item = {
    'sword': Item('Sword', 'A sharp, shiny blade used for stabbing zombies.'),
    'shotgun': Item('Shotgun', 'A short ranged weapon used for killing zombies.')
}


# Add items to rooms
room['outside'].items.append(item['sword'])
room['outside'].items.append(item['shotgun'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Player1', room['outside'])

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


def start_game():
    while True:
        print(
            f"\n*************************************\nCurrent Location: {player.current_room.name}")
        print(
            f"{player.current_room.description}\n*************************************")
        if len(player.current_room.items) != 0:
            print("Available Items:\n")
            for item in player.current_room.items:
                print(f"{item}")
            print("************************************************************")
        if len(player.items) != 0:
            print("Current Items:\n")
            for item in player.items:
                print(f"{item}")
            print("************************************************************")

        # def get_item_input():
        #     item_input = input(
        #         'Take or drop items? (take ITEM_NAME or drop ITEM_NAME): ').split(' ')
        #     return item_input

        # def get_direction_input():
        #     direction_input = input(
        #         'Which direction would you like to go? (n, s, e, w, q to quit): ')
        #     return direction_input

        def direction_error():
            print('ERROR: Please choose a valid direction.')

        # def set_player_items(item_input):
        #     if len(item_input) == 1 and item_input[0] == '':
        #         pass
        #     elif len(item_input) == 2 and item_input[0] == 'take':
        #         global item
        #         action = item_input[0]
        #         chosen_item = item_input[1]
        #         try:
        #             if item[chosen_item] in player.current_room.items:
        #                 player.items.append(item[chosen_item])
        #         except KeyError:
        #             print("Item entered is not available.")

        # def set_new_location(direction_input):
        #     if direction_input == 'n':
        #         if player.current_room.n_to is not None:
        #             player.current_room = player.current_room.n_to
        #         else:
        #             print_error()

        #     elif direction_input == 's':
        #         if player.current_room.s_to is not None:
        #             player.current_room = player.current_room.s_to
        #         else:
        #             print_error()
        #     elif direction_input == 'e':
        #         if player.current_room.e_to is not None:
        #             player.current_room = player.current_room.e_to
        #         else:
        #             print_error()
        #     elif direction_input == 'w':
        #         if player.current_room.w_to is not None:
        #             player.current_room = player.current_room.w_to
        #         else:
        #             print_error()
        #     else:
        #         print('Please enter a valid character.')

        def get_player_input():
            player_input = input(
                'Enter n, s, e, or w to move. Enter q to quit.\nTo take or drop items, enter "take/get ITEM_NAME" or "drop ITEM_NAME"\nPlease enter a command: ').split(' ')
            return player_input

        def apply_player_input(player_input):
            if len(player_input) == 1:
                command = player_input[0]
                if command == 'n':
                    if player.current_room.n_to is not None:
                        player.current_room = player.current_room.n_to
                    else:
                        direction_error()
                elif command == 's':
                    if player.current_room.s_to is not None:
                        player.current_room = player.current_room.s_to
                    else:
                        direction_error()
                elif command == 'e':
                    if player.current_room.e_to is not None:
                        player.current_room = player.current_room.e_to
                    else:
                        direction_error()
                elif command == 'w':
                    if player.current_room.w_to is not None:
                        player.current_room = player.current_room.w_to
                    else:
                        direction_error()
                elif command == 'i' or command == 'inventory':
                    if len(player.items) != 0:
                        print('Inventory:')
                        for items in player.items:
                            print(items)
                    else:
                        print('You do not have any items in your inventory.')
                else:
                    print('Please enter a valid character.')
            elif len(player_input) == 2:
                item_action = player_input[0]
                item_name = player_input[1]
                global item
                if item_action == 'take' or item_action == 'get':
                    try:
                        if item[item_name] in player.current_room.items:
                            player.items.append(item[item_name])
                            print(item[item_name].on_take())
                            player.current_room.items.remove(item[item_name])
                    except KeyError:
                        print("Error: Unable to pick up item.")
                elif item_action == 'drop':
                    try:
                        if item[item_name] in player.items:
                            player.items.remove(item[item_name])
                            print(item[item_name].on_drop())
                            player.current_room.items.append(item[item_name])
                    except KeyError:
                        print("Error: Unable to drop item.")

        player_input = get_player_input()

        if player_input[0] == 'q':
            print('Goodbye!')
            break
        apply_player_input(player_input)


start_game()

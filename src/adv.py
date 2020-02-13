from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("apron", "A discarded, dusty apron. It has the words 'Patricia's Diner' written on the front."), Item("foot", "A rotten, maggot-ridden, severed foot. You hope it has nothing to do with Patricia, or her diner.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("note", "A crumpled note. On closer inspection you can see something written on it... \n '2:47am, don't be late! \n And bring the spade! \n Margory'")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("frog", "A green and red frog who looks up at you blinking. You can't figure out if he's bored or if he's desperately trying to communicate.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("book", "A heavy, ancient tome entitled 'Master Python in 10 days'")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("map", "A treasure map that indicates the location of the treasure room itself. There is some chewing gum stuck to the edge of it and a doodle depicting a stick man shooting what looks like a water pistol.")]),
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
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

print('\n --------------------------------------\n',
'Welcome to Magical Apocalypse - Part 9 \n',
'--------------------------------------\n')


name = input(f" Welcome! Please enter your name: ")
player = Player(name, room['outside'], items = [])

# player = Player("Lisa", room['outside'])
# print(player)


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

direction = " "


def welcome_message():
    print(f'\n ---------------------- \n {player} \n ---------------------- \n ')

noGoMessage = "\n Sorry, you can't go in that direction."    

welcome_message()
while True:   
    print(player.room)
    cmd = input(f"\n Please type a command. For help, type 'h' ").split()
    current_room = player.room 
    if cmd[0] == 'n':
        print(f'\n ...\n\n You chose north...')
        if current_room.n_to is not None:
            player.room = current_room.n_to 
        else:
            print(noGoMessage)
    elif cmd[0] == 'w':
        print(f'\n ...\n\n You chose west...')
        if current_room.w_to is not None:
            player.room = current_room.w_to   
        else:
            print(noGoMessage)
    elif cmd[0] == 'e':
        print(f"\n ...\n\n You chose east...")
        if current_room.e_to is not None:
            player.room = current_room.e_to 
        else:
            print(noGoMessage) 
    elif cmd[0] == 's':
        print(f"\n ...\n\n You chose south...")
        if current_room.s_to is not None:
            player.room = current_room.s_to
        else:
            print(noGoMessage)  
    elif cmd[0] == 'i':
        print(player.print_inventory())   

    elif cmd[0] == 'get':
        if len(cmd) > 1:
            player.get_item(cmd[1])
            player.room.remove_item(cmd[1])
        else:
            print(f"Which item do you want to get?")

    elif cmd[0] == 'drop':
        if len(cmd) > 1:
            player.discard_item(cmd[1])
            player.room.add_item(cmd[1])
        else:
            print(f"Which item do you want to drop?")        

    elif cmd[0] == 'q':
        print(f"\n ...\n\n You decided to quit the game.")
        break
    else:
        print(f"Please enter a valid command.")                                    
            

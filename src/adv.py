from room import Room
from player import Player

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
room['treasure'].s_to = room['narrow'] #I don't fully understand what these dot notation bits actually do. Do they just mean that the room on the left with this dot notation is reassigned to the room on the right?

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Lisa", room['outside'])
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
    print(player)

noGoMessage = "Sorry, you can't go in that direction."    

welcome_message()
while True:   # I followed the examples in the folder here but wasn't entirely sure if I needed the while True statement.
    print(player.room)
    direction = input(f" Please choose a direction: n, s, e or w ")
    current_room = player.room #This is the only way I could get this whole task to work - by assigning player.room to a new variable/label. I'm still not fully sure how we are accessing the .n_to etc. I just tested it with the previous implementation and it actually works without it now... I have no idea what I did wrong but I'll leave this comment for now anyway.
    if direction == 'n':
        print(f'You chose north...')
        if current_room.n_to is not None:
            player.room = current_room.n_to 
        else:
            print(noGoMessage)
    elif direction == 'w':
        print(f'You chose west...')
        if current_room.w_to is not None:
            player.room = current_room.w_to   
        else:
            print(noGoMessage)
    elif direction == 'e':
        print(f"You chose east...")
        if current_room.e_to is not None:
            player.room = current_room.e_to 
        else:
            print(noGoMessage) 
    elif direction == 's':
        print(f"You chose south...")
        if current_room.s_to is not None:
            player.room = current_room.s_to
        else:
            print(noGoMessage)   
    elif direction == 'q':
        print(f"You decided to quit the game.")
        break
    else:
        print(f"Please enter a valid direction, n, s, e or w.")                                    
            

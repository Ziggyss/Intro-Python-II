# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        self.items = []

    def __str__(self):
        return f'Welcome to the game, {self.name}.'

    def get_item(self, item):
        #I need to write some code here to get the correct item
        self.items.append(item)
        print(f" You picked up the {item}. It seemed useful at the time.")   

    def discard_item(self, item):
        self.items.remove(item)
        print(f" You dropped the {item}. You didn't really need it anyway.")    

    def print_inventory(self):
        output = ''
        if len(self.items) != 0:
            output += f" You are carrying:"
            for i in self.items:
                output += f' -- {i}'
                return output
    #For some reason I cannot get this loop to print out more than one of the items the player is holding... Not sure why yet.            
                
        else:
            return(f"\n Your pockets are empty, but your spirits are high.")          

        
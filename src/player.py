# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def __str__(self):
        return f'Welcome to the game, {self.name}.'

    def get_item(self, item):
        self.items.append(item) 
        print(f" You picked up the {item}. It seemed useful at the time.")   

    def print_inventory(self):
        if len(self.items) != 0:
            print(f" You are carrying:")
            for i in self.items:
                    return(f' -- {i}') 
        else:
            print(f"\n Your pockets are empty, but your spirits are high.")          

        
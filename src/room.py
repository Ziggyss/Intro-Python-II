# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def add_item(self, item):
        for item in self.items:
           self.items.append(item)          

    def remove_item(self, item):
        for item in self.items:
            self.items.remove(item)   
    #At this point the code will remove an item from a room successfully but it will not add it again                 

    def __str__(self):
        output = ''
        output += f'\n You are here: {self.name} \n \n {self.description}\n'
        if len(self.items) != 0:
            output += f'\n Wait! There are some items in this room........... \n'
            for i in self.items:
                output += f'\n {i.name}: \n {i.description} \n ------------------------------------------ '
            output += f'\n Will you take anything on your quest?'    
    
        else:
            output += f'\n You see no items to help you on your quest...'

        return output    
            
           
            

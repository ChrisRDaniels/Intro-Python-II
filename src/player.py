# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.item = []

    def move(self, direction):
        new_room = self.current_room.get_direction(direction)
        if new_room is not None:
            self.current_room = new_room
            print(self.current_room)
        else:
            print("Your path is blocked!")
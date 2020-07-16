from room import Room
from player import Player
#from item import Item

class Room(object):

  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.paths = {}

  def go(self, direction):
    return self.paths.get(direction, None)

  def add_paths(self, paths):
    self.paths.update(paths)

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

# set up variables
wants_to_quit = False
player = Player(room['outside'])
player = Player(input("What is your name? "), room['outside'])

# Move command, will handle move attempts
def go(dir):
    """
    dir values:
    0: north
    1: east
    2: south
    3: west
    """
    # print('Moving in direction',dir)

    # grab current room connections
    conns = [
        player.cur_room.n_to,
        player.cur_room.e_to,
        player.cur_room.s_to,
        player.cur_room.w_to
    ]

    if conns[dir] is not None:
        player.cur_room = conns[dir]
    if hasattr(player.cur_room, dir+"_to"):
        player.cur_room = getattr(player.cur_room, dir+"_to")
    else:
        print("You can't go that way.")
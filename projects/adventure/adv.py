from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n', ]
traversal_path = []
#----------------------------------------------DO NOT TOUCH ANYTHING ABOVE THIS LINE----------------------------------

def dft(starting_room):
    s = Stack()
    s.push(starting_room)
    visited_rooms = set()
    while s.size() > 0:
        current_room = s.pop()
        if current_room not in visited_rooms:
            print(current_room)
            visited_rooms.add(current_room)
            exits = player.current_room.get_exits()
            for exit in exits:
                s.push(exit)














#---------------------------------------------DO NOT TOUCH ANYTHING BELOW THIS LINE-------------------------------------
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    print('Move: ', move) # n, n
    # print('Traversal Path: ', traversal_path)
    player.travel(move)
    # print(player.travel)
    visited_rooms.add(player.current_room)
    print('Current Room: ', player.current_room.get_exits())

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

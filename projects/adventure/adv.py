from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


#----------------------------------------------DO NOT TOUCH ANYTHING ABOVE THIS LINE----------------------------------

# Fill this out with directions to walk
# traversal_path = ['n', 'n', ]
traversal_path = []

backtrack = {'n':'s', 's':'n', 'w':'e', 'e':'w'}
path = []
visited_rooms = {}


visited_rooms[player.current_room.id] = player.current_room.get_exits()
# print('Visited Rooms: ', visited_rooms) # {0: ['n', 's', 'w', 'e']}

while len(visited_rooms) < len(room_graph) - 1:
    if player.current_room.id not in visited_rooms:
        visited_rooms[player.current_room.id] = player.current_room.get_exits()
        # print(visited_rooms[player.current_room.id]) # No Output
        previous_room = path[-1]
        visited_rooms[player.current_room.id].remove(previous_room)
    while len(visited_rooms[player.current_room.id]) < 1:
        previous_room = path.pop()
        traversal_path.append(previous_room)
        player.travel(previous_room)
    move = visited_rooms[player.current_room.id].pop()
    traversal_path.append(move)
    path.append(backtrack[move])
    player.travel(move)

        



# def move():
#     visited_rooms = set()
#     player.current_room = world.starting_room
#     visited_rooms.add(player.current_room)

#     for move in traversal_path:
#         player.travel(move)
#         visited_rooms.add(player.current_room)


# def dft(starting_room):
#     s = Stack()
#     s.push(starting_room)
#     visited_rooms = set()
#     while s.size() > 0:
#         current_room = s.pop()
#         if current_room not in visited_rooms:
#             print(current_room)
#             visited_rooms.add(current_room)
#             exits = player.current_room.get_exits_string()
#             for exit in exits:
#                 s.push(exit)


# move()











#---------------------------------------------DO NOT TOUCH ANYTHING BELOW THIS LINE-------------------------------------
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    # print('Move: ', move) # n, n
    # print('Traversal Path: ', traversal_path)
    player.travel(move)
    # print(player.travel)
    visited_rooms.add(player.current_room)
    # print('Current Room: ', player.current_room.get_exits())

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

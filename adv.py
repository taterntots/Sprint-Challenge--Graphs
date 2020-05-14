from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
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
# traversal_path = ['n', 'n']

s = Stack()
s.push([player.current_room.id])

traversal_path = []
visited = {}

print('Visited_Initial:', visited)
print('Traversal_Initial:', traversal_path)

if player.current_room.id not in visited:
    visited[player.current_room.id] = {}
    for direction in player.current_room.get_exits():
        visited[player.current_room.id][direction] = '?'

print('NEW VISITED:', visited)

# while len(player.current_room.get_exits()) != 1:
#     # print('Size:', s.size())
#     path = s.pop()
#     curr_room = player.current_room.id

        # for next_room in player.current_room.get_exits():
        #     # print('next room:', next_room)
        #     traversal_path.append(next_room)
        #     s.push(player.current_room.get_room_in_direction(next_room).id)
        #     player.travel(next_room)

# print('Finished Traversal:', traversal_path)

# print('CURRENT ROOM ID:', player.current_room.id)
# print('CURRENT ROOM EXITS:', player.current_room.get_exits())

# visited[player.current_room.id] = player.current_room.get_exits()

# print('Room Paths:', visited)
# print('Length of visited:', len(visited))
# # print('Room Graph:', room_graph)
# print('Length of Room Graph:', len(room_graph))


# print('blerg', visited)

# # While the number of rooms visited is less than the number of rooms in the map
# while len(visited) < len(room_graph):
#     # Begin tracking the visited rooms
#     # If the room is not in our path (not visited)
#     if player.current_room.id not in visited:
#         visited[player.current_room.id] = {}
#         for direction in player.current_room.getExits():
#             visited[player.current_room.id][direction] = '?'


# print(visited)
# Remove 

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

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

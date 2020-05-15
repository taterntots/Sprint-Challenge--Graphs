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

# -----------------------------------------------------------
# s = Stack()
# s.push([player.current_room.id])

# traversal_path = []
# visited = {}
# path = {}
# visited2 = {}

# path[player.current_room.id] = player.current_room.get_exits()
# visited2[player.current_room.id] = player.current_room.get_exits()

# print(path)

# print('Visited_Initial:', visited)
# print('Traversal_Initial:', traversal_path)

# if player.current_room.id not in visited:
#     visited[player.current_room.id] = {}
#     for direction in player.current_room.get_exits():
#         visited[player.current_room.id][direction] = '?'

# print('NEW VISITED:', visited)

# while len(visited) < len(room_graph):
#     if player.current_room.id not in visited:
#         pass

# -----------------------------------------------------------

# print('CURRENT ROOM ID:', player.current_room.id)
# print('CURRENT ROOM EXITS:', player.current_room.get_exits())
# print('Room Paths:', visited)
# print('Length of visited:', len(visited))
# print('Room Graph:', room_graph)
# print('Length of Room Graph:', len(room_graph))

# while len(visited) < len(room_graph):
#     remaining_rooms = []
#     for direction in visited:
#         print(direction)
#         if visited[direction] == '?':
#             remaining_rooms.append(direction)
# print('REMAINING ROOMS:', remaining_rooms)
    
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

# -----------------------------------------------------------

# Define some variables
traversal_path = []
visited = {}
reverse_visit = []
invert_direction = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

print('CURRENT ROOM ID:', player.current_room.id)
print('CURRENT ROOM EXITS:', player.current_room.get_exits())
print('Length of visited:', len(visited))
print('Length of Room Graph:', len(room_graph))
# print('Room Graph:', room_graph)

# Add our starting room with all available exits to the visited dictionary
visited[player.current_room.id] = player.current_room.get_exits()
print('Starting Room Path:', visited)

# While the number of visited rooms is less than the total number of rooms in the graph
while len(visited) < len(room_graph) - 1:

    # ----------------------------------------------------------
    # ------------------- Track visited rooms ------------------
    # ----------------------------------------------------------

    # If the current room is not in our visited dictionary
    if player.current_room.id not in visited:
        # Add it to our visited list with associated exits as values
        visited[player.current_room.id] = player.current_room.get_exits()
        # print('REVERSE', reverse_visit)
        # Define the last room direction to be the last direction in our reverse list (the exit)
        last_room_direction = reverse_visit[-1]
        # print(last_room_direction)
        # Removes the direction we came from, taking it out of our visited list
        visited[player.current_room.id].remove(last_room_direction)
        # print('REMOVE DIRECTION:', visited)

    # ----------------------------------------------------------
    # ------------------ Traversing Dead Ends ------------------
    # ----------------------------------------------------------

    print('LENGTH:', len(visited[player.current_room.id]))
    # When we hit a dead end or a room has no more unexplored pathways
    while len(visited[player.current_room.id]) == 0: 
        # Track our movement count as we backtrack through already visited rooms
        reverse_direction = reverse_visit.pop()
        # print(reverse_direction)
        traversal_path.append(reverse_direction)
        # Reverse our direction
        player.travel(reverse_direction)

    # ----------------------------------------------------------
    # --------------- Traversing Available Exits ---------------
    # ----------------------------------------------------------

    # Define our movement to the first direction in our visited dictionary
    walking_direction = visited[player.current_room.id].pop(0)
    print(walking_direction)
    # Track our movement count as we walk to the next room
    traversal_path.append(walking_direction)
    # Store the inverted direction of the new room we are about to walk into in our reverse_visit list
    reverse_visit.append(invert_direction[walking_direction])
    # Move to the first exit available in the current room
    player.travel(walking_direction)

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

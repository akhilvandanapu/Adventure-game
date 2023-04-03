#!/usr/bin/env python
# coding: utf-8

# In[28]:


import json
with open('map.json', 'r') as a:
    json_data = a.read()
    map_data = json.loads(json_data)
#     print(map_data)

game_state = { 'current_room' : 0, 'inventory': [] }

def get_current_room(map_data, game_state):
    return map_data[game_state['current_room']]

def move(game_map, game_state, direction):
    current_room = get_current_room(map_data, game_state)
    if direction in current_room['exits']:
        game_state['current_room'] = current_room['exits'][direction]
        print(f'You go {direction}. \n')
        current_room = get_current_room(map_data, game_state)
        print('>',current_room['name']+'\n')
        print(current_room['desc']+'\n')
        exits = current_room['exits']
        exit_str = " ".join(exits)
        if 'items' in current_room:
            print('Items: '+ ','.join(current_room['items'])+'\n')
        print(f"Exits: {exit_str}"+'\n')
    else:
        print("There's no way to go",direction,end='.\n')
    
        
def look(game_map, game_state):
    current_room = get_current_room(game_map, game_state)
    print('>',current_room['name']+'\n')
    print(current_room['desc']+'\n')
    exits = current_room['exits']
    exit_str = " ".join(exits)
    if 'items' in current_room:
        ite=', '.join(current_room['items'])
        if ite:
            print('Items: ',ite+'\n')
    print(f"Exits: {exit_str}"+'\n')
                    
    
def get(game_map, game_state, item):
    current_room = get_current_room(game_map, game_state)
    if 'items' in current_room:
        if item in current_room['items']:
            game_state['inventory'].append(item)
            current_room['items'].remove(item)
            print(f"You pick up the {item}.")
        else:
            print('There\'s no',item,'here.')
    else:
        print('There\'s no',item,'here.')
                    

def drop(game_map, game_state, item):
    current_room = get_current_room(game_map, game_state)
    # print(item)
    if item in game_state['inventory']:
        game_state['inventory'].remove(item)
        current_room['items']=current_room.get('items',[])
        current_room['items'].append(item)
        print(f"You drop the {item}.")
    else:
        print("You don't have that item.")
    

current_room = get_current_room(map_data, game_state)
print('>',current_room['name']+'\n')
print(current_room['desc']+'\n')
exits = current_room['exits']
exit_str = " ".join(exits)
if 'items' in current_room:
    print('Items:', ''.join(current_room['items'])+'\n')
print(f"Exits: {exit_str}"+'\n')

while True:
    try:
        command = input('What would you like to do? ').lower()
        
        parts = command.split()
        verb = parts[0]
        if verb == 'quit':
            print("Goodbye!")
            break
        elif verb == 'look':
            look(map_data, game_state)
        elif verb == 'get':
            if len(parts) < 2:
                print("Sorry, you need to 'get' something.")
            else:
                item = ''.join(parts[1])
                get(map_data, game_state, item)
        elif verb == 'drop':
            if len(parts) < 2:
                print("Drop what?")
            else:
                item = ''.join(parts[1])
                
                drop(map_data, game_state, item)
        elif verb =='go': 
            if len(parts)<2:
                print('Sorry, you need to \'go\' somewhere.')
            else:
                move(map_data, game_state, parts[1])
        elif verb == 'inventory':
            inve=game_state['inventory']
            if inve:
                print('Inventory:',)
                print(' ','\n '.join(inve))
            else:
                print('You\'re not carring anything.')
            

        else:
            print(f"I didnt get the command: {command}.")
    except EOFError as e:
        print('Use \'quit\' to exit the game')


    


# In[26]:


# import json

# # Load the game map
# # with open('map.json') as f:
# #     game_map = json.load(f)
# # import json
# with open('map.json', 'r') as a:
#     json_data = a.read()
#     game_map = json.loads(json_data)
# #     print(map_data)

# # Initialize the game state
# game_state = {
#     'current_room': 0,
#     'inventory': []
# }

# # Helper functions
# def get_current_room(game_map, game_state):
#     return game_map[game_state['current_room']]

# def move(game_map, game_state, direction):
#     current_room = get_current_room(game_map, game_state)
#     if direction in current_room['exits']:
#         game_state['current_room'] = current_room['exits'][direction]
#         print(f"You move {direction} to {get_current_room(game_map, game_state)['name']}.")
#         return True
#     else:
#         print("You can't go that way.")
#         return False

# def look(game_map, game_state):
#     current_room = get_current_room(game_map, game_state)
#     print(current_room['name'])
#     print(current_room['description'])
#     print("Exits:")
#     for direction in current_room['exits']:
#         print(f"{direction}: {game_map[current_room['exits'][direction]]['name']}")

# def take(game_map, game_state, item):
#     current_room = get_current_room(game_map, game_state)
#     if item in current_room['items']:
#         game_state['inventory'].append(item)
#         current_room['items'].remove(item)
#         print(f"You take the {item}.")
#     else:
#         print("That item is not here.")

# def drop(game_map, game_state, item):
#     current_room = get_current_room(game_map, game_state)
#     if item in game_state['inventory']:
#         game_state['inventory'].remove(item)
#         current_room['items'].append(item)
#         print(f"You drop the {item}.")
#     else:
#         print("You don't have that item.")

# # Game loop
# while True:
#     current_room = get_current_room(game_map, game_state)
#     command = input("> ")
#     parts = command.split()
#     verb = parts[0]
#     if verb == 'quit':
#         print("Goodbye!")
#         break
#     elif verb == 'look':
#         look(game_map, game_state)
#     elif verb == 'take':
#         if len(parts) < 2:
#             print("Take what?")
#         else:
#             item = ' '.join(parts[1:])
#             take(game_map, game_state, item)
#             print(current_room['name'])
#             print(current_room['description'])
#             print("Exits:")
#             for direction in current_room['exits']:
#                 print(f"{direction}: {game_map[current_room['exits'][direction]]['name']}")
#     elif verb == 'drop':
#         if len(parts) < 2:
#             print("Drop what?")
#         else:
#             item = ' '.join(parts[1:])
#             drop(game_map, game_state, item)
#             print(current_room['name'])
#             print(current_room['description'])
#             print("Exits:")
#             for direction in current_room['exits']:
#                 print(f"{direction}: {game_map[current_room['exits'][direction]]['name']}")
#     elif verb in current_room['exits']:
#         if move(game_map, game_state, verb):
#             print(current_room['name'])
#             print(current_room['description'])
#             print("Exits:")
#             for direction in current_room['exits']:
#                 print(f"{direction}: {game_map[current_room['exits']]}")


# In[ ]:





# In[ ]:





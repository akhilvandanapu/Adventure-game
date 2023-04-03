Name : Akhil Vandanapu
Stevens login ID: avandana
GitHub Repo: https://github.com/akhilvandanapu/Adventure-game
Hours worked on project : 15

Testing the code:

I have implemented my code based on the example map you have mentioned in the project.
So, after running the code at first you will be white room having exits: north east
	-if you go to north you will enter blue room having exits: east south
		-if you go to east you will go to green room having exits: west south
			- if you go to the west you will go back to the blue room again
			- if you go to south you will enter the red room having items "rose" and having exits: north west
				-if you go to north you will enter green room again
				-if you go to west you will go back to white room again
		-if you go to south you will go back to the white room
	-if you go to east you will enter red room having exits: north west
		-if you go to north you will enter green room having exits: west south
			- if you go to west you will enter blue room having exits: east south
				-if you enter east you will go to green again
				-if you enter south you will enter white room again
			-if you go to south you will enter red room again
		-if you go to west you will enter white room again.
		
		
Above is baseline behavior but if you give just direction like "east" or "west" instead of "go east" or "go west", It will say "I didnt get the command: east."
and asks you enter the input again

"go" verb:
after entering every room it will provide details of that room like this  

> A white room

You are in a simple room with white walls.

Exits: north east

It will take you to the other rooms ex: go east
if you give only go instead of go east, it will give this output "Sorry, you need to 'go' somewhere."
if you any exits other then available ones it give like this "There's no way to go west"


"look" verb:
It will print the current room details

"get" verb:
it will get the items in the room if you have otherwise it will print like this "There's no rose anywhere."

"inventory" verb:
it will show what items you are carrying.
if you don't have any it will show like "You're not carrying anything."

"quit" verb:

use the "quit" to end the program.


Bugs and Issues: In drop extension i can only drop the rose in green room but not in any other room, because i couldn't add items dictionary to other rooms.

Difficult issue or bug I resolved:

i used ',' in print statements because of that test caeses didn't get passed for me, after i replaced it with '+' i got my test cases passed. It may look simple one but took me a while figure it out.



Extensions:

1)Drop: 

As mentioned in the project this verb will drop the items which you already have.
In my map I have a rose in red room.
You can go to red room from white room(starting room) by choosing east exit.
you can pick the rose from that room and drop it any other room.




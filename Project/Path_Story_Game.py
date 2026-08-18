
with open("./project./story.txt" , "r") as f:
    data = f.read()
    dictionary = {
        "[SECTION_1]" : '''You wake up in a dark cave. A torch is on the ground and there are 2 tunnels.
1. Take the torch and go left
2. Leave the torch and go right
What do you choose?
NEXT:1->SECTION_2|2->SECTION_3''' , 
        "[SECTION_2]" : '''The torch lights up ancient drawings on the wall. The tunnel ends at a heavy door with 2 keyholes.
1. Search the floor for keys
2. Try to push the door open
What do you choose?
NEXT:1->SECTION_4|2->ENDING_1''' , 
        "[SECTION_3]" : '''It's pitch black. You trip and fall into a deep pit.
GAME OVER
NEXT:->ENDING_2''',
        "[SECTION_4]" : '''You found 2 rusty keys! One is gold, one is silver. The door has 2 keyholes.
1. Use the gold key
2. Use the silver key
What do you choose?
NEXT:1->ENDING_3|2->ENDING_1''',
        "[ENDING_1]" : '''The door creaks open to a room full of monsters. 
BAD ENDING: You didn't escape.
NEXT:END''',
         "[ENDING_2]" : '''The door creaks open to a room full of monsters. 
BAD ENDING: You didn't escape.
NEXT:END''',
         "[ENDING_3]" : '''The gold key turns! Behind the door is a chest of treasure and a way out to sunlight.
GOOD ENDING: You escaped with the treasure!
NEXT:END''',
    }
# testing if the dictionary run or not , its run on my side 
# print(dictionary)
current_section = dictionary["[SECTION_1]"]
def game(current_section):
    choice = input("Choose your action : 1. Take the torch and go left , 2. Leave the torch and go right")
    


        

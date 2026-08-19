# Open the story file and read its entire contents into one big text string
with open("./project/story.txt", "r") as f:
    data = f.read()
# Empty dictionary that will hold every section/ending: 
# key = section label (e.g. "[SECTION_1]"), value = that section's text
dictionary = {}

# Split the whole file into separate section blocks, wherever there's a blank line
blocks = data.split("\n\n")
# Go through each block one at a time and add it to the dictionary
for block in blocks:
    block = block.strip()        # remove extra leading/trailing whitespace
    if block == "":               # skip any accidentally empty blocks
        continue
    lines = block.split("\n", 1)    # split into: [0] the label line, [1] everything else
    label = lines[0].strip()        # e.g. "[SECTION_1]"
    content = lines[1].strip()      # the story text + NEXT line, still combined
    dictionary[label] = content     # store label -> content in the dictionary

# Now split every dictionary value into two separate parts:
# the story text the player reads, and the NEXT info that says where choices lead


for key, value in dictionary.items():
    parts = value.split("NEXT:")
    dictionary[key] = parts 
# print(dictionary["[SECTION_2]"])
 # after this, dictionary[key] = [story_text, next_info]

# Runs one "turn" of the game for a given section.
# section = [story_text, next_info] for the current point in the story
# name = the label of this section (e.g. "[SECTION_1]"), used to record endings
def game(section,name):
# Check if this is an ending section (endings have "END" with no further choices)
    if section[1].strip()  == "END":
        print(section[0])        # show the ending text to the player
        # Save this ending's name to progress.txt, keeping a permanent history
        # "a" = append mode, so past endings aren't erased

        with open("./project/progress.txt" , "a") as f:     
            f.write(name + "\n")
        # Ask the player if they want to play again
        again = input("Type R to restart the game or Q for quit: ")
        if again== "R":
             # Restart the game from the very beginning
            game(dictionary["[SECTION_1]"] , "[SECTION_1]")
        return  # stop this function here — this playthrough is finished

    # --- Everything below only runs for normal (non-ending) sections ---

    print(section[0])     # show the story text and the choices to the player
     # Ask the player to pick option 1 or 2
    choice = input("Enter your decision: Type 1 for 1st choose and 2 for 2nd choose: ")
    # Break the NEXT info (e.g. "1->SECTION_2|2->SECTION_3") into separate routes
    routes = section[1].split("|")
     # Check each route to find the one matching the player's choice
    for route in routes :
        parts = route.split("->")  # parts[0] = choice number, parts[1] = destination name
        if parts[0]== choice:      # this route matches what the player typed

            destination = parts[1]  # e.g. "SECTION_2"

            key_name = "[" + destination + "]"    # rebuild the dictionary key format

            next_section = dictionary[key_name]   # look up that section's data

           # Move the game forward to the next section (function calls itself)  
            game(next_section, key_name)
# Kick off the game, starting at Section 1      
game(dictionary["[SECTION_1]"] , "[SECTION_1]" )
        

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names_file = open("input/names/invited_names.txt", "r")
starting_letter = open("input/Letters/starting_letter.txt", "r")
content = starting_letter.read()
name = names_file.readlines()
invited_people = []
for names in name:
    names = names.strip('\n')
    invited_people.append(names)
for people in invited_people:
    invitation = open(f"Output/ReadyToSend/invitation for {people}", "w")
    new_content = content.replace("[name]", f"{people}")
    invitation.write(new_content)
    
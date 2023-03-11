# Get a list of names stripped of \n and end spaces
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names_list = names_file.readlines()
    print(names_list)
    for num in range(len(names_list)):
        names_list[num - 1] = names_list[num -1].strip()
    print(names_list)

#make local letter variable
with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_template = letter_file.read()
    # Go through the list of names and make a new letter with each name filled in
    for name in names_list:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as ready_to_send:
            new_letter = letter_template.replace("[name]", name)
            ready_to_send.write(new_letter)

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
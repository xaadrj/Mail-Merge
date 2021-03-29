#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as invited_name:
    invited_name = invited_name.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read();
    for name in invited_name:
        txt = name.strip()
        new_letter = content.replace("[name]", txt)
        with open(f"./Output/ReadyToSend/letter_for_{txt}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)






    # for name in invited_name:
    #     txt = name.strip()
    #     with open("./Input/Letters/starting_letter.txt") as letter:
    #    ,
    #                                                                      mode="w") as new_letter:
    #         for line in letter:
    #             add_name = line.replace("[name]", txt)
    #             new_letter.write(add_name)



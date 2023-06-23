# placeholder = "[name]"
with open("./Input/Names/invited_names.txt") as names_data:
    names = names_data.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        stripped_name = name.strip()
        print(stripped_name)
        new = letter.replace("[name]", stripped_name )
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode = "w") as completed_letter:
            completed_letter.write(new)




## C:\Users\shash\PycharmProjects\Mail Merge Project Start
## /Users/shash/PycharmProjects/Mail Merge Project Start/Input/Letters/starting_letter.txt




#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
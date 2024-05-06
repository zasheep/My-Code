#201458599, Aminuddin_Zariff-CA05.py
#November, 2019
#Select an actor and create an alien name for each actor. Output the Actor's name and their Alien name
import random
def create_Actor():
    actor_list = ["andrei stephens", "harry venables", "phillipa blythe", "yuan spield", "sadiq elbahi", "stephanie wynne", "zeng ergan"]
    return actor_list
def create_List(): #This function creates a list when needed
    list = []
    return list
def create_Alien_List(name_Chosen): #this function removes spaces from converting our Actor's char into lists
    alienCharacterList = create_List()
    nameList = list(name_Chosen)
    while " " in nameList:
        if " " in nameList:
            nameList.remove(" ")
        else:
            nameList = nameList
    for i in range(5):
        character_Chosen = random.choice(nameList)
        nameList.remove(character_Chosen)
        alienCharacterList.append(character_Chosen)
    return alienCharacterList
def create_String(List): #this function joins the elements of a list together into a string likewise to concatenating
    alien_Name_String = "".join(List)
    return alien_Name_String
def choose_Actor(name_Choose): #this function chooses an actor from our list of actors
    name_Chosen = random.choice(name_Choose)
    return name_Chosen
def has_Vowel(nameList): #this function checks if any vowels are in the alien name
    vowel_A = 'a'
    vowel_E = 'e'
    vowel_I = 'i'
    vowel_O = 'o'
    vowel_U = 'u'
    if vowel_A in nameList \
    or vowel_E in nameList or vowel_I in nameList\
    or vowel_O in nameList or vowel_U in nameList:  #Lines 37-39 got too long so I broke it up into 3 lines
        del nameList[3:]
        return nameList
    else:
        return nameList
def main():
    actorList = create_Actor()
    vowelsList = create_List()
    no_VowelsList = create_List()
    vowels_AlienList = create_List()
    no_Vowels_AlienList = create_List()

    for i in range(len(actorList)):
        name_Chosen = choose_Actor(actorList)   #chooses an actor
        actorList.remove(name_Chosen)   #actor's name is removed from the list so they aren't chosen twice
        alienName = create_Alien_List(name_Chosen)   #removing spaces, Alien name's characters are chosen
        name_String = has_Vowel(alienName)   #Vowel checking
        alienNameJoint = create_String(name_String)   #Alien name is produced
        if len(alienNameJoint) == 5:
            alienNameJoint = alienNameJoint + 'a'
            no_Vowels_AlienList.append(alienNameJoint)
            no_VowelsList.append(name_Chosen)
        else:
            vowels_AlienList.append(alienNameJoint)
            vowelsList.append(name_Chosen)
            string_Name = create_String(vowels_AlienList)  #The characters are concatenated into a string

    print(string_Name,"presents Harry of the Rings")  #Output
    print("Actor Name\t\tAlien Name")
    for i in range(len(vowelsList)):
        print(vowelsList[i],"\t\t",vowels_AlienList[i])
    for i in range(len(no_VowelsList)):
        print(no_VowelsList[i],"\t\t",no_Vowels_AlienList[i])

main()

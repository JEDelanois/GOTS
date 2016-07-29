#Game of Thrones 
#Built to gain practice in buidling dictionaries and lists
#The dictionaries and lists cover some of the main houses and characters

#Characters
#John Snow Character
jon_snow = {'first_name': 'Jon', 'last_name': 'Snow', 'alive': True, 'good': True}
#Ned Stark Character
ned_stark = {'first_name': 'Ned', 'last_name': 'Stark', 'alive': False, 'good': True}
#Tyrion Lannister Character
tyrion_lannister = {'first_name': 'Tyrion', 'last_name': 'Lannister', 'alive': True, 'good': True, 'drinks': '',}
#Tywin Lannister Character
tywin_lannister = {'first_name': 'Tywin', 'last_name': 'Lannister', 'alive': False, 'good': False}

#Special Information
#Tyrion drinking history by episode
tyrion_drinking_episode = {}

#Special Functions
#Tyrion drinking adding
def add_drinking_episode(episode, number_drinks):
	tyrion_drinking_episode[add_drinking_episode[episode]] = number_drinks
	

#Race
#Westerosian

#Unsullied

#Dothraki 

#Wildings

#White Walkers



#Lists with the members of each house
#House Stark
house_stark = [jon_snow, ned_stark]
#House Lannister
house_lannister = [tyrion_lannister, tywin_lannister]
#House Tyrel 

#House Targaryen 

#House Beratheon 

#House 






#Characters in Game of Thrones
characters = [jon_snow, ned_stark, tyrion_lannister, tywin_lannister]

#Which characters are still alive
print("The following characters are still alive:")
for character in characters:
	if character['alive'] == True:
		print("\t" + character['first_name'] + " " + character['last_name'])

#Roster of who's good and who's bad
print("\nEvil and Good roster:")
for character in characters:
	if character['good'] == True:
		print("\t" + character['first_name'] + " " + character['last_name'] + ": Good")
	else:
		print("\t" + character['first_name'] + " " + character['last_name'] + ": Evil")
 	
#Input number of drinks in episode













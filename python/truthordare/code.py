from getpass import getpass
type_of_gameplay = 0
PlayerList = []
DareList =[]
ResultList = []
from random import randint
import random
def play_function():
    type_of_gameplay = random.randint(1,5)
    random_dare = randint(0, len(DareList) - 1)
    for player_name in PlayerList:
        if PlayerList.index(player_name) + 1 == random_player:
            name_of_random_player = player_name
    for dare in DareList:
        if DareList.index(dare) == random_dare:
            name_of_random_dare = dare
    if type_of_gameplay == 1:
        print """
""" + name_of_random_player + " is the King."
        print "Congrats, you are the King! Your word is absolute!"
        kings_dare_verified = False
        while kings_dare_verified == False:
            kings_dare = raw_input("What will be the King's dare?: ")
            if len(kings_dare) == 0:
                print "Don't leave this blank!"
            else:
                kings_dare_verified = True
        victim_of_king_verified = False
        while victim_of_king_verified == False:
            victim_of_king = raw_input("""NOTE: The King is Person """ + str(random_player) + " and there are " + str(len(PlayerList)) + """ players in the game.
Who will the King use their dare upon? (Use a number to represent the person): """)
            if not victim_of_king.isdigit():
                print "Please put in a number that represents the person."
            elif int(victim_of_king) == random_player:
                print "You can't give a dare to yourself."
            elif int(victim_of_king) > len(PlayerList):
                print "There are " + str(len(PlayerList)) + " players, and Person " + victim_of_king + " is not one of them."
            elif len(victim_of_king) == 0:
                print "Don't leave this blank!"
            else:
                victim_of_king_verified = True
                for player_name in PlayerList:
                    if PlayerList.index(player_name) + 1 == int(victim_of_king):
                        name_of_victim = player_name
    else:
        print """
The dare for Person """ + str(random_player) + """ includes the following instructions:
""" + name_of_random_dare
    something = raw_input("Press enter to reveal the number of each player: ")
    print "The randomly generated players and their names are:"
    for player_name in PlayerList:
        print "Person " + str(PlayerList.index(player_name) + 1) + " is " + player_name
    win_or_lose_verified = False
    while win_or_lose_verified == False:
        win_or_lose = raw_input("Did the dared person successfully complete their dare?: ")
        if win_or_lose.lower() == "yes":
            win_or_lose_verified = True
            question_or_not_verified = False
            while question_or_not_verified == False:
                question_or_not = raw_input("Was the dare a question?: ")
                if question_or_not.lower() == "yes":
                    question_or_not_verified = True
                    answer = raw_input("What did the player answer for the question?: ")
                    if type_of_gameplay == 1:
                        new_result = name_of_victim + " was given the question '" + kings_dare + "' by King " + name_of_random_player + " and answered it with '" + answer + "'."
                        ResultList.append(new_result)
                        print "Good job for answer a the King's question! I hope it wasn't too hard!"
                    else:
                        new_result = name_of_random_player + " was given the question '" + name_of_random_dare + "' and answered it with '" + answer + "'."
                        ResultList.append(new_result)
                        print "Good job for answering that question! I hope that wasn't too hard!"
                elif question_or_not.lower() == "no":
                    question_or_not_verified = True
                    if type_of_gameplay == 1:
                        new_result = name_of_victim + " was given the dare '" + kings_dare + "' by King " + name_of_random_player + " and won."
                        ResultList.append(new_result)
                        print "Good job for doing the King's dare! I hope it wasn't too hard!"
                    else:
                        print "Good job for doing the dare! I hope that wasn't too hard!"
                        new_result = name_of_random_player + " was given the dare '" + name_of_random_dare + "' and won."
                        ResultList.append(new_result)
                elif len(question_or_not) == 0:
                    print "Don't leave this blank!"
                else:
                    print "Please enter yes or no!"
        elif win_or_lose.lower() == "no":
            win_or_lose_verified = True
            if type_of_gameplay == 1:
                new_result = name_of_victim + " was given the dare '" + kings_dare + "' by King " + name_of_random_player + " and lost."
                ResultList.append(new_result)
                print "It's a shame you didn't win against the King. Better luck next time."
            else:
                print "Hmm... were they too chicken to do it? Better luck next time."
                new_result = name_of_random_player + " was given the dare '" + name_of_random_dare + "' and lost."
                ResultList.append(new_result)
        elif len(win_or_lose) == 0:
            print "Don't leave this blank!"
        else:
            print "Please put in either yes or no!"
def family_and_friend_dares_function():
    DareList.append("Starting from 1000, count backwards by 7.")
    DareList.append("Do a dance requested by Person " + str(random_victim))
    DareList.append("Sing a song in a foreign accent.")
    DareList.append("Dance with no music.")
    DareList.append("Let Person " +  str(random_victim) + " draw something on your face with pen.")
    DareList.append("Do 10 push ups.")
    DareList.append("What feature about you do you get complimented on the most?")
    DareList.append("Draw Person " + str(random_victim))
print "Hello, and welcome to the King's Dare game by Hania."
game_command = ""
while game_command != "quit":
    game_command = raw_input("""
What would you like to do? See below for a list of commands:
"play" - Play a round of the game
"help" - Give instructions on how to play
"add a player" - Add another player to join the game
"add a dare" - Adds a dare to be put in the game
"remove a dare" - Removes a pre-existing dare
"remove a player" - Remove a player that left the game
"print" - Display the current up to date results of the game
"quit" - End the program
Type one of the commands above in the following space: """)
    if game_command.lower() == "play":
        if len(PlayerList) < 3:
            print """
Not enough players to start the game. A minimum of 3 players is required."""
        elif len(DareList) < 9:
            print """
Not enough dares to start the game. A minimum of 9 dares is required."""
            CPU_dare_game_verified = False
            while CPU_dare_game_verified == False:
                CPU_dare_game = raw_input("Would you like to play with already-made dares?: ")
                if len(CPU_dare_game) == 0:
                    print "Don't leave this blank! Write yes or no!"
                elif CPU_dare_game.lower() == "no":
                    print "Okay. Add more dares to play the game."
                    CPU_dare_game_verified = True
                elif CPU_dare_game.lower() == "yes":
                    CPU_dare_game_verified = True
                    type_of_dares_verified = False
                    while type_of_dares_verified == False:
                        type_of_dares = raw_input("What category would you like? (Pick family, friends, or truth): ")
                        if type_of_dares.lower() == "family" or type_of_dares.lower() == "relatives":
                            random.shuffle(PlayerList)
                            random_player = randint(1, len(PlayerList))
                            type_of_dares_verified = True
                            family_and_friend_dares_function()
                            play_function()
                        elif type_of_dares.lower() == "friend" or type_of_dares.lower() == "friends":
                            random.shuffle(PlayerList)
                            random_player = randint(1, len(PlayerList))
                            random_victim = randint(1,len(PlayerList))
                            while random_victim == random_player:
                                random_victim = random.randint(1,len(PlayerList))
                            type_of_dares_verified = True
                            family_and_friend_dares_function()
                            DareList.append("Sing an anime song.")
                            DareList.append("Imitate Person " + str(random_victim))
                            DareList.append("If you can bring one person to your college as a room mate, who would they be?")
                            DareList.append("Lay your head on Person " + str(random_victim) +"'s shoulder.")
                            DareList.append("Give a pickup line to Person " + str(random_victim))
                            DareList.append("Make a diss track about Person " + str(random_victim))
                            DareList.append("Sing a love song to Person " + str(random_victim))
                            DareList.append("If you could be invisible whenever you want, what's the first thing you would do?")
                            DareList.append("Personality or looks?")
                            DareList.append("Summarize a story to make the story sound weirder than it is and have Person " + str(random_victim) + " guess the story.")
                            DareList.append("What is the weirdest thing you've dreamed about?")
                            DareList.append("What is your worst fear?")
                            DareList.append("Have you ever wished you were raised differently?")
                            play_function()
                        elif type_of_dares.lower() == "truth" or type_of_dares.lower() == "questions":
                            random.shuffle(PlayerList)
                            random_player = randint(1, len(PlayerList))
                            random_victim = randint(1,len(PlayerList))
                            while random_victim == random_player:
                                random_victim = random.randint(1,len(PlayerList))
                            type_of_dares_verified = True
                            DareList.append("What makes you happy?")
                            DareList.append("Who's one stranger that you still remember?")
                            DareList.append("If you can bring one person to your college as a room mate, who would they be?")
                            DareList.append("Would you like to be famous, and if so, in what way?")
                            DareList.append("If there is a crystal ball that will tell you your life, future, and so forth, what will you ask?")
                            DareList.append("Complete the sentence: I wish I can have someone of whom I can share ______ with")
                            DareList.append("Tell Person " + str(random_victim) + " something you like about them.")
                            DareList.append("What would be the ideal way for you to die?")
                            DareList.append("What does it feel like to crush on someone?")
                            DareList.append("Personality or looks?")
                            DareList.append("Have you ever been heartbroken?")
                            DareList.append("What is your worst decision so far?")
                            DareList.append("When's the last time you cried?")
                            DareList.append("Name a conflict in your life that impacted who you are today?")
                            DareList.append("What is your biggest regret?")
                            DareList.append("What's the nicest thing you've done to someone?")
                            DareList.append("What's the nicest thing someone has done for you?")
                            DareList.append("What song describes you? If you can, sing your favorite line.")
                            DareList.append("How have you changed since you were young?")
                            DareList.append("If your younger self could see you and who they became, what would be something they're disappointed about?")
                            DareList.append("What's something beautiful about you?")
                            DareList.append("How have you changed?")
                            DareList.append("What's the best advice you've been given?")
                            DareList.append("What moment did you felt most alive?")
                            DareList.append("What's the biggest lie you've told?")
                            DareList.append("If your life was a movie, what would be the title?")
                            DareList.append("What is your favorite memory?")
                            DareList.append("What would be your first impression of yourself?")
                            DareList.append("What's your biggest pet peeve?")
                            DareList.append("What's one thing you change about yourself?")
                            DareList.append("When did you realize you're not like everyone else?")
                            DareList.append("What's one strange fact about you?")
                            DareList.append("If you had to live without one of your five sense, which would it be?")
                            DareList.append("If you can have one super power (NOT OP), what will it be and why did you pick it?")
                            DareList.append("What is the worst thing you've ever done?")
                            DareList.append("What's the last thing you searched in up?")
                            DareList.append("What is your worst fear?")
                            play_function()
                        elif len(type_of_dares) == 0:
                            print "Don't leave this blank!"
                        else:
                            print "Please answer with yes or no!"
                else:
                    print "Please answer with either yes or no!"
        else:
            random.shuffle(PlayerList)
            random_player = randint(1, len(PlayerList))
            random_victim = randint(1,len(PlayerList))
            while random_victim == random_player:
                random_victim = random.randint(1,len(PlayerList))
            play_function()
    elif game_command.lower() == "add a dare":
        dares_to_put = " " #how many more dares a player wants to put
        dares_already_put = 0 #how many extra dares the players has put
        question_verified = False #whether they have put an answer to the question "How many more dares?"
        while question_verified == False:
            dares_to_put = raw_input("""
How many dares would you like to put?: """)
            if len(dares_to_put) == 0:
                print "Don't leave any inputs blank."
            elif dares_to_put.lower() == "idk" or dares_to_put.lower() == "unsure":
                print "Add as many dares as you want until it's enough!"
                question_verified = True
                anonymous_verified = False
                print """
NOTE: When writing the dare, do NOT include the names of any players.
Instead of saying "I dare you to fight Bob", say "I dare you to fight Person #/#".
'Person #/#' will be a randomized player. The first '#' represents the player, 
while the second '#' is only for when the first '#' is the same number as the 
person who's doing the dare. 
For example, if Person 2 gets the dare of fighting Person 2, Person 2 can't do 
anything.  In that scenario, instead of saying 'Person 2', say 'Person 2/5', 
where '5' represents the substitute of Person 2 when Person 2 is the one who's dared.
NOTE: Also, you may include questions as a dare.
"""
                more_dares = True
                while more_dares == True:
                    anonymous_verified = False
                    while anonymous_verified == False:
                        anonymous = raw_input("Would you like the dare you're about to add be hidden?: ")
                        if anonymous.lower() == "yes":
                            anonymous_verified = True
                            print "(YES, you're typing something. In order to keep it hidden and anonymous, what you typed is not shown but it WILL be saved.)"
                            if dares_already_put == 0:
                                dare = getpass("""What dare would you like to add?: """)
                                if len(dare) == 0:
                                    print "Don't leave anything empty."
                                else:
                                    DareList.append(dare.capitalize())
                                    print "Your dare has been added."
                                    dares_already_put += 1
                                    more_dares_verified = ""
                                    more_dares_verified = raw_input("Would you like to add another dare?: ")
                                    if more_dares_verified.lower() == "yes":
                                        more_dares = True
                                    elif more_dares_verified.lower() == "no":
                                        more_dares = False
                                    elif len(more_dares_verified) == 0:
                                        print "Don't leave this blank!"
                                    else:
                                        print "Please put 'yes' or 'no'."
                            else:
                                dare = getpass("""What is your next dare?: """)
                                if len(dare) == 0:
                                    print "Don't leave anything empty."
                                else:
                                    DareList.append(dare.capitalize())
                                    print "Your dare has been added."
                                    dares_already_put += 1
                                    more_dares_verified = ""
                                    more_dares_verified = raw_input("Would you like to add another dare?: ")
                                    if more_dares_verified.lower() == "yes":
                                        more_dares = True
                                    elif more_dares_verified.lower() == "no":
                                        more_dares = False
                                    elif len(more_dares_verified) == 0:
                                        print "Don't leave this blank!"
                                    else:
                                        print "Please put 'yes' or 'no'."
                        elif anonymous.lower() == "no":
                            anonymous_verified = True
                            if dares_already_put == 0:
                                dare = raw_input("""What dare would you like to add?: """)
                                if len(dare) == 0:
                                    print "Don't leave anything empty."
                                else:
                                    DareList.append(dare.capitalize())
                                    print "Your dare has been added."
                                    dares_already_put += 1
                                    more_dares_verified = ""
                                    more_dares_verified = raw_input("Would you like to add another dare?: ")
                                    if more_dares_verified.lower() == "yes":
                                        more_dares = True
                                    elif more_dares_verified.lower() == "no":
                                        more_dares = False
                                    elif len(more_dares_verified) == 0:
                                        print "Don't leave this blank!"
                                    else:
                                        print "Please put 'yes' or 'no'."
                            else:
                                dare = raw_input("""What is your next dare?: """)
                                if len(dare) == 0:
                                    print "Don't leave anything empty."
                                else:
                                    DareList.append(dare.capitalize())
                                    print "Your dare has been added."
                                    dares_already_put += 1
                                    more_dares_verified = ""
                                    more_dares_verified = raw_input("Would you like to add another dare?: ")
                                    if more_dares_verified.lower() == "yes":
                                        more_dares = True
                                    elif more_dares_verified.lower() == "no":
                                        more_dares = False
                                    elif len(more_dares_verified) == 0:
                                        print "Don't leave this blank!"
                                    else:
                                        print "Please put 'yes' or 'no'."
                        elif len(anonymous) == 0:
                            print "Don't leave this blank!"
                        else:
                            print "Please put 'yes' or 'no'."
            elif not dares_to_put.isdigit():
                print "Please put in a positive integer to represent the number of dares you would like to add."
            elif int(dares_to_put) == 0:
                question_verified = True
                print "Why choose to add a dare if you weren't going to put any?"
            elif int(dares_to_put) > 30:
                question_verified = True
                print "That's quite a lot of dares. If you DO wish to put that many dares, don't do it all at once."
            else:
                print """
NOTE: When writing the dare, do NOT include the names of any players.
Instead of saying "I dare you to fight Bob", say "I dare you to fight Person #/#".
'Person #/#' will be a randomized player. The first '#' represents the player, 
while the second '#' is only for when the first '#' is the same number as the 
person who's doing the dare. 
For example, if Person 2 gets the dare of fighting Person 2, Person 2 can't do 
anything.  In that scenario, instead of saying 'Person 2', say 'Person 2/5', 
where '5' represents the substitute of Person 2 when Person 2 is the one who's dared.
NOTE: Also, you may include questions as a dare.
    """
                while int(dares_to_put) > dares_already_put:
                    question_verified = True
                    anonymous_verified = False
                    while anonymous_verified == False:
                        anonymous = raw_input("Would you like the dare you're about to add be hidden?: ")
                        if anonymous.lower() == "yes":
                            anonymous_verified = True
                            print "(YES, you're typing something. In order to keep it hidden and anonymous, what you typed is not shown but it WILL be saved.)"
                            if dares_already_put == 0:
                                dare = getpass("""What dare would you like to add?: """)
                                if len(dare) == 0:
                                    print "Don't leave anything empty."
                                else:
                                    DareList.append(dare.capitalize())
                                    print "Your dare has been added."
                                    dares_already_put += 1
                            else:
                                dare = getpass("""What is your next dare?: """)
                                if len(dare) == 0:
                                    print "Don't leave anything empty."
                                elif int(dares_to_put) == dares_already_put:
                                    print "That's all the dares to add."
                                else:
                                    DareList.append(dare.capitalize())
                                    print "Your dare has been added."
                                    dares_already_put += 1
                        elif anonymous.lower() == "no":
                            anonymous_verified = True
                            if dares_already_put == 0:
                                dare = raw_input("""What dare would you like to add?: """)
                                if len(dare) == 0:
                                    print "Don't leave anything empty."
                                else:
                                    DareList.append(dare.capitalize())
                                    print "Your dare has been added."
                                    dares_already_put += 1
                            else:
                                dare = raw_input("""What is your next dare?: """)
                                if len(dare) == 0:
                                    print "Don't leave anything empty."
                                elif int(dares_to_put) == dares_already_put:
                                    print "That's all the dares to add."
                                else:
                                    DareList.append(dare.capitalize())
                                    print "Your dare has been added."
                                    dares_already_put += 1
                        elif len(anonymous) == 0:
                            print "Don't leave this blank!"
                        else:
                            print "Please put 'yes' or 'no'."
    elif game_command.lower() == "remove a dare":
        if len(DareList) == 0:
            print """
There are no dares to remove. Please add a dare first."""
        else:
            print """
"""
            for dare in DareList:
                print str(DareList.index(dare)) + " : " + dare
            dare_remove = raw_input("""
Which dare would you like to remove? (Type 'clear' to clear everything): """)
            if not dare_remove.isdigit():
                if dare_remove.lower() == "clear" or dare_remove.lower() == "clear all" or dare_remove.lower() == "clear everything" or dare_remove.lower() == "remove all" or dare_remove.lower() == "remove everything" or dare_remove.lower() == "delete all" or dare_remove.lower() == "delete everyhting":
                    del DareList[:]
                    print "All dares have been removed."
                else:
                    print "Please put in an integer corresponding to the dare next time."
            elif int(dare_remove) > len(DareList):
                print "The dare you are trying to remove is not in the game."
            elif len(dare_remove) == 0:
                print "Don't leave anything blank!"
            else:
                del DareList[int(dare_remove)]
                print "The dare has been removed. What else would you like to do?"
    elif game_command.lower() == "add a player":
        players_to_put = " " #how many more players to put
        players_already_put = 0 #how many players have already been put
        question_verified = False #whether they have put an answer to the question ‘How many more players?’
        while question_verified == False:
            players_to_put = raw_input("""
How many players would you like to put?: """)
            if len(players_to_put) == 0:
                print "Don't leave any inputs blank."
            elif not players_to_put.isdigit():
                print "Please put in a positive integer to represent the number of players you would like to add."
            elif int(players_to_put) == 0:
                question_verified = True
                print "Why choose to add a player if you weren't going to put any?"
            elif int(players_to_put) > 30:
                question_verified = True
                print "That's quite a lot of dares. If you DO wish to put that many dares, don't do it all at once.."
            else:
                question_verified = True
                while int(players_to_put) > players_already_put:
                    if players_already_put == 0:
                        player_name = raw_input("What is the player's name?: ")
                        if len(player_name) == 0:
                            print "Don't leave anything empty."
                        else:
                            PlayerList.append(player_name.capitalize())
                            print "The player has been added."
                            players_already_put += 1
                    elif int(players_to_put) == players_already_put:
                        print "That's all the players to add."
                    else:
                        player_name = raw_input("Who is the next player?: ")
                        if len(player_name) == 0:
                            print "Don't leave anything empty."
                        else:
                            PlayerList.append(player_name.capitalize())
                            print "The player has been added."
                            players_already_put += 1
    elif game_command.lower() == "remove a player":
        if len(PlayerList) == 0:
            print """
There are no players to remove. Please add one first."""
        else:
            print """
"""
            for player_name in PlayerList:
                print str(PlayerList.index(player_name)) + " : " + player_name
            player_remove = raw_input("""
Which player would you like to remove?: """)
            if int(player_remove) > len(PlayerList):
                    print "The player you're trying to remove is not part of the game."
            elif not player_remove.isdigit():
                print "Please put in an integer corresponding to the player next time."
            elif len(player_remove) == 0:
                print "Don't leave anything blank!"
            else:
                del PlayerList[int(player_remove)]
                print "The player has been removed. What else would you like to do?"
    elif game_command.lower() == "print":
        if len(ResultList) == 0:
            print """
There are no results to display. Please play a game first."""
        else:
            print """
Below are the current results of the game:
            """
            for new_result in ResultList:
                print new_result
    elif game_command.lower() == "help":
        print """
DESCRIPTION:
This game is like Truth or Dare, but it's fair! In Truth or Dare, most people
ask dares targetting to specific people with prejudice. Additionally, people also
ask dares knowing they don't have to do the dare. In this game, I have made a 
system where the dares and players are randomized so you'll never know who has
to do what.
But if you're limited to the dares you add, where's the fun in that? Well, I'll
tell you! There is built-in function in the game where will randomly pick a 
player to be 'the King', whose words are absolute! However, as the role of being
a King is too powerful, I've limited the chance of that feature happening to 20%.

NAVIGATION INSTRUCTIONS:
1) Before playing, add some players and dares. The game would not start if there 
aren't enough of them. If you can't think of any dares, you may use the
pre-made dares and add on the them.
- To add a dare, type 'add a dare'
- To add a player, type 'add a player'
^^^ You cannot misspell those exact commands
---> When writing the dare, do NOT include the names of any players. Also, you 
may include questions as a dare.
2) If you put in the wrong player/dare, accidentally misspelled one, or realize
that one of them is not needed for the game, you can remove them.
- To remove a dare, type 'remove a dare'
- To remove a player, type 'remove a player'
^^^ You cannot misspell those exact commands
---> When you delete them, make sure to put the right number that corresponds 
to the player/dare you wish to delete. Otherwise, you may end up removing the
wrong player/dare.
3) In order to play, you must start a game.
- To start the game, type 'play'
^^^ You cannot misspell that exact command
4) Having fun and forgot what happened in the game? No worries! You can find the
results by printing them.
- To print the results, type 'print'
^^^ You cannot misspell that exact command

PLAYING INSTRUCTIONS:
When the game starts, it will pick a random dare for a random person to do.
This random person will be known as 'Person #'. Each player will be assigned a 
random number, and one of those players will have to do the dare.
Additionally, at least one of the dares would allow a random person to be the King.
1) If you don't have enough dares but you have enough players, you can use the
premade dares. These dares come in three categories:
- Family: Limited and kid-friendly
- Friends: More lineant, casual, and fun
- Truth: ONLY questions
2) Randomly, a person will be crowned as a King. When they ask for the dare, put
in the dare but do NOT specify the person that has to do the dare. The program
will ask that question after you write down the dare. 
3) The program will also ask if the person dared has done the dare. This info
is used when printing the results.
4) When the program asks 'Is the dare a question?', it wants to know if the dare
allows the player to answer something. This is important because the computer
will later ask what the player answered. This info will be used when printing
the results of the game.
5) Have fun and I hope you'll enjoy this!
"""
    elif len(game_command) == 0:
        print """
Don't leave the command blank, please."""
    elif not game_command.lower() == "quit":
        print """
Please do one of the commands below."""

print """
Goodbye. Thanks for playing, and I hope you had fun!"""

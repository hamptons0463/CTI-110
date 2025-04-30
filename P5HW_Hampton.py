## Stephanie Hampton
## Date 04.21.2025
## P5LAB
## Spelling Game
## guess how to spell different emoji with 2 modes

## if possible store top score. 
## maybe

#pip install art
#pip install emoji
## librarys to import
from art import *
import random
import time

def spelling_words():
    ## words and emojis associated for spelling

    words_emojis = {"👻" : 'ghost', "👽" : 'alien', "🦷" : 'tooth',"👑" : 'crown',"📞" : 'phone',"⛵️" : 'boat', "🥕" : 'carrot',"💀" : 'skull', "🤖" : 'robot', "🧠" : 'brain', "👗" : 'dress', "🎩" : 'hat', "👟" : 'shoe', "🐇" : 'bunny', "🐪" : 'camel', "🌙" : 'moon', "🌳" : 'tree', "🌈" : 'rainbow', "🌊" : 'wave', "🍋" : 'lemon', "🍪" : 'cookie', "🥄" : 'spoon', "🧂" : 'salt', "🛷" : 'sled', "🎸" : 'guitar', "🏆" : 'trophy', "🚗" : 'car',"🏈" : 'football', "🚀" : 'rocket', "🏠" : 'house', "🏰" : 'castle', "💰" : 'money', "🧺" : 'basket', "📎" : 'clippy', "🕙" : 'clock', "💍" : 'ring'}

    return words_emojis
    
def player_character2():

    player_name2 = 'na'
    ## asking for player name
    confirm_player_name2 = 'n'
    while confirm_player_name2.lower() == 'n':
        print()
        player_name2 = input("What is your name? ")
        confirm_player_name2 = input(f"You entered '{player_name2}' is that correct? (y/n) ").lower()
    
    correct_answers = 0
    wrong_answers = 0
    hints = 3
    
    player2 = {"name" : player_name2, "hints" : hints, "correct_answers" : correct_answers, "wrong_answers" : wrong_answers}

    return(player2)

def player_character():

    ## asking for player name
    player_name = 'na'
    confirm_player_name = 'n'
    while confirm_player_name.lower() != 'y':
        print()
        player_name = input("What is your name? ")
        confirm_player_name = input(f"You entered '{player_name}' is that correct? (y/n) ").lower()
    
    ## difficulty level?
    lifeline_confirm = 'n'

    while lifeline_confirm.lower() != 'y':
        print()
        print("What level of difficulty do you want?")
        print()
        print("(1) Elite: 1 Life, 0 hints \n(2) Challenge: 2 lives, 2 hints\n(3) Easy: 3 lives, 3 hints")
        print()

        hints = int(input("Enter the associated number to your challenge rating: "))

        if hints == 3:
            retry = 3
            lifeline_confirm = input("You selected Easy. Correct? (y/n) ")
        elif hints == 2:
            retry = 2
            lifeline_confirm = input("You selected Challenge. Correct? (y/n) ")
        elif hints == 1:
            hints = 0
            retry = 1
            lifeline_confirm = input("You selected Elite. Correct? (y/n) ")
        else:
            print("Sorry, that selection is incorrect please try again. ")

        retry_starting_value = retry

        ## correct answers to win

        correct_answers = 0
    
    print()

    player = {"name" : player_name, "hints" : hints, "lives" : retry, "starting_lives" : retry_starting_value, "correct_answers" : correct_answers}

    return(player)

def spelling_words_empty_questionmark(words_emojis):
    ## check if dict is empty before continuing the game. If empty end game. 

    if len(words_emojis) == 0:
        print()
        print("Congratulations! You have spelled all the emojis in the game!")
        print()
        print("I can teach you nothing else. The student has become the master.")
        print()
        tprint("Great Work","rand")
        time.sleep(3)
        return True
    
    else:
        return False
        

def p1end_game_statement(player):
    good_job = {"You are on 🔥!", "You're the zest! 🍊", "You did a 🍇 job!","That was magical 🪄🪄🪄", "You are one smart 🍪", "You are doing 🦕-mite!", "You are a ⭐!", "You got 🥇 place!"}
    bad_job = {"Your score is a joke!🤡", "Even the monkey doesnt want to see your score! 🙈", "Well bless your heart 💔", "🧚‍♀️ Even the fairy god-mother couldn't save your score.", "That was a farce. 🎭", "Participation award. 🥉"}

    if player['correct_answers'] >= 5:
        print(random.choice(list(good_job)))
    else:
        print(random.choice(list(bad_job)))

def p2end_game_statement(player2):
    good_job = {"You are on 🔥!", "You're the zest! 🍊", "You did a 🍇 job!","That was magical 🪄🪄🪄", "You are one smart 🍪", "You are doing 🦕-mite!", "You are a ⭐!", "You got 🥇 place!"}
    bad_job = {"Your score is a joke!🤡", "Even the monkey doesnt want to see your score! 🙈", "Well bless your heart 💔", "🧚‍♀️ Even the fairy god-mother couldn't save your score.", "That was a farce. 🎭", "Participation award. 🥉"}

    if player2['correct_answers'] > player2['wrong_answers']:
        print (random.choice(list(good_job)))
    else:
        print (random.choice(list(bad_job)))

def spell_check(words_emojis, player):

    print("Spell the emoji's!")
    time.sleep(2)
    # get emoji from emoji dict in own function
    
    ## while statement for user entered spelling
    ## i am pretty sure easier way but this is the way we goin

    while player['lives'] > 0:

        if spelling_words_empty_questionmark(words_emojis):
            time.sleep(1)
            break

        #assign rando emoji to a variable
        random_emoji_to_use = random.choice(list(words_emojis.keys()))
        #assign associated rando value to a variable
        random_emoji_spelling = words_emojis[random_emoji_to_use]

        print()

        # player input for spelling
        player_spelling = input(f"How do you spell:{random_emoji_to_use}? ").lower()
        print()

        time.sleep(1)

        if player_spelling == random_emoji_spelling:

            print(f"Correct, {player['name']}!")
            print()
            time.sleep(1)
            print(f"You have {player['hints']} hints remaining and {player['lives']} lives left.")

            player['correct_answers'] = player['correct_answers'] + 1

            ## remove emoji from dict so wont be reused.
            words_emojis.pop(random_emoji_to_use)

        ## if spelling is wrong and still have lifeline then give hint

        else:
            while player_spelling != random_emoji_spelling:
                
                if player['hints']  >= 1:
                    print(f"Incorrect, {player['name']}!")
                    print()
                    time.sleep(1)
                    ## deduct a hint point
                    player['hints'] = player['hints'] - 1

                    ## hint
                    random_letter = random.choice(random_emoji_spelling)

                    print(f"Here is a hint.")
                    print(f"The {random_emoji_to_use} is spelled using the letter '{random_letter}'.")
                    print(f"You have {player['hints']} hints remaining and {player['lives']} lives left.")
                    print()
                    time.sleep(1)
                    player_spelling = input(f"How do you spell:{random_emoji_to_use}? ").lower()
                    print()

                    if player_spelling == random_emoji_spelling:

                        print(f"Correct, {player['name']}!")
                        print()
                        time.sleep(1)
                        print(f"You have {player['hints']} hints remaining and {player['lives']} lives left.")

                        player['correct_answers'] = player['correct_answers'] + 1

                        ## remove emoji from dict so wont be reused.
                        words_emojis.pop(random_emoji_to_use)
                
                elif player['lives'] > 1:
                    ## must remove a life 
                    player['lives'] = player['lives'] - 1
                    ## add a wrong answer point
                    time.sleep(1)
                    print(f"You have run out of hints. You have still have {player['lives']} lives left.")
                    time.sleep(1)
                    print(f"Try again.")
                    print()
                    time.sleep(1)

                    player_spelling = input(f"How do you spell:{random_emoji_to_use}? ").lower()
                    print()

                ## ends game
                else:
                    time.sleep(2)
                    print()
                    print(f"Game Over, {player['name']}!")
                    time.sleep(1)
                    print()
                    print(f"You got {player['correct_answers']} correct.")
                    time.sleep(1)
                    p1end_game_statement(player)
                    time.sleep(5)
                    return
                    
        ## remove emoji from dict so wont be reused.
        #words_emojis.pop(random_emoji_to_use)

        

def spelling_test(words_emojis, player2):
    ## eight questions, final one is no hints. get 3 hints in total. steal from how to play.

    ## implemint timed difficulty if time allows...need to look up

    print()
    print("Prepare for your quiz!")
    print()
    time.sleep(1)
    print("...3")
    time.sleep(1)
    print("...2")
    time.sleep(1)
    print("...1")
    time.sleep(1)
    print
    print()
    print("GO!")
    print()
    time.sleep(.5)

    ## number of questions to ask will ask final at end

    #assign rando emoji to a variable

    for x in range(1,8):

        #assign associated rando value to a variable
        random_emoji_to_use = random.choice(list(words_emojis.keys()))
        random_emoji_spelling = words_emojis[random_emoji_to_use]

        #show hints left
        time.sleep(.5)
        print()
        print(f"Type 'hint' for a little extra help.")
        print(f"You have {player2['hints']} remaining.")
        print()

        ## asking user if to spell emoji
        user_emoji_spelling = input(f"{x}) {random_emoji_to_use} ").lower()
        
        while user_emoji_spelling == 'hint':

            if player2['hints'] == 0:
                time.sleep(1)
                print("You have no more hints available.")
                print()
            
            else:
                random_letter = random.choice(random_emoji_spelling)
                time.sleep(1)
                print(f"{random_emoji_to_use} contains the letter '{random_letter}'.")
                print()
                player2['hints'] = player2['hints'] - 1

            time.sleep(1)
            user_emoji_spelling = input(f"{x})How do you spell '{random_emoji_to_use}'? ").lower()

        else:

            if user_emoji_spelling == random_emoji_spelling:
                player2['correct_answers'] = player2['correct_answers'] + 1
            else:
                player2['wrong_answers'] = player2['wrong_answers'] + 1

        ## remove so no duplicates
        words_emojis.pop(random_emoji_to_use)

    ## final question
    
    random_emoji_to_use = random.choice(list(words_emojis.keys()))
    random_emoji_spelling = words_emojis[random_emoji_to_use]

    time.sleep(1)
    print()
    print("This is the final question. Hints are not available.")
    print()
    time.sleep(1)
    user_emoji_spelling = input(f"8) {random_emoji_to_use} ").lower()
    
    if user_emoji_spelling == random_emoji_spelling:
        player2['correct_answers'] = player2['correct_answers'] + 1
    else:
        player2['wrong_answers'] = player2['wrong_answers'] + 1
    time.sleep(1)
    print()
    print(f"Game Over, {player2['name']}!")
    time.sleep(1)
    print()
    print(f"You got {player2['correct_answers']} right and {player2['wrong_answers']} wrong.")
    print()
    time.sleep(1)
    p2end_game_statement(player2)
    print()
    time.sleep(1)

def how_to_play():
    print (" = = = HOW TO PLAY = = = ")
    print()
    print(" (1) Standard \n (2) Spelling Test \n (3) Main Menu")
    print()
    how_to_play = int(input("Please make your selection: "))
    print()
    if how_to_play == 1:
        time.sleep(1)
        print("Standard.")
        print()
        time.sleep(.5)
        print("Spell the words the emojis represent.")
        print("No spaces, all lower-case.")
        print("You will have a set number of hints,") 
        print("depending on your selected difficulty.")
        print("Once your hints are exhausted, your lives") 
        print("will be deducted until they reach zero.")
        print("At that point it will be game over.")
        print()
        time.sleep(5)
    elif how_to_play == 2:
        time.sleep(1)
        print("Spelling Test.")
        print()
        time.sleep(.5)
        print("Spell the words the emoji's represent.")
        print("No spaces, all lower-case. ")
        print("There will be eight emoji's")
        print("on your spelling test.")
        print("You will have 3 hints.")
        print("The final emoji must be solved without ANY help.")

        print()
        time.sleep(5)
    else:
        print("Returning to Main Menu")
        time.sleep(5)
    return
   

def main():
    
    print()
    print("="*32)
    print("= 🐸🐗🪼  Spelling Bee  🐐🦨🦐 =")
    print("="*32)
    print()

    menu_option = '0'
    while menu_option != '4':
        print()
        print("Please choose from the options below to get started. 😺")
        print()
        print(" (1) Standard \n (2) Spelling Test  \n (3) How to play \n (4) Exit. ")
        print()
        menu_option = input("Where do you want to go? ")
        print()

        if menu_option == '1':
            #start gameplay
            print("Welcome!")
            #player_character()
            player = player_character()
            spell_check(spelling_words(),player)
            print()
            
        elif menu_option == '2':

            #start gameplay
            print("Welcome!")
            #player character()
            player2 = player_character2()
            spelling_test(spelling_words(),player2)

            pass
        elif menu_option == '3':
            
            how_to_play()

        elif menu_option == '4':
        
            print()
            print("Thank you for playing!")
            print("Game is closing")
            print()
            break

    else:
        print("That was not a valid selection, please try again. ")


if __name__ == "__main__":
    main()


from gameplay.game import Game
from scripts.split_difficulty import Dificulty
import requests

language = input("Please, choose language (LV/ENG) : ").upper()

if language == "LV":
    
    if_new_words = Dificulty(words_all=1)
    if_new_words.diff()

    difficulty_info = 'Hello!', 'There are 3 difficulty levels:"\n"1st - bez garumzīmēm un mīkstinājumiem and more than 6 letters"\n"2nd - ar garumzīmēm un mīkstinājumiem and more than 6 letters"\n"3rd - ar garumzīmēm un mīkstinājumiem and less than 6 letters'
    ## ievadi varbūt vajag while ciklā -> atkārtoti prasa ievadi, kamēr izvēlas 1 no trim
    print(difficulty_info)

    while True:
        difficulty = input("Please, choose your game difficulty level (easy/medium/hard) : ")

        if difficulty == 'easy':
            with open('data/easy_words.txt', 'r', encoding='utf-8') as file:
                file_contents = file.read()
                break
        elif difficulty == 'medium':
            with open('data/medium_words.txt', 'r', encoding='utf-8') as file:
                file_contents = file.read()
                break
        elif difficulty == 'hard':
            with open('data/hard_words.txt', 'r', encoding='utf-8') as file:
                file_contents = file.read()
                break
        else:
            print("Invalid input!")

    words = list(file_contents.split("', '"))

    # Spēles palaišana 

    while True:
        word = words.pop()
        game = Game(word)
        game.play()
        
        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again == "y": 
            continue
        else: 
            break
        
elif language == "ENG" :
    
    url = 'https://random-word-api.herokuapp.com/word?number=1'
    response = requests.get(url)
    json_response = response.json()
    
    game = Game(json_response[0])
    game.play()

else:
    print("You can only choose LV or ENG")
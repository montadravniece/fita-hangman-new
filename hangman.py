import random
from gameplay.game import Game

# Tika ielasīts vārda saraksts
with open('data/words.txt', 'r', encoding='utf-8') as file: 
    file_content = file.read()
    words = file_content.split("\n")
    random.shuffle(words)
    
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
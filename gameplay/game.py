import random

# Spēles pamatfunkcijas 

words = "JAKA" ,"KURMIS", "SNIEGS"

word = random.choice(words)
word_progress = list(len(word) * "-")

lives = 6
word_is_guessed = False
guessed_letters = set()
missed_letters = set()
missed_words = set()

def print_status():
    print(f"Word: {''.join(word_progress)}")
    print(f"Lives: {lives}")
    print(f"Missed letters: {', '.join(missed_letters)}")
    print(f"Missed words: {', '.join(missed_words)}")

# Spēles kods 

while lives > 0 and word_is_guessed == False:
    print_status()
    
    guess = input("Please try and guess a letter: ").upper()

    if len(guess) == 0:
        # Ja nav ievadīts nekas
        print("Enter at least one letter")
        continue
    elif len(guess) == 1:
        # Ja ievadīts viens simbols
        if not guess.isalpha():
            print("Please enter a letter")
            continue
        
        if guess in guessed_letters or guess in missed_letters:
            print("You already tried this letter")
            continue
        
        if guess in word:
            print("Correct you guessed a letter")
            guessed_letters.add(guess)
            # Atklājam atminētos burtus
            for index, letter in enumerate(word):
                if letter in guessed_letters:
                    word_progress[index] = letter
            # Pārbaudam vai vārds ir atminēts
            if word == ''.join(word_progress):
                word_is_guessed = True
        else:
            print("Wrong! Please try guessing another letter")
            missed_letters.add(guess)   
            lives -= 1
            
    else:
        # Ja ievadīti vairāki simboli
        if len(guess) != len(word):
            print("Word lenght in not correct try again")
            continue
        
        if guess in missed_words:
            print("You already tried this word")
            continue
            
        if word == guess:
            word_is_guessed = True
        else:
            print("Wrong word") 
            missed_words.add(guess)
            lives -= 1    
        
    print()
    
if word_is_guessed:
    print("Congrats You WON! ")
else:
    print("You Lost")
    print(f"Correct word: {word}")
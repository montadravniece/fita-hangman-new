class Game:
    def __init__(self, word):
        self.word = word
        self.word_progress = list(len(word) * "-")
        self.lives = 6
        self.word_is_guessed = False
        self.guessed_letters = set()
        self.missed_letters = set()
        self.missed_words = set()

    # Spēles funkcijas

    def print_status(self):
        print()
        print(f"Word: {''.join(self.word_progress)}")
        print(f"Lives: {self.lives}")
        print(f"Missed letters: {', '.join(self.missed_letters)}")
        print(f"Missed words: {', '.join(self.missed_words)}")
        print()

    # Spēles kods 
    
    def play(self):
        while self.lives > 0 and self.word_is_guessed == False:
            self.print_status()
            
            guess = input("Please try and guess a letter: ").upper()

            if len(guess) == 0:
                # Ja nav ievadīts nekas
                print("Enter at least one letter\n")
                continue
            
            if len(guess) == 1:
                # Ja ievadīts viens simbols
                if not guess.isalpha():
                    print("Please enter a letter\n")
                    continue
                
                if guess in self.guessed_letters or guess in self.missed_letters:
                    print("You already tried this letter\n")
                    continue
                
                if guess in self.word:
                    print("Correct you guessed a letter")
                    self.guessed_letters.add(guess)
                    # Atklājam atminētos burtus
                    for index, letter in enumerate(self.word):
                        if letter in self.guessed_letters:
                            self.word_progress[index] = letter
                    # Pārbaudam vai vārds ir atminēts
                    if self.word == ''.join(self.word_progress):
                        self.word_is_guessed = True
                else:
                    print("Wrong! Please try guessing another letter")
                    self.missed_letters.add(guess)   
                    self.lives -= 1       
            else:
                # Ja ievadīti vairāki simboli
                if len(guess) != len(self.word):
                    print("Word lenght in not correct try again\n")
                    continue
                
                if guess in self.missed_words:
                    print("You already tried this word\n")
                    continue
                    
                if self.word == guess:
                    self.word_is_guessed = True
                else:
                    print("Wrong word") 
                    self.missed_words.add(guess)
                    self.lives -= 1    
            
        print("\nGame over!")
        if self.word_is_guessed:
            print("Congrats You WON!")
            print(f"Word: {self.word}")
        else:
            print("You Lost!")
            print(f"Correct word: {self.word}")
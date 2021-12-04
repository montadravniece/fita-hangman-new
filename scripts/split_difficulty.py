class Dificulty:
    def __init__(self, words_all):
        self.words_all = words_all

    def diff(self):
        with open('data/words.txt', 'r', encoding='utf-8') as file:
            words_all = file.read()

        words_split = []
        words_split = words_all.split("\n")

        easy_words = []
        medium_words = []
        hard_words = []

        hard_letters = ['Ā', 'Č', 'Ē', 'Ģ', 'Ī', 'Ķ', 'Ļ', 'Ņ', 'Š', 'Ū', 'Ž']

        # izveido vārdnīcu -> katram vārdam unikālo simbolu skaits
        # unique_count_word = {}
        # for word in words_split:
        #   unique_count_word[word] = len(set(word))

        # print(unique_count_word)
        ########

        # dificulty 3
        for words in words_split:
            for character in hard_letters:
                if character in words and len(words) < 7:
                    hard_words.append(words)

        # dificulty 2
        for words in words_split:
            for character in hard_letters:
                if character in words and len(words) > 6:
                    medium_words.append(words)

        # difficulty 1

        a = set(words_split)
        b = set(hard_words)
        c = set(medium_words)
        easy_words = a - b - c

        # cikls, kas vienkārši sadala visus vārdus 3 sarežģītības pakāpēs tikai pēc vārda garuma
        # for word in words_split:
        #   if len(word) > 6:
        #     easy_words.append(word)
        #   elif len(word) > 14:
        #     hard_words.append(word)
        #   else:
        #     medium_words.append(word)
        # ####

        # print(easy_words)

        with open('data/easy_words.txt', 'w', encoding='utf-8') as file:
            file.write(str(set(easy_words)))

        with open('data/medium_words.txt', 'w', encoding='utf-8') as file:
            file.write(str(set(medium_words)))

        with open('data/hard_words.txt', 'w', encoding='utf-8') as file:
            file.write(str(set(hard_words)))

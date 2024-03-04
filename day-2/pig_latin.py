"""
    Pig  Latin is a word game that transforms english words
    to a parody of  latin:

    if a word begins with consonant
        - remove the letter
        - put the letter in the last
        - add 'ay' following the letter
    if the word brgins with vowel
        - simply add 'yay' to the last
"""
class PigLatin():
    vowels = ['a', 'e' , 'i', "o", 'u']
    def __init__(self, eng):
        self.eng = eng
    
    def piggy(self):
        words = self.split_eng(self.eng)
        piggy = ""
        for word in words:
                if word[0].lower() in self.vowels:
                    piggy +="{} ".format((self.append_last_vowel(word)) ) 
                else:
                    piggy += "{} ".format(self.append_last_consonant(word))  
        print(piggy)

    @staticmethod    
    def split_eng(sentense):
        """ Splits the english sentense and retuns a list of words"""
        return sentense.split(" ")

    @staticmethod
    def append_last_vowel(word):
        return (word + "yay")
    
    @staticmethod
    def append_last_consonant(word):
        first_letter = word[0]
        piggy_word = word[1:] + first_letter + "ay"
        return piggy_word
    
if __name__ == "__main__":
    eng = input("Enter English Sentense: ")
    piggy = PigLatin(eng)
    piggy.piggy()
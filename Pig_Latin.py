def vowel_word(a):
    """Function adds "way" at the end of the word."""   
    add="way"
    output=word+add
    return output

def first_vowel(s):
    """Function finds the index of the first vowel"""
    for index, char in enumerate(s):
        if char in 'aeiou':
            return index

#obtain user input and convert the string into list
words=str(input("Enter a line of text:"))
wordList=words.split()

#Converts English into Pig Latin
for word in wordList:
    
    #Pig Latin word for the English word that starts with a vowel
    if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
        print(vowel_word(word),end=' ')
    
    #Pig Latin word for the English word that does not starts with a vowel
    else:
        p=first_vowel(word)
        term_one=word[p:]
        term_two=word[0:p]
        term_three="ay"
        vocab=(term_one + term_two+term_three)
        print(vocab,end=' ')

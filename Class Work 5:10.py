


print('Welcome to the Pig Latin Translator!')


pyg = 'Sof'

original = input('Enter a word: ')


if len(original) and original.isalpha() > 0:
    word = original.lower()
    first = word[1]

    
 
    new_word = word[1:len(word)] + first + pyg
    print(new_word)
 
else:
    print('empty')


import random
from collections import Counter

someWords = \
    '''random,math,statistics,Counter,dict,keys,values,
dict,keys,values,items,get,update,del,clear,
fromkeys,copy,pop,setdefault,max,min,count,
sorted,copy,len,tuple,count,index,sorted,min,max,sumlen,list, 
append,extend,insert,count,index,remove,pop,reverse,
sort,min,max,sum,len,capitalize,title,upper,lower,count,find,
index,isalnum,islower,isupper,isspace,isalpha,isdigit,split,
partition,strip,lstrip,rstrip,replace'''

m = 1
someWords = someWords.split(',')
while m == True:
    word = random.choice(someWords)
    if __name__ == '__main__':
        print ('Guess the word! HINT: this can be a python module or the name of a function in python')

        for i in word:
            print ('_', end = ' ')
        print ()

        playing = True
        letterGuessed = ''
        chances = len(word) + 2
        correct = 0
        flag = 0
        try:
            while chances != 0 and flag == 0:
                print ()
                chances -= 1

                try:
                    guess = str(input('Enter your first guess: '))
                except:
                    print ('Enter only a letter!')
                    continue

                if not guess.isalpha():
                    print ('Enter only a LETTER')
                    continue
                elif len(guess) > 1:
                    print ('Enter only a SINGLE letter')
                    continue
                elif guess in letterGuessed:
                    print ('You have already guessed that letter')
                    continue

                if guess in word:
                    k = word.count(guess)
                    for _ in range(k):
                        letterGuessed += guess

                for char in word:
                    if char in letterGuessed and Counter(letterGuessed) \
                        != Counter(word):
                        print (char, end = ' ')
                        correct += 1
                    elif Counter(letterGuessed) == Counter(word):

                        print ('The word is: ', end = ' ')
                        print (word)
                        flag = 1
                        print ('Congratulations, You won!')
                        break
                        break
                    else:
                        print ('_', end = ' ')

            if chances <= 0 and Counter(letterGuessed) != Counter(word):
                print ()
                print ('You lost! Try again..')
                print ('The word was {}'.format(word))
        except KeyboardInterrupt:

            print ()
            print ('Bye! Try again.')
            exit()
    continue

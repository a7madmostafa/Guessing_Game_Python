#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint

Actual = randint(1,100)

guesses= [] 
i=0

while(True):
    Guess= int(input('Guess the number:   '))
    guesses.append(Guess)
    
    if Guess < 1 or Guess > 100 :
        print('Out of Bounds')
        continue
        
    elif len(guesses) == 10:
        print(' You tried 10 times and you could not guess the number \n Game Over!')
        print('Actual Number is: ',Actual)
        break
        
    elif Guess == Actual :
        print ("Wow, you've guessed Correctly this time")  
        print('You have guessed it in ' + str(len(guesses)) + ' times')
        break
        
    elif abs(Guess - Actual) <= abs(guesses[i-1] - Actual) :
        print(' you are closer to target ') 
        
    else:  
        print(' you are farther from the target ')
        
    i+=1


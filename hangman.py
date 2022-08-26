#!/usr/bin/env python3

import time

name = input("Please tell me your name! :: \n")
time.sleep(1)
print("Hello {}! \nWelcome to my world!! \n".format(name.upper())) 
time.sleep(1.5)
print("¯\_( ͡• ‿‿ ͡•)_/¯ ¯\_( ͡• ‿‿ ͡•)_/¯ ¯\_( ͡• ‿‿ ͡•)_/¯ \n")
time.sleep(2)
z = input("Are you ready to play game with me? \n")
print ("you said {}".format(z.upper()))

if z in ["Yes", "y", "ya", "yep", "yess", "yes"]:
    print("Woo-hoo!!! \n")
    time.sleep(2)
else:
    print("It is sad to see you go! \n")
    time.sleep(1)
    print("(╥﹏╥) (╥﹏╥) (╥﹏╥) \n")
    exit()

q = input("Please select one from the lists \n A) Countries \n B) Continents \n C) States in the US \n")

if q in ["A", "a"]:
    print("Let's play!")
    
elif q in ["B", "b"]:
    print("Let's go!")
    
elif q in ["C", "c"]:
    print("Let's do it!")
    
else:
    print("You did not select the topic from the list! ... Bye Bye")
    quit()
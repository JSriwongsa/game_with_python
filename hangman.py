#!/usr/bin/env python3

import time

name = input("Please tell me your name! :: \n")
time.sleep(1)
print("Hello {}! Welcome to my world!! \n".format(name)) 
time.sleep(2)
print("¯\_( ͡• ‿‿ ͡•)_/¯ ¯\_( ͡• ‿‿ ͡•)_/¯ ¯\_( ͡• ‿‿ ͡•)_/¯ \n")
time.sleep(3)
z = input("Are you ready to play game with me? \n")
print ("you said {}".format(z))

if z in ["Yes", "y", "ya", "yep", "yess", "yes"]:
    print("Let's go!!! \n")
    time.sleep(2)
else:
    print("It is sad to see you go! \n")
    time.sleep(1)
    print("(╥﹏╥) (╥﹏╥) (╥﹏╥) \n")
    exit()

q = input("Please select one from the lists \n A) Countries in the world \n B) Continents in the world \n C) States in the US \n")

if q in ["A", "a"]:
    country1 = input(" _ _ _ _ _ \n")
    if country1 in ["A", "a"]:
        print("_ a _ a _")
    else:
        print("Please try again!")
elif q in ["B", "b"]:
    region1 = input("_ _ _ _ _ _ _ _ \n")
    if region1 in ["A", "a"]:
        print("A _ _ _ _ _ a _")
    else:
        print("Please try again!")
elif q in ["C", "c"]:
    state1 = input("_ _ _ _ _ \n")
    if state1 in ["A", "a"]:
        print("_ _ a _ _")
    else:
        print("Please try again!")
else:
    print("You did not select the topic from the list! ... Bye Bye")
    quit()



    




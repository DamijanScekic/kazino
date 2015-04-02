# coding=utf-8
from random import randint
secret = randint(1,10)
print("Pozdravljeni v spletni igri UGANI SKRITO STEVILKO!")
guess = 0
while guess != secret:
    g = raw_input("Poizkusi svojo sreco! Ugani stevilko od 1 do 10: ")
    guess = int(g)
    if guess == secret:
        print("Cestitamo! Zadeli ste GLAVNI DOBITEK!")
    else:
        if guess > secret:
            print("Zal, več srece prihodnjic. Namig: dobitna stevilka je manjsa! ")
        else:
            print ("Zal, več srece prihodnjic. Namig: dobitna stevilka je vecja! ")
print("Hvala, nasvidenje!")
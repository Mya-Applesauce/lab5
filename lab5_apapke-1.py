"""
lab5_apapke-1
Ari Papke
dice rolling game
02/14/26
"""

import random

die_results = [1,2,3,4,5,6]

print("Hello there! Let's play a game!")

keep_playing = ""

while keep_playing != "quit":
    keep_playing = input("Ready to roll?")
    if keep_playing == "yes" or "Yes" or "yeah" or "sure" or "ok" or "okay" or "alright":
        result_1 = random.choice(die_results)
        result_2 = random.choice(die_results)
        if keep_playing != "no" or "No":
            if (result_1 + result_2) == 2:
                print(f"Ouch! You got the unfortunate double 1 for a total of 2! That's a Snake Eyes! Better luck next time!")
            elif (result_1 + result_2) == 3:
                print(f"You got a {result_1} & {result_2} for a total of 3! That's an Ace Caught a Deuce!")
            elif (result_1 + result_2) == 4:
                if result_1 == 2:
                    print(f"You got the double 2 for a total of 4! That's a Little Joe from Kokomo!")
                else:
                    print(f"You got a {result_1} & {result_2} for a total of 4!")
            elif (result_1 + result_2) == 5:
                    print(f"You got a {result_1} & {result_2} for a total of 5! That's a Little Phoebe!")
            elif (result_1 + result_2) == 6:
                if result_1 == 3:
                    print(f"You got the double 3 for a total of 6! That's a Jimmy Hicks from the Sticks!")
                else:
                    print(f"You got a {result_1} & {result_2} for a total of 6!")
            elif (result_1 + result_2) == 7:
                if (result_1 == 1) or (result_1 == 6): 
                    print(f"You got a {result_1} & {result_2} for a total of 7! That's a Six Ace!")
                else:
                    print(f"You got a {result_1} & {result_2} for a total of 7!")
            elif (result_1 + result_2) == 8:
                if result_1 == 4:
                    print(f"You got the double 4 for a total of 8! That's a Eighter from Decatur!")
                else:
                    print(f"You got a {result_1} & {result_2} for a total of 8!")
            elif (result_1 + result_2) == 9:
                print(f"You got a {result_1} & {result_2} for a total of 9! That's a Nina from Pasadena!")
            elif (result_1 + result_2) == 10:
                if result_1 == 5:
                    print(f"You got the double 5 for a total of 10! That's a Puppy Paws!")
                else:
                    print(f"You got a {result_1} & {result_2} for a total of 10!")
            elif (result_1 + result_2) == 11:
                if (result_1 == 6) or (result_1 == 5):
                    print(f"You got a {result_1} & {result_2} for a total of 11! That's a Six Five no Jive!")
            elif (result_1 + result_2) == 12:
                if result_1 == 6:
                    print(f"Congrats! You got the lucky double 6 for a total of 12! That's a Boxcars! You're today's big winner!")
            
        else:
            print("See ya later!")
            break

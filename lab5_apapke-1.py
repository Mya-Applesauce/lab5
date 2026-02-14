"""
lab5_apapke-1
Ari Papke
dice terms
02/14/26
"""

import random

die_results = [1,2,3,4,5,6]

while input != quit:
    keep_playing = input("Ready to roll?")
    if keep_playing == "yes" or "Yes" or "yeah" or "sure":
        result_1 = random.choice(die_results)
        result_2 = random.choice(die_results)
        if (result_1 + result_2) == 2:
            print(f"Snake Eyes")
        elif (result_1 + result_2) == 3:
            print(f"Ace Caught a Deuce")
        elif (result_1 + result_2) == 4:
            print(f"Little Joe from Kokomo")
        elif (result_1 + result_2) == 5:
            print(f"Little Phoebe")
        elif (result_1 + result_2) == 6:
            print(f"Jimmy Hicks from the Sticks")
        elif (result_1 + result_2) == 7:
            print(f"Six Ace")
        elif (result_1 + result_2) == 8:
            print(f"Eighter from Decatur")
        elif (result_1 + result_2) == 9:
            print(f"Nina from Pasadena")
        elif (result_1 + result_2) == 10:
            print(f"Puppy Paws")
        elif (result_1 + result_2) == 11:
            print(f"Six Five no Jive")
        elif (result_1 + result_2) == 12:
            print(f"Boxcars")
    elif keep_playing == "no":
        break
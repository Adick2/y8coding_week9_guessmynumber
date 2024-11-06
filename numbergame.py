
from random import randint

correct = randint(16,64)
number = None
while number != correct:
    print("Guess my number")
    number = int(input()) 
    if number > correct:
        print("LOWER!")
    if number < correct:
        print("HIGHER!")
    if number == correct:
        print("YOU WON!!!!!")
    five_less = number - 5
    five_more = number + 5

    if number >= five_less and number <= five_more:
        print("ALMOST! WITHIN 5 AWAY")

# the user will choose a number
# this program will guess the number
# the user will say "yes" or "higher" or "lower"
# the program will ask to play again or exit
guess = 10
number = int(input ("CHOOSE A NUMBER BETWEEN 1 AND 20 "))
while number > 20 or number < 1:
    number = int(input ("YOU PICKED OUTSIDE OF THE RANGE >:C PICK BETWEEN 1 AND 20 "))

correctness = input (f"Is your number {guess}? ")

if guess == number and (correctness == "higher" or correctness == "lower"):
    print ("why would you lie... :C ")

else:
    while correctness == "higher":
        guess = guess + 1
        correctness = input (f"Is your number {guess}? ")

    while correctness == "lower":
        guess = guess - 1
        correctness = input (f"Is your number {guess}? ")


    while correctness == "yes":
        print ("yay!")
        break

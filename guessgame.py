import random

print("Welcome to the random guessing game :)")

def random_number():
    print("I'm thinking of number between 1 to 100.")
    num=random.randint(1,101)
    return num
    
number=random_number()

def difficulty():
    diff = input("choose the type of difficulty type 'easy''medium''hard' :")
    if diff == "easy":
        lives=10
        print("You have 10 attempts to guess the correct number")
    elif diff == "hard":
        lives=5
        print("You have 5 attempts to guess the correct number")
    else:
        lives=7
        print("You have 7 attempts to guess the correct number")
    return lives

no_of_lives=difficulty()
guess_number = False
for guess in range(no_of_lives):
    while not guess_number:
        guess = int(input("Make a guess :"))
        if guess < number:
            print("too low :(")
            no_of_lives-=1
            print(f"You have {no_of_lives} attempts to guess the correct answer ")
        elif guess > number:
            print("too high :(")
            no_of_lives-=1
            print(f"You have {no_of_lives} attempts to guess the correct answer ")
        else:
            print(f"You have won the game guess number is {number} ;)")
            guess_number = True

if no_of_lives == 0:
    print("You have loose the game :(")
else:
    print("congragulations ;)")

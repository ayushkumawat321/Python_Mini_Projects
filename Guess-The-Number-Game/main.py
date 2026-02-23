## GUESS THE NUMBER GAME
import random
print("--------------------------------------------------------------------------")
print("GUESS THE NUMBER GAME:-")
print("--------------------------------------------------------------------------")
print("Rules - Try to guess a random number between 1 to 100")
print("      - If your Guess is Higher than the number , it says 'Try Lower' ")
print("      - If your Guess is Lower than the number , it says 'Try Higher' ")
print("      - Good Luck!")
print("--------------------------------------------------------------------------")
num = random.randint(1,100)
guess = -1
count = 0
# while loop to ask number from user until guessed right
while(guess!=num):
    guess = int(input("Enter a Guess : "))
    if(guess>num):
        print("Try Lower")
    elif(guess<num):
        print("Try Higher")
    count += 1
# file handling to generate high score
with open("highscore.txt") as f:
    if(int(f.read())>count):
        with open("highscore.txt","w") as f:
            f.write(str(count))
with open("highscore.txt") as f:
    hscore = f.read()
# results of the game
print("--------------------------------------------------------------------------")
print("CONGRATULATIONS!!!")
print(f"Number    --> {num}")
print(f"Attempts  --> {count}")
print(f"Highscore --> {hscore}")





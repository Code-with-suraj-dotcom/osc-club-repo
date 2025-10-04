import random

selected_number = random.randint(1, 100)


selected_number = random.randint(1, 100)
attempts = 0


print("welcome to Random Guess Game!!")
print("I have selected a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if(guess > selected_number):
        print("Too high! Try Again.")
    elif(guess < selected_number):
        print("Too low! Try Again.")
    else:
        print(f"🎉Congratulations! You've guessed the number {selected_number} in {attempts} attempts.")
        break


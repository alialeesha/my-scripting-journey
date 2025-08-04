import random

def guess_random_number(num):
    random_number = random.randint(1, 100)
    attempts = 0

    if num < 1 or num > 100:
        print("Please enter a number between 1 and 100.")
    elif num == random_number:
        print("Congratulations! You guessed the number correctly.")
    else:
         while num != random_number:
             attempts +=1
             if num < random_number:
                 print("Too low! Try again.")
             else:
                 print("Too high! Try again.")
             num = int(input("Guess again: "))

         print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.")

if __name__ == "__main__":
    try:
        user_input = int(input("Guess a number between 1 and 100: "))
        guess_random_number(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

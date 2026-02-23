import random

best = None

while True:
    secret = random.randint(1, 100)
    attempts = 7

    print("\nI picked a number between 1 and 100. You have 7 tries!")

    for i in range(1, 8):
        guess = int(input("Guess " + str(i) + ": "))
        attempts = 7 - i

        if guess == secret:
            print("Correct! You got it in", i, "tries.")
            if best is None or i < best:
                best = i
                print("New best score:", best)
            break
        elif guess < secret:
            print("Too low!", attempts, "attempts left")
        else:
            print("Too high!", attempts, "attempts left")
    else:
        print("Out of tries! The number was", secret)

    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Best score:", best)
        break

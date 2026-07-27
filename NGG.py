import random 
secret = random. randint(1, 50)
attempts = 0

while attempts < 5:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1

    if guess == secret:
        print(" You won! You guessed the right number!")
        break

    difference = (secret - guess)

    if difference > 20:
        print("Ice cold!")
    elif difference > 10:
        print("Cold!")
    elif difference > 5:
        print("Warm!")
    else:
        print("Hot!")

    lives = 5 - attempts

    for i in range(lives):
        print("*", end=" ")
    print()

else:
    print(" Game over! ")
    print("The secret number was:", secret)


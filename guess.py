secret = 9
guess_count = 0
limit = 3
while guess_count < limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret:
        print("You won")
        break
else:
    print("You failed ")

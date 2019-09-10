import random

secret = random.randint(1, 10)

attempts = 0
while attempts < 5:
    try:
        guess = int(input('?'))
    except ValueError:
        continue
    attempts += 1
    if guess == secret:
        print("Ok")
        break
    if guess > secret:
        print(">")
    else:
        print("<")
else:
    print("You are loozer")
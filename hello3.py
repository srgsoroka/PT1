import random

secret = random.randint(1,10)

while True:
    try:
        guess=int(input('?'))
    except ValueError:
        continue
    if guess==secret:
        print("Ok")
        break
    if guess>secret:
        print(">")
    else:
        print("<")
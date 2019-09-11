tasks = {}

while True:
    action = input("""a - add
 l - list
 q - quit\n?""").lower()
    if action=='q':
        break
    elif action == 'a':
        date=input('Date?')
        task=input('Task?')
        if date not in tasks:
            tasks[date] = [task]
        else:
            tasks[date].append(task)
    elif action=='l':
        date = input('Date?')
        print(tasks[date])

print(tasks)
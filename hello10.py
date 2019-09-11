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
        if date in tasks:
            for task in tasks[date]:
                print(tasks[date])
        else:
            print("There are no task on this date " +date)
    else:
        print("Incorrect input")

print(tasks)
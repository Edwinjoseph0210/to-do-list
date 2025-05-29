tasks = []
while True:
    cmd = input("Add/View/Exit: ").lower()
    if cmd == 'add': tasks.append(input("Task: "))
    elif cmd == 'view': print(*tasks, sep="\n")
    elif cmd == 'exit': break

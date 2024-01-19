with open("teksts2.txt", "r") as f:
    for i, line in enumerate(f):
        if i == 2:
            print(line)

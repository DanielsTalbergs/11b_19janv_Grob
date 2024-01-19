faila_nosaukums = input("Ievadi faila nosaukumu: ")
with open(faila_nosaukums, "r") as file:
    faila_saturs = file.read()
print(faila_saturs)

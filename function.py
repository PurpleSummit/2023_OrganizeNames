names = []

with open("names.csv") as file:
    for line in file:
        name, category = line.rstrip().split(",")
        OC = {"name": name, "category": category}
        names.append(OC)

for n in sorted(names, key=lambda p: (p["category"], p["name"])):
    print(f"{n['name']} - {n['category']}")

# menu.no.walrus.py
flavors = ["pistachio", "malaga", "vanilla", "chocolate"]
prompt = "Choose your flavor: "

print(flavors)

while True:
    choice = input(prompt)
    if choice in flavors:
        break

    print(f"Sorry, '{choice}' is not a valid option.")

print(f"You chose '{choice}'.")

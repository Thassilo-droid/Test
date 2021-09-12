x = input("Willst du mich abbrechen?")
while x != "Ja":
    x = input("Willst du mich abbrechen?")
    if x == "Goldfisch":
        break
else:
    print("Goldfisch wurde nicht gefressen")

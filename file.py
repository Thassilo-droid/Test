import random
RandomZahl = random.randrange(1, 101)
SpielerInput = int(input("Rate eine Zahl von 1 bis 100: "))

while RandomZahl != SpielerInput:
    print("Zahl war falsch!")
    if RandomZahl > SpielerInput:
        print("Die RandomZahl war größer!")
    else:
        print("Die RandomZahl war kleiner!")

    SpielerInput = int(input("Rate eine Zahl von 1 bis 100: "))

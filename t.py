
import random

print("Wilkommen zum Game: Wählen sie eine von 3 Türen und hoffen sie auf die Ziege!")

Ziegenbuch= {1:None, 2:None, 3: None}

Türenliste= [1, 2, 3]

AusgewählteTür = random.choice(Türenliste)

Ziegenbuch[AusgewählteTür] = "Ziege"

GewählteTür = int(input("Wählen Sie eine Tür aus: "))
print("Sie haben die Tür "+ str(GewählteTür) + " ausgewählt")

if Ziegenbuch[GewählteTür] == "Ziege":
    print("Sie haben richtig geraten")
    RichtigGeraten=True
else:
    print("Keine Ziege für Sie")
    RichtigGeraten=False

if RichtigGeraten==False:
    print("Sie haben noch eine Chance")
    ZweiteGewählteTür= int(input("Wählen Sie noch eine Tür aus: "))
    if ZweiteGewählteTür == GewählteTür:
        print("JUNGE BIST DU DUMM!")
    else:
        if Ziegenbuch[ZweiteGewählteTür] == "Ziege":
            print("Sie haben eine Ziege gewonnen")
        else:
            print("Sie haben WIEDER falsch geraten")

#Copmuter sucht sich random Schre, Stein, Papier rausX
#Benutzer wird nach Schere Stein oder Papier befragtX
#Benutzereingabe muss abgeglichen werden ob es Schere Stein oder Papier istX
#Wenn die Angabe richtig ist muss sie mit der des Computers verglichen werden
#Wenn Spieler den PC besiegt Siegermachricht wenn nicht dann Verlustnachricht

import random
ComputerHand = ["Schere", "Stein", "Papier"]
ComputerWahl = random.choice(ComputerHand)

BenutzerHand = input("Wählen Sie Schere, Stein oder Papier: ")

if BenutzerHand not in ComputerHand:
    print("JUNGE WAS SOLL DAS DENN")
else:
    NutzerGewinnt = None
    if BenutzerHand == "Schere" and ComputerWahl == "Schere":
        NutzerGewinnt = None
    if BenutzerHand == "Schere" and ComputerWahl == "Stein":
        NutzerGewinnt = False
    if BenutzerHand == "Schere" and ComputerWahl == "Papier":
        NutzerGewinnt = True
    if BenutzerHand == "Stein" and ComputerWahl == "Schere":
        NutzerGewinnt = True
    if BenutzerHand == "Stein" and ComputerWahl == "Stein":
        NutzerGewinnt = None
    if BenutzerHand == "Stein" and ComputerWahl == "Papier":
        NutzerGewinnt = False
    if BenutzerHand == "Papier" and ComputerWahl == "Schere":
        NutzerGewinnt = False
    if BenutzerHand == "Papier" and ComputerWahl == "Stein":
        NutzerGewinnt = True
    if BenutzerHand == "Papier" and ComputerWahl == "Papier":
        NutzerGewinnt = None

    print(ComputerWahl)
    if NutzerGewinnt == None:
        print("Unentschieden")
    elif NutzerGewinnt == True:
        print("Sie haben gewonnen")
    else:
        print("Sie haben verloren")

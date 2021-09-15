#Gameshow die der Anwender im Terminal spielen kann
#Es gibt 3 Runden
#In jeder Runde kann eine von 3 Fragen gestellt werdeny
#Die Fragen können sein Buchstabensalat (richtiges wort aus buchstaben erraten)
#                       Mathematikaufgabe
#                       Host denkt an Blau rot oder Grün Spieler muss die Farbe erraten
# jeder runde gibt einen Punkt bei 2 oder mehr punkten gewonnen sonst verloren
import random

Rundenzahl = 0
FragenDick = {0 : "LÖSE DEN BUCHSTABENSALAT WENN SIE KEIN LAUCH SIND", 1: "LÖSE DIE MATHEMATIKAUFGABE, SIE HUND", 2: "ERRATEN SIE OB ICH AN BLAU ROT ODER GRÜN DENKE"}
AktuelleFrage = None
Wortliste = ["Apfel", "Ficker", "Ihrler", "Straub", "Hörnig"]
Zahl1 = None
Zahl2 = None
Rechenzeichen = ["+", "-", "*", "/"]
Farbliste = ["Blau", "Rot", "Grün"]
Punktzahl = 0


print("TAG ICH BIN DER GAMEMASTER UND WILLKOMMEN ZU EINER NEUEN RUNDE")
input("WAS IST IHR NAME?: ")
print("LOS GEHTS!")

for _ in range(3):
    print()
    print("DIE " + str(Rundenzahl+1) + ". RUNDE BEGINNT JETZT!")
    AktuelleFrage = random.choice(list(FragenDick.keys()))
    print(FragenDick[AktuelleFrage])
    if AktuelleFrage == 0:
         wort = random.choice(Wortliste)
         zw_wort = wort
         wort = list(wort)
         random.shuffle(wort)
         ausgegebenes_wort = ""
         for el in wort:
             ausgegebenes_wort += el
         print("WAS BEDEUTET " + ausgegebenes_wort)
         antwort = input("WAS DENKEN SIE JETZT?: ")
         if antwort == zw_wort:
             print("RICHTIG DIGGAH!")
             Punktzahl += 1
    elif AktuelleFrage == 1:
        Zahl1 = random.randrange(0, 100)
        Zahl2 = random.randrange(0, 100)
        operator = random.choice(Rechenzeichen)
        aufgabe = str(Zahl1) + " "+operator+" "+str(Zahl2)
        endwert = eval(aufgabe)
        print(aufgabe)
        antwort = int(input("WAS IST IHR ERGEBNIS? NOOB!: "))
        if antwort == round(endwert, 2):
            print("MATHEMATIK SO HART GENOMMEN WIE ICH DEINE MUM! ... HAHAHA")
            Punktzahl += 1
        else:
            print("VERSCHISSEN!")
    elif AktuelleFrage == 2:
        GamemasterFarbe = random.choice(Farbliste)
        antwort = input("SAGEN SIE Rot, Grün ODER Blau!: ")
        if antwort == GamemasterFarbe:
            print("RICHTIG, FARBGENIE")
            Punktzahl += 1
        else:
            print("FALSCH!")
    if Rundenzahl == 2:
        if Punktzahl >= 2:
            input("SIE HABEN GEWONNEN HERR, ... WIE WAR NOCHMAL IHR NAME?: ")
            print("WIE DEM AUCH SEI, GRATULATION HERR SPIELER")
        else:
            print("SIE SIND EIN LOOSER!")


    Rundenzahl += 1

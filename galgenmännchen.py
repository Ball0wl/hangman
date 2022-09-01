import random

woerter = "Baum Tetrahydrocannabinol Krawatte Auto Flagge".split()
erraten = []
ratewort = random.choice(woerter)
nutzereingabe = ""
fehlversuche = 7


for buchstabe in ratewort:
    erraten.append("_")
while nutzereingabe != "bye":
    for ausgabe in erraten:
        print(ausgabe, end=" ")
    print()
    nutzereingabe = input("Dein Vorschlag: ")
    x = 0
    for buchstaben in ratewort:
        if buchstaben.lower() == nutzereingabe.lower():
            print("Treffer")
            erraten[x] = buchstaben
            fehlversuche += 1
        x += 1
    print()

    if '_' in erraten:
        fehlversuche -= 1
        print("Du hast noch ", fehlversuche, "Fehler offen!")
        if fehlversuche == 0:
            print("Du hast verloren!")
            break
    else:
        print("gewonnen! das Wort war: ", ratewort)
        break


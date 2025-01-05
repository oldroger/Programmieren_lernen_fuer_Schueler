import random
import time

# Zähler für die richtigen Antworten
richtige_antworten = 0
anzahl_fragen = 20
strafzeit = 25
gestellte_aufgaben = []

start_time = time.time()
# Stelle 20 Fragen
for i in range(20):

    zahl1 = random.randint(2, 20)
    zahl2 = random.randint(2, 20)

    while (zahl1, zahl2) in gestellte_aufgaben:
        zahl1 = random.randint(2, 20)
        zahl2 = random.randint(2, 20)  

    gestellte_aufgaben.append((zahl1, zahl2))
    gestellte_aufgaben.append((zahl2, zahl1))


    # Berechnung des korrekten Ergebnisses
    tatsaechliches_ergebnis = zahl1 * zahl2

    # Benutzereingabe für das Ergebnis

    erwartetes_ergebnis = int(input(f"Was ist das Ergebnis von {zahl1} * {zahl2}? "))

    # Überprüfung der Antwort
    if erwartetes_ergebnis == tatsaechliches_ergebnis:
        print("Richtig!")
        richtige_antworten += 1
    else:
        print(f"Falsch! Das korrekte Ergebnis ist {tatsaechliches_ergebnis}.")

# Gesamtergebnis anzeigen
duration = (int)(time.time() - start_time)
penalty_seconds = strafzeit * (anzahl_fragen - richtige_antworten)

print(f"\nDu hast {richtige_antworten} von 20 Fragen in {duration} Sekunden richtig beantwortet.")
print(f"\nErgebniszeit: {duration + penalty_seconds} Sekunden.")


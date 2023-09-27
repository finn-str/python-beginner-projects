import datetime
import os
import csv

# Variablen definieren
jetzt = datetime.datetime.now()
# Datum und Uhrzeit im folgenden Format "2023-09-26 15:47"
formatiert = jetzt.strftime("%Y-%m-%d %H:%M")
pfad = "/workspaces/python-beginner-projects/projects/expense_tracker/"
filename = "ausgaben.csv"
csvdelimiter = ";"

if os.path.exists(pfad + filename):
    with open(pfad + filename, 'r') as file:
        lines = file.readlines()
        konto = int(''.join([char for char in lines[0] if char.isdigit()])) # extract number out of String
    print(konto)
else:
    konto = int(input("Was ist ihr aktueller Kontostand: "))
    data = [
        ["Kontostand:", konto],
        ["Type", "Amount", "Reason", "Date"],
        ]
    with open(pfad + filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=csvdelimiter)
        writer.writerows(data)
    print("CSV file has been created!")


def schreibeKonto(kontoneu):
    # Die Datei öffnen und den Inhalt einlesen
    with open(pfad + filename, 'r') as file:
        lines = file.readlines()
        # Änderungen an der ersten Zeile vornehmen
        lines[0] = "Kontostand:," + str(kontoneu) + "\n"
        # Den aktualisierten Inhalt zurück in die Datei schreiben
    with open(pfad + filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=csvdelimiter)
        writer.writerows(lines)


def kontostand():
    message = "Ihr Kontostand liegt nun bei: " + str(konto) + "€." + " | " + formatiert
    print(message)


def neueAusgabe(betrag, zweck):
    global formatiert
    global konto
    konto = konto - betrag
    schreibeKonto(konto)
    new_data = ["Expense", betrag, zweck, formatiert]
    with open('sample.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)
    message = "Sie haben " + str(betrag) + '€ für "' + zweck + '" ausgegeben.' + " | " + formatiert
    print(message)


def neuesEinkommen(betrag, quelle):
    global formatiert
    global konto
    konto = konto + betrag
    schreibeKonto(konto)
    new_data = ["Income", betrag, quelle, formatiert]
    with open('sample.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)
    message = "Sie haben " + str(betrag) + '€ durch "' + quelle + '" erhalten.' + " | " + formatiert
    print(message)


while True:
    print("\nWählen sie von 1 bis 10:\n")
    print("1: Neue Ausgabe")
    print("2: Neues Einkommen")
    print("3: Kontostand Einsehen")
    eingabe = int(input("\nWelche Aktion wollen Sie durchführen: "))
    if (eingabe == 1):
        print()
        betrag = int(input("Betrag: "))
        zweck = input("Zweck: ")
        neueAusgabe(betrag, zweck)
    elif (eingabe == 2):
        print()
        betrag = int(input("Betrag: "))
        quelle = input("Quelle: ")
        neuesEinkommen(betrag, quelle)
    elif (eingabe == 3):
        print()
        kontostand()
    else:
        print("\nBitte geben sie eine gültige Eingabe an.")

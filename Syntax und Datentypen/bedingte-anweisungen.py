# Bedingte-Anweisungen sind entscheidend für die Steuerung des Programmflusses
# Sie ermöglichen es das bestimmte Teile des Codes unter bestimmten Bedingungen ausgeführt werden

# Entscheidungsfindung im Programm
# Else ist eine Fallback-Funktion der Wert false ist
# Elif bedinungen Prüfen
alter = 8
if alter < 13:
    print("Du bist ein Kind.")
elif alter < 18:
    print("Du bist ein Jungentlicher.")
else:
    print("Du bist Volljährig.")
    
# Verschachtelte bedingung
alter = 19
hat_führerschein = False
if alter >= 18:
    if hat_führerschein:
        print("Du darfst auto fahren.")
    else:
        print("Du bist volljährig, aber darfst kein Auto fahren")
else:
    print("Du bist nicht Volljährig.")
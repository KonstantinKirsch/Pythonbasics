zahlen = [1, 2, 3, 4, 5] # Wir beginnen die Schleife mit for und weisen der neuen 
for zahl in zahlen:      # Variable zahl die Werte aus unserem Array [] zahlen zu
    print(zahl)          # die Variable zahl wird du die Positionen des Arrays durchiterriert
    
# while-Schleife wird genutzt solange etwas wahr ist. Wir bei Vorgängen angewand bei  
# denen die Anzahl der Durchgänge nicht bekannt ist und wird mit False beendet

i = 1         # Ausgangswert
while i <= 5: # i ist kleiner als-oder-gleich 5 // Bedingungen für die While-Schleife
    print(i)  # gibt den aktuellen Wert von i aus
    i += 1    # Der Wert von i wird um + 1 erhöht bis Wert 5
              # Solange die Zahl 5 nicht erreicht ist, ist die Bedingung True und läuft weiter
              # Ist die Zahl 5 erreicht, kann die While-Schleife nicht auf 6 iterrieren
              # weil dann die Bedingungen nicht mehr gegeben ist i = 1 kleiner-als 5 oder-glech 5za
              
zahlen1 = [1, 2, 3, 4, 5]
for zahl1 in zahlen1:
    if zahl1 == 3:
        continue # 3 Aus dem Array wird übersprungen
    print(zahl1)
    if zahl1 == 4: 
        break # Wenn die 4 Erreicht wird wird der Vorgang abgebrochen
    
for i in range(1, 3): # Verschachtelte for Schleife
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
    
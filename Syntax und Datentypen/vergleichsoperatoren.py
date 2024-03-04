a = 5
b = 10
c = 9
print(a == b) # Gleichheitsoperator == // Gibt False aus, da 5 nicht gleich 10 ist
print(a != b) # Ungleichsoperator != // Gibt True aus, da 5 nicht gleich 10 ist
print(a > b) # Größer-als-Operator > // Gibt False aus, da 5 nicht größer als 10 ist
print(a < b) # Kleiner-als-Operator < // Gibt True aus, da 5 nicht größer als 10 ist

print(a >= b) # Größer-als-oder-gleich-Operator >= //
              # Gibt Flase aus, da 5 nicht größer als oder gleich 10 ist
              
print(a <= b) # Kleiner-als-oder-gleich-Operator >= //
              # Gibt True aus, da 5 nicht größer als oder gleich 10 ist
              
if a < b and b > c: # Verknüpfung von Operatoren in if-Anweisung
    print("B ist großer als A und C")
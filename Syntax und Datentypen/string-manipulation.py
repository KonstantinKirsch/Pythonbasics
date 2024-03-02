vorname = "Anna"    # Eine Verkettung von Strings wird durch den + Operator erreicht
nachname = "Müller" # Damit String 1 und String 2 nicht zusammengeschribeen werden müssen wir ein
vollständiger_name = vorname + " " + nachname #  + " " verwenden um ein Leerzeichen hinzuzufügen 
print("Vollständiger Name:", vollständiger_name)

text = "Python-Programmierung" # Mit sliceing können wir Sting in dem Fall
teil = text[7:15]              # 8 - 16 Stelle Ausschneiden
print("Gecliceter Text:", teil) # Ausgabe "Programm"

text2 = "Python-Programmierung" # Mit sliceing ::2 können wir jede zweite
teil2 = text2[::2]              # indizes Stelle vom String ausgeben
print("Gecliceter Text:", teil2) 

name = "Lara"
alter = 28 # Mit .format haben wir die Platzhalter {} befüllt
text3 = "Mein Name ist {} und ich bin {} Jahre alt.".format(name, alter)
print(text3) # Formatierung (format()-Methode)

text4 = f"Mein Name ist {name} und ich bin {alter} Jahre alt."
print(text4) # Bei der Formazierung mit f-String sind schon die Platzhalter {} befüllt 





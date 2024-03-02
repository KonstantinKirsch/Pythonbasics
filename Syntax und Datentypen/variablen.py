# Eine Variable ist ein Speicherplatz für ein Wert
x = 5
name = "Max"

a, b, c = 5, 4, "Tim"

alter = 30 # Integer Ganz Zahl
gewicht = 14.5 # Float fliesender Punkt
name = "Alex" # String Stang an Zeichenketten
gewicht = 15

def meine_function(): # lokale Variable ist nur in einer Funktion gültig
    lokal = "Ich bin lokal"
    print(lokal)
    
def set_global_var(): # globale Variabke ist auch außerhalb der Funktion "im ganzen Code" einsetzbar
    global global_var
    global_var = "Global"
    
    print(global_var)
    


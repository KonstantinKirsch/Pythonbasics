# and-Operator prüft gleichzeitig mehrere Bedingungen
# or-Operator prüft ob mindestens 1 von mehren Bedingungen wahr ist
# not-Operator prüft ob eine Bedingung nicht war ist
alter = 20
student = True
if alter >= 18 and student:
    print("Du bist ein Volljähriger Student.")
if alter < 13 or student:
    print("Du bist entweder jünger als 13 oder Student.")
if not student:
    print("Du bist kein Student.")
if (alter > 18 and student) or (alter < 13): # Kombinierte Bdingung
    print("Du bist entweder ein volljähriger Student oder jünger als 13.")
    
# Schreibe ein Python-Programm, das das Alter einer Person überprüft und feststellt, 
# ob sie für den Eintritt in eine Veranstaltung zugelassen ist. Die Bedingungen sind:

# Wenn die Person mindestens 18 Jahre alt ist, darf sie ohne weitere Überprüfung eintreten.
# Wenn die Person zwischen 14 und 17 Jahre alt ist, muss sie einen Nachweis 
# über die Einverständniserklärung der Eltern vorlegen, um einzutreten.
# Wenn die Person jünger als 14 Jahre alt ist, ist der Eintritt nicht gestattet.   

alter = 13
Erlaubnis = False
if alter >= 18:                                          # Wenn
    print("Person ist berechtig eintretten zu können.")
elif alter >= 14 and alter <= 17 and Erlaubnis:          # oder
    print("Person braucht erlaubnis von den Eltern.")
else:                                                    # nicht
    print("Person darf nicht eintretten.")
    
    
    
    
    
    
    
    
    
    

    



deutsch = ["eins", "zwei", "drei", "vier"]
englisch = ["one", "two", "three", "four"]

def uebersetze_wort(wort):
    for i in range(len(deutsch)):
        if wort == deutsch[i]:
            return englisch[i]
    return "Keine Übersetzung gefunden."

eingabe = input("deutsches Wort eingeben: ")
uebersetzung = uebersetze_wort(eingabe)
print("Die englische Übersetzung ist:", uebersetzung)
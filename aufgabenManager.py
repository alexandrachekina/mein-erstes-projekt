
aufgaben = [
    {
        "title": "programmieren1",
        "prioritaet": "hoch",
        "erledigt": True,
        "matrikel": 0
        
    },

    {
        "title": "Mathematik",
        "prioritaet": "hoch",
        "erledigt": True,
        "matrikel": 1
        
    },
    {
        "title": "Theoretische Informatik",
        "prioritaet": "niedrig",
        "erledigt": False,
        "matrikel": 2
        
    }

]

def aufgabenmanager(aufgaben):
    for aufgabe in aufgaben:
        print (aufgabe.get("title"))

def aufgabenHinzufügen(aufgabe):
    aufgaben.append(aufgabe)
    return aufgabe

def aufgabenLöschen(matrikelnummer):
    for aufgabe in aufgaben:
        if aufgabe["matrikel"] == matrikelnummer:
            aufgaben.remove(aufgabe)
            return True

    return False


def statusAufgabeändern(matrikelnummer):
    for aufgabe in aufgaben:
        if aufgabe["matrikel"] == matrikelnummer:
            aufgabe["erledigt"] = not aufgabe["erledigt"]
            return aufgabe
        

    return None

def statusgeben(matrikelnummer):
    for aufgabe in aufgaben:
        if aufgabe["matrikel"] == matrikelnummer:
            return aufgabe["erledigt"]

    return None

def aufgabenSpeichern():
    with open("taskManager.txt", "w") as datei:
        for aufgabe in aufgaben:
            for key, value in aufgabe.items():
                datei.write(key + " " + str(value)+ "\n")

aufgabenSpeichern()

def aufgabenLaden():
    with open("taskManager.txt", "r") as datei:
        for zeile in datei:
            teile = zeile.strip().split()
            print(teile)

aufgabenLaden()
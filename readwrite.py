userfile = open("venv/Studenten.csv", "w")
name = "leer"
while name != "":
    name = input("Geben sie den Namen ein: ")
    alter = input("Geben sie das Alter ein: ")
    if name != "":
        userfile.write(name)
        userfile.write(";")
        userfile.write(alter)
        userfile.write("\n")
file1 = open("venv/filecount.txt", "r")
ausgabe = file1.readline()
while ausgabe != "":
    print(ausgabe)
    ausgabe = file1.readline()

file1.close()
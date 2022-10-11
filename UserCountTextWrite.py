zahl = 0
loop = 1
file1 = open("venv/filecount.txt", "w")
while zahl < 1 or zahl > 10:
    zahl = input("Geben sie eine Zahl zwischen 1 und 10 ein: ")
    zahl = int(zahl)

while loop <= zahl:
    file1.write(str(loop))
    file1.write("\n")
    loop = loop + 1

file1.close()


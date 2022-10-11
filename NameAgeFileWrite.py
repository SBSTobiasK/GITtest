file1 = open("venv/file.txt", "w")

name = input("Geben sie ihren Namen ein: ")
alter = input("Geben sie ihr alter ein: ")

file1.write(name)
file1.write("\n")
file1.write(alter)
file1.close()
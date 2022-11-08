def nettozubrutto(netto):
    return netto * 1.19

a = input("Geben sie den Nettowert ein: ")
a = (float(a))
brutto = nettozubrutto(a)
print("Bruttowert:", brutto)
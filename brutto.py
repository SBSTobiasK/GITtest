def nettozubrutto(netto, steuer=1.19):
    return netto * steuer

def bruttozunetto(brutto, steuer=1.19):
    return brutto / steuer

netto = input("Geben sie den Nettowert ein: ")
netto = (float(netto))
mwst = 1.19
bruttowert = nettozubrutto(netto, mwst)
print("Bruttowert:", bruttowert)
nettowert = bruttozunetto(bruttowert, mwst)
print("Nettowert:", nettowert)
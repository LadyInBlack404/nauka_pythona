imie = "Julia"
wiek = 27
temp_ciala = 35.8

print("Hello World! " + imie)
print("Wiek: {0}".format(wiek))
print("Temperatura: {0}".format(temp_ciala))

imie_up = imie.replace("J", "H")

print("Po hiszpansku: " + imie_up)

if imie.index("lia") != -1:
    print(imie + "xxx")

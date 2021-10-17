"""
    Ex. 6: Modificati urmatoarea bucata de cod astfel incat
    la rulare, la a doua afisare, sa avem inca un element in dictionar,
    cu cheia 3 si valoarea 'CMI3'
"""

# In variabila d1 vom salva urmatorul dictionar:
d1 = {
    1: 'CMI',
    2: 'CMI2'
}

# Afisam dictionarul inainte de schimbare
print(d1)

# Schimbam valoarea de la cheia 2, din 'CMI2' in 'CMI'
d1[2] = 'CMI'

# Afisam dictionarul dupa schimbare
print(d1)

# Adaugam inca un element in dictionar, cu cheia 3 si valoarea 'CMI3'
d2 = {
     3:'CMI3'
}
print (d2)
d1.update(d2)
print(d1)


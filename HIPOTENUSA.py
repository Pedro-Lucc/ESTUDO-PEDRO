cat1 = float(input('DIGITE O PRIMEIRO CATETO: '))
cat2 = float(input('DIGITE O SEGUNDO CATETO: '))

hip = (cat1 ** 2) + (cat2 ** 2)
hipotenusa = hip ** 0.5

print(f'A SOMA DOS CATETOS {cat1:.0f} E {cat2:.0f} FORMAM A HIPOTENUSA {hipotenusa:.0f}')
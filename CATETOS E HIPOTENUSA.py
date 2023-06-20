import math

ca = float(input('CATETO ADJACENTE: '))
co = float(input('CATETO OPOSTO : '))
hip = math.hypot(co, ca)

print(f'\nA HIPOTENUSA EQUIVALE A {hip:.2f}\nCOM OS CATETOS TENDO OS VALORES {co:.2f} E {ca:.2f} ')

import math

ang = float(input('Digite o angulo desejado: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))


print(f'A TANGENTE É: {tang:.2f}')
print(f'O COSCENO É: {cos:.2f}')
print(f'O SENO É: {sen:.2f}')


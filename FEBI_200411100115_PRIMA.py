# FEBI FADLILAH NUR AMINAH 200411100115
angka = int(input('angka = '))
temp = 0
for i in range(1,angka+1):
    if angka % i == 0:
        temp += 1
if temp == 2:
    print(angka, 'adalah bilangan prima') 
else:
    print(angka, 'adalah bukan bilangan prima')
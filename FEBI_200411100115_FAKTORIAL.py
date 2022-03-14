# FEBI FADLILAH NUR AMINAH 200411100115

n = int(input('masukkan angka : '))
temp = 1
for num in range(1,n+1): 
    temp = temp * num
print('faktorial dari {}! adalah {}'.format(n,temp))
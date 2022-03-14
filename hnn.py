def hanoi (n,A,B,C) :
    if n == 1 :
        print(f'Pindahkan lempengan {n} dari {A} ke {B}')
        print(A,B,C)
    else :
        hanoi (n-1,A,C,B)
        print(f'Pindahkan lempengan {n} dari {A} ke {B}')
        print(A,B,C)
        hanoi (n-1,C,B,A)

#a = 'A'
#b = 'B'
#c = 'C'
a = '|1|'
b = '|2|'
c = '|3|'
print (a,b,c)
hanoi (3,a,b,c)
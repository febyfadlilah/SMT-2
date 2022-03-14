# 200411100115 FEBI FADLILAH NUR AMINAH

def  towers(n,awal,bantuan,tujuan):
    if n > 0 :
        towers(n-1,awal,tujuan,bantuan)
        urut(n,awal,tujuan)
        print(f"A:\n{display(A)}\nB:\n{display(B)}\nC:\n{display(C)}")
        towers(n-1,bantuan,awal,tujuan)

def urut(n,awal,tujuan):
    print(f'lempengan - {n} dari - {awal[0]} ke - {tujuan[0]}')
    temp = awal[1].pop(0)
    tujuan[1].insert(0,temp)

def display(data):
    temp = ""
    for i in (data[1]):
        temp += f'|{i}|\n'
    return temp

n = int(input('Masukkan Jumlah Lempengan : '))
A = ["A",[x for x in range(1,n+1)]]
B = ["B",[]]
C = ["C",[]]
print(f"Perpindahan {n} Lempengan dari A ke C dengan menggunakan Bantuan B")
print(f"A:\n{display(A)}\nB:\n{display(B)}\nC:\n{display(C)}")
towers(n,A,B,C)
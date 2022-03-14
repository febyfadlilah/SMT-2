def seqSearch(listdata, data):
    cek = 0
    data1 = []
    while cek < len(listdata):
        if listdata[cek] == data:
            data1.append(cek)
            cek +=1
        else:
            cek+=1
    if data1 ==[]:
        data1 = "data tidak ada"
    return data1,cek

a = [1,5,9,8,1,5,10,26,5,12]
[hasil,jumlahIterasi] = seqSearch(a,9)
print("Posisi Data =",hasil)
print("Jumlah Iterasi",jumlahIterasi)
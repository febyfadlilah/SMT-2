#FEBI FADLILAH NUR AMINAH (200411100115)

def seqSearch(listData,data):
    print("Data =",listData)
    print("Data yang dicari =",data)
    hsl = []
    key = 0
    while key < len(listData) :
        if data == listData[key] :
            hsl.append(key)
            key += 1
        else :
            key += 1
    if hsl == []:
        hsl = "Data Tidak Ada"
    return hsl,key

a = [1,5,9,8,1,5,10,26,5,12]
[hasil,jumlahIterasi] = seqSearch(a,0)
#[hasil,jumlahIterasi] = seqSearch(a,5)
#[hasil,jumlahIterasi] = seqSearch(a,9)
print("Posisi Data =",hasil)
print("Jumlah Iterasi",jumlahIterasi)
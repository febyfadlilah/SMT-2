#FEBI FADLILAH NUR AMINAH (200411100115)

def orderedSeqSch(listData,data):
    print("Data =",listData)
    print("Data yang dicari =",data)
    hsl = []
    see = True
    key = 0
    while key < len(listData) and see:
        if data == listData[key] :
            hsl.append(key)
        elif data < listData[key] :
            see = False
        key += 1
    if hsl == []:
        hsl = "Data Tidak Ada"
    return hsl,key

a = [1,1,5,5,5,8,9,10,12,26]
#[hasil,iterasi] = orderedSeqSch(a,0)
#[hasil,iterasi] = orderedSeqSch(a,5)
[hasil,iterasi] = orderedSeqSch(a,9)
print("Posisi Data =",hasil)
print("Jumlah Iterasi",iterasi)
#FEBI FADLILAH NUR AMINAH(200411100115)

def binSearch(listData,data):
    print("Data =",listData)
    print("Data yang dicari =",data)
    first = 0
    last = len(listData) - 1
    hsl = []
    see = True
    key = 0
    while first <= last and see :
        mid = (first + last) // 2
        if data == listData[mid] :
            hsl.append(mid)
            if (mid+1) == len(listData) :
                see = False
            elif data == listData[mid+1]:
                first = mid+1
            elif data == listData[mid-1]:
                last = mid-1
            else :
                see = False
        elif data < listData[mid] :
            last = mid-1
        else :
            first = mid+1
        key += 1
    if hsl == [] :
        hsl = "Data Tidak Ada"
    return hsl,key

a = [1,1,5,5,5,8,9,10,12,26]
#[hasil,iterasi] = binSearch(a,1)
[hasil,iterasi] = binSearch(a,26)
#[hasil,iterasi] = binSearch(a,10)
#[hasil,iterasi] = binSearch(a,20)
print("Posisi Data =",hasil)
print("Jumlah Iterasi",iterasi)
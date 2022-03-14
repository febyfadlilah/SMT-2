def orderedSeqSch(listdata, data):
    stop=False
    count=0
    j=0
    data1=[]
    while j<len(listdata) and not (stop):
        if listdata[j] == data:
            count+=1
            data1.append(j)
            while listdata [j+1]==listdata[j]:
                data1.append(j+1)
                j +=1
                count+=1
            stop=True
        elif listdata[j] > data:
            count+=1
            stop= True
        else:
            j+=1
            count+=1
    if data1 == []:
        data1 = 'data tidak ada'
    return data1,count

a = [1,1,5,5,5,8,9,10,12,26]
[hasil,iterasi] = orderedSeqSch(a,9)
print("Posisi Data =",hasil)
print("Jumlah Iterasi",iterasi)
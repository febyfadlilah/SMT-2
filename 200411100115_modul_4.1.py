#FEBI FADLILAH NUR AMINAH (200411100115)
import random
def pengecekan(data) :
    if len(data)%2 == 0 :
        return (len(data)//2)
    else :
        return ((len(data)+1)//2)

def pengurutan(data) :
    for i in range (len(data)-1) :
        if data[i]>data[i+1] :
            return True
    return False

def sorting (data) :
    print ('Data = ',data)
    n = pengecekan(data)
    x = len(data)
    i = 0
    while i < (n) :
        if pengurutan(data) :
            for f in range (0,x-1,2) :
                if data[f] > data[f+1] :
                    data[f],data[f+1] = data[f+1],data[f]
            print(f'Genap - ganjil Sorting\n{data}')
        if pengurutan(data) :
            for b in range (1,x-1,2) :
                if data[b] > data[b+1] :
                    data[b],data[b+1] = data[b+1],data[b]
            print(f'Ganjil - genap Sorting\n{data}')
        i+=1
    return data


#a = [13,12,10,8,7,5,11,2]
#a = [1,2,3,4,5]
a = random.sample(range(0,20),9)
print ('Data yang sudah urut = ',sorting(a))
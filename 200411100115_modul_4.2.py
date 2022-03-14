#FEBI FADLILAH NUR AMINAH (200411100115)
import random
def pengurutan(data) :
    for i in range (len(data)-1) :
        if data[i]>data[i+1] :
            return True
    return False

def urut(data) :
    print('Data awal = ',data)
    x = len(data)
    i=0
    while i < (len(data)//2) :
        if pengurutan(data) :
            print('iterasi ke-',i+1)
            key = i
            for y in range (i+1,x) :
                if data[key] > data[y] :
                    key = y
            data[i],data[key]=data[key],data[i]
            print('Urut data minimal : ',data)
        if pengurutan(data) :
            x -= 1
            key = x
            for j in range(x-1,i,-1) :
                if data[key] < data[j] :
                    key = j
            data[x],data[key]=data[key],data[x]
            print('Urut data maksimal :',data)
        i += 1
    return data

#a = [10,2,5,8,1,20,7,12,4]
#a = [1,2,3,4]
a = random.sample(range(0,15),9)
b = urut(a)
print('Data Urut = ',b)
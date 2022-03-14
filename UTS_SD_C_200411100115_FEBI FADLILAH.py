def urut(data) :
    n = len(data)
    for i in range(len(data)//2) :
        print('iterasi ke-',i)
        ind = n-1
        for y in reversed(range(i,n-1)) :
            if data[ind] < data[y] :
                ind = y
        data[n-1],data[ind]=data[ind],data[n-1]
        print('maksimal',data)
        ind = i
        for y in range (i+1,n-1) :
            if data[ind] > data[y] :
                ind = y
        data[i],data[ind]=data[ind],data[i]
        print('minimal',data)
        n -= 1
    return data

a = [10,15,30,9,2,80,75,2,82,99]
b = urut(a)
print('Ascending Selection Sort = ',b)
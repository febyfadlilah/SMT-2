def bubble (data) :
    x = len(data)
    i = 1
    while x > 0 :
        print('iterasi ke-',i)
        temp = 0
        for j in range(x-1) :
            if a[j]>a[j+1] :
                data[j],data[j+1] = data[j+1],data[j]
                temp += 1
            print(data)
        if temp == 0 :
            x = 0
        x -= 1
        i += 1
    print('Data terurut',data)
a = [10,6,7,1,10,12,100,1,0,23,45,7,8,9]
print('Data yang akan diurutkan',a)
bubble(a)
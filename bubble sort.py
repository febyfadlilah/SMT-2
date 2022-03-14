def bubble (data) :
    x = len(data)
    i = 1
    while x > 0 :
        print('iterasi ke-',i)
        for y in reversed(range(i,x-1)) :
                if data[y] < data[y-1] :
                    data[y],data[y-1] = data[y-1],data[y]
                print (data)
        x -= 1
        i+=1
    print('Data terurut',data)
a = [12,11,5,1,0]
print('Data yang akan diurutkan',a)
bubble(a)
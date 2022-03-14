def bubble(data):
    x = len(data)
    i = 0
    while i < len(data)//2:
        print("iterasi ke-",i+1)
        temp = 0
        for j in range(i,x-1):
            if data[j] > data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                temp += 1
            print(data)
        if temp == 0:
            x = 0
        else:
            print("iterasi kanan ke kiri")
            for y in reversed(range(i+1,x-1)):
                if data[y] < data[y-1]:
                    data[y],data[y-1]=data[y-1],data[y]
                print(data)
        x -= 1
        i += 1
    print('Data terurut',data)
       
a = [5,4,3,2,1]
print ('Data yang akan diurutkan',a)
bubble(a)	
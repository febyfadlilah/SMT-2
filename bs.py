def acak (listk,i,j) :
    listk[i],listk[j] = listk[j], listk[i]

def bubble(mylist):
    b = 1
    cek = True
    pj = len(mylist)
    while pj > 1 and cek :
        print('iterasi ke-',b)
        cek = False
        i = 1
        while i < (len(mylist)) :
            if mylist[i]<mylist[i-1] :
                cek = True
                acak(mylist,i,i-1)
            i+=1
        print(mylist)
        if not cek :
            print("hasil = %s" %str(mylist))
        pj -=1
        b += 1
    
a = [12,0,5,1,11,20,4,2]
print(bubble(a))

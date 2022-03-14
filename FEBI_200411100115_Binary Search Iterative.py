import random 
def binarySearch(mylist, data):
    first = 0
    last = len(mylist) - 1
    found = 0
    stop= False
    while (first <= last) and not stop:
        mid = (first + last) // 2
        if (mylist[mid] == data):
            found = found+1
            print("Data ke-{0} ditemukan pada indeks ke: {1}".format(found,mid))
            if (mylist[mid+1]==mylist[mid] or mylist[mid-1]==mylist[mid]):
               stop=False
               if (mylist[mid+1]==mylist[mid]):
                   first=mid+1
               elif (mylist[mid-1]==mylist[mid]):
                   last=mid-1
            else:
                stop=True
            
        else:
            if data < mylist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found > 0:
        print("Data ditemukan sebanyak ",found,"kali")
    else:
        print("Data tidak ditemukan")
        
a = random.sample(range(0,100),20)
#a = [6,7,2,1,4,3,11,16,111,2,0,1,2,25,2,6,99,2,1,4]
a.sort()
print (a)
b=int(input("masukkan data yang ingin dicari= "))
print("data yang akan dicari adalah",b)
binarySearch(a,b)


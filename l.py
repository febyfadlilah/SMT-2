def createQueue ():
    q=[]
    return (q)
def enqueue (q,data):
    q.insert(0,data)
    return (q)
def dequeue(q):
    data=q.pop()
    return (data)
def isEmpty(q):
    return (q==[])
def size(q):
    return (len(q))

def task(n) :
    data = createQueue ()
    for i in range (n) :
        nama = [input('Nama proses ke-{} : '.format(i)),int(input('Waktu Proses : '))]
        enqueue(data,nama)
    return data

def main (data,time) :
    print('Antrian Proses Beserta Waktunya : ',data)
    ang = 1
    while not(isEmpty(data)) :
        print('iterasi ke-{}'.format(ang))
        que = dequeue (data) 
        print(que)
        if que[1] > time :
            que[1] -= time
            enqueue (data,que)
            print ("\tproses",que[0],"sedang di proses, dan sisa waktu proses",que[0],' = ',que[1])
        else :
            print('\tproses',que[0],'telah selesai diproses')
        print('\tData proses yang tersisa :',data)
        ang += 1

a = int(input("Jumlah proses yang akan dijadwal di CPU = "))
b = task(a)
print ('Antrian Proses = ',b)
waktu = int(input('Waktu proses CPU = '))
main(b,waktu)
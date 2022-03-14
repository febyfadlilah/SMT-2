def sparseMatrix () :
    mat = { }
    row = int(input('Jumlah Baris = '))
    col = int(input('Jumlah Kolom = '))
    ele = int(input('Jumlah data = '))
    while len(mat) < ele:
        stop = False
        bar = int(input('Baris ke- ? '))
        if bar < row:
            while not(stop) :
                kol = int(input('Kolom ke- ? '))
                if kol < col:
                    data = int(input('matrik ['+str(bar)+','+str(kol)+'] = '))
                    mat [bar,kol] = data
                    stop = True
    return mat,row,col
def displayData (mat,row,col) :
    for a in range (row) :
        print ('|',end='')
        for b in range (col) :
            value = str(mat.get((a,b),0))
            print(' '*(5-len(value)) + value,end='')
        print('     |')
    print('-'*30)

def multSparseMatrix(matx1,matx2,row1,col1,row2,col2):
    mult = {}
    for x in range(row1):
        for y in range(col2):
            nilai = 0
            for z in range(col1):
                nilai += matx1.get((x,z),0) * matx2.get((z,y),0)
            mult[x,y] = nilai
    return mult
#createSparseMatrix
def createSparseMatriks():
    mat = {}
    bar =int(input("Jumlah Baris = "))
    kol =int(input("Jumlah Kolom = "))
    data =int(input("Jumlah data = "))
    i = 1
    while i <= data:
        baris = int(input("Baris ke-?"))
        if baris >= bar:
            True
        else:
            kolom = int(input("Kolom ke-?"))
            if kolom >= kol:
                True
            else:
                nilai = int(input("Matrik["+str(baris)+","+str(kolom)+"]= "))
                mat[baris,kolom]=nilai
                i+=1
    return mat,bar,kol

#displayData
def displayData(mat,bar,kol):
    for a in range (bar) :
        print ('|',end='')
        for b in range (kol) :
            value = str(mat.get((a,b),0))
            print(' '*(5-len(value)) + value,end='')
        print('     |')
    print('-'*30)

#multSparseMatriks
def multSparseMatrix(matx1,matx2,row1,col1,row2,col2):
    mult = {}
    for x in range(row1):
        for y in range(col2):
            nilai = 0
            for z in range(col1):
                nilai += matx1.get((x,z),0) * matx2.get((z,y),0)
            mult[x,y] = nilai
    return mult
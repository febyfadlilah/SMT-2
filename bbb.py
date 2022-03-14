import bb as sparse 

#membuat matriks
print('Matrik-1')
matriks1,bar1,kol1 = sparse.createSparseMatriks()
print(' ')
print('Matrik-2')
matriks2,bar2,kol2 = sparse.createSparseMatriks()
print(' ')
#nampilin matriks
print('matrik 1 = ')
sparse.displayData(matriks1,bar1,kol1)
print('matrik 2 = ')
sparse.displayData(matriks2,bar2,kol2)
#perkalian
kali = sparse.multSparseMatrix(matriks1,matriks2,bar1,kol1,bar2,kol2)
print('Hasil Perkalian Matriks')
print('matrik 1 = ')
sparse.displayData(matriks1,bar1,kol1)
print('matrik 2 = ')
sparse.displayData(matriks2,bar2,kol2)
print ('Hasil = ')
sparse.displayData(kali,bar1,kol2)
import FEBI_200411100115_MODUL1_sparse as sparse 

#membuat matriks
print('Matrik-1')
matriks1,row1,col1 = sparse.sparseMatrix ()
print(' ')
print('Matrik-2')
matriks2,row2,col2 = sparse.sparseMatrix ()
print(' ')
#nampilin matriks
print('matrik 1 = ')
sparse.displayData(matriks1,row1,col1)
print('matrik 2 = ')
sparse.displayData(matriks2,row2,col2)
#perkalian
kali = sparse.multSparseMatrix(matriks1,matriks2,row1,col1,row2,col2)
print('Hasil Perkalian Matriks')
print('matrik 1 = ')
sparse.displayData(matriks1,row1,col1)
print('matrik 2 = ')
sparse.displayData(matriks2,row2,col2)
print ('Hasil = ')
sparse.displayData(kali,row1,col2)
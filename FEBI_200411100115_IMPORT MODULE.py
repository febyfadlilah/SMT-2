import FEBI_200411100115_MODULE as mat
# create matrik
print('create matriks 1')
a = mat.createmat(3,3)
print('create matriks 2')
b = mat.createmat(3,3)
# print matriks
mat.display(a, 'matriks 1')
mat.display(b, 'matriks 2')
# perkalian matriks
c = mat.multmat(a,b)
# print matriks
mat.display(c, 'matriks 1 * matriks 2')
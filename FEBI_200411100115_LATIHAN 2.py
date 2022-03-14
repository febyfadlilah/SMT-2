# FEBI FADLILAH NUR AMINAH 200411100115

def createmat(baris,kolom):
    mat = [] 
    for x in range(baris):
        isi = []
        for y in range(kolom):
            isi.append(int(input('matriks ({},{}) = '.format(x,y))))
        mat.append(isi)
    return mat
# perkalian matriks
def multmat(mat1,mat2):
    mat = []
    if len(mat1[0]) == len(mat2):
        for x in range(len(mat1)):
            data = []
            for y in range(len(mat2[0])):
                isi = 0
                for z in range(len(mat1[0])):
                    isi += mat1[x][z] * mat2[z][y]
                data.append(isi)
            mat.append(data)
    else:
        return False
    return mat    
# display matriks
def display(mat,name):
    print(name)
    if mat != False:
        for x in range(len(mat)):
            print('|', end='')
            for y in range(len(mat[x])):
                data = str(mat[x][y])
                print(' '*(4-len(data)) + data, end='')
            print('   |')
    else:
        print('ukuran matriks salah')

#main program
print('Create matriks 1')
matriks1 = createmat(3,3)
print(' ')
print('Create matriks 2')
matriks2 = createmat(3,3)
print(' ')
display(matriks1,'matriks 1')
print(' ')
display(matriks2,'matriks 2')
print(' ')
kali = multmat(matriks1,matriks2)
display(kali,'matriks 1 * matriks 2')
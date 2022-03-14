import FEBI_200411100115_FUNGSI_STACKS as st
def konversi(angka):
    hasil = ' '
    s = st.stack()
    while angka>0 :
        st.push(s,angka % 2)
        angka//=2
    while not(st.isEmpty(s)) :
        hasil += str(st.pop(s))
    return hasil
a=int(input('Masukkan Angka = '))
print('Konversi biner dari ',a,'adalah',konversi(a))
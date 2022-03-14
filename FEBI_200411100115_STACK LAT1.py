import FEBI_200411100115_FUNGSI_STACKS as st
def reverseWord(data):
    s = st.stack()
    hasil = ' '
    for i in data :
        st.push(s,i)
    while not(st.isEmpty(s)) :
        hasil += st.pop(s)
    return hasil
a=str(input('Masukkan kata = '))
b = reverseWord(a)
print('Reverse Word dari',a,'adalah',b)
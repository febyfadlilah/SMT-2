import FEBI_200411100115_FUNGSI_STACKS as st
# fungsi pengecekan kurung
def cek_kurung(data):
    stk = st.stack()
    cek = True
    buka = '({['
    tutup = ')}]'
    for i in data :
        if i in buka :
            st.push(stk,i)
        elif i in tutup :
            if not(st.isEmpty(stk)) :
                if buka.index(st.peek(stk))==tutup.index(i) :
                    st.pop(stk)
                else :
                    return ('kurung buka dan tutup kurung tidak cocok')      
            else :
                return ('jumlah tutup kurung lebih banyak')
    if not(st.isEmpty(stk)) :
        return ('jumlah buka kurung lebih banyak')
    return (cek)

# fungsi operasi
def evaluasi (data) :
    oper = st.stack()
    operator = '+-/*'
    for i in data :
        if i not in operator : 
            st.push(oper,i)
        else :
            op1 = float(st.pop(oper))
            op2 = float(st.pop(oper))
            if i=='+' :
                hsl = op2 + op1
            elif i=='-' :
                hsl = op2 - op1
            elif i == '*' :
                hsl = op2 * op1
            else :
                hsl = op2 / op1
            st.push (oper,hsl)
    return (st.pop(oper))

def infixTopostfix(data) :
    if cek_kurung(data) is True:
        s = st.stack()
        operator = {'*':3,'/':3,'+':2,'-':2,'(':1,'[':1,'{':1}
        kurung = {')':'(','}':'{',']':'['}
        hasil = ""
        for i in data :
            if i.isnumeric() :
                hasil += i
            elif i in kurung.values() :
                st.push(s,i)
            elif i in kurung.keys() :
                temp = st.pop(s)
                while temp != kurung[i] :
                    hasil += temp
                    temp = st.pop(s)
            else :
                while not(st.isEmpty(s)) and operator[st.peek(s)] >= operator[i] :
                    hasil += st.pop(s)
                st.push(s,i)
        while not(st.isEmpty(s)) :
            hasil += st.pop(s)
        return True,hasil
    else :
        return False,cek_kurung(data)

start = True
while start :
    a = str(input('masukkan string operasi aritmatika = '))
    x,y = infixTopostfix(a)
    if x is True :
        print('infix : ',a,' ; ','postfix : ',y,' = ',evaluasi(y))
    else:
        print(y)
    if input("lagi ? y/t = ")=="t":
        start=False

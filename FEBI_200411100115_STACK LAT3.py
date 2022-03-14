import FEBI_200411100115_FUNGSI_STACKS as st

def cek_kurung(data):
    stk = st.stack()
    cek = True
    for i in data:
        if i == '(':
            st.push(stk,i)
        elif i == ')' and not(st.isEmpty(stk)) and st.peek(stk) == '(':
            st.pop(stk)
        elif i == ')' and st.isEmpty(stk):
            cek = False
            print('kelebihan tutup kurung')
    while not(st.isEmpty(stk)):
        st.pop(stk)
        cek = False 
        print('kelebihan kurung buka')
    return cek

def InfixtoPostfix(data):
    if cek_kurung(data):
        operator = {'*':2,'/':2,'+':1,'-':1,'(':0}
        s = st.stack()
        output = []
        nilai = data.split()
        angka = '0123456789'
        for i in nilai:
            if i in angka:
                output.append(i)
            elif i == '(':
                st.push(s,i)
            elif i == ')':
                temp = st.pop(s)
                while temp != '(':
                    output.append(temp)
                    temp = st.pop(s)
            else:
                while not(st.isEmpty(s)) and operator[st.peek(s)] >= operator[i]:
                    output.append(st.pop(s))
                st.push(s,i)
        while not(st.isEmpty(s)):
            output.append(st.pop(s))
        return " ".join(output)
    return data


b = str(input('Masukkan Angka : '))
a = InfixtoPostfix(b)
print(a)
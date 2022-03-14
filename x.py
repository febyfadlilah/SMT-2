import FEBI_200411100115_FUNGSI_STACKS as st

def aval (data) :
    oper = st.stack()
    operator = '+-/*'
    for i in data :
        if i not in operator :
            st.push(oper,i)
        else :
            op1 = float(st.pop(oper))
            op2 = float(st.pop(oper))
            if i=='+' :
                hsl = op1 + op2
            elif i=='-' :
                hsl = op1 - op2
            elif i == '*' :
                hsl = op1 * op2
            else :
                hsl = op1 / op2
            st.push (oper,hsl)
    return (st.pop(oper))

print(aval('6*7+7'))
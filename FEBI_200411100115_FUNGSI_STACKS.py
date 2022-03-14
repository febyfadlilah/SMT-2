def stack() :
    s = []
    return s
def push(s,data):
    s.append(data)
def pop(s):
    data = s.pop()
    return data
def peek(s) :
    data = s[len(s)-1]
    return (data)
def isEmpty(s) :
    return (s==[])
def size(s):
    return(len(s))
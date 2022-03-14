class node:
    def __init__(self,item):
        self.name = item
        self.next = None
    def getData(self):
        return self.name
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.name = newdata
    def setNext(self, new):
        self.next = new

class linked:
    def __init__(self):
        self.head = None
    def add(self, data):
        temp = node(data)
        temp.setNext(self.head)
        self.head = temp
    def add_l(self, data):
        if self.head is None:
            self.add(data)
            return
        current = self.head
        while current.next is not None:
            current = current.getNext()
        current.setNext(node(data))
    def add_index(self, index, data):
        if index == 0:
            self.add(data)
            return
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                temp = node(data)
                temp.setNext(current.getNext())
                current.setNext(temp)
                break
            current = current.getNext()
            count += 1
    def insertNext(self, item, data):
        current = self.head
        while current != None:
            if current.getData() == item:
                break
            current = current.getNext()
        if current is None:
            print("item tidak ada")
            return
        temp = node(data)
        temp.setNext(current.getNext())
        current.setNext(temp)
    def insertPrevious(self, item, data):
        if self.head.name == item:
            self.add(data)
            return
        current = self.head
        while current.getNext():
            if current.getNext().name == item:
                break
            current = current.getNext()
        if current.getNext() is None:
            print("item tidak ada")
            return
        temp = node(data)
        temp.setNext(current.getNext())
        current.setNext(temp)
    def remove(self, item):
        current = self.head
        found = False
        prev = None
        while not found:
            if current.getData() == item:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev == None:
            self.head = current.getNext()
        else:        
            prev.setNext(current.getNext())
    def display(self):
        a = self.head
        while a != None:
            print(a.getData(),"=> ", end="")
            a = a.getNext()
        print('')
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found :
            if current.getData() == item:
                found = True
            else :
                current = current.getNext()
        return found

my = linked()
my.add(1)
my.add(2)
my.add(3)
my.add(4)
my.display()
my.insertNext(3,5)
my.display()
my.insertPrevious(2,0)
my.display()
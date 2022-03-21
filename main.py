class LinkedList:
    def __init__(self):
        self.length = 0
        self.headNode = None
        self.tail = None

    def addNode(self, value):
        newNode = Node(value)
        if (self.headNode == None):
            self.headNode = newNode
            return
        else:
            temp = self.headNode
            while (temp.nextNode != None):
                temp = temp.nextNode
            temp.nextNode = newNode

    def getValues(self):
        temp = self.headNode
        if (temp != None):
            print("obsah listu:", end=" ")
            while (temp != None):
                print(temp.value, end=" ")
                temp = temp.nextNode
            print()
        else:
            print("list je prazdny")

    def getHead(self):
        return self.headNode

    def getTail(self):
        return self.tail

    def removeValues(self, value):
        if self.headNode is None:
            return None
        else:
            cur = self.headNode
            prev = None
            while cur.value != value and cur.nextNode is not None:
                prev = cur
                cur = cur.nextNode

            if cur.value == value:
                if cur == self.headNode:
                    if cur.nextNode is None:
                        self.headNode = None
                    else:
                        self.headNode = cur.nextNode
                else:
                    if cur.nextNode is None:
                        prev.nextNode = None
                    else:
                        prev.nextNode = cur.nextNode
            else:
                return None

    def insert(self, value, position):
        newNode = Node(value)
        if (position < 1):
            print("\npozicia musi byt >=1")
        elif (position == 1):
            newNode.nextNode = self.headNode
            self.headNode = newNode
        else:
            temp = self.headNode
            for i in range(1, position - 1):
                if (temp != None):
                    temp = temp.nextNode
            if (temp != None):
                newNode.nextNode = temp.nextNode
                temp.nextNode = newNode
            else:
                print("\nhodnota je nulova")

class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def setNextNode(self, node):
        self.nextNode = node

    def getValue(self):
        return self.value

dll = LinkedList()
dll.addNode(666)
dll.addNode(777)
dll.addNode(888)
dll.addNode(333)
dll.addNode(444)
dll.insert(10, 6)
dll.removeValues(2)
dll.getValues()
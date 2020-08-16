class node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:

    def __init__(self):
        self.head = node()
        self.length = 0

    def add(self, data):
        self.newNode = node(data)
        curr = self.head
        while(curr.next != None):
            curr = curr.next
        curr.next = self.newNode
        self.length += 1
        print("Node Created Successfully with Data = {}".format(self.newNode.data))

    def displayList(self):
        curr = self.head.next
        while(curr.next != None):
            print(curr.data, end=" ")
            curr = curr.next
        print(curr.data)

    def pop(self):
        curr = self.head.next
        while(curr.next.next != None):
            print(curr.data)
            curr = curr.next
        curr.next = None
        print("Popped Element, New List : ", end="")
        self.displayList()
        self.length -= 1

    def getLen(self):
        return self.length


ll = linkedList()
ll.add(5)
ll.add(10)
ll.add(15)
ll.displayList()

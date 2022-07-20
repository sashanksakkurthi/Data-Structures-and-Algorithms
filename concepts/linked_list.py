
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    # print all elements
    def print_list(self):
        list = []
        temp = self.head 
        while temp != None:
            list.append(temp.data)
            temp = temp.next
        print(list)
    
    # add element at first
    def add_at_first(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
     
    # add element at last
    def add_at_last(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = newNode

    # add element at middle
    def add_at_middle(self,data):
        pass

    # remove element at first
    def remove_first(self):
        pass
     
    # remove element at last
    def remove_last(self):
        pass

    # sort list in insertion sort
    def insertion_sort(self):
        if self.head is None:
            return self.head
        current = self.head
        while current is not None:
            start = self.head
            while start is not None:
                if start.data > current.data:
                    temp = start.data
                    start.data = current.data
                    current.data = temp
                start = start.next
            current = current.next
        



        


list = LinkedList()
list.add_at_first(3)
list.add_at_first(5)
list.add_at_first(2)
list.add_at_first(7)
list.add_at_first(6)
list.insertion_sort()
list.print_list()


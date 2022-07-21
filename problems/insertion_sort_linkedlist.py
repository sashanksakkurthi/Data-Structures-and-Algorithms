# Given a singly linked list, sort the list (in ascending order) using insertion sort algorithm.

# Example 1:

# Input:
# N = 10
# Linked List = 30->23->28->30->11->14->
#               19->16->21->25 
# Output : 11 14 16 19 21 23 25 28 30 30 
# Explanation :
# The resultant linked list is sorted.

# Example 2:

# Input : 
# N = 7
# Linked List=19->20->16->24->12->29->30 
# Output : 12 16 19 20 24 29 30 
# Explanation : 
# The resultant linked list is sorted.
 
# Expected Time Complexity : O(n2)
# Expected Auxiliary Space : O(1)


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
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  

    def append(self, info):
        new_node = Node(info)
        if self.size == 0:  
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1  

    def deleteAtLocation(self, location):
        if self.size == 0:  
            print("The list is empty.")
            return

        if location >= self.size:
            print("Location is out of bounds.")
            return

        if location == 0:  
            self.head = self.head.next
        else:
            current = self.head
            previous = None
            count = 0
            while count < location:
                previous = current
                current = current.next
                count += 1
            # Unlink the target node
            previous.next = current.next
        self.size -= 1  
def printList(ll):
    current = ll.head
    while current:
        print(current.info, end=" -> ")
        current = current.next
    print("None")
ll = LinkedList()
ll.append(12)
ll.append(56)
ll.append(76)
ll.append(11)
ll.append(0)
printList(ll)
ll.deleteAtLocation(0)
printList(ll)  
ll.deleteAtLocation(2) 
printList(ll)

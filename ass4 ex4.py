class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  

    def append(self, info):
        """Function to append a new node at the end of the linked list."""
        new_node = Node(info)
        if self.size == 0:  
            self.head = new_node
        else:
            # Find the last node and link the new node at the end
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1  # Increment size after appending a node

    def deleteAtLocation(self, location):
        """Function to delete a node at a given location."""
        if self.size == 0:  # Check if the list is empty
            print("The list is empty.")
            return

        if location >= self.size:  # Check if location is out of bounds
            print("Location is out of bounds.")
            return

        if location == 0:  # Deleting the head node
            self.head = self.head.next
        else:
            current = self.head
            previous = None
            count = 0
            # Traverse to the node just before the one we want to delete
            while count < location:
                previous = current
                current = current.next
                count += 1
            # Unlink the target node
            previous.next = current.next
        self.size -= 1  # Decrement size after deletion

# Function to print the linked list for verification
def printList(ll):
    current = ll.head
    while current:
        print(current.info, end=" -> ")
        current = current.next
    print("None")

# Creating a linked list and appending nodes
ll = LinkedList()
ll.append(12)
ll.append(56)
ll.append(76)
ll.append(11)
ll.append(0)
printList(ll)

# Deleting nodes at specific locations
ll.deleteAtLocation(0)
printList(ll)  # Delete head node (12)
ll.deleteAtLocation(2)  # Delete node at new location 2 (11)

# Print the current state of the linked list
printList(ll)

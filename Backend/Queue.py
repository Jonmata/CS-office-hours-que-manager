# Create a Linked List Node Class
class Node:
    def __init__(self, name):
        # Instance variables 
        self.name = name
        self.next = None

        # Getter Functions
        def get_name(self):
            return self.name
        
        def get_next(self):
            return self.next



# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Method enqueue students to the back for the queue
    def enqueue(self, name):
        new_node = Node(name)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        else: 
            self.tail.next = new_node
            self.tail = new_node


    def dequeue(self, name):
        current_node = self.head
        prev_node = None
        # List is empty
        if (current_node == None):
            return
        # List only has one node 
        if (self.head.name == self.tail.name and self.head.name == name):
            self.head = None
            self.tail = None
        else:
            # removing first person in the queue
            if (current_node.name == name):
                self.head = current_node.next
            else:
                # removing a node that's not the head node
                prev_node = current_node
                while(current_node.name != self.tail.name):
                    if (current_node.name == name):
                        prev_node.next = current_node.next
                    prev_node = current_node
                    current_node = current_node.next

                #Tail node is the node to remove
                if (self.tail.name == name):
                    self.tail = prev_node
                    prev_node.next = None
                    return
                  



    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.name)
            current_node = current_node.next

'''
llist = LinkedList()

llist.enqueue('a')
llist.dequeue('a')

llist.enqueue('New Student')
llist.printLL()


llist.enqueue('a')
llist.enqueue('b')
llist.enqueue('c')
llist.enqueue('d')
llist.enqueue('e')

#llist.printLL()


llist.dequeue('a')

llist.dequeue('d')
llist.dequeue('c')

llist.enqueue('c')
llist.enqueue('a')

#llist.printLL()


llist.dequeue('b')

llist.enqueue('the')

llist.enqueue('v')
llist.enqueue('w')
llist.enqueue('x')

#llist.printLL()


llist.dequeue('v')
llist.dequeue('the')



#llist.enqueue('a')
llist.dequeue('x')

#llist.printLL()
llist.dequeue('1000')

#llist.printLL()



llist.dequeue('w')
llist.dequeue('c')
llist.dequeue('x')

llist.dequeue('1000')




llist.dequeue('a')
#llist.printLL()

llist.dequeue('e')

#llist.printLL()

llist.enqueue('new student')
llist.printLL()
                

'''


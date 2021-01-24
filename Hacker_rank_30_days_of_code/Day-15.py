class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
    #Complete this method
        new_node = Node(data)
        original_head = head
        # Empty list?
        if (head == None):
            head = Node(data)
        else:
            current_node = head
            while (current_node.next != None):
                # Move forward
                current_node = current_node.next
            current_node.next = Node(data)
        return head

mylist= Solution()
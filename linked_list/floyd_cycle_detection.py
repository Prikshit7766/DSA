
#Floyd's Cycle Detection Algorithm : This algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for detecting cycles in linked lists.

class Node:
    def __init__(self, data=None, next_node=None):
        # Initialize a node with data and reference to the next node
        self.data = data         # Data stored in the node
        self.next_node = next_node # Reference to the next node in the list

class LinkedList:
  def __init__(self):
    # Initialize an empty linked list with head set to None
    self.head = None


  def print(self):
    if self.head is None:
      print("Linked List is empty")
      return
    iterator = self.head
    list_str = ' '
    while iterator:
      list_str += str(iterator.data) + '-->'
      iterator = iterator.next_node
    print(list_str)

  
  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return
    iterator = self.head
    while iterator.next_node:
      iterator = iterator.next_node

    iterator.next_node = Node(data, None)

    
  def detect_loop(self):
    if self.head is None:
        return False
    
    slow = self.head
    fast = self.head

    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node

        if slow == fast:
            return True
    
    return False



if __name__ == "__main__":
    # Create a linked list without a loop
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)

    print("Linked list without a loop:")
    linked_list.print()
    print("Loop detected:", linked_list.detect_loop())  # Should print False

    # Create a linked list with a loop
    linked_list_with_loop = LinkedList()
    linked_list_with_loop.insert_at_end(1)
    linked_list_with_loop.insert_at_end(2)
    linked_list_with_loop.insert_at_end(3)
    linked_list_with_loop.insert_at_end(4)
    linked_list_with_loop.insert_at_end(5)

    linked_list_with_loop.head.next_node.next_node.next_node.next_node = linked_list_with_loop.head.next_node.next_node
    print("Loop detected:", linked_list_with_loop.detect_loop())
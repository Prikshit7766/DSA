class Node:
    def __init__(self, data=None, next_node=None):
        # Initialize a node with data and reference to the next node
        self.data = data         # Data stored in the node
        self.next_node = next_node # Reference to the next node in the list

class LinkedList:
  def __init__(self):
    # Initialize an empty linked list with head set to None
    self.head = None

  ## Method to display all elements inside the Linked List
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

  ## Insertion of an element

  ## 1. Beginning of the Linked List
  ## Time Complexity : O(1)
  def insert_at_begining(self, data):
    node = Node(data, self.head)
    self.head = node                          # important to note that self.head is updated to the new node address (reffernce to the new node is stored in self.head)
  
  ## 2. End of the Linked List
  ## Time Complexity : O(n)
  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return
    iterator = self.head
    while iterator.next_node:
      iterator = iterator.next_node

    iterator.next_node = Node(data, None)

  ## Method to count number of elements inside Linked List
  def count_length(self):
    count = 0
    iterator = self.head
    while iterator:
      count += 1
      iterator = iterator.next_node
    return count

  ## 3. Insertion at any index
  def insert_at_index(self, data, idx):
    if idx < 0 or idx > self.count_length():
      raise Exception("Invalid Index")
  
    if idx == 0:
      self.insert_at_begining(data)
      return
    
    count = 0
    iterator = self.head
    while iterator:
      if count == idx - 1:
        node = Node(data, iterator.next_node)
        iterator.next_node = node
        break
      
      iterator = iterator.next_node
      count += 1
      
  ## To store all the elements in a list
  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)
  
  ## Removal of an element inside Linked List
  def removal_at_index(self, idx):
    ## Invalid Index
    if idx<0 or idx >= self.count_length():
      raise Exception("Invalid Index")
    ## Deletion at beginning
    if idx == 0:
      self.head = self.head.next_node
      return
    ## Deletion at any other index value
    count = 0
    iterator = self.head
    while iterator:
      if count == idx - 1:
        iterator.next_node = iterator.next_node.next_node
        break
      
      iterator = iterator.next_node
      count += 1
    
  ## To search for a node in a Linked List
  def search(self, data):
    if self.head == None:
      return False
    iterator = self.head
    while iterator:
      if iterator.data == data:
        return True
      else:
        iterator = iterator.next_node
    return False

if __name__ == '__main__':
  list_1 = LinkedList()
  list_1.insert_at_begining(45)
  list_1.insert_at_begining(50)
  list_1.insert_at_end(46)
  list_1.insert_at_end(34)
  list_1.insert_at_end(78)
  list_1.insert_at_end(90)
  list_1.print()
  list_1.removal_at_index(2)
  list_1.print()
  result = list_1.search(36)
  if result:
    print("Search Found")
  else:
    print("Search Not Found")

  list_1.insert_at_index(37,2) 
  list_1.print()

  list_2 = LinkedList()
  list_2.insert_values(["Jatin","Arvind","Suneetha","Ritu","Taral","Nafisa","Sriteja"])
  list_2.print()
  print("Count of number of elements inside Linked List:",list_2.count_length())
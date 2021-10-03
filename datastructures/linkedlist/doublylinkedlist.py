# Doubly Linked List:
#   - Doubly linked list is a type of linked list in which each node has two links,
#     one to the previous node and one to the next node.
#   - It is a data structure that is used to implement a stack and a queue.

# Node:
#   - Each node has a data field and a link to the next node.
#   - The last node in the list has a link to None.

class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

  def __str__(self):
      return str(self.data)


class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

  def prepend(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node


  def print_list(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

  def remove(self, data):
    current = self.head
    while current:
      if current.data == data:
        if current.prev is not None:
          current.prev.next = current.next
        else:
          self.head = current.next
        if current.next is not None:
          current.next.prev = current.prev
        else:
          self.tail = current.prev
        break
      current = current.next

  def remove_all(self, data):
    current = self.head
    while current:
      if current.data == data:
        if current.prev is not None:
          current.prev.next = current.next
        else:
          self.head = current.next
        if current.next is not None:
          current.next.prev = current.prev
        else:
          self.tail = current.prev
      current = current.next
  
  def remove_last(self):
    if self.tail is not None:
      if self.tail.prev is not None:
        self.tail.prev.next = None
      else:
        self.head = None
      self.tail = self.tail.prev

  def remove_first(self):
    if self.head is not None:
      if self.head.next is not None:
        self.head.next.prev = None
      else:
        self.tail = None
      self.head = self.head.next

  def remove_at(self, index):
    if index == 0:
      self.remove_first()
    else:
      current = self.head
      for i in range(index-1):
        current = current.next
      current.next = current.next.next
      current.next.prev = current

  def insert_at(self, index, data):
    if index == 0:
      self.prepend(data)
    else:
      current = self.head
      for i in range(index-1):
        current = current.next
      new_node = Node(data)
      new_node.next = current.next
      current.next.prev = new_node
      new_node.prev = current
      current.next = new_node

  def insert_after(self, data, new_data):
    current = self.head
    while current:
      if current.data == data:
        new_node = Node(new_data)
        new_node.next = current.next
        current.next.prev = new_node
        new_node.prev = current
        current.next = new_node
        break
      current = current.next


  def insert_before(self, data, new_data):
    current = self.head
    while current:
      if current.data == data:
        new_node = Node(new_data)
        new_node.prev = current.prev
        current.prev.next = new_node
        new_node.next = current
        current.prev = new_node
        break
      current = current.next


  def reverse(self):
    current = self.head
    prev = None
    while current:
      next = current.next
      current.next = prev
      current.prev = next
      prev = current
      current = next
    self.head = prev



# Linked List:
#   - A linked list is a linear data structure that consists of a sequence of nodes
#   - Each node contains a piece of data and a reference to the next node in the sequence
#   - The last node in the sequence is called the tail
#   - The first node in the sequence is called the head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def append(self, data):
    node = Node(data)
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node
    self.size += 1

  def prepend(self, data):
    node = Node(data)
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      node.next = self.head
      self.head = node
    self.size += 1

  def insert(self, index, data):
    if index == 0:
      self.prepend(data)
    elif index == self.size:
      self.append(data)
    else:
      node = Node(data)
      current = self.head
      for i in range(index-1):
        current = current.next
      node.next = current.next
      current.next = node
      self.size += 1


  def remove(self, index):
    if index == 0:
      self.head = self.head.next
    else:
      current = self.head
      for i in range(index-1):
        current = current.next
      current.next = current.next.next
    self.size -= 1


  def get(self, index):
    if index < 0 or index >= self.size:
      return None
    current = self.head
    for i in range(index):
      current = current.next
    return current.data

  def __str__(self):
    current = self.head
    string = ""
    while current is not None:
      string += str(current.data) + " "
      current = current.next
    return string

if __name__ == '__main__':
  ll = LinkedList()
  ll.append(1)
  ll.append(2)
  ll.append(3)
  print(ll)
  ll.prepend(0)
  print(ll)
  ll.insert(2, 4)
  print(ll)
  ll.remove(2)
  print(ll)
  print(ll.get(2))
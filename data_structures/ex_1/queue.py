from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size += 1
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    node = self.storage.remove_head()
    if node:
      self.size -= 1
      return node

  def len(self):
    return self.size

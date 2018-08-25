class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    node = Node(value)
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.tail.set_next(node)
      self.tail = node

  def remove_head(self):
    if self.head is None:
      return None
    elif self.head.get_next() is None:
      removed = self.head
      self.head = None
      self.tail = None
      return removed.get_value()
    else:
      removed = self.head
      self.head = removed.get_next()
      removed.set_next(None)
      return removed.get_value()

  def contains(self, value):
    current = self.head
    while current:
      if current.get_value() == value:
        return True
      current = current.get_next()
    return False

  def get_max(self):
    if self.head is None:
      return None
    max = self.head.get_value()
    current = self.head.get_next()
    while current:
      if current.get_value() > max:
        max = current.get_value()
      current = current.get_next()
    return max

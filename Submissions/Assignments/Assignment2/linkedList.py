## Working with Linked List

# creating a NODE

## how a single node looks like 
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

###########

# creating a linked list
## insertion and traversal

class linkedList:
  def __init__(self):
    self.head = None

  def __checkUnderflow(self):
    if self.head == None:
      print("Oops!!! List is empty!")
      return True
    return False
  
  #################################################

  # insert at begining
  def push(self, newData):
    newNode = Node(newData)
    newNode.next = self.head # points to node that was head earlier
    self.head = newNode # making new node as head
  
  # insert at a specific location (Data)
  def insertAfter(self, prevData, newData):
    temp = self.head
    while((temp.data is not prevData) and (temp is not None)):
      temp = temp.next
    if temp is None:
      print(prevData," itself does not exist!!")
    else:
      newNode = Node(newData)
      newNode.next = temp.next
      temp.next = newNode
    return
  
  # insert at the end
  def append(self, newNode):
    newNode = Node(newNode)
    if self.head is None:
      self.head = newNode
    else:
      last = self.head
      while(last.next):
        last = last.next
      last.next = newNode
    return

  #################################################

  # deletion
  def deleteData(self, data):
    if self.__checkUnderflow():
      return
    
    temp = self.head    
    if temp.data == data:
      self.head = self.head.next
      return
    else:
      while((temp.next is not None) and (temp.next.data is not data)):
        temp = temp.next
      if temp.next is None:
        print("No such element in list! Can\'t delete!!")
      else:
        temp.next = temp.next.next
      return
  
  def deleteNode(self, nodeNum):
    if self.__checkUnderflow():
      return
    
    if nodeNum == 1:
      self.head = self.head.next
      return
    else:
      count = 2
      temp = self.head
      while(count != nodeNum):
        temp = temp.next
        count += 1
      if temp is None:
        print("List has fewer nodes! Can\'t delete!!")
      else:
        temp.next = temp.next.next
    return



  #################################################

  # printing
  def printList(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next
    return


################

## implementation
if __name__ == '__main__':
  lList = linkedList()
  
  # insertion ->   1,2,3,4
  print("\nList after adding 1, 2, 3 & 4")
  lList.append(1)
  lList.append(2)
  lList.append(3)
  lList.append(4)
  # display
  lList.printList()

  lList.push(0) # at beg
  # display
  print("\nList after adding 0 in beginning")
  lList.printList()

  # adding 5 between 2 and 3
  lList.insertAfter(2,5) # after 2
  # display
  print("\nList after adding 5 between 2 & 3")
  lList.printList()

  # deleting node having data 4
  lList.deleteData(4)
  # display
  print("\nList after deleting 4")
  lList.printList()

  # deleting 2nd node
  lList.deleteNode(2)
  # display
  print("\nList after deleting second node")
  lList.printList()

  # add 6 at the end
  print("\nList after adding 6 at the end")
  lList.append(6)
  # display
  lList.printList()

  # deleting 1st node
  lList.deleteNode(1)
  # display
  print("\nList after deleting first node")
  lList.printList()

## Bucket

## structure of the Bucket to store every history as a details (as one NODE)
class bucketLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  # checking overflow condition
  def __checkUnderflow__(self):
    if self.head == None:
      return True
    return False
  
  #######################################
  # adding the element
  #######################################

  def addNode(self, node):
    temp = node
    if self.head is None:
      self.head = self.tail = temp
    else:
      temp.next = self.head
      self.head = temp
  
  #######################################
  # deleting the url
  #######################################

  def deleteData(self, url):
    if self.__checkUnderflow__():
      return False
    
    temp = self.head    
    if temp.getURL() == url:
      self.head = self.head.next
      return True
    else:
      while temp.next is not None:
        if temp.next.getURL() == url:
          temp.next = temp.next.next
          return True
        temp = temp.next
    return False
  
  #######################################
  # searching
  #######################################

  def checkDuplicateEntries(self, URL):
    if self.__checkUnderflow__():
      return False
    temp=self.head
    flagFound = False
    COUNT = 0
    while(temp):
      if temp.getURL() == URL:
        COUNT += 1
        flagFound = True
      temp = temp.next
    if flagFound:
      return COUNT
    else:
      return False
  
  def trackDateWise(self, time):
    if self.__checkUnderflow__():
      return
    temp=self.head
    flag = False
    while(temp):
      if temp.getTimeStamp() == time:
        flag = True
        print("->",temp.getURL())
      temp = temp.next
    return flag
  
  #######################################
  # Print
  #######################################
  
  def printList(self):
    if self.__checkUnderflow__():
      return
    temp=self.head
    while(temp):
      temp.printNodeData()
      temp = temp.next
    print("\n")
    return
  
  def printURLOnly(self):
    if self.__checkUnderflow__():
      return
    temp=self.head
    while(temp):
      print("->",temp.getURL())
      time.sleep(0.15)
      temp = temp.next
    return

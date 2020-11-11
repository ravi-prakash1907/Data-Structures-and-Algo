

## makes array to hold buckets

class historyTracker:
  def __init__(self):
    self.totalNodes = 0
    self.history = self.__freshMemory__()
    self.backup = None ## holds the backup
  

  #########################################
  #######     Private Functions     #######
  #########################################

  def __totalNodeCounter__(self, added):  # added is boolean val
    if added:
      self.totalNodes += 1  # increament total node count by 1
    else:
      self.totalNodes -= 1  # decreament total node count by 1
    self.history[0] = self.totalNodes
    return
  
  def __freshMemory__(self):
    ## Init
    
    self.bkt1 = bucketLinkedList()
    self.bkt2 = bucketLinkedList()
    self.bkt3 = bucketLinkedList()
    self.bkt4 = bucketLinkedList()
    self.bkt5 = bucketLinkedList()
    self.bkt6 = bucketLinkedList()
    self.bkt7 = bucketLinkedList()
    self.bkt8 = bucketLinkedList()
    self.bkt9 = bucketLinkedList()
    
    self.totalNodes = 0
    initArray = [self.totalNodes,self.bkt1,self.bkt2,self.bkt3,self.bkt4,self.bkt5,self.bkt6,self.bkt7,self.bkt8,self.bkt9]
    return initArray

  # checking overflow condition
  def __checkUnderflow__(self):
    if self.totalNodes == 0:
      print("Browsing history is empty!!\n")
      return True
    return False
  
  #########################################
  #########################################

  
  #########################################
  #######      Public Functions     #######
  #########################################

  #######      Insert
  def insert(self):
    if self.totalNodes == 100:
      print("Ooops!! Not enough memory, insertion is not possible!")
      return False
    else:
      self.__totalNodeCounter__(True)
      newEntry = Node()
      index = newEntry.getBucketIndex()
      if index < 10:
        temp = self.history[index]
        self.history[index].addNode(newEntry)
        print("Added!!")
      else:
        print("Error in hash function! Insertion failed!!")
      return True
  

  #######      Remove first occurance    

  def delete(self):
    if not self.__checkUnderflow__():
      url = input("Enter the url to remove from the tracked history: ")
      if url[:4] != 'www.' or url[:4] != 'http':
        print("Invalid URL entered! Terminating deletion!!")
        return False
      flag = False
      for index in range(1,10):
        if self.history[index] is not None:
          if self.history[index].deleteData(url):
            flag = True
            self.__totalNodeCounter__(False)  # false means decrement counter (see fun defination)
      if flag:
        print("One occurance removed from the browsing history!")
      else:
        print("Provided URL does not exist in browsing history! Deletion failed!!")
      return True
    return False


  #######      All History 
  def historyViewer(self):
    if not self.__checkUnderflow__():
      tempChoice = input("\nPress 'Y' for detailed history: ")

      print("\n\n\nListing your browsing history:\n------------------------------")
      index = 1
      while index < 10:
        if self.history[index] is not None:
          if tempChoice == 'y' or tempChoice == 'Y':
            # (in Detail)
            self.history[index].printList()
          else:
            # (URLs Only)
            self.history[index].printURLOnly()
        index += 1
      return True
    return False


  #######      Search
  def search(self):
    ## by url
    if not self.__checkUnderflow__():
      print("\n1. Search by URL \n2. Search by Date\n")
      tempChoice = input("Enter your choice: ")
      if tempChoice == '1':
        url = input("Enter the URL: ")
        if url[:4] != 'www.' or url[:4] != 'http':
          print("Invalid URL entered! Terminating search!!")
          return False
        flagURL = False
        dupCount = 0
        for index in range(1,10):
          searched = self.history[index].checkDuplicateEntries(url) # list 
          if searched:
            dupCount += searched
            flagURL = True
        if flagURL:
          print("\n\n"+str(dupCount),"duplicate entries found for:\n->",url)
        else:
          print("No history found!\n")
      
      ## by date
      elif tempChoice == '2':
        flagTime = False
        date = input("Enter the Date (dd/mm/yyyy): ")
        if re.search('^(0[1-9]|[12][0-9]|3[01])[/.](0[1-9]|1[012])[/.](19|20)\d\d$', date):
          hashValue = numericToHashValue(date)
          print("\n\nOn",date+", you visited:\n----------------------------")
          if not self.history[hashValue].trackDateWise(date): # returns false if element was not there
            print("\nNo history available!")
        else:
          print("\nInvalid date entered!!")
      
      else:
        print("\nInvalid choice!!")
      
      return True
    return False
  

  #######      Format Memory
  def refreshMemory(self):
    if not self.__checkUnderflow__():
      print("Are you sure you want to refresh?? It's suggested to take a backup first!!")
      tempChoice = input("\n1. Take Backup \n2. I already have it! Refresh anyways!!\n\nYour choice: ")
      if tempChoice == '1':
        backup = self.backupHistory()
      if tempChoice == '1' or tempChoice == '2':
        self.history=self.__freshMemory__()
        print("\nMemory Refreshed!!")
        return True
      else:
        print("Invalid input!!")
    return False
  

  #######      Backup
  def backupHistory(self):
    if not self.__checkUnderflow__():
      print("\nHold on! We're taking the backup!!...")
      time.sleep(2)
      arrLen = len(self.history)
      backup = bucketLinkedList()
      for index in range (1,(arrLen-1)):
        if backup.head is None:
          backup.head = self.history[index].head
          backup.tail = self.history[index].tail
        if backup.tail is not None:
          backup.tail.next = self.history[index+1].head
          backup.tail = self.history[index+1].tail
      print("Backup completed successfully!")
      self.backup = bucketLinkedList()
      self.backup = backup
      tempChoice = input("\nWant to refresh memory? (y/n): ")
      if tempChoice == 'y' or tempChoice == 'Y':
        self.history = self.__freshMemory__()
        print("\nMemory Refreshed!!")
      return True
    return False


  #######      Restore
  def restoreBackup(self):
    if self.backup is not None:
      self.history = self.__freshMemory__()
      print("\nHold on! We're restoring your Backup...")
      time.sleep(2)

      tempNode = self.backup.head      
      while tempNode is not None:
        index = tempNode.getBucketIndex()
        newNode = tempNode
        tempNode = tempNode.next
        newNode.next = None
        self.history[index].addNode(newNode)
        self.totalNodes += 1
      self.history[0] = self.totalNodes
      print("\n"+str(self.totalNodes),"entries restored!!")
      return True
    
    else:
      print("\nNo Backup Found!!")
      return False


  #######      Total History Counts
  def countHistory(self):
    if not self.__checkUnderflow__():
      print("\nTotal URLs in tracked history:",self.totalNodes)
      return True
    return False
  
  

  #########################################
  #########################################

  


from datetime import datetime

### Hash Value Generator

def numericToHashValue(aString):
  numericNow = ''
  for i in aString:
    if i.isnumeric():
      numericNow = numericNow + i
  numericNow = int(numericNow)
  hashValue = bucketHashGenerator(numericNow)
  return hashValue
    
def bucketHashGenerator(num):
  if len(str(num)) != 1:
    reminder = 0
    while num != 0:
      reminder += num%10
      num //= 10
      res = bucketHashGenerator(reminder)
    return res
  else:
    return num
    
 ###  NODE
 
 class Node:
  def __init__(self):
    # parameters ---> private to this class
    self.__URL = self.__setURL__()
    self.__timeStamp,self.__bucketIndex = self.__setTimeData__()
    # link
    self.next = None
  
  ###############################
  
  # Setters
  def __setTimeData__(self):
    now = datetime.now()
    nowStr1 = now.strftime("%d/%m/%Y")

    nowStr2 = str(nowStr1)    
    bucketIndex = numericToHashValue(nowStr2)
    
    return nowStr1,bucketIndex
  
  def __setURL__(self):
    flag = False
    url = input("Enter the URL: ")
    if url[:4] == 'www.' or url[:4] == 'http':
      flag = True
    while not flag:
      url = input("Invalid URL! Enter a valid URL: ")
      if url[:4] == 'www.' or url[:4] == 'http':
        flag = True
    return url
  
  
  ############################

  # Getters  
  def getTimeStamp(self):
    return self.__timeStamp
  
  def getURL(self):
    return self.__URL
  
  def getBucketIndex(self):
    return self.__bucketIndex
  
  #############################
  # Display

  def printNodeData(self):
    print("\nDate = ",self.getTimeStamp())
    print("Visited URL = ",self.getURL())
    #print("Bucket Index = ",self.getBucketIndex())
    return

## Libries
import matplotlib.pyplot as plt
from random import randint
import numpy as np
%precision 2

## for formatted output in python-notebook
from IPython.display import clear_output


#############################
### Competition Data Tree ###
#############################

####  Data of One Topic  ####
## holds total questions' and their aggr. marks
class answerCount:
  def __init__(self):
    self.__marksCount = None
    self.__marks = None
  
  def setMarks(self, gotList):
    self.__marksCount = len(gotList)
    self.__marks = sum(gotList)
      
  def getCount(self):
    return self.__marksCount
  def getMarks(self):
    return self.__marks

## holds all questions' outcome from a topic
class topic:
  def __init__(self):
    self.topicMarks = None
    self.correctAns = answerCount()
    self.incorrectAns = answerCount()
    self.NA = answerCount()


################################
### Result of One Competitor ###
################################

####  Result of One Candidate/Student  ####
class competitor:
  def __init__(self):
    self.grade = ''
    self.bonus = 0

    ## actual marks + pointes based on
    ## right/wrong/not-attempted que.
    self.bonus = 0
    self.marksByTopic = []
    self.topics = []
  
  def addTopic(self,topicMarkList):
    newTopic = topic()

    newTopic.topicMarks = sum(topicMarkList)
    newTopic.correctAns.setMarks(list(filter(lambda x: (x>0), topicMarkList)))
    newTopic.incorrectAns.setMarks(list(filter(lambda x: (x<0), topicMarkList)))
    newTopic.NA.setMarks(list(filter(lambda x: (x==0), topicMarkList)))

    self.topics.append(newTopic)
    return newTopic.topicMarks
  
  def setBonus(self):
    bonus = 0
    for index in range(len(self.topics)):
      topic = self.topics[index]
      rights = topic.correctAns.getMarks()
      wrongs = topic.incorrectAns.getMarks()
      left = topic.NA.getMarks()
      
      bonus += (index+1)*(rights-wrongs)      
      if left != 0 and wrongs < left+right:
        bonus += left
    
    return bonus

  
  def getTopic(self,topicNum):
    if topicNum in list(range(1,6)):
      return self.topics[topicNum-1]
    return False
  
  def addResult(self,result):
    for topicMarks in result:
      self.marksByTopic.append(self.addTopic(topicMarks))
    self.bonus = self.setBonus()
    return sum(self.marksByTopic)
  
  def setGrade(self, g):
    self.grade = g
  
  

################################
### Complete Database Holdes ###
################################

## creates a list of marks awarded for every question grouped by the 5 topics 
## creates a list of marks awarded for every question grouped by the 5 topics 
class competitiveExam:
  def __init__(self, answerKey = None):
    self.__answerKey = self.__putSolutions(answerKey)
    self.scores = None
    self.competitors = []
  
  ###################################################################
  ##################      PRIVATE FUNCTIONS      ####################
  ###################################################################

  ## stores actual solution
  def __putSolutions(self,ansKey):
    while not ansKey:
      try:
        ansKey = eval(input("Enter the correct solutions as a list: "))
      except:
        continue
    return ansKey
      

  ## marks for every question of curent section
  def __marksInTopicRcrcv(self, answerSheet, init = 0, stop = None):
    unitTopicQ = len(self.__answerKey)//20
    init *= unitTopicQ
    if stop is None:
      stop = len(answerSheet) - unitTopicQ*19
    else:
      stop *= unitTopicQ

    markList = []
    incorrectAns = 0

    for index in range(init, stop,1):
      if answerSheet[index] == self.__answerKey[index]:
        markList.append(float(1))
      elif answerSheet[index] == None:
        markList.append(float(0))
      else:
        incorrectAns += 1
        markList.append(-incorrectAns/2)
      
    return markList


  def __topicMarks(self, answerSheet, init, topic):
    topicRes = []
    indxList = [10,14,17,19]

    if topic == 5:
      topicRes.append(self.__marksInTopicRcrcv(answerSheet, init))
    else:
      stop = indxList[topic-1]
      topicRes.append(self.__marksInTopicRcrcv(answerSheet, init, stop))
      topicRes += self.__topicMarks(answerSheet, stop, topic+1)
        
    return topicRes


  ####    EXAM STATS    ####
  def __getGrade(self, pCent):
    if pCent > 95:
      return 'O'
    elif pCent > 90:
      return 'A+'
    elif pCent > 85:
      return 'A'
    elif pCent > 75:
      return 'B+'
    elif pCent > 65:
      return 'B'
    elif pCent > 55:
      return 'C'
    elif pCent > 45:
      return 'D'
    else:
      return 'F'

  def __findGrade(self, part, total):
    pCent = self.__getPercent(part, total)
    return self.__getGrade(pCent)
  
  def __getPercent(self, part, total):
    return part*100/total
  
  def __getPercentile(self, loc):
    gotMarks = self.scores[loc]
    studentsBehind = len(self.scores[self.scores < gotMarks])
    

    if dupMarksLoc > 1:
      dupMarksLoc = len(np.where(self.scores == gotMarks)[0])
      getWithExtra = lambda x: gotMarks + self.competitors[x].bonus
      thisWithExtra = getWithExtra(loc)
      dupMarksLoc.remove(loc)      
      dupComparision = np.array(list(map(getWithExtra, dupMarksLoc)))
      studentsBehind += len(dupComparision[dupComparision < thisWithExtra])

    percentile = studentsBehind*100 / len(self.scores)
    
    return percentile
  

  ###################################################################
  ###################      PUBLIC FUNCTIONS      ####################
  ###################################################################
 
 
  # gives a list of the marks for all of the questions
  # grouped by the topic viz.  [[T1], [T2],...., [T5]]
  def addCompetitor(self, answerSheet):  
    marklist = self.__topicMarks(answerSheet, 0, 1)
    
    newCompetitor = competitor()
    finalMarks = newCompetitor.addResult(marklist)
    
    newCompetitor.setGrade(self.__findGrade(finalMarks,len(self.__answerKey)))

    self.competitors.append(newCompetitor)
    if self.scores is None:
      self.scores = np.array([finalMarks])
    else:
      self.scores = np.append(self.scores, finalMarks)
  
  def getCompetitor(self,rNo):
    score = self.scores[rNo]
    competitorData = self.competitors[rNo]
    return (competitorData,score)

  
  
  ###########################################################################
  ###########################################################################

  ###########################################################################
  ###########################################################################
  def gradingSys(self):
    print("\nMaximum Marks:  ",len(self.__answerKey),"\n"+"-"*20,"\n")
    print("Marks (%) \t\t Grade Assigned\n","\n"+"-"*9,"\t\t","-"*15,"\n")
    for percent in [95, 90, 85, 75, 65, 55, 45]:
      print("Above {}% \t\t\t{}".format(percent, self.__findGrade(percent+1,100)))
    print("Below or Equals to {}% \t\t{}".format(45, self.__findGrade(45,100)))

  def competitionStats(self):
    if len(self.competitors) > 0:
      MM = len(self.__answerKey)
      omitGrade = lambda x: x.grade
      gradelist = list(map(omitGrade, self.competitors))

      gradeDict = {}
      for grd in ['O','A+','A','B+','B','C','D','F']:
        gradeDict[grd] = len(list(filter(lambda x: (x==grd), gradelist)))
      
      #############
      print("""
      Maximum Marks: {}
      Average Marks scored by students: {}
      Toppers Marks: {} \t(scored by {} student(s))
      """.format(MM, sum(self.scores)/MM, max(self.scores), 
                 len(list(filter(lambda x: (x==max(self.scores)), self.scores)))))

      print("\n\nOverall Outcome of Competition: \n")
      keys, values = gradeDict.keys(), gradeDict.values()
      plt.bar(range(len(values)), values, color='b')
      plt.xticks(range(len(values)), keys)
      plt.show()
    else:
      print("Results will be out soon!! Keep checking the portal!")

  def competitorStats(self):
    if len(self.competitors) > 0:
      MM = len(self.__answerKey)
      unitSecMarks = MM//20
      mmByTopic = list(unitSecMarks*i for i in [10,4,3,2,1])

      index = int(input("Enter the roll number (0 to {}): ".format(len(self.competitors))))
      if index >= len(self.competitors):
        print("Results will be out soon!! Keep checking the portal!")
        return False
      
      thisCompetitor,finalScore = self.getCompetitor(index)
      grades = thisCompetitor.grade
      marksByTopic = thisCompetitor.marksByTopic

      print("""
      Roll No.: {}
      Marks Scored: {}/{}  ({}%)\n
      Grade: {}
      Percentile: {}
      Maximum scored in: Topic-{}   ({} marks)
      Minimum scored in: Topic-{}   ({} marks)
      """.format(index, finalScore, MM, self.__getPercent(finalScore,MM), 
                 grades, self.__getPercentile(index), 
                 marksByTopic.index(max(marksByTopic))+1, max(marksByTopic), 
                 marksByTopic.index(min(marksByTopic))+1, min(marksByTopic)))

      topics = ['Topic-1', 'Topic-2', 'Topic-3', 'Topic-4', 'Topic-5']
      topicPCent = []

      for i in range(len(marksByTopic)):
        topicPCent.append(self.__getPercent(marksByTopic[i],mmByTopic[i]))
      
      print("\n\nMark Distribution by Topic: \n")
      ## topicPCent can be kept as it is from above for loop
      topicPCent = marksByTopic
      plt.bar(range(len(topicPCent)), topicPCent, color='b')
      plt.xticks(range(len(topicPCent)), topics)
      plt.show()
      return True
    else:
      print("Results will be out soon!! Keep checking the portal!")
      return False
    
  
##################################################################
########                   DRIVER CODE                    ########
##################################################################
  
################          MAIN MENU          ################
def menu():
  print("""
         Main-Menu
        -----------\n
        1) Evaluate an Answersheet
        2) Upload & Evaluate All 100 Answersheets (autometically)
        3) Overall Exam Stats
        4) Check Your Result
        5) Grading Criteria

        ** Any other key to exit!
        """)
  return input("\nEnter your choice: ")
  

################        MAIN FUNCTION        ################
if __name__ == '__main__':
  # 20 questions with all ans as 1  ---->  replace 20 by num of questions
  thisCompetitiveExam = competitiveExam(answerKey = [1]*20)

  while True:
    clear_output()  
    ch = menu()
    
    ## Decision
    if ch == '1':
      clear_output(wait=True)
      ans = [1,0]*10
      if thisCompetitiveExam.addCompetitor(ans):
        print("Graded Successfully!/n")
      input("\nPress Enter!!") 

    elif ch == '2':
      clear_output(wait=True)
      ####
      numOfQue = 19071999   ## 100
      ansKey = [1]*numOfQue
      thisCompetitiveExam = competitiveExam(answerKey = ansKey)
      for rNo in range(1000):
        answerSheet = []
        for i in range(numOfQue):
          num = randint(1,1000)%100
          if num%10 == 0:
            answerSheet.append(0)
            #num = ''
          else:
            answerSheet.append(1)
        thisCompetitiveExam.addCompetitor(answerSheet)
      ####
      print("Results are ready!\n")
      input("\nPress Enter!!") 

    elif ch == '3':
      clear_output(wait=True)
      thisCompetitiveExam.competitionStats()
      input("\nPress Enter!!") 

    elif ch =='4':
      clear_output(wait=True)
      thisCompetitiveExam.competitorStats()
      input("\nPress Enter!!") 

    elif ch =='5':
      clear_output(wait=True)
      thisCompetitiveExam.gradingSys()
      input("\nPress Enter!!") 

    else:      
      clear_output(wait=True)
      del(thisCompetitiveExam)
      print("Good Bye!")
      break



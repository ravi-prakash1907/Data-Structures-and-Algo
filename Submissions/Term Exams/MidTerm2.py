## Libries
import numpy as np
import matplotlib.pyplot as plt
from random import randint
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



################################
### Result of One Competitor ###
################################

####  Result of One Candidate/Student  ####
class competitor:
  def __init__(self):
    self.grade = ''
    self.marksByTopic = []
    self.topics = []
  
  def addTopic(self,topicMarkList):
    newTopic = topic()

    newTopic.topicMarks = sum(topicMarkList)
    newTopic.correctAns.setMarks(list(filter(lambda x: (x>0), topicMarkList)))
    newTopic.incorrectAns.setMarks(list(filter(lambda x: (x<0), topicMarkList)))

    self.topics.append(newTopic)
    return newTopic.topicMarks
  
  def getTopic(self,topicNum):
    if topicNum in list(range(1,6)):
      return self.topics[topicNum-1]
    return False
  
  def addResult(self,result):
    for topicMarks in result:
      self.marksByTopic.append(self.addTopic(topicMarks))
    return sum(self.marksByTopic)
  
  def setGrade(self, g):
    self.grade = g
  


################################
### Complete Database Holdes ###
################################

## creates a list of marks awarded for every question grouped by the 5 topics 
class competitiveExam:
  def __init__(self, answerKey = None):
    self.__answerKey = self.__putSolutions(answerKey)
    self.scores = []
    self.competitors = []
  
  ## stores actual solution
  def __putSolutions(self,ansKey):
    while not ansKey:
      try:
        ansKey = eval(input("Enter the correct solutions as a list: "))
      except:
        continue
    return ansKey
      
  
  ###########################################################################


  ## counts total questions in current topic
  def __queInTopic(self,topicNum):
    unitTopicQ = len(self.__answerKey)//20

    if topicNum == 1:
      return unitTopicQ*10
    
    elif topicNum == 2:
      return unitTopicQ*4
    
    elif topicNum == 3:
      return unitTopicQ*3
    
    elif topicNum == 4:
      return unitTopicQ*2
    
    ## puts all left questions in section as the year of birth may or may not be
    ## divisible by 20 leading to impossible division of question
    ## in ratio 10:4:3:2:1
    elif topicNum == 5:
      return len(self.__answerKey) - unitTopicQ*19
    
    else:
      return 0
  
  ## returns the index of questions for current topic/section
  def __topicSlice(self,topicNum):
    prvTopics = lambda x: list(range(1,x))
    tillThisTopic = lambda x: list(range(1,x+1))

    # index of first question of this section
    begIndex = sum(list(map(self.__queInTopic,prvTopics(topicNum))))
    # index of last question of this section
    endIndex = sum(list(map(self.__queInTopic,tillThisTopic(topicNum))))

    return (begIndex, endIndex)
  
  
  ###########################################################################


  ## marks for every question of curent section
  def __marksInTopic(self, answerSheet, topicNum):
    sectionRange = self.__topicSlice(topicNum)
    init = sectionRange[0] 
    stop = sectionRange[1]

    markList = []
    incorrectAns = 0

    for index in range(init, stop,1):
      if answerSheet[index] == self.__answerKey[index]:
        markList.append(float(1))
      elif answerSheet[index] == None:
        markList.append(float(0))
      elif answerSheet[index] != self.__answerKey[index]:
        incorrectAns += 1
        markList.append(float(-incorrectAns/2))
    
    return markList
  
  
  ###########################################################################

  
  # gives a list of the marks for all of the questions
  # grouped by the topic viz.  [[T1], [T2],...., [T5]]
  def addCompetitor(self, answerSheet):
    marklist = []
    for topic in range(1,6):
      marklist.append(self.__marksInTopic(answerSheet, topic))
    
    newCompetitor = competitor()
    finalMarks = newCompetitor.addResult(marklist)
    newCompetitor.setGrade(self.findGrade(finalMarks,len(self.__answerKey)))

    self.competitors.append(newCompetitor)
    self.scores.append(finalMarks)
  
  def getCompetitor(self,rNo):
    score = self.scores[rNo]
    competitorData = self.competitors[rNo]
    return (competitorData,score)

  
  
  ###########################################################################

  ####    EXAM STATS    ####
  def getGrade(self, pCent):
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

  def findGrade(self, part, total):
    pCent = self.getPercent(part, total)
    return self.getGrade(pCent)
  
  def getPercent(self, part, total):
    return part*100/total
  
  
  ########               USERS INTERACT HERE                ########
  
  def gradingSys(self):
    print("\nMaximum Marks:  ",len(self.__answerKey),"\n"+"-"*20,"\n")
    print("Marks (%) \t\t Grade Assigned\n","\n"+"-"*9,"\t\t","-"*15,"\n")
    for percent in [95, 90, 85, 75, 65, 55, 45]:
      print("Above {}% \t\t\t{}".format(percent, self.findGrade(percent+1,100)))
    print("Below or Equals to {}% \t\t{}".format(45, self.findGrade(45,100)))

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
      mmByTopic = list(map(self.__queInTopic,list(range(1,6))))

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
      Maximum scored in: Topic-{}   ({} marks)
      Minimum scored in: Topic-{}   ({} marks)
      """.format(index, finalScore, MM, float(self.getPercent(finalScore,MM)), 
                grades, marksByTopic.index(max(marksByTopic))+1, max(marksByTopic), 
                marksByTopic.index(min(marksByTopic))+1, min(marksByTopic)))

      topics = ['Topic-1', 'Topic-2', 'Topic-3', 'Topic-4', 'Topic-5']
      topicPCent = []

      for i in range(len(marksByTopic)):
        topicPCent.append(self.getPercent(marksByTopic[i],mmByTopic[i]))
      
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
  # 100 questions with ans. = 1  -->  replace 100 by 19071999
  thisCompetitiveExam = competitiveExam(answerKey = [1]*100)

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
      numOfQue = 100 #19071999
      ansKey = [1]*numOfQue
      thisCompetitiveExam = competitiveExam(answerKey = ansKey)
      for rNo in range(100):
        answerSheet = []
        for i in range(numOfQue):
          num = 1
          if randint(1,1000)%7 == 0:
            num = 0
          answerSheet.append(num)
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
      print("Good Bye!")
      break












#!/usr/bin/env python
# coding: utf-8

# In[2]:


import glob
import random

def makeVocabFile(filename, vocabDict):
   # Creates a vocabulary list in a file based on the dictionary passed.
   fd = open(filename, "w")

   for engWord in vocabDict.keys():# The file in TXT is separated by: and the back half is put in this section
      fd.write(cnWord + ":")
      fd.write(str(vocabDict[cnWord]).replace('[','').replace(']', '').replace("\', \'",",").replace("\'",""))
      fd.write('\n')
      
   fd.close()

def quizQuestion(cnWord, ans, testword):
   '''
   Quizzes the user on one specific Chinese word.

   Receives: Chinese word and a list of English words.
   Returns: True or False, depending on the question was answered correctly.
   '''
   incorrect = False
   i = 1

   print
   print ("中文: " + cnWord)
   print ("输入" + str(len(ans)) + " 相应的英文单词.")
      
   while (len(ans) > 0 and incorrect == False):
      #print the actual input and the expected input
      print(testword)
      print(ans)
      # take testword and ans as sets in order to do subtraction afterwords
      a = set(testword)
      b = set(ans)
      if (testword == ans):
         # remove the answered word from the list
         ans = list(b-a)
         i += 1
      else:
         print ("Incorrect.")
         print ("The correct answer is:" + ans[0])
         incorrect = True

   if not incorrect:
      print("Correct!")

   print
   print ("---")


   return not incorrect

def createDict(filename):
   '''
   Loads a dictionary based on a file containing vocabulary words.

   Receieves: Vocabulary file to read in.
   Returns: Dictionary with key being Chinese word and item being list of English words.
   '''
   vocabDict = {}   

   fd = open(filename, "r", encoding='UTF-8')
   
   for line in fd:
      line = line.strip()

      tokens = line.split(":")      
      cnWord = tokens[0]
      engWords = tokens[1]
      
      engWordList = tokens[1].split(",")
      
      vocabDict[cnWord] = engWordList

   fd.close()

   return vocabDict


def vocabTest():
   '''
   Loads a dictionary based on a file containing vocabulary words.

   Receieves: Vocabulary file to read in.
   Returns: Dictionary with key being Chinese word and item being list of English words.
   '''
   vocabTest = [] # Initiate a empty list to store the results
   f = open('test_input0.txt', "r", encoding='UTF-8')
   sourceInLines = f.readlines()  # Read the content by lines
   f.close()
   for line in sourceInLines:
      temp1 = line.strip('\n')  # strip the line changing symbol '\n'
      temp2 = temp1.split(',')  # split the list by ','
      vocabTest.append(temp2)
   return vocabTest


   
def main():
   '''
   GUIDE:
   1. User chooses a vocabulary list.
   2. The complete quiz list is generated.
   3. The input is tested.
   '''
   fileList = glob.glob("*.txt")

   if len(fileList) == 0:
      print ("There are no vocab lists available!")
      return

   print ("Welcome to the vocabulary quiz program.  Select one of the following word lists:")
   
   for file in fileList:
      print ("\t"+ file)
   
   filename = input("Please make your selection: ")
   
   while filename not in fileList:
      filename = input("Please make a valid selection: ")

   vocabDict = createDict(filename)
   #initiate a list with all the words
   quizList = vocabDict.keys()
   
   numCorrect = 0
   incorrectDict = {}
 
   #Test each word
   inputWord = vocabTest()
   a = 0

   for word in quizList:
      a += 1
      if quizQuestion(word, vocabDict[word][:], inputWord[a-1]) == True:
         numCorrect += 1
      else:
         incorrectDict[word] = vocabDict[word]


   #Show the result with a given input
   print(str(numCorrect) + (" out of 16 correct."))

main()


# In[ ]:





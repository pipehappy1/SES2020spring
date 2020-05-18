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

def quizQuestion(cnWord, engWords):
   '''
   Quizzes the user on one specific Chinese word.
   Receives: Chinese word and a list of English words.
   Returns: True or False, depending on if the question was answered correctly.
   '''
   incorrect = False
   i = 1

   print
   print ("中文: "+ cnWord)
   print ("输入" + str(len(engWords)) + " 相应的英文单词.")
      
   while (len(engWords) > 0 and incorrect == False):
      engWord = input("Word [" + str(i) + "]: ")  # input your answer

      if (engWord in engWords):  # If your answer is right
         engWords.remove(engWord)
         i += 1 
      else:                     # If your answer is wrong
         print ("Incorrect.")
         print ("The correct answer is:" + engWords[0])
         incorrect = True

   if not incorrect:
      print ("Correct!")

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

   fd = open(filename, "r", encoding='UTF-8')# Open the file and recognize the cnWord
   
   for line in fd:
      line = line.strip()  # The number of test words in the wordlist

      tokens = line.split(":")      
      cnWord = tokens[0]
      engWords = tokens[1]
      
      engWordList = tokens[1].split(",")   # More than one answer
      
      vocabDict[cnWord] = engWordList

   fd.close()

   return vocabDict
   
def main():
   '''
   GUIDE:
   1. User chooses a vocabulary list.
   2. User chooses number of words in list to be quizzed on.
   3. Random quiz list is generated.
   4. User is quizzed on each word.
   5. If the user missed any, user given option to make a new vocab list of missed words.
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
  
   noQs = int(input(str(len(vocabDict)) + " entries found.  How many words would you like to be quizzed on? "))

   # make sure we get a valid input
   while(noQs < 1 or noQs > len(vocabDict)):
      noQs = int(input("Invalid input.  Please try again: "))

   # generates a quiz by sampling without replacement
   quizList = random.sample(vocabDict.keys(), noQs)
   
   numCorrect = 0
   incorrectDict = {}
 
   # quizzes user on each word
   for word in quizList:
      if quizQuestion(word, vocabDict[word][:]) == True:
         numCorrect += 1
      else:
         incorrectDict[word] = vocabDict[word]

   print
   str(numCorrect) + (" out of ")+ str(noQs) + (" correct.")

main()


# In[ ]:





# In[ ]:





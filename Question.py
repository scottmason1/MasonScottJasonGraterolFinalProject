'''
Scott Mason and Jason Graterol
smason8@binghamton.edu and jgrater1@binghamton.edu
CS110
Section B54 and B57
Final Project
'''

import random
from PIL import Image

'''This module provides all logic needed for the U.S Capitals Quiz
'''

class Question:

  capitalsDict = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',-
                    'Arizona': 'Phoenix', \
                    'Arkansas': 'Little Rock',
                    'California': 'Sacramento', 'Colorado': 'Denver', \
                    'Connecticut': 'Hartford', 'Delaware': 'Dover',
                    'Florida': 'Tallahassee', \
                    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
                    'Idaho': 'Boise', 'Illinois': \
                      'Springfield', 'Indiana': 'Indianapolis',
                    'Iowa': 'Des Moines', 'Kansas': \
                      'Topeka', 'Kentucky': 'Frankfort',
                    'Louisiana': 'Baton Rouge', 'Maine': \
                      'Augusta', 'Maryland': 'Annapolis',
                    'Massachusetts': 'Boston', 'Michigan': \
                      'Lansing', 'Minnesota': 'Saint Paul',
                    'Mississippi': 'Jackson', 'Missouri': \
                      'Jefferson City', 'Montana': 'Helena',
                    'Nebraska': 'Lincoln', 'Nevada': \
                      'Carson City', 'New Hampshire': 'Concord',
                    'New Jersey': 'Trenton', \
                    'New Mexico': 'Santa Fe', 'New York': 'Albany',
                    'North Carolina': 'Raleigh',
                    'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
                    'Oklahoma': 'Oklahoma City',
                    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
                    'Rhode Island': 'Providence',
                    'South Carolina': 'Columbia',
                    'South Dakota': 'Pierre', 'Tennessee':
                      'Nashville', 'Texas': 'Austin',
                    'Utah': 'Salt Lake City', 'Vermont':
                      'Montpelier', 'Virginia': 'Richmond',
                    'Washington': 'Olympia', 'West Virginia': \
                      'Charleston', 'Wisconsin': 'Madison',
                    'Wyoming': 'Cheyenne'}

  #Creates new question class
  def __init__(self):
    self.__state = ""
    self.__capital = ""

  #Returns the length of the state dictionary
  def getLength(self):
    return len(Question.capitalsDict)

  #Returns a random number no larger than the length of the dictionary
  def getRandom(self):
    return random.randrange(0, self.getLength(), 1)

  #Returns the state in the random index number
  def getState(self, number):
    return list(Question.capitalsDict.keys())[number]

  #Returns the Capital of the state
  def getCapital(self, state):
    return Question.capitalsDict[state]

  #Deletes the entry of the dictionary associated with the index
  def deleteEntry(self, number):
    del Question.capitalsDict[self.getState(number)]

  #Returns a copy of the dictionary
  def copyDictionary(self):
    return Question.capitalsDict.copy()

  #Restores the dictionary to the copy
  def restoreDictionary(self, copy):
    Question.capitalsDict = copy

  #Returns a sorted list of the keys of the dictionary
  def sortedKeyList(self):
    return sorted(list(Question.capitalsDict.keys()))

  #Resizes an image (NOTE: Requires Pillow module to be installed)
  def imageResize(self, inputImage, width, height):
    image = Image.open(inputImage)
    imageResize = image.resize((width, height))
    return imageResize

  #Returns true or false if answer matches the capital for the state
  def correctAnswer(self, answer, number):
    #print(answer)
    #print(Question.STATE_CAPITALS[self.getState(number)])
    return answer.lower() == Question.capitalsDict \
      [self.getState(number)].lower()

  # -- Convert to Str -----------------------------------------------------
  def __str__(self, number):
    return "The state is " + self.getState(number) + " and the answer is " \
           + self.getCapital(self.getState(number))

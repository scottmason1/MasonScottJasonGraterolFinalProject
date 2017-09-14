-'''
Scott Mason and Jason Graterol
smason8@binghamton.edu and jgrater1@binghamton.edu
CS110
Section B54 and B57
Final Project
'''

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from Question import *

'''This file contains all elements of the GUI needed for the U.S Capitals
Quiz'''

'''This class contains elements of the initial GUI to run,
linking to other elements of the program'''

class GeoGUI:

  MAIN_WINDOW_WIDTH = 490
  MAIN_WINDOW_HEIGHT = 470

  MAIN_IMAGE_WIDTH = 490
  MAIN_IMAGE_HEIGHT = 353

  #Constructor
  def __init__(self, master):

    #Model
    self.__question = Question()

    self.__win = master

    #Sets the title of the window
    self.__win.title("U.S Capitals Quiz")

    #Centers the window on the screen
    self.__mainScreenWidth = self.__win.winfo_screenwidth()
    self.__mainScreenHeight = self.__win.winfo_screenheight()
    self.__mainXCoord = (self.__mainScreenWidth / 2) - (
    GeoGUI.MAIN_WINDOW_WIDTH / 2)
    self.__mainYCoord = (self.__mainScreenHeight / 2) - (
    GeoGUI.MAIN_IMAGE_HEIGHT / 2) - 75
    self.__win.geometry("%dx%d+%d+%d" % (GeoGUI.MAIN_WINDOW_WIDTH, \
                                         GeoGUI.MAIN_WINDOW_HEIGHT, \
                                         self.__mainXCoord, \
                                         self.__mainYCoord))

    #Label for the Title
    self.__mainLabel = Label(self.__win,
                             text="Welcome to the U.S Capitals Quiz",
                             width=50, fg='red')
    self.__mainLabel.grid(row=1, column=2, padx=1, pady=1)

    #Button to start quiz
    self.__quizButton = Button(self.__win, text="Begin Quiz",
                               command=self.quizMaker, width=10, fg="blue")
    self.__quizButton.grid(row=51, column=2)

    #Button to start answer key
    self.__stateButton = Button(self.__win, text="Answer Key",
                                command=self.tableStates, fg="blue")
    self.__stateButton.grid(row=52, column=2)

    #Resize image
    image = self.__question.imageResize("unitedstates.png", \
                                GeoGUI.MAIN_IMAGE_WIDTH, \
                                GeoGUI.MAIN_IMAGE_HEIGHT)

    photo = ImageTk.PhotoImage(image)

    #Create Button that links to larger view of image
    self.__mapButton = Button(self.__win, command=self.mapStates,
                              image=photo)
    self.__mapButton.image = photo
    self.__mapButton.grid(row=50, column=2)

    #Create button that exits the program
    self.__exitButton = Button(self.__win, text="Exit", command=self.exit,
                               width=5, fg="blue")
    self.__exitButton.grid(row=54, column=2)

  #Event Handlers

  #Hides initial GUI window and opens a window with a list of states.
  #Clicking on buttons shows that states capital, and clicking again
  #returns button text to capital
  def tableStates(self):

    #Hides initial GUI Window
    self.__win.withdraw()

    WINDOW_WIDTH = 954
    WINDOW_HEIGHT = 285

    ANSWER_KEY_SPACE = 10
    ANSWER_KEY_COUNT = 7

    self.__answer = Toplevel()

    #Set window title
    self.__answer.title("Answer Key")

    #Center window
    self.__answerScreenWidth = self.__answer.winfo_screenwidth()
    self.__answerScreenHeight = self.__answer.winfo_screenheight()
    self.__answerXCoord = (self.__mainScreenWidth / 2) - (
      WINDOW_WIDTH / 2)
    self.__answerYCoord = (self.__mainScreenHeight / 2) - (
      WINDOW_HEIGHT / 2) - 75
    self.__answer.geometry("%dx%d+%d+%d" % (WINDOW_WIDTH, \
                                         WINDOW_HEIGHT, \
                                         self.__answerXCoord, \
                                         self.__answerYCoord))

    #Override what happens when X Button is clicked
    self.__answer.protocol('WM_DELETE_WINDOW', self.quit)

    #Initialize Values
    stateRow = 0
    columnState = 0
    self.__buttonText = {}

    #Create window
    for stateIndex in range(0, len(self.__question.sortedKeyList())):

      #When to go to new column
      if stateIndex % ANSWER_KEY_SPACE == 0:
        columnState += ANSWER_KEY_COUNT
        stateRow = 0

      #Create label with state on list
      self.__labelState = Label(self.__answer,
                                text=self.__question.sortedKeyList() \
                                  [stateIndex])
      self.__labelState.grid(row=stateRow, column=columnState)

      #Create dictionary of StringVar, set button text
      self.__buttonText[stateIndex] = StringVar()
      self.__buttonText[stateIndex].set("Capital")

      #Create button, use lambda to pass count into event handler
      self.__buttonState = Button(self.__answer, \
                                  textvariable=self.__buttonText \
                                    [stateIndex], width=15, command=lambda\
                                  count=stateIndex: self.showCapital(count))

      self.__buttonState.grid(row=stateRow, column=columnState + 2)

      stateRow += 1

      # print(self.__labelDict)
      # print(self.__buttonState)

    #Create Button to return to main page program
    self.__exitButton = Button(self.__answer, text = "Return To Main Page",\
                                 command = self.quit)
    self.__exitButton.grid(row = 11, column = 23)

  #Closes Answer key Window, shows initial GUI Window
  def quit(self):
    self.__answer.destroy()
    self.__win.deiconify()

  #Controls text on Buttons in Answer Key Window
  def showCapital(self, count):
    if self.__buttonText[count].get() == "Capital":
      #print(count)
      self.__buttonText[count].set \
        (self.__question.getCapital \
           (self.__question.sortedKeyList()[count]))
    else:
      self.__buttonText[count].set("Capital")

  #Opens up enlarged view of map
  def mapStates(self):

    IM_WIDTH = 1280
    IM_HEIGHT = 922

    self.__mapWindow = Toplevel()

    #Set title of window
    self.__mapWindow.title("Map of the U.S")

    #Center window
    self.__mapXCoord = (self.__mainScreenWidth / 2) - (
      IM_WIDTH / 2)
    self.__mapYCoord = (self.__mainScreenHeight / 2) - (
      IM_HEIGHT / 2) - 50
    self.__mapWindow.geometry("%dx%d+%d+%d" % (IM_WIDTH, \
                                         IM_HEIGHT, \
                                         self.__mapXCoord, \
                                         self.__mapYCoord))

    #Place enlarged view on screen
    photo = PhotoImage(file="unitedstates.png")
    self.__photoLabel = Label(self.__mapWindow, image = photo)

    self.__photoLabel.grid()

    self.__mapWindow.mainloop()

  #Close initial GUI window, open up Quiz GUI Window
  def quizMaker(self):
    root.withdraw()
    QuizGUI()

  #Exit Program
  def exit(self):
    self.__win.destroy()

'''
This class creates the GUI for the Quiz
'''

class QuizGUI:

  WINDOW_WIDTH = 490
  WINDOW_HEIGHT = 430

  IMAGE_WIDTH = 490
  IMAGE_HEIGHT = 303

  #Constructor
  def __init__(self):

    self.__question = Question()

    #Initialize values
    self.__continueBox = None
    self.__score = 0

    #Get random number
    self.__number = self.__question.getRandom()

    self.__quizWindow = Toplevel()

    #Set window title
    self.__quizWindow.title("U.S Capitals Quiz")

    #Center Window
    self.__screenWidth = self.__quizWindow.winfo_screenwidth()
    self.__screenHeight = self.__quizWindow.winfo_screenheight()
    self.__xCoord = (self.__screenWidth / 2) - (QuizGUI.WINDOW_WIDTH / 2)
    self.__yCoord = (self.__screenHeight / 2) - \
                    (QuizGUI.WINDOW_HEIGHT / 2) - 35
    self.__quizWindow.geometry("%dx%d+%d+%d" % (QuizGUI.WINDOW_WIDTH, \
                                                QuizGUI.WINDOW_HEIGHT, \
                                                self.__xCoord, \
                                                self.__yCoord))

    #Get states image associated with number
    image = self.__question.imageResize(self.__question.getState \
                                          (self.__number) + '.png', \
                                        QuizGUI.IMAGE_WIDTH, \
                                        QuizGUI.IMAGE_HEIGHT)

    #Place image in Window
    self.__photo = ImageTk.PhotoImage(image)
    self.__photoLabel = Label(self.__quizWindow, image=self.__photo)
    self.__photoLabel.grid(row = 1, column = 1, sticky = E, columnspan = 11)

    #print(Question.STATE_CAPITALS)
    #print(len(Question.STATE_CAPITALS))

    #Create label for question
    self.__questionLabel = Label(self.__quizWindow, \
                                 text = "What is the capital" + \
                                        " of the state shown?")
    self.__questionLabel.grid(row = 2, column = 4)

    #Create entry box for answer input
    self.__answerInput = Entry(self.__quizWindow, width = 30)
    self.__answerInput.bind('<Return>', self.enableButton)
    self.__answerInput.grid(row = 3, column = 4)

    #Create Next Button
    self.__nextButton = Button(self.__quizWindow, text = "Next", \
                               command = self.checkAnswer)
    self.__nextButton.configure(state='disabled')
    self.__nextButton.grid(row = 4, column = 4)

    #Create Return To Main Page Button
    self.__returnButton = Button(self.__quizWindow, \
                                 text = "Return To Main Page", \
                                 command = self.quitButton)
    self.__returnButton.grid(row = 6, column = 4)

    #Create score tracker
    self.__scoreLabel = Label(self.__quizWindow, text = "Score: ")
    self.__scoreLabel.grid(row = 5, column = 9)
    self.__scoreTracker = StringVar()
    self.__scoreTracker.set(str(self.__score) + '%')
    self.__trackerLabel = Label(self.__quizWindow, \
                                textvariable = self.__scoreTracker)
    self.__trackerLabel.grid(row = 6, column = 9)

    #Create questions remaining tracker
    self.__remaining = Label(self.__quizWindow, \
                             text = "Questions Remaining:")
    self.__remaining.grid(row = 5, column = 3)
    self.__remainingCount = IntVar()
    self.__remainingCount.set(len(Question.capitalsDict))
    self.__countLabel = Label(self.__quizWindow, \
                         textvariable = self.__remainingCount)
    self.__countLabel.grid(row = 6, column = 3)

    #Create copy of dictionary
    self.__copy = self.__question.copyDictionary()

    #Set what happens when X Button is pressed
    self.__quizWindow.protocol('WM_DELETE_WINDOW', self.quitButton)

  #Event handlers

  #Enables Next Button when text is in box after Enter is pressed
  def enableButton(self, event):
    self.__continueBox = self.__answerInput.get()
    if(self.__continueBox):
      self.__nextButton.configure(state='normal')

  #Closes window, restores dictionary to original and unhides the initial
  #window
  def quitButton(self):
    self.__quizWindow.destroy()
    self.__question.restoreDictionary(self.__copy)
    root.deiconify()

  #Update the state picture after the next window is pressed, update score,
  #and update questions remaining
  def updatePicture(self):

    image = self.__question.imageResize(self.__question.getState  \
                                          (self.__number) + '.png', \
                                        QuizGUI.IMAGE_WIDTH, \
                                        QuizGUI.IMAGE_HEIGHT)

    self.__photo2 = ImageTk.PhotoImage(image)
    self.__photoLabel.configure(image = self.__photo2)
    self.__photoLabel.image = self.__photo2

    self.__scoreTracker.set(str(self.__score) + '%')
    self.__remainingCount.set(len(Question.capitalsDict))

  #Check answer after next button is pressed
  def checkAnswer(self):

    scoreStr = str(self.__score) + '%'

    #Disable Next Button
    self.__nextButton.configure(state='disabled')

    #Check answer input against capitals dictionary
    if self.__question.correctAnswer \
        (self.__answerInput.get(), self.__number):
      messagebox.showinfo("Correct!", "Correct!")
      self.__score += 2
    else:
      messagebox.showinfo("Incorrect!", \
                          "Incorrect! \nThe state is %s" \
                          % (self.__question.getState(self.__number) + \
                             " and the capital is %s" % \
                             (self.__question.getCapital \
                                (self.__question.getState(self.__number)))))

    #Set new score
    self.__scoreTracker.set(scoreStr)

    #Delete entry in dictionary of state just asked
    self.__question.deleteEntry(self.__number)

    #For programmer use, to test what happens when quiz ends
    if (self.__answerInput.get().upper() == "MAKE IT STOP"):
      Question.capitalsDict.clear()

    #Clear entry box
    self.__answerInput.delete(0, END)

    #Determine if program can continue
    if (len(Question.capitalsDict) > 0):
      self.__number = self.__question.getRandom()
      self.updatePicture()

    #End Quiz
    else:
      self.quitButton()
      messagebox.showinfo('Total Score', "Your total score was %s!" \
                          % scoreStr)

      #Restore dictionary to original copy
      self.__question.restoreDictionary(self.__copy)

#Start program
root = Tk()
GeoGUI(root)
root.mainloop()

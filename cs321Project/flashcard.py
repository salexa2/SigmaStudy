#creates a flashcard object 

#from turtle import back
from tkinter import * 
import customtkinter


class flashcard:
 
   front_card = ""
   back_card = ""
   state = 0
  
   #color
   #setcolor
   #themes

   #gets the front of card
   def getFront(self):
       return self.front_card
   #gets the back of card
   def getBack(self):
       return self.back_card
   #sets the front of card
   def setFront(self,front_input):
       self.front_card = front_input
   #sets the back of card
   def setBack(self,back_input):
       self.back_card = back_input
   #prints the front of a card
   def printFront(self):
       print("front:" + self.front_card +"\n")
   #prints the back of a card
   def printBack(self):
       print("back:" + self.back_card + "\n")
   #flips the card
   def flip(self, card_frame, state):
       if(state==0):
         #  print("here\n")
           card_frame.configure(text=self.getBack())
           self.state = 1
         

       else:
          # print("here2\n")
           card_frame.configure(text =self.getFront())
           self.state = 0
         
   #displays the flash card
   def displayCard(self, root):
       print("Unit Testing 4.0: Card should show\n")
       card_frame = customtkinter.CTkButton(root, text_color = "#000000", text = self.getFront(), hover_color="#F7F7F7", fg_color="#FFFFFF",width = 1000,height = 400, command = self.flip(card_frame,self.state)) 
       card_frame.place(x = 100, y= 100)
      

   
       
        
    



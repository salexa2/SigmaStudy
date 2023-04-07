#from ast import Delete
from tkinter.tix import COLUMN
from flashcardset import * 
import tkinter 
from tkinter import * 
import customtkinter
from PIL import Image  

class gallary():

  
    #holds a list of play buttons,frames, and labels for each set

   

    #list of flashcard sets - a list of lists
    library = []
    #the gallary 
    root = None
    #base number of rows and columns that hold each set 
    row_num = 0
    column_num = 0 
  

    def __init__(self,gal,main):
        self.library = main
        self.root = gal
    #prints the num of sets
    def print_size(self):
        print("Count:", len(self.library))
        print("\n")

    def optionmenu_callback(self, choice):
      pass
          

    
    #displays all the flashcard sets
    def display(self):
        count = 0
        posx = 50
        posy = 100
        self.print_size()



        for i in self.library:   
           # print("count var: ",count)
            if(count < len(self.library)):
                gallary_frame = customtkinter.CTkFrame(self.root, width = 100, height = 100)
                gallary_frame.place(x = posx, y = posy)
                i.displaySet(gallary_frame,self.root)
                combobox = customtkinter.CTkOptionMenu(master=gallary_frame, fg_color = "#279400", button_color = "#279400", dropdown_hover_color = "#1C6B00" ,  width = 15, height = 15,values=["Edit", "Delete Set"], command = self.optionmenu_callback)
                combobox.place(x= 35,y=75)
                combobox.set("Edit")  # set initial value
              

                posx+=150
               
            if(posx == 800):
                posx = 0
                posy+= 50
            count+=1
        return

    



       
   


             



        




       








   





    






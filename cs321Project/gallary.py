#from ast import Delete
from tkinter.tix import COLUMN

import tkinter 
from tkinter import * 
import customtkinter

import flashcardset 
from flashcardset import *
from SaveAndLoad import *
 

class gallary():


    #list of flashcard sets - a list of lists
    lib = []
    #base number of rows and columns that hold each set 
    row_num = 0
    column_num = 0 
    #saved name - DO NOT TOUCH THIS
    saveName  = "data.json"
    # set initial value
    #constructor
    def __init__(self):
       pass 

    #return gallerys set - a list of lists 
    def returnGal(self):
        return self.lib

    #prints the num of sets
    def print_size(self):
        print("Count:", len(self.lib))
        print("\n")
   
    #gets the size of the set 
    def getSize(self):
        return len(self.lib)

    #call to create a set
    def create_Set(self,upload_frame):
        print("Unit Testing 2.1: Flashcard set created\n")
        flashset = flashcardset(upload_frame,self)
        flashset.creating_set_page()
       # return
     
     #adds a set to the gallary
    def add_Set(self,flset):
         self.lib.append(flset)

    #returns the saveName - DO NOT TOUCH 
    def return_saveN(self):
        return self.saveName

    #prints all the sets of a gallary 
    def print_Gal(self):
        print("__________________\n")
        for x in self.lib:
         print(x.printAll())
        print("__________________\n")
    


     #edit, delete a set, shuffle a ste possibly 
    def optionmenu_callback(self, choice):
       print("optionmenu dropdown clicked:", choice)


    #displays all the flashcard sets on the gallary page
    def display(self, galf):
        upload_label = customtkinter.CTkLabel(galf, text="This is the Gallary", font=customtkinter.CTkFont(size=20, weight="bold"))
        upload_label.place(x=600,y=0)
        count = 0
        posx = 50
        posy = 100

        optionmenu_var = customtkinter.StringVar(value="✍")



        print("Unit Testing 3.1: Gallary: shows all the sets\n")
       

        for i in self.lib:   
           # print("count var: ",count)
            if(count < len(self.lib)):
                set_frame = customtkinter.CTkFrame(galf, width = 100, height = 100)
                set_frame.place(x = posx, y = posy)
                i.displaySet(set_frame,galf)
                combobox = customtkinter.CTkOptionMenu(set_frame, fg_color = "#279400", button_color = "#279400", dropdown_hover_color = "#1C6B00" , width = 18, height = 18,values=["Edit", "Delete"],font=customtkinter.CTkFont(size=14), command = self.optionmenu_callback, variable = optionmenu_var)
                combobox.place(x= 27,y=75)
                combobox.set("✍")  # set initial value
              

                posx+=150
               
            if(posx == 1200):
                posx = 50
                posy+= 100
            count+=1
        return
    #loads flashcard sets (called on program launch) --DO NOT TOUCH UNLESS YOU'RE CHASE 
    def loadSets(self):
        loader = SaveAndLoad.load_data(self.saveName);
        if loader is None:
            print("no saved data found")
            return
       
        self.lib = loader.copy();




    



       
   


             



        




       








   





    






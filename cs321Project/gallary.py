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
    #gallarys main frame
    galframe = None
   


    #constructor
    def __init__(self,root):
       self.mainr = root

    #return gallerys set - a list of lists 
    def returnGal(self):
        return self.lib

    def setLib(self,newlib):
        self.lib = newlib

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
        flashset = flashcardset(upload_frame)
        flashset.creating_set_page(self)
       # return
     
     #adds a set to the gallary
    def add_Set(self,flset):
         self.lib.append(flset)

    #removes a set 
    def remove_Set(self,cardset):
        self.lib.remove(cardset)

    #returns the saveName - DO NOT TOUCH 
    def return_saveN(self):
        return self.saveName

    #prints all the sets of a gallary 
    def print_Gal(self):
        print("__________________\n")
        for x in self.lib:
         print(x.printAll())
        print("__________________\n")
    
    #gets the gallarys main frame
    def get_galFrame(self):
        return self.galframe
    
    #sets the gal frame for use later
    def set_galFrame(self,frame):
       self.galframe = frame


  
    #displays all the flashcard sets on the gallary page
    def display(self, galf):
        upload_label = customtkinter.CTkLabel(galf, text="This is the Gallary", font=customtkinter.CTkFont(size=20, weight="bold"))
        upload_label.place(x=600,y=0)
        count = 0
        posx = 50
        posy = 100

        


        print("Unit Testing 3.1: Gallary: shows all the sets\n")
       

        for i in self.lib:   
           # print("count var: ",count)
            if(count < len(self.lib)):
                set_frame = customtkinter.CTkFrame(galf, width = 100, height = 100)
                set_frame.place(x = posx, y = posy)
                i.displaySet(set_frame,galf,self)
               
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




    



       
   


             



        




       








   





    






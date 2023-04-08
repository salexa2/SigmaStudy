from flashcard import * 
import tkinter 
from tkinter import * 
import customtkinter
from SaveAndLoad import *




class flashcardset:

    #-------------GLOBAL VARIABLE------------------

    #WARNING: we use global so that way the flashsets do not merge. Do not remove global in this set.

    #list of flashcards
    global flashset 
    #set name
    global flash_name  
    #keeps track of current set index
    global index
    #reference to gallary object
    global gall
    #flashcard set creation frame.
    global flashframe

    #global play_button   - del later
  
  
    #constructor
    def __init__(self, uploadf,gal_Set):
        self.flash_frame = customtkinter.CTkFrame(uploadf, width = 550, height = 375, fg_color= "#279400")
        self.flash_frame.place(x =700,y=100)
        self.flashset = []
        self. flash_name = ""
        self.index = 0
        self.gall = gal_Set
        #self.play_button = customtkinter.CTkImage(light_image=Image.open("widgets\start-green-play-icon-1.png"))


     #-----------------FUNCTIONS----------------------       
    #Gets the size of a set
    def get_Size(self):
        return len(self.flashset)
    #Gets a sets name
    def get_Name(self):
        return self.flash_name
    #sets a sets name
    def set_Name(self, name):
        self.flash_name = name

    #print oiut all the cards of a set 
    def printAll(self):
        print("---FlashCard Set---\n")
        print(self.get_Name())
        for x in self.flashset :
           x.printFront()
           x.printBack()

        print("---FlashCard End---\n")
    #displays a card
    def displayCard(self,root,index):
        cardIndex = index
        print("Unit Testing 3.4: display current card\n")
        self.flashset[cardIndex].printFront()
        self.flashset[cardIndex].printBack()
        self.flashset[cardIndex].displayCard(root)


     #helps move to the next card
    def updateCount(self,play_f, button):
           self.index = self.index + 1

          # print("index:\n",self.index)
          # print("size:\n",self.get_Size())
           print("Unit Testing 3.5: Gallary: next card should show\n")
           if(self.index == self.get_Size()-1):
               print("disabled")
               button.configure(state = "disabled") 


           self.displayCard(play_f,self.index)
           
    #takes us back to gallary by removing the frame that's displaying hte flashcards and resets index back to 0       
    def removepframes(self,play_f):

        print("Unit Testing 3.n: Gallary: flashcard should be closed \n")
        self.index = 0
        play_f.destroy()
        return
    
    '''
    def removeCard(self,root):

        print("index1:%d", self.index)
        if(self.get_Size() == 0):
            print("this bad")
        self.flashset.remove(self.flashset[self.index])
        
        if(self.index == 0 and self.get_Size() == 0):
            self.removepframes()
         
        if(self.index == 0 and self.get_Size() > 0):
         self.index= self.index + 1 
        else:
           self.index= self.index - 1 


        if(self.get_Size()> 0):
         self.play(root)

        print(self.index)
        return 
    '''   
     
       
   #page that holds each flashcard- called once - DO NOT TOUCH THIS UNLESS UR SHADAI
    def play_Page(self,galf):
         print("Unit Testing 3.2: Gallary: Flashcard should display \n")
         play_f = customtkinter.CTkFrame(galf, fg_color="#279400" ,width =1200 ,height = 700) 
         play_f.place(x= 50, y= 50)
       
         done_button = customtkinter.CTkButton(play_f, text = "✓" , text_color ="#000000", fg_color= "#FFFFFF", hover_color = "#CFCFCF" ,corner_radius = 200, width = 25, height = 30, font = ("Helvetica",18), anchor="center", command = lambda:self.removepframes(play_f))
         done_button.place(x=1100, y= 650)

         if (self.get_Size()>1):
             next_card = customtkinter.CTkButton(play_f, text =  "next", width = 25,height = 30, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda:self.updateCount(play_f,next_card))
             next_card.place(x = 1000, y = 650)
       

         self.displayCard(play_f,self.index)
         
   
    #finishes making a visual set and associates each play button with it's own se - DO NOT TOUCH UMLESS UR SHADAI
    def displaySet(self,set_frame,galf):
         set_label = customtkinter.CTkLabel(set_frame, text = self.get_Name(),font=customtkinter.CTkFont(size=16, weight="bold"))
         set_label.place(x = 50, y = 30, anchor = "center")
         play_b = customtkinter.CTkButton(set_frame, text = "▶️",width = 5,height = 5, border_width=0, hover_color= "#279400", fg_color= "transparent", font=customtkinter.CTkFont(size=10), command = lambda: self.play_Page(galf))
         play_b.place(x = 15, y = 85, anchor = "center")
         return

    #creates a flashcard  and inserts it into set after + is hit
    def create_a_Card(self,front,back):
        print("Unit Testing 2.3: Creates a card\n")
        new = flashcard()
        new.setFront(front)
        new.setBack(back)
        self.insertCard(new)
    
    #inserts card into set
    def insertCard(self,card):
        print("Unit Testing 2.4: Inserts a card into a set\n")
        self.flashset.append(card)
        print("Unit Testing 2.5: Calls the creating set page.n")
        self.creating_set_page()


    #adds a flashcard set to the gallary object
    def addtoGal(self):
        #creats a name for set otherwise no name
        self.gall.loadSets()
        dialog = customtkinter.CTkInputDialog(text="What would you like to name your set?", title= "New FlashCard Set")
        self.set_Name(dialog.get_input())
        #adds set to gallary object.
        self.gall.add_Set(self)
        SaveAndLoad.save_data(self.gall.returnGal(), self.gall.return_saveN());
        #destroys the create frame
        self.flash_frame.destroy()
        self.printAll()
        

    #UI for creating set 
    def creating_set_page(self):
         print("Unit Testing 2.2: Flashcard Page should show\n")
     
        #frontinput, 
         front_card_input= customtkinter.CTkEntry(self.flash_frame, width= 500,height=50, font = ("Helvetica", 20), placeholder_text = "Enter Term", placeholder_text_color= "#000000")
         front_card_input.place(x = 25,y=15) 
         #backinput 
         back_input = customtkinter.CTkTextbox(self.flash_frame,width=500,height= 250, font = ("Helvetica", 18))
         back_input.place(x= 25, y=85) 
         back_input.insert(END,"Enter Definition")
 
         #creates another card, inserts previous card, doesn't insert a card till the "+" button is hit.
         next_button = customtkinter.CTkButton(self.flash_frame, text= "+", text_color ="#000000", fg_color= "#FFFFFF",hover_color = "#CFCFCF" , corner_radius = 200, width = 30, height = 30, font = ("Helvetica",18), anchor="center", command = lambda:self.create_a_Card(front_card_input.get(), back_input.get("1.0",END)))
         next_button.place(x=435, y= 338)

         #creates a set
         done_button = customtkinter.CTkButton(self.flash_frame, text = "✓" , text_color ="#000000", fg_color= "#FFFFFF", hover_color = "#CFCFCF" ,corner_radius = 200, width = 25, height = 30, font = ("Helvetica",18), anchor="center", command = lambda: self.addtoGal())
         done_button.place(x=480, y= 338)




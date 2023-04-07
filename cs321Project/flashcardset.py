
from flashcard import * 
import tkinter 
from tkinter import * 
import customtkinter
from PIL import Image 




class flashcardset:

    global flashset 
    global flash_name  
    global play_button 
    global index
    global delete_pframes 
    
    

    def __init__(self):
        self.flashset = []
        self. flash_name = ""
        self.play_button = customtkinter.CTkImage(light_image=Image.open("widgets\start-green-play-icon-1.png"))
        self.index = 0
        self.delete_pframes = []
                

    def get_Size(self):
        return len(self.flashset)
    def get_Play(self):
        return self.play_button
    def get_Image(self): 
        return self.set_image
    def get_Name(self):
        return self.flash_name
    def set_Name(self, name):
        self.flash_name = name
    def create_a_Card(self,front,back):
        new = flashcard()
        new.setFront(front)
        new.setBack(back)
        return new


       #inserts card into set
    def insertCard(self,card):
        self.flashset.append(card)
    def printAll(self):
        print("---FlashCard Set---\n")
        print(self.get_Name())
        for x in self.flashset :
           x.printFront()
           x.printBack()

        print("---FlashCard End---\n")

    def displayCard(self,root,index):
        cardIndex = index
        print("Unit Testing 4.0: display current card\n")
        self.flashset[cardIndex].printFront()
        self.flashset[cardIndex].printBack()
        print("\n------------")
        self.flashset[cardIndex].displayCard(root)


     #helps move to the next card
    def updateCount(self,root):
           self.index = self.index + 1
           self.play(root)
    #takes us back to gallary and sets index back to 0 so when the user tries to play set, it's back at 0.      
    def removepframes(self):
        for x in self.delete_pframes:
            x.destroy()
            self.index = 0
        print("check4.2\n")
        return
    
    def removeCard(self,root):

        print("index1:%d", self.index)

        self.flashset.remove(self.flashset[self.index])
        
        if(self.index == 0 and self.get_Size() == 0):
            self.removepframes()
         
        if(self.index == 0 and self.get_Size() > 0):
         self.index= self.index + 1 
        else:
           self.index= self.index - 1 


        if(self.get_Size()> 0):
         self.play(root)
        
        return 
       
     
       
   
        
   

        

     #plays/modifies a flashcard set
    def play(self,root):

        
       if(self.get_Size()>0):
           play_frame = customtkinter.CTkFrame(root, fg_color="#279400" ,width =1200 ,height = 700) 
           play_frame.place(x= 50, y= 50)

           #adds frame to set for later 
           self.delete_pframes.append(play_frame)


           #next card
           if(self.index < self.get_Size()-1):
               next_card = customtkinter.CTkButton(play_frame, text =  "next", width = 25,height = 30, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center",  command = lambda:self.updateCount(root))
               next_card.place(x = 1000, y = 650)
        
           #done reviewing 
           done_button = customtkinter.CTkButton(play_frame, text = "✓" , text_color ="#000000", fg_color= "#FFFFFF", hover_color = "#CFCFCF" ,corner_radius = 200, width = 25, height = 30, font = ("Helvetica",18), anchor="center", command = lambda:self.removepframes())
           done_button.place(x=1100, y= 650)

           my_image = customtkinter.CTkImage(light_image=Image.open(r'C:\Users\shana\Documents\SemesterProject321\testing321\widgets\trash-icon-png-9.png', 'r'))

           remove_card = customtkinter.CTkButton(play_frame, text = "🚮",fg_color= "transparent",border_width=0, width = 25, height = 30, command = lambda:self.removeCard(root))
           remove_card.place(x = 1180, y = 16 ,anchor="center")

           #edit button 

       
           self.displayCard(play_frame,self.index)
       
       

     


    def displaySet(self,gallary_frame,root):
  
         set_label = customtkinter.CTkLabel(gallary_frame, text = self.get_Name(),font=customtkinter.CTkFont(size=16, weight="bold"))
         set_label.place(x = 50, y = 30, anchor = "center")
         play_b = customtkinter.CTkButton(gallary_frame, text = "", image = self.get_Play(),width = 5,height = 5, border_width=0, fg_color= "transparent",  command = lambda:self.play(root))
         play_b.place(x = 15, y = 85, anchor = "center")
         return
         
         





       

    
  
   
   


    








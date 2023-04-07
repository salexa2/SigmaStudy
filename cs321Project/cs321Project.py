import tkinter 
from tkinter import * 
import customtkinter
from tkinter import filedialog
from flashcardset import * 
from gallary import *
from SaveAndLoad import *


"""
BASIC TOD0:
-cancel cards mid creation/click on other tabs (if user hits an x, and there's atleast 1 card in the set, it will ask the user if they're sure they want to cancel, and will close the flashpage)
-remove a card from set
-edit a card from a set
-make a list/gallary of sets and display in gallery
-save the card sets - library holds the list of flshcard sets(chase)
-make it so when a user clicks on a tab, it has the previos data from before the user changed the page(maybe make a boolean of sorts that says the page is active)
-make a button to display the cards (flashcard gallery)
-make the GUI for the cards (maybe have some basic colors(red/white,blue/white.etc))
-transciption to text
-other



Basic Summary: This program outputs a transcript from video and allows users to create flashcards (Will implement extra features later)
"""

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

 # configure window
root = customtkinter.CTk() 
root.title("Sigma Study")
root.geometry(f"{1100}x{580}")

# configure grid layout (4x4)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)


#---------------------variables-------------------
library = []
saveName = "data.json"

#-------------------functions-----------------------
def change_appearance_mode_event( new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)
       
def file_open():
    #gets the video
    root.filename = filedialog.askopenfilename(title="Select Video", filetypes=(("avi files","*.avi"),("mp4 files","*.mp4"), ("txt files", "*.txt")))
    if (len(root.filename) == 0): 
        return None
        
    #convert the video to a text file named txtfile


    #Code here  
    
    return root.filename

#opens a text file and displays it in text field.
def openf(default_text):
   
    text_File = file_open()
    if(text_File != None):
         text_temp = open(text_File, 'r')
         text = text_temp.read()
         default_text.insert(END,text)
         text_temp.close()

#adds the card to the set.
def addCard(upload_frame,flashset,front,back):
    card = flashset.create_a_Card(front,back)
    flashset.insertCard(card)
    flashcard_page(upload_frame,flashset)

#creates an empty set 
def create_a_set(upload_frame):
    flashset = flashcardset()
    flashcard_page(upload_frame,flashset)
    print("Unit Testing 2.0: Closed Flashcard_page")

def addSet(flashset):
    global library
    loadSets()
    dialog = customtkinter.CTkInputDialog(text="What would you like to name your set?", title= "New FlashCard Set")
    flashset.set_Name(dialog.get_input())
    library.append(flashset)
    SaveAndLoad.save_data(library, saveName);
    upload_page()
   
    #prints out the flash card sets to terminal 
    print("__________________\n")
    for x in library:
        print(x.printAll())
    print("__________________\n")
    

#loads flashcard sets (called on program launch)
def loadSets():
    loader = SaveAndLoad.load_data(saveName);
    if loader is None:
        print("no saved data found")
        return
    global library
    library = loader.copy();
 
#-------------------pages---------------

#opens a flashcard creator.
def flashcard_page(upload_frame,flashset):
 flash_frame = customtkinter.CTkFrame(upload_frame, width = 550, height = 375, fg_color= "#279400")
 flash_frame.place(x =700,y=100)
#frontinput, 
 front_card_input= customtkinter.CTkEntry(flash_frame, width= 500,height=50, font = ("Helvetica", 20), placeholder_text = "Enter Term", placeholder_text_color= "#000000")
 front_card_input.place(x = 25,y=15) 
 #backinput 
 back_input = customtkinter.CTkTextbox(flash_frame,width=500,height= 250, font = ("Helvetica", 18))
 back_input.place(x= 25, y=85) 
 back_input.insert(END,"Enter Definition")
 
 #creates another card, inserts previous card, doesn't insert a card till the "+" button is hit.
 next_button = customtkinter.CTkButton(flash_frame, text= "+", text_color ="#000000", fg_color= "#FFFFFF",hover_color = "#CFCFCF" , corner_radius = 200, width = 30, height = 30, font = ("Helvetica",18), anchor="center", command = lambda: addCard(upload_frame,flashset,front_card_input.get(),back_input.get("0.0","end")))
 next_button.place(x=435, y= 338)

 #creates a set
 done_button = customtkinter.CTkButton(flash_frame, text = "✓" , text_color ="#000000", fg_color= "#FFFFFF", hover_color = "#CFCFCF" ,corner_radius = 200, width = 25, height = 30, font = ("Helvetica",18), anchor="center", command = lambda:addSet(flashset))
 done_button.place(x=480, y= 338)



def upload_page():
   
   upload_frame = customtkinter.CTkFrame(root, width = 1350, height = 800)
   upload_frame.grid(row=0,column = 2, sticky="w")
   #delete later 
   upload_label = customtkinter.CTkLabel(upload_frame, text="This is the Upload Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
   upload_label.place(x=600,y=0)
   #holds default text box
   default_text = customtkinter.CTkTextbox(upload_frame,width=600,height= 650, font = ("Helvetica", 16))
   default_text.place(x= 50, y=100)

   upload_file_button = customtkinter.CTkButton(upload_frame, text= "File Upload", fg_color= "#279400", hover_color="#1C6B00", command = lambda:openf(default_text))
   upload_file_button.place(x=100, y=50)

   create_set_button = customtkinter.CTkButton(upload_frame, text= "Create Set", fg_color= "#279400", hover_color="#1C6B00", command = lambda:create_a_set(upload_frame))
   create_set_button.place(x=250, y=50)

   print("Unit Testing 1.0: Upload page: upload page should show\n")


def gallary_page():
   loadSets()
   gallary_frame = customtkinter.CTkFrame(root, width = 1350, height = 800) 
   gallary_frame.grid(row=0,column = 2, sticky="w")
   upload_label = customtkinter.CTkLabel(gallary_frame, text="This is the Gallary", font=customtkinter.CTkFont(size=20, weight="bold"))
   upload_label.place(x=600,y=0)
   gal = gallary(gallary_frame,library)

   gal.print_size()
   if(len(library)>0):
        gal.display()
   


   print("Unit Testing 4.0: Gallary page: gallary page should show\n")


# create sidebar frame with widgets
sidebar_frame = customtkinter.CTkFrame(root, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
sidebar_frame.grid_rowconfigure(4, weight=1)


#Menu Label 
logo_label = customtkinter.CTkLabel(sidebar_frame, text="MENU", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

sidebar_button_1 = customtkinter.CTkButton(sidebar_frame, text= "Upload", fg_color= "#279400", hover_color="#1C6B00", command= upload_page)
sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

sidebar_button_2 = customtkinter.CTkButton(sidebar_frame, text= "Flashcard Gallary",fg_color= "#279400",hover_color="#1C6B00", command=gallary_page)
sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

sidebar_button_3 = customtkinter.CTkButton(sidebar_frame, text= "Extra features...",fg_color= "#279400",hover_color="#1C6B00")
sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

#Appearance mode change 
appearance_mode_label = customtkinter.CTkLabel(sidebar_frame, text="Appearance Mode:",  anchor="w")
appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
appearance_mode_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame,fg_color= "#279400", button_color= "#279400",button_hover_color= "#1C6B00", values=["Light", "Dark", "Default"],command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

root.mainloop()
      



import tkinter 
from tkinter import * 
import customtkinter
from tkinter import filedialog
import gallary 
from gallary import *




"""
BASIC TOD0: UPDATED (4/9/2023)
-transciption implementation 
- Extra features ideas:
    calander 
    timer
    Learning  - quiz, crossword, matching..? show  4 definitions on the left if even number even 3 defin if off, empty entry bars above them , three terms on write, type in the terms, if the terms match the front input then  the user gets points
    language accessibility ??
    text to speech on each card
    blind mode - hot key gallary = 1, to create a set = 2, hot key for front card input = w hot key for back input = s, hot key for done button,  display a set = 3, hot key to read the front card outloud a, hot key to click the card and read the input
    study plan maker - asks questions, spits out a study plan 
    Study tips - methods
    About 
 




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

saveName = "data.json"
gally = gallary(root)


#-------------------functions-----------------------
def change_appearance_mode_event( new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)
 

def file_open():
    #gets the video
    root.filename = filedialog.askopenfilename(title="Select Video", filetypes=(("avi files","*.avi"),("mp4 files","*.mp4"), ("txt files", "*.txt")))
    if (len(root.filename) == 0): 
        return None
        
    #convert the video files to a text file named txtfile


    #Code here  
    
    return root.filename


       
'''
-------------------------------------------------------FARAZZ IMPLEMENT HERE--------------------------------
Use custom tkinter to create an entry box widget to take in your youtbe link , put s button next to it thst wheen clicked, command = getLink()
in the getLink, implement your code to get the transcript from the link. linkbar is a param = string/value of the entrybox, it is essentially the string of the link so do with it what you will
'''
#opens a text file and displays it in text field.
def openf(default_text):
   
    text_File = file_open()
    if(text_File != None):
         text_temp = open(text_File, 'r')
         text = text_temp.read()
         default_text.insert(END,text)
         text_temp.close()

#takes in a link to a video, gets a transcript from it, converts it to text - FARAZZ
def getLink(linkbar, default_text):

    print(linkbar)



    #linkbar code to text..<inset cide>..... output a text_f - replace none
    #to import and use whatever class do import class name and from classname import * , contact Dai or Chase for assistance
    ''''
    Uncomment once you get the textt file of the transcript

    text_f = None
    
    
    #pastes the transcript in text box 
    if(text_f != None):
         text_temp = open(text_f, 'r')
         text = text_temp.read()
         default_text.insert(END,text)
         text_temp.close()
    '''





#-------------------pages---------------


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

   #LINK ENTRY - FARAAZ
   link_entry = customtkinter.CTkEntry(master=upload_frame, placeholder_text="CTkEntry")
   link_entry.place(x = 250, y =50)

   link_button = customtkinter.CTkButton(upload_frame, text= "Enter", fg_color= "#279400", hover_color="#1C6B00", width = 50, height = 28, command = lambda:getLink(link_entry.get(),default_text))
   link_button.place(x= 390, y=50)
   #----------------------

   print("Unit Testing 2.0: Gallary should create a set\n")
   create_set_button = customtkinter.CTkButton(upload_frame, text= "Create Set", fg_color= "#279400", hover_color="#1C6B00", command = lambda: gally.create_Set(upload_frame))
   create_set_button.place(x=450, y=50)


   #CREATE ENTRY BUTTON FOR FARAZZ



   print("Unit Testing 1.0: Upload page: upload page should show\n")


def gallary_page():
   gally.loadSets()

   gallary_frame = customtkinter.CTkFrame(root, width = 1350, height = 800) 
   gallary_frame.grid(row=0,column = 2, sticky="w")
   upload_label = customtkinter.CTkLabel(gallary_frame, text="This is the Gallary", font=customtkinter.CTkFont(size=20, weight="bold"))
   upload_label.place(x=600,y=0)

   gally.set_galFrame(gallary_frame)
 
   create_set_button = customtkinter.CTkButton(gallary_frame, text= "Create Set", fg_color= "#279400", hover_color="#1C6B00", command = lambda: gally.create_Set(gallary_frame))
   create_set_button.place(x=1200, y=10)
   

   print("Unit Testing 3.0: Gallary page: gallary page should show\n")
   gally.print_size()
   gally.print_Gal()
   
   if(gally.getSize()>0):
       gally.display(gallary_frame)




   


   


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
      



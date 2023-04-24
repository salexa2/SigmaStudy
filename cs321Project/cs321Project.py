import tkinter 
from tkinter import * 
from minimalistic import extract_video_id, get_transcript, save_transcript_to_file
import customtkinter
from tkinter import filedialog
import gallary 
from gallary import *
import month
from month import * 
import datetime
import WeeklyRoutinePlanner
from WeeklyRoutinePlanner import  *
import Year
from Year import *
import atexit


#study app that aids students in studying

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


 # configure window
root = customtkinter.CTk() 
root.title("Sigma Study")
root.geometry(f"{1350}x{700}")


# configure grid layout (4x4)
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=3)
                


#---------------------variables-------------------

saveName = "data.json"
current_time = datetime.datetime.now()


#----------------Object-------------------
gally = gallary(root)
year = Year(current_time.month)
#curr_month = month(current_time.month)
planner = WeeklyRoutinePlanner()



def exit_handler():
    year.saveCall()
    gally.saveSets()
    planner.savePlanner()

#On exit Function caller
atexit.register(exit_handler)

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
    video_id = extract_video_id(linkbar)
    if video_id:
        transcript = get_transcript(video_id)
        if transcript:
            save_transcript_to_file(transcript, "transcript.txt")
            default_text.delete('1.0', END)
            default_text.insert(END, transcript)
        else:
            print("Could not get the transcript")
    else:
        print("Invalid YouTube URL")



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

    


def optionmenu_callback(choice):
    customtkinter.deactivate_automatic_dpi_awareness()
    customtkinter.set_widget_scaling(float(choice))  



#-------------------pages---------------


def upload_page():
   
   upload_frame = customtkinter.CTkFrame(root, width = 1150, height =700)
   upload_frame.grid(column = 1,row =0, columnspan = 2, rowspan = 2 ,sticky = "NSEW",padx=5)
   #upload_frame.rowconfigure(0, weight = 1)
   ##upload_frame.rowconfigure(1, weight = 3)
   #upload_frame.columnconfigure(0, weight = 2)
   #upload_frame.columnconfigure(1, weight = 2)
   #delete later 
   #upload_label = customtkinter.CTkLabel(upload_frame, text="This is the Upload Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
   #upload_label.place(x=600,y=0)
   #holds default text box
   default_text = customtkinter.CTkTextbox(upload_frame,width=600,height= 650, font = ("Helvetica", 16))
   default_text.place(x= 50, y=100)

   upload_file_button = customtkinter.CTkButton(upload_frame, text= "File Upload", fg_color= "#279400", hover_color="#1C6B00", command = lambda:openf(default_text))
   upload_file_button.place(x=100, y=50)

   #LINK ENTRY - FARAAZ
   link_entry = customtkinter.CTkEntry(master=upload_frame, placeholder_text="Youtube Link")
   link_entry.place(x = 250, y =50)

   link_button = customtkinter.CTkButton(upload_frame, text= "Enter", fg_color= "#279400", hover_color="#1C6B00", width = 50, height = 28, command = lambda:getLink(link_entry.get(),default_text))
   link_button.place(x= 390, y=50)
   #----------------------

   print("Unit Testing 2.0: Gallary should create a set\n")
   create_set_button = customtkinter.CTkButton(upload_frame, text= "Create Set", fg_color= "#279400", hover_color="#1C6B00", command = lambda: gally.create_Set(upload_frame, create_set_button))
   create_set_button.place(x=450, y=50)


   #CREATE ENTRY BUTTON FOR FARAZZ



   print("Unit Testing 1.0: Upload page: upload page should show\n")


def gallary_page():
   gally.loadSets()

   gallary_frame = customtkinter.CTkFrame(root, width = 1150, height = 700) 
   gallary_frame.grid(column = 1,row =0 ,sticky = "NSEW",padx=5)
   #upload_label = customtkinter.CTkLabel(gallary_frame, text="This is the Gallary", font=customtkinter.CTkFont(size=20, weight="bold"))
   #upload_label.place(x=600,y=0)

   gally.set_galFrame(gallary_frame)

                             

   print("Unit Testing 3.0: Gallary page: gallary page should show\n")
   gally.print_size()
   gally.print_Gal()


  
   if(gally.getSize()>0):
       gally.display(gallary_frame)
   gally.createButtons(gallary_frame)


def calander_page():
     calander_frame = customtkinter.CTkFrame(root, width = 1150, height = 700) 
     calander_frame.grid(column = 1,row =0 ,sticky = "NSEW",padx=5)
    # calander_label = customtkinter.CTkLabel(calander_frame, text="This is the Calander", font=customtkinter.CTkFont(size=20, weight="bold"))
    # calander_label.place(x=600,y=0)

     
     side_label = customtkinter.CTkLabel( calander_frame, text="Events", font=customtkinter.CTkFont(size=20, weight="bold"))
     side_label.place(x=1150,y=70)
     side_taskframe = customtkinter.CTkFrame(calander_frame, width = 250, height = 650) 
     side_taskframe.place(x = 1060, y = 100)

     #
     #if(curr_month.numbDays() == 0):
     #curr_month.checkMonth(side_taskframe)
     #defaut
     #default_weekday =  curr_month.weekDay(current_time.year,current_time.month,1)
     #print("the first of the default month lies on a ", default_weekday)
     #curr_month.checkMonth()
     year.setMonthFrame(calander_frame)
     year.showMonth(side_taskframe)


     optionmenu_var = customtkinter.StringVar(value=year.getCurrMonth())
     #display month 
     monthmenu = customtkinter.CTkOptionMenu(calander_frame, fg_color = "#279400",  button_color = "#279400", dropdown_hover_color = "#1C6B00" , width = 40,
     height = 25,values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
     font=customtkinter.CTkFont(size=20), command = lambda choice: year.setMonth(choice,side_taskframe), variable = optionmenu_var)
     monthmenu.place(x = 500, y = 50)



def helperP(planner,form_frame):
    if(planner.checkV()==False):
        if(planner.getValues()==False):
         planner.formPage(form_frame)


def helperP2(planner,form_frame,next_button):
    if(planner.checkV()==False):
        if(planner.getValues()==False):
            if(planner.getValuesH() == False):
              print("hobby show")
              planner.hobbyPage(form_frame,next_button)
           
           


def RequiredForm(plan_frame,planner,gen):
    #values reset 
     #ran.configure(state ="disabled")
     planner.reset()
     print("form should show")
     gen.configure(state = "disabled")
     temp_frame = customtkinter.CTkFrame(plan_frame, width = 1150, height =750) 
     temp_frame.pack()

     next_button = customtkinter.CTkButton(temp_frame, text = "add Task", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: helperP(planner,form_frame))
     next_button.pack(anchor= "n", pady = 15)
     hobby_button = customtkinter.CTkButton(temp_frame, text = "Add Hobbies", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda:helperP2(planner,form_frame,next_button))
     hobby_button.pack(anchor= "n", pady = 15)
     done_button = customtkinter.CTkButton(temp_frame, text = "Done", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: planner.printPlan(temp_frame, gen))
     done_button.pack(anchor = "n", pady = 15)
     
     form_frame = customtkinter.CTkScrollableFrame(temp_frame, width = 1150, height = 700) 
     form_frame.pack(side=TOP)

   
     
     planner.formPage(form_frame)
   





def plan_page():
     plan_frame = customtkinter.CTkScrollableFrame(root, width = 1150, height =750) 
     plan_frame.grid(column = 1,row =0 ,sticky = "NSEW",padx=5)
     
     planner.planner_getFrame(plan_frame)
     planner.displayPlan()
     #random_button = customtkinter.CTkButton(plan_frame, text = "RandomGenerate", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", state= "disabled",corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: planner.randomGen())
     #random_button.pack(pady = 10)

     gen_button = customtkinter.CTkButton(plan_frame, text = "Generate", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: RequiredForm(plan_frame,planner, gen_button))
     gen_button.pack(pady = 19)
     planner.show_All()
     
def settings_page():
    settings_frame = customtkinter.CTkFrame(root, width = 1150, height = 750) 
    settings_frame.grid(column = 1,row =0 ,sticky = "NSEW",padx=5)
    settings_label = customtkinter.CTkLabel(settings_frame, text="Settings", font=customtkinter.CTkFont(size=20, weight="bold"))
    settings_label.place(x=60,y=30)
    scale_label = customtkinter.CTkLabel(settings_frame, text="Changes the scaling to fit screen size:")
    scale_label.place(x=40,y=80)
    scaling = customtkinter.CTkOptionMenu(settings_frame, fg_color = "#279400",  button_color = "#279400", dropdown_hover_color = "#1C6B00" , width = 140, height = 25,values=[".2", ".4",".5", ".6", ".8","1", "1.2","1.3","1.4",  "1.5" , "1.6" , "1.8", "1.9", "2"], command =  optionmenu_callback)
    scaling.place(x= 40,y=125)
       

          
    


   


   


# create sidebar frame with widgets
sidebar_frame = customtkinter.CTkFrame(root, width=200, height = 800)
sidebar_frame.grid(column =0, row=0, sticky = "W")
#sidebar_frame.grid_rowconfigure(5, weight=1)


#Menu Label 
logo_label = customtkinter.CTkLabel(sidebar_frame, text="MENU", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.place(x = 60, y =10)

sidebar_button_1 = customtkinter.CTkButton(sidebar_frame, text= "Upload", fg_color= "#279400", hover_color="#1C6B00", command= upload_page)
sidebar_button_1.place(x = 20, y = 50)

sidebar_button_2 = customtkinter.CTkButton(sidebar_frame, text= "Flashcard Gallary",fg_color= "#279400",hover_color="#1C6B00", command=gallary_page)
sidebar_button_2.place(x = 20, y = 100)

sidebar_button_3 = customtkinter.CTkButton(sidebar_frame, text= "Calander",fg_color= "#279400",hover_color="#1C6B00",command= calander_page)
sidebar_button_3.place(x = 20, y = 150)

sidebar_button_4 = customtkinter.CTkButton(sidebar_frame, text= "Study Plan",fg_color= "#279400",hover_color="#1C6B00", command = plan_page)
sidebar_button_4.place(x = 20, y = 200)

sidebar_button_5 = customtkinter.CTkButton(sidebar_frame, text= "Settings",fg_color= "#279400",hover_color="#1C6B00", command = settings_page)
sidebar_button_5.place(x = 20, y = 250)

#Appearance mode change 
appearance_mode_label = customtkinter.CTkLabel(sidebar_frame, text="Appearance Mode:",  anchor="w")
appearance_mode_label.place(x = 20, y = 700)
appearance_mode_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame,fg_color= "#279400", button_color= "#279400",button_hover_color= "#1C6B00", values=["Light", "Dark", "Default"],command=change_appearance_mode_event)
appearance_mode_optionemenu.place(x = 20, y = 750)






root.mainloop()
      



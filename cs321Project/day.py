import tkinter 
from tkinter import * 
import customtkinter
class day():

    day_name = 1
    event_name = ""
    event_description =  ""
   

    #list of events/tasks "event nam"
    #list od descriptions
    #remove event
    #add an event
    #edit an event
    def set_name(self,name):
        self.day_name = name
    def day_frame(self, month_frame,posx,posy):
       day_frame = customtkinter.CTkButton(month_frame, text_color = "#FFFFFF", text = self.day_name,font=customtkinter.CTkFont(size=25, weight="bold"), hover_color="#DBDBDB", fg_color="transparent",width = 50,height = 50, ) 
       day_frame.place(x = posx, y= posy)

   
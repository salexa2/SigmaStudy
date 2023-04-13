import datetime
import tkinter 
from tkinter import * 
import customtkinter
import day
from day import *

class month():
     #list of days- we wanna save this so when a month is displayed the eveents for that day are saved
    daysInMonth = []
    week   = ['Sunday', 
                  'Monday', 
                  'Tuesday', 
                  'Wednesday', 
                  'Thursday',  
                  'Friday', 
                  'Saturday']
    week_xpos = []
    monthframe = None
    currentMonth = None
    dayStart = 'Sunday'
    current_time = datetime.datetime.now()


    
    #constructor
    def __init__(self, month):
       self.currentMonth = month
    def setMonthFrame(self,frame):
        self.monthframe = frame

    def weekDay(self,year, month, day):
        offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        afterFeb = 1
        if month > 2: afterFeb = 0
        aux = year - 1700 - afterFeb
        # dayOfWeek for 1700/1/1 = 5, Friday
        dayOfWeek  = 5
        # partial sum of days betweem current date and 1700/1/1
        dayOfWeek += (aux + afterFeb) * 365                  
        # leap year correction    
        dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
        # sum monthly and day offsets
        dayOfWeek += offset[month - 1] + (day - 1)               
        dayOfWeek %= 7
        self.dayStart = self.week[int(dayOfWeek)]
        return self.week[int(dayOfWeek)]

    def place_days(self,frame):
         posx = 50
         posy = 20
         
         for i in self.week:
            self.week_xpos.append(posx)
            print("tempx\n", posx)
            day_label = customtkinter.CTkLabel(frame, text=i[:1], text_color = "#FFFFFF", font=customtkinter.CTkFont(size=25,  weight="bold"))
            day_label.place(x = posx, y =posy)
            posx = posx + 145

    def place_dayFrames(self,frame,tempx,tempy,num):
         counter = 1

          
         while(counter <num):
             n_day = day()
             n_day.set_name(counter)
             n_day.day_frame(frame,tempx,tempy)
             self.daysInMonth.append(n_day)

             tempx= tempx+145
             
             if(tempx >= 920):
               print("limit met\n", tempx)
               tempx = self.week_xpos[0]-20
               tempy = tempy+ 90
              
             counter = counter + 1

    #checks the month and displays the page/calande
    def checkMonth(self):
        self.weekDay(self.current_time.year, self.currentMonth, 1)
       
       
        if(self.currentMonth  == 1):
            #display that months page
            print("january") 
            num = 32
   
            jan_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            jan_frame.place(x = 50, y = 100)

            self.place_days(jan_frame)
           

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(jan_frame,tempx,tempy,num)
                

           
        elif(self.currentMonth  == 2):
            print("february\n")
            num = 29
            feb_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            feb_frame.place(x = 50, y = 100)

            
            self.place_days(feb_frame)
            

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(feb_frame,tempx,tempy, num)
                
        elif(self.currentMonth  == 3):
            print("march\n")
            num = 32
            mar_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            mar_frame.place(x = 50, y = 100)

            
            self.place_days(mar_frame)
            

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(mar_frame,tempx,tempy, num)

        elif(self.currentMonth  == 4):
            print("april\n")
            num = 31
            april_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            april_frame.place(x = 50, y = 100)

            
            self.place_days(april_frame)
            

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(april_frame,tempx,tempy, num)
                
        elif(self.currentMonth  == 5):
            print("may\n")
            num = 32
            may_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            may_frame.place(x = 50, y = 100)

            
            self.place_days(may_frame)
            

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(may_frame,tempx,tempy, num)

        elif(self.currentMonth  == 6):
            print("june\n")
            num = 31
            june_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            june_frame.place(x = 50, y = 100)

            
            self.place_days(june_frame)
            

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(june_frame,tempx,tempy, num)
        elif(self.currentMonth  == 7):
            print("july\n")    
            num = 32
            july_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            july_frame.place(x = 50, y = 100)

            
            self.place_days(july_frame)
            

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(july_frame,tempx,tempy, num)
        elif(self.currentMonth  == 8):
            print("august\n")    
            num = 32
            aug_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            aug_frame.place(x = 50, y = 100)

            
            self.place_days(aug_frame)
            

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(aug_frame,tempx,tempy, num)
        elif(self.currentMonth  == 9):
            print("september\n")  
            num = 31
            sep_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            sep_frame.place(x = 50, y = 100)

            
            self.place_days(sep_frame)
            

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(sep_frame,tempx,tempy, num)
        elif(self.currentMonth  == 10):
            print("october\n") 
            num = 32
            octo_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            octo_frame.place(x = 50, y = 100)

            
            self.place_days(octo_frame)
            

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(octo_frame,tempx,tempy, num)
        elif(self.currentMonth  == 11):
            print("november\n")
            num = 31
            nov_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            nov_frame.place(x = 50, y = 100)

            
            self.place_days(nov_frame)
            

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(nov_frame,tempx,tempy, num)
        else:
            print("december\n")
            num = 32
            dec_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            dec_frame.place(x = 50, y = 100)
            self.place_days(dec_frame)            
            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(dec_frame,tempx,tempy, num)
    #sets the month if user uses drop down
    def setMonth(self,choice):
        if(choice == "January"):
            self.currentMonth = 1 
        elif(choice == "February"):
            self.currentMonth = 2 
        elif(choice == "March"):
            self.currentMonth = 3
        elif(choice == "April"):
            self.currentMonth = 4           
        elif(choice == "May"):               
            self.currentMonth = 5 
        elif(choice == "June"):
            self.currentMonth = 6   
        elif(choice == "July"):
             self.currentMonth = 7     
        elif(choice == "August"):
            self.currentMonth = 8
        elif(choice == "September"):
            self.currentMonth = 9     
        elif(choice == "October"):
             self.currentMonth = 10                    
        elif(choice == "November"):
             self.currentMonth = 11            
        elif(choice == "December"):
             self.currentMonth = 12      

        self.dayStart = self.weekDay(self.current_time.year, self.currentMonth, 1)
        print("the 1 of the set month starts on:", self.dayStart)

           
       
       
       
        print("The month is now:")
        self.checkMonth()












    

    










from operator import truediv
from ssl import DefaultVerifyPaths
import Weekday
from Weekday import *
import tkinter 
from tkinter import * 
import customtkinter
import random 
from datetime import *

class WeeklyRoutinePlanner():
 #planner = [Weekday(0),Weekday(1),Weekday(2),Weekday(3),Weekday(4),Weekday(5),Weekday(6)]

 savedValues = []
 task_frame = None
 taskName = ""
 taskSTime =""
 taskETime = None
 days= []
 planner = []
 Checkbutton1 = None
 Checkbutton2 = None 
 Checkbutton3 = None
 Checkbutton4 = None
 Checkbutton5 = None 
 Checkbutton6 = None
 Checkbutton7 = None
 military_time = ""
 military_time2 = ""
 tempPlanner = planner

 currentType = 0

 hobbyName = None
 times = -1
 maxx = -1
 when = -1
 pos = -1
 mainf = None
 switch = -1
 ErrorType = ['*Incomplete Task!*','!PM/AM Invalid!*', '*Invalid Time Format!-H:M AM/PM(Spaced)*', 'Conflicting Times']

 def __init__(self, p):
     self.planner = [Weekday(0,p),Weekday(1,p),Weekday(2,p),Weekday(3,p),Weekday(4,p),Weekday(5,p),Weekday(6,p)]

     self.mainf = p 
                        
 def clearA(self):
     for i in self.planner:
         i.cleartypes()
 

     
 def displayPlan(self)  :
     for i in self.planner:
         i.getweekFrame()
     return
 def randomGen(self):
     for h in self.planner:
         h.randomize()

 def printValues(self):

     for i in self.savedValues:
         print("weekday num:",i)

     print ("name", self.taskName.get())
     print ("taskSTime", self.taskSTime.get())
     print("taskETime", self.taskETime.get())

 def printPlan(self,frame,gen):
     if(self.currentType == 0):
          self.getValues()
     else:
         if(self.times>0):  # if user even entered anything 
            self.getValuesH() #saves any h values
    
     print("WEEKLY ROUTINE\n")
     for i in self.planner:

          i.showAll()
     
     frame.destroy()
     gen.configure(state = "normal")
    # ran.configure(state = "normal")
    
 def optionmenu_callbackT(self,choice):#times a day
    #print("optionmenu dropdown clicked:", choice)
    self.times = int(choice)
 def reset(self):
    self.clearA()
    
 def optionmenu_callbackM(self,choice):#max
  #  print("optionmenu dropdown clicked:", choice)
    self.maxx = int(choice)

 def optionmenu_callbackP(self,choice):#When
   # print("optionmenu dropdown clicked:", choice)

    if(choice == "Before"):
         self.pos ='0'
    elif(choice == "After"):
         self.pos ='1'
    elif(choice == "Between"):
         self.pos = '2'
 
 def optionmenu_callbackW(self,choice):#times of  day
    #print("optionmenu dropdown clicked:", choice)
    if(choice == "Morning"):
         self.when ='0'
    elif(choice == "Afternoon"):
         self.when ='1'
    elif(choice == "Evening"):
         self.when = '2'

 
 
 def hobbyPage(self,form_frame,nextbutton):
     self.currentType = 1
     nextbutton.configure(state = "disabled")
     optionmenu_var = customtkinter.StringVar(value="Times a Week")
     optionmenu_var1 = customtkinter.StringVar(value="Max Hours a Day")
     optionmenu_var2 = customtkinter.StringVar(value="Time of Day")
     optionmenu_var3 = customtkinter.StringVar(value="When Would You  Want to do your Hobbies?")
 

     task_frame = customtkinter.CTkFrame(form_frame, fg_color = "#279400", width = 1000, height = 100) 
     task_frame.pack(side = TOP)

     self.taskName = customtkinter.CTkEntry(master=task_frame, placeholder_text="TaskName")
    
     self.taskName.place(x = 10, y = 10)

     combobox1 = customtkinter.CTkOptionMenu(task_frame,  dropdown_hover_color = "#1C6B00" , width = 20, height = 20,values=['1','2','3','4','5','6','7'] ,font=customtkinter.CTkFont(size=12),command = self.optionmenu_callbackT ,variable = optionmenu_var)
     combobox1.place(x=10,y=40)

     combobox2 = customtkinter.CTkOptionMenu(task_frame,   dropdown_hover_color = "#1C6B00" , width = 30, height = 20,values=['1','2','3','4','5','6','7','8'], font=customtkinter.CTkFont(size=12), command = self.optionmenu_callbackM,variable = optionmenu_var1)
     combobox2.place(x=200,y=40)

     combobox3 = customtkinter.CTkOptionMenu(task_frame, dropdown_hover_color = "#1C6B00" , width = 30, height = 20,values=["Morning", "Afternoon", "Evening"], font=customtkinter.CTkFont(size=12), command = self.optionmenu_callbackW,variable = optionmenu_var2)
     combobox3.place(x=350,y=40)

     combobox4 = customtkinter.CTkOptionMenu(task_frame , dropdown_hover_color = "#1C6B00" , width = 30, height = 20,values=["Before", "After", "Between"], font=customtkinter.CTkFont(size=12), command = self.optionmenu_callbackP, variable = optionmenu_var3)
     combobox4.place(x= 500,y=40)
    
     divider = customtkinter.CTkLabel(master = form_frame, text="___________________________________________________________________________________________________________________________________________________________________________________________", font=customtkinter.CTkFont(size=20, weight="bold"))
     divider.pack()
   
 def formPage(self,form_frame):

     #task boxes 
     self.task_frame = customtkinter.CTkFrame(form_frame, fg_color = "#279400", width = 1000, height = 100) 
     self.task_frame.pack(side = TOP)
     self.taskName = customtkinter.CTkEntry(master=self.task_frame, placeholder_text="TaskName")
     self.taskName.place(x = 10, y = 10)

     self.taskSTime = customtkinter.CTkEntry(master=self.task_frame, placeholder_text="Task Start Time")
     self.taskSTime.place(x = 200, y = 10)
     self.taskETime = customtkinter.CTkEntry(master=self.task_frame, placeholder_text="Task End Time")
     self.taskETime.place(x = 400, y = 10)

     

     self.Checkbutton1 =  BooleanVar(form_frame)
     self.Checkbutton1.set(False)
     self.Checkbutton2 =  BooleanVar(form_frame)
     self.Checkbutton2.set(False)
     self.Checkbutton3 =  BooleanVar(form_frame)
     self.Checkbutton3.set(False)
     self.Checkbutton4 =  BooleanVar(form_frame)
     self.Checkbutton4.set(False)
     self.Checkbutton5 =  BooleanVar(form_frame)
     self.Checkbutton5.set(False)
     self.Checkbutton6 =  BooleanVar(form_frame)
     self.Checkbutton6.set(False)
     self.Checkbutton7 =  BooleanVar(form_frame)
     self.Checkbutton7.set(False)
     

  
     Button1 = customtkinter.CTkCheckBox(self.task_frame, text = "Sunday", 
                          variable = self.Checkbutton1,
                          onvalue = True,
                          offvalue = False,
                          height = 2, 
                          width = 10)
  
     Button2 = customtkinter.CTkCheckBox(self.task_frame, text = "Monday",
                          variable = self.Checkbutton2,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10)
  
     Button3 = customtkinter.CTkCheckBox(self.task_frame, text = "Tuesday",
                          variable = self.Checkbutton3,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10)
     Button4 = customtkinter.CTkCheckBox(self.task_frame, text = "Wednesday",
                          variable = self.Checkbutton4,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10)
     Button5 = customtkinter.CTkCheckBox(self.task_frame, text = "Thursday",
                          variable = self.Checkbutton5,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10)  
     Button6 = customtkinter.CTkCheckBox(self.task_frame, text = "Friday",
                          variable = self.Checkbutton6,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10)  
     Button7 = customtkinter.CTkCheckBox(self.task_frame, text = "Saturday",
                          variable = self.Checkbutton7,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10)

     Button1.place(x = 10, y = 60)
     Button2.place(x = 110, y = 60)
     Button3.place(x = 210, y = 60)
     Button4.place(x = 310, y = 60)
     Button5.place(x = 410, y = 60)
     Button6.place(x = 510, y = 60)
     Button7.place(x = 610, y = 60)

     
     
     divider = customtkinter.CTkLabel(master = form_frame, text="___________________________________________________________________________________________________________________________________________________________________________________________", font=customtkinter.CTkFont(size=20, weight="bold"))
     divider.pack()
    
 def checkV(self):
     if(self.taskName.get()==""):
           print("Incomplete Task : 100")
           error = customtkinter.CTkLabel(master = self.task_frame, text="Incomplete Task!*", text_color ="#FF0000",font=customtkinter.CTkFont(size=10, weight="bold"))
           error.place(x = 800, y= 90)
           return True
     '''
      if(self.switch == -1):
         print("Incomplete Task Error: 200")
         error = customtkinter.CTkLabel(master = self.task_frame, text="Incomplete Task!*", text_color ="#FF0000",font=customtkinter.CTkFont(size=10, weight="bold"))
         error.place(x = 800, y= 90)
         return True
      '''
     return False
      


 def addRValues(self): # 0, 1, 3
                #verification
               print("in r values\n")
               if(self.currentType == 1):
                   return False
               try:

                   if("PM" in self.taskSTime.get()):
          
                        if("AM" in self.taskETime.get()):
                            print("error Caught except am/pm")
                            error = customtkinter.CTkLabel(master = self.task_frame, text="PM-AM Invalid!*", text_color ="#FF0000",font=customtkinter.CTkFont(size=10, weight="bold"))
                            error.place(x = 800, y= 50)
                            return True
                   self.military_time = datetime.strptime(self.taskSTime.get(), '%I:%M %p').strftime('%H:%M')
                   self.military_time2 = datetime.strptime(self.taskETime.get(), '%I:%M %p').strftime('%H:%M')
                   print("were good")
               except:
                            print("error Caught except")
                            error = customtkinter.CTkLabel(master = self.task_frame, text="*Invalid/Conflicting Times!*", text_color ="#FF0000",font=customtkinter.CTkFont(size=10, weight="bold"))
                            error.place(x = 800, y= 5)
                            return True    
               else:
                    return self.verifyTwo()        
                   
                
                    
                   
                
               
 def  verifyTwo(self):
    #%I is for regular time. %H is for 24 hr time, aka "military time"
                   #%p is for AM/PM
                    sub_list = ["PM", "AM"]
                    for sub in sub_list:
                        startN = self.military_time.replace(' ' + sub + ' ', ' ')
                        endN = self.military_time2.replace(' ' + sub + ' ', ' ')
     
                    h, m = map(int, startN.split(':'))
                    h1, m2 = map(int, endN.split(':'))

                    if(h>h1):
                        return True
                    elif(h==h1):
                        if(m >m2 or m == m2):
                            return True

                    


                    print(f"militarytime is {self.military_time}")

                    for c in self.savedValues:
                       print("checked:",c)
                       check = self.planner[c].checkTimeConflict(self.taskName.get(), self.military_time,self.military_time2)
                       if(check == True):
                         error = customtkinter.CTkLabel(master = self.task_frame, text="*Invalid/Conflicting Times!*", text_color ="#FF0000",font=customtkinter.CTkFont(size=10, weight="bold"))
                         error.place(x = 800, y= 5)
                         return True
                    #self.printValues()
                    for i in self.savedValues:
                     print("i", i)
                     self.planner[i].createARequiredTask(self.taskName.get(),self.military_time,self.military_time2)
                    return False


                
 def addHValues(self,value):
     if(value == 1):
          if self.times == -1 or self.maxx == -1 or self.pos == -1:
              error = customtkinter.CTkLabel(master = self.task_frame, text="Empty Form!*", text_color ="#FF0000",font=customtkinter.CTkFont(size=10, weight="bold"))
              error.place(x = 800, y= 90)
              return True
 
     count = 0
     temp  = []
     while(count<self.times):
         var = random.randrange(7)
         while(var in temp):
             var = random.randrange(7)
         temp.append(var) # picks random days for times
         count = count + 1
     
     for b in temp:
        print("value got:",b)

     for v in temp :
        self.planner[v].createAHobby(self.taskName.get(),self.times,float(self.maxx),self.when,self.pos)
     #temp.clear()
     return False
         
    
  
 def getValues(self): 

     
     self.days.append(self.Checkbutton1)
     self.days.append(self.Checkbutton2)
     self.days.append(self.Checkbutton3)
     self.days.append(self.Checkbutton4)
     self.days.append(self.Checkbutton5)
     self.days.append(self.Checkbutton6)
     self.days.append(self.Checkbutton7)

     counter = 0
     for e in self.days:
         if(e.get() == True):
             self.switch == 1
             print("here:",counter)
             self.savedValues.append(counter)
         counter = counter + 1
     #self.printValues()
     checkingTime = self.addRValues()
     if(checkingTime == True):
         print("checking time ")
         self.days.clear()
         self.savedValues.clear()

         return True

     self.savedValues.clear()
    # self.taskName = None
     #self.taskSTime = None
    # self.taskETime = None
     self.days.clear()
     return False
 
 def getValuesH(self):
     self.combobox1 = None #times a day
     self.combobox2 = None # max hours
     self.combobox3  =None # time of day
     self.combobox4 = None  # before or after tasks
     self.addHValues(1)
     return False
     



    






import tkinter as tk
from tkinter import * 
from tkinter.messagebox import showinfo
import datetime
from datetime import datetime


dt = datetime.now() #GET CURRENT DATE, HOUR<(military), minutes, seconds, and miniseconds now

App = Tk()
App.geometry('400x400') #Creating the GUI 
App.title('Age Calculator App')
NameLabels = Label(App, text = 'Welcome to the Age Calculator!',bg='Aqua').place(x=105, y=10)
App.configure(bg='Orange')
NameLabel = Label(App,text = 'Enter your Date of Birth',bg='Aqua').place(x=70,y=50)

#String entered Label
Dayv = tk.StringVar()
Monthv = tk.StringVar()
Yearv = tk.StringVar()

#Creating the labels for the widgets for Month, Year, and month.
Day = tk.Label(text = 'Day *Enter as DD', bg='Aqua',width=18)
Day.place(x=20,y=85)
Month = tk.Label(text = 'Month *Enter as MM',bg='Aqua',width=18)
Month.place(x=20,y=115)
Year = tk.Label(text='Year *Enter as YYYY',bg='Aqua',width=18)
Year.place(x=20,y=145)

#Entry for the user to input the information
Day1 = Entry(App, textvariable=Dayv).place(x=180,y=85)
Day2= Entry(App, textvariable=Monthv).place(x=180,y=115)
Day3=Entry(App, textvariable=Yearv).place(x=180,y=145)

#Check function for if it is a leap yr
def is_leapyr(x):
    if(x%400==0 and x%100==0):
        return True
    elif(x%4==0 and x % 100 !=0):
        return True
    else:
        return False

#Dictionary for amount of days in a month:
YearM = {
    1: 31, 
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

#HELPER FUNCTIONS
def var():
    x1Str = Dayv.get() #Saves Birth-DAY as string
    x2Str = Monthv.get() # Saves Birth-Month as a string
    x3Str = Yearv.get() #Saves Birth-Year as a string
    return (x1Str + x2Str + x3Str) #return statement DD MM YYYY 

def Yrage(d, m, y):
    age = dt.year - y #Age if bday already happened in the year
    if(dt.month<m):
        age-=1
    elif(dt.month==m and dt.day<d): #checks if the day happened or not in a month
        age-=1
    return age

def daysAlive(d, m,y):
    days_A = (dt.year-y) * 365
    x1 = 0
    count=0
    sum = 0
    for xxxx in range(y, dt.year): #checks for leap year
        if(is_leapyr(xxxx)):
            count+=1
    if(dt.month==m):
            x1 = d-dt.day #get the amount of days and subtract it from days alive
            if(dt.day==d):
                print("HAPPY B-DAY")
    elif(dt.month<m): #b-day didn't happen yet this year
        x1 = YearM[dt.month]- dt.day + d 
        if(dt.month+1!=m): #Add all days between the two months and subtract them.
            for i in range(dt.month+1, m):
                x1 += YearM[i]
    elif(dt.month>m): #checks if bday happened already
        sum = dt.day
        if(is_leapyr(dt.year) and 2<dt.month): #check if february happened already if leep year
            sum+=1
        sum += YearM[m]-d
        for i in range(m+1, dt.month):
            sum += YearM[i] 
    days_A = days_A + count + sum - x1 #Formula daysAlive = (current year - birthYr) * 365 + (#LeapYrs-365) + or - totalDays
    return days_A

def hrAlive(p1):
    hr_A = ((p1 * 24) + dt.hour) #days * (hrs per day) + todays hours
    return hr_A
 
def minAlive(p2):
    min_A = ((p2*60)) + dt.minute #hours * (minutes per hour) + minutes now
    return min_A

#Pressing CALCULATE button
def calculate():
    str1 = var()
    if(str1[0]=='0'): #Remove '0' from DD ex: 02
        day = str1[1:2]
    else:
        day = str1[0:2]
    dayInt = int(day) #Gives me an int days
    if(str1[2]=='0'): #Same thing for months(remove '0')
        month = str1[3:4]
    else:
        month = str1[2:4]
    monthInt = int(month) #Gives me int months
    yearInt = int(str1[4:]) #Gives me the int year
    Age = Yrage(dayInt, monthInt, yearInt) 
    DayA = daysAlive(dayInt,monthInt, yearInt) #Days alive
    hrA = hrAlive(DayA) #hours alive
    minA = minAlive(hrA) #minutes alive
    msg = f"Years Old: {Age}\nDays Alive: {DayA:,}\nHours Alive: {hrA:,}\nMinutes Alive: {minA:,}" 
    showinfo("Age calcs:", msg)

cal_button=Button(App,
    text="Calculate",
    width=17,
    height=2,
    bg="Aqua",
    fg="Black",
    command=calculate
 ).place(x=70,y=185)


App.mainloop()
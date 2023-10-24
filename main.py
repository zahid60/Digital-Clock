from tkinter import *
import datetime

def date_time():
    time =datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime("%p")
    date=time.strftime("%d")
    month=time.strftime("%m")
    year=time.strftime("%y")
    day=time.strftime("%a")

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.after(200,date_time)

Clock = Tk()
Clock.title("Digital Clock")
Clock.geometry("1000x500")
Clock.config(bg="yellow")

#### Time Start  ####
lab_hr=Label(Clock,text="00",font=("Times New Roman",60,"bold"),bg="red",fg="white")
lab_hr.place(x=120,y=50,height=110,width=100)

lab_hr_txt=Label(Clock,text="Hour",font=("Times New Roman",20,"bold"),bg="red",fg="white")
lab_hr_txt.place(x=120,y=190,height=40,width=100)

lab_min=Label(Clock,text="00",font=("Times New Roman",60,"bold"),bg="red",fg="white")
lab_min.place(x=340,y=50,height=110,width=100)

lab_min_txt=Label(Clock,text="Min",font=("Times New Roman",20,"bold"),bg="red",fg="white")
lab_min_txt.place(x=340,y=190,height=40,width=100)

lab_sec=Label(Clock,text="00",font=("Times New Roman",60,"bold"),bg="red",fg="white")
lab_sec.place(x=560,y=50,height=110,width=100)

lab_sec_txt=Label(Clock,text="Sec",font=("Times New Roman",20,"bold"),bg="red",fg="white")
lab_sec_txt.place(x=560,y=190,height=40,width=100)

lab_am=Label(Clock,text="00",font=("Times New Roman",40,"bold"),bg="red",fg="white")
lab_am.place(x=780,y=50,height=110,width=100)

lab_am_txt=Label(Clock,text="AM/PM",font=("Times New Roman",20,"bold"),bg="red",fg="white")
lab_am_txt.place(x=780,y=190,height=40,width=100)



#####   Date  Start  #####

lab_date=Label(Clock,text="00",font=("Times New Roman",60,"bold"),bg="red",fg="white")
lab_date.place(x=120,y=270,height=110,width=100)

lab_date_txt=Label(Clock,text="Date",font=("Times New Roman",20,"bold"),bg="red",fg="white")
lab_date_txt.place(x=120,y=410,height=40,width=100)

lab_mo=Label(Clock,text="00",font=("Times New Roman",60,"bold"),bg="red",fg="white")
lab_mo.place(x=340,y=270,height=110,width=100)

lab_mo_txt=Label(Clock,text="Month",font=("Times New Roman",20,"bold"),bg="red",fg="white")
lab_mo_txt.place(x=340,y=410,height=40,width=100)

lab_year=Label(Clock,text="00",font=("Times New Roman",60,"bold"),bg="red",fg="white")
lab_year.place(x=560,y=270,height=110,width=100)

lab_year_txt=Label(Clock,text="year",font=("Times New Roman",20,"bold"),bg="red",fg="white")
lab_year_txt.place(x=560,y=410,height=40,width=100)

lab_day=Label(Clock,text="00",font=("Times New Roman",40,"bold"),bg="red",fg="white")
lab_day.place(x=780,y=270,height=110,width=100)

lab_day_txt=Label(Clock,text="Day",font=("Times New Roman",20,"bold"),bg="red",fg="white")
lab_day_txt.place(x=780,y=410,height=40,width=100)


date_time()
Clock.mainloop()
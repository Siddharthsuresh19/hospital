from tkinter import*
import mysql.connector as my
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msg
import csv
import os
mydata=[]
def homepage():
    root = Tk()
    root.title("CENTRALIZED HOSPITAL MANAGEMENT FOR PAITENTS")
    root.geometry("1600x1600")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    
    
    label2 = Label( root, text ="CENTRALIZED HOSPITAL MANAGEMENT FOR PAITENTS",fg="black",bg="#856ff8",borderwidth=5, width = 50)
    label2.pack(pady = 50)
    label2.configure(font=("Algerian",17,"bold"))  

    def tech():
        root.destroy()
        alll()
        
    b=Button (root,text="Indian Health Department Login",borderwidth=5, width = 35,command=tech)
    b.place(x=600,y=200)
    b.configure(font=("Castellar",10,"bold"))
    def logg():
       root.destroy()
       hoslog()
        
    b1=Button(root,text="Hospital Login",borderwidth=5, width = 35,command=logg)
    b1.place(x=600,y=300)
    b1.configure(font=("Castellar",10,"bold"))
    def logg1():
        root.destroy()
        humanlog()
        
    b2=Button(root,text="Human Login",borderwidth=5, width = 35,command=logg1)
    b2.place(x=600,y=400)
    b2.configure(font=("Castellar",10,"bold"))

    root.mainloop()

def call():
    homepage()
##################################################################################################

################################################################################################
def alll():
    root=Tk()
    root.geometry("1600x1600")
    root.title("Indian Health Department Login")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    m=Label(root,text="INDIAN HEALTH DEPARTMENT",fg="black",bg="blue",borderwidth=5, width = 50)
    m.place(x=400,y=50)
    m.configure(font=("Algerian",17,"bold")) 
    w=Label(root,text="User Name",borderwidth=5, width =10,font=("Castellar",10,"bold"),bg="#856ff8")
    w.place(x=500,y=200)
    z=Label(root,text="Password",borderwidth=5, width =10,bg="#856ff8",font=("Castellar",10,"bold"))
    z.place(x=500,y=300)
    t=Entry(root,borderwidth=5, width = 50,font=("Times New Roman",10,"bold"))
    t.place(x=700,y=200)
    t1=Entry(root,borderwidth=5, width = 50,show="*",font=("Times New Roman",10,"bold"))
    t1.place(x=700,y=300)

    def llen():
        con=my.connect(host="localhost",user="root",password="22MIS0162",database="hospital")
        cur=con.cursor()
        cur.execute("select * from login where username='"+t.get()+"' and password='"+t1.get()+"'")
        d=cur.fetchall()
        if d:
            for x in d:
                    msg.showinfo("Login Status","Login Successfully "+t.get())
                    root.destroy()
                    adminpage()
                    
        else:
            msg.showinfo("Login Status","Username/Password Invalid "+t.get())
    b=Button(root,text="Submit",borderwidth=5, width =10,command=llen)
    b.place(x=700,y=400)
    def back():
        root.destroy()
        call()
    b1=Button(root,text="Home",borderwidth=5, width =10,command=back)
    b1.place(x=800,y=400)
    root.mainloop()
###########################################################################################
def adminpage():
     
    root=Tk()
    root.geometry("1600x1600")
    root.title("Admin")

    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
   
    m=Label(root,text="LOGIN PAGE",fg="black",bg="blue",borderwidth=5, width = 50,font=("Algerian",17,"bold"))
    m.place(x=600,y=50)
    
    def hlogg():
        root.destroy()
        hosreg()
    b=Button(root,text="Hospital Login",borderwidth=5, width = 35,command=hlogg,font=("Castellar",10,"bold"))
    b.place(x=700,y=200)
    
    def rep():
        root.destroy()
        hreport()
       

    b1=Button(root,text="Report",borderwidth=5, width = 35,command=rep,font=("Castellar",10,"bold"))
    b1.place(x=700,y=300)
    
    def back():
        root.destroy()
        alll()
    b2=Button(root,text="Back",borderwidth=5, width = 17,command=back,font=("Castellar",10,"bold"))
    b2.place(x=850,y=400)
    
    root.mainloop()
######################################################################################################
def hoslog():
     root=Tk()
     root.geometry("1600x1600")
     root.title("Hospital Login")
    
    
     C = Canvas(root, bg="blue", height=250, width=300)
     filename = PhotoImage(file = "IMG_4557.png")
     background_label = Label(root, image=filename)
     background_label.place(x=0, y=0, relwidth=1, relheight=1)
     C.place(x=0,y=0)
   
     
     m=Label(root,text="HOSPITAL LOGIN",fg="black",bg="blue",borderwidth=5, width =20)
     m.place(x=600,y=50)
     m.configure(font=("Algerian",17,"bold")) 
     w=Label(root,text="User Name",bg="#856ff8",font=("Castellar",10,"bold"))
     w.place(x=600,y=200)
     z=Label(root,text="Password",bg="#856ff8",font=("Castellar",10,"bold"))
     z.place(x=600,y=300)
     t=Entry(root,borderwidth=5, width = 45,font=("Times New Roman",10,"bold"))
     t.place(x=750,y=200)
     t1=Entry(root,borderwidth=5, width = 45,show="*",font=("Times New Roman",10,"bold"))
     t1.place(x=750,y=300)
     def lleng():
         con=my.connect(host="localhost",user="root",password="hitech",database="hospital")
         cur=con.cursor()
         cur.execute("select * from logg where username='"+t.get()+"' and password='"+t1.get()+"'")
         d=cur.fetchall()
         if d:
              for x in d:
                   msg.showinfo("Login Status","Login Successfully "+t.get())
                   root.destroy()
                   hospital()
         else:
            msg.showinfo("Login Status","Username/Password Invalid "+t.get())
     b=Button(root,text="Submit",borderwidth=5, width =10,command=lleng)
     b.place(x=750,y=400)
     def back():
         root.destroy()
         call()
     b1=Button(root,text="Home",borderwidth=5, width =10,command=back)
     b1.place(x=840,y=400)
     root.mainloop()
#################################################################################################
def humanlog():
     root=Tk()
     root.geometry("1600x1600")
     root.title("Human Login")

     C = Canvas(root, bg="blue", height=250, width=300)
     filename = PhotoImage(file = "IMG_4557.png")
     background_label = Label(root, image=filename)
     background_label.place(x=0, y=0, relwidth=1, relheight=1)
     C.place(x=0,y=0)     
     m=Label(root,text="HUMAN LOGIN",fg="black",bg="blue",borderwidth=5, width =30)
     m.place(x=600,y=50)
     m.configure(font=("Algerian",17,"bold")) 
     w=Label(root,text="User Name",borderwidth=5, width =10)
     w.place(x=600,y=200)
     
     w.configure(bg="#856ff8",font=("Castellar",10,"bold"))
     z=Label(root,text="Password",borderwidth=5, width =10)
     z.place(x=600,y=300)
     z.configure(bg="#856ff8",font=("Castellar",10,"bold"))
     t=Entry(root,borderwidth=5, width = 45)
     t.place(x=750,y=200)
     t.configure(font=("Times New Roman",10,"bold"))
     t1=Entry(root,borderwidth=5, width = 45,show="*")
     t1.place(x=750,y=300)
     t1.configure(font=("Times New Roman",10,"bold"))
     def lleng():
         con=my.connect(host="localhost",user="root",password="hitech",database="hospital")
         cur=con.cursor()
         cur.execute("select * from log1 where username='"+t.get()+"' and password='"+t1.get()+"'")
         d=cur.fetchall()
         if d:
              for x in d:
                   msg.showinfo("Login Status","Login Successfully "+t.get())
                   root.destroy()
                   humanreport()
         else:
            msg.showinfo("Login Status","Username/Password Invalid "+t.get())
     b=Button(root,text="Submit",borderwidth=5, width =10,command=lleng)
     b.place(x=750,y=400)
     def back():
         root.destroy()
         call()
     b=Button(root,text="Home",borderwidth=5, width =10,command=back)
     b.place(x=850,y=400)
     root.mainloop()
###############################################################################################
def humanreport():
    db=my.connect(host="localhost",user="root",password="hitech",database="hospital")
    cur=db.cursor()
    root=Tk()
    root.geometry("1600x1600")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    root.title("Human Login")
    m=Label(root,text="HUMAN REPORT",fg="black",bg="pink",borderwidth=5, width = 50,font=("Algerian",17,"bold"))
    m.place(x=600,y=50)
    w=Label(root,text="Aadhar number",bg='#856ff8',font=("Castellar",10,"bold"))
    w.place(x=500,y=200)   
    z=Label(root,text="Date of Birth",bg='#856ff8',font=("Castellar",10,"bold"))
    z.place(x=500,y=250)
    t=Entry(root,borderwidth=3, width = 40,font=("Times New Roman",10,"bold"))
    t.place(x=700,y=200)
    t1= DateEntry(root, width= 36, background= "magenta3", foreground= "white",bd=2,font=("Times New Roman",10,"bold"))
    t1.place(x=700,y=250)

    xyz=LabelFrame(root,text="report")
    xyz.place(x=100,y=400)
    trv=ttk.Treeview(xyz,columns=(1,2,3,4,5,6,7,8,9,10),show="headings",height="7")
    trv.pack()
    

    trv.heading(1,text="Id")
    trv.heading(2,text="Name")
    trv.heading(3,text="Contact")
    trv.heading(4,text="DOB")
    trv.heading(5,text="Gender")
    trv.heading(6,text="Blood")
    trv.heading(7,text="Aadhar")
    trv.heading(8,text="Address")
    trv.heading(9,text="Disease")
    trv.heading(10,text="Date")
   

    trv.column(1,width=100)
    trv.column(2,width=100)
    trv.column(3,width=150)
    trv.column(4,width=200)
    trv.column(5,width=100)
    trv.column(6,width=100)
    trv.column(7,width=100)
    trv.column(8,width=100)
    trv.column(9,width=100)
    trv.column(10,width=100)
    
    
    sc=Scrollbar(xyz,orient=VERTICAL,command=trv.yview)
    sc1=Scrollbar(xyz,orient=HORIZONTAL,command=trv.xview)
    trv.configure(xscrollcommand=sc1.set,yscrollcommand=sc.set)
    
    sc.pack(side=RIGHT,fill=Y)
    sc1.pack(side=BOTTOM,fill=X)
    def data():
        sql="select * from pat where aadhar = '"+t.get()+"' and dob ='"+t1.get()+"'"
        cur.execute(sql)
        rows=cur.fetchall()
        global mydata
        mydata=rows
        trv.delete(*trv.get_children()) 
        for i in rows:
            trv.insert('','end',values=i)
    b1=Button(root,text="view",borderwidth=5, width =10,command=data)
    b1.place(x=600,y=300)

    def export():
        if len(trv.get_children()) < 1:
            msg.showerror("No Data","No data Available to export")
            return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File",".csv"),("All Files",".*")))
        with open(fln,mode='w' ) as myfile:
            exp=csv.writer(myfile,delimiter=",")
            for i in mydata:
                exp.writerow(i)
        msg.showinfo("Export Status","Exported Successfuly")
        

    b2=Button(root,text="Export",borderwidth=5, width =10,command=export)
    b2.place(x=700,y=300)
    def back():
        root.destroy()
        humanlog()
    b=Button(root,text="Back",borderwidth=5, width =10,command=back)
    b.place(x=800,y=300)
    root.mainloop()         
########################################################################################
def hosreg():
    
    root=Tk()
    root.geometry("1600x1600")
    root.title("hlogin")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    m=Label(root,text="HOSPITAL LOGIN",fg="black",bg="blue",borderwidth=5, width = 50)
    m.place(x=400,y=50)
    m.configure(font=("Algerian",17,"bold")) 
    w=Label(root,text="Hospital Name")
    w.place(x=200,y=200)
    w.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w1=Label(root,text="Hospital Location")
    w1.place(x=200,y=250)
    w1.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w2=Label(root,text="Hospital Address")
    w2.place(x=200,y=300)
    w2.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w3=Label(root,text="Date")
    w3.place(x=200,y=400)
    w3.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    t=Entry(root,borderwidth=4, width = 50)
    t.place(x=400,y=200)
    t.configure(font=("Times New Roman",10,"bold"))
    t1=Entry(root,borderwidth=4, width = 50)
    t1.place(x=400,y=250)
    t1.configure(font=("Times New Roman",10,"bold"))
    t2=Text(root,borderwidth=2, width = 30,height=3)
    t2.place(x=400,y=300)
    t2.configure(font=("Times New Roman",17,"bold"))
    t3 = DateEntry(root, width= 50, background= "magenta3", foreground= "white",bd=2)
    t3.place(x=400,y=400)
    t3.configure(font=("Times New Roman",10,"bold"))
   
    
    def sub():
        con=my.connect(host="localhost",user="root",password="hitech",database="hospital")

        cursor=con.cursor()
        str="INSERT INTO management(name,location,address,date) values('"+t.get()+"','"+t1.get()+"','"+t2.get("1.0",END)+"','"+t3.get()+"')"
        cursor.execute(str)
        cursor.execute("commit")
        msg.showinfo("Submit Status","Register Successfully")
    b=Button(root,text="Submit",borderwidth=5, width =10,command=sub)
    b.place(x=400,y=500)
    def back():
        root.destroy()
        adminpage()        
    b1=Button(root,text="Back",borderwidth=5, width =10,command=back)
    b1.place(x=500,y=500)
    def clear():
        t.delete(0,END)
        t1.delete(0,END)
        t2.delete("1.0","end")
    b2=Button(root,text="Clear",borderwidth=5, width =10,command=clear)
    b2.place(x=600,y=500)
    root.mainloop()
#######################################################################################
def hreport():
     
    root=Tk()
    root.geometry("1600x1600")
    root.title("Admin")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    m=Label(root,text="HOSPITAL REPORT",fg="black",bg="blue",borderwidth=5, width = 50)
    m.place(x=600,y=50)
    m.configure(font=("Algerian",17,"bold"))

    def grep():
        root.destroy()
        greport()
    b=Button(root,text="Gobal Report",borderwidth=5, width = 25,command=grep)
    b.place(x=700,y=200)
    b.configure(font=("Times New Roman",10,"bold"))
    def lrep():
        root.destroy()
        lreport()
    b1=Button(root,text="Local Report",borderwidth=5, width = 25,command=lrep)
    b1.place(x=700,y=300)
    b1.configure(font=("Times New Roman",10,"bold"))

    
    def back():
        root.destroy()
        adminpage()
    b2=Button(root,text="Back",borderwidth=5, width = 14,command=back)
    b2.place(x=850,y=400)
    b2.configure(font=("Times New Roman",10,"bold"))
    root.mainloop()

################################################################################################
def greport():
     
    db=my.connect(host="localhost",user="root",password="hitech",database="hospital")
    cur=db.cursor()
    root=Tk()
    root.geometry("1600x1600")
    root.title("GOBAL REPORT")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    m=Label(root,text="GOBAL REPORT",font=("Algerian",17,"bold"),fg="black",bg="pink",borderwidth=5, width = 50)
    m.place(x=600,y=50)
   
        
    w=Label(root,text="Starting Date",bg='#856ff8',font=("Castellar",10,"bold"))
    w.place(x=500,y=200)
    
    z=Label(root,text="Ending Date",bg='#856ff8',font=("Castellar",10,"bold"))
    z.place(x=500,y=250)
    
    
    t=DateEntry(root, width= 50, background= "magenta3", foreground= "white",bd=2)
    t.place(x=700,y=200)
    t.configure(font=("Times New Roman",10,"bold"))
    t1=DateEntry(root, width= 50, background= "magenta3", foreground= "white",bd=2)
    t1.place(x=700,y=250)
    t1.configure(font=("Times New Roman",10,"bold"))
    xyz=LabelFrame(root,text="report")
    xyz.place(x=50,y=500)
    trv=ttk.Treeview(xyz,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show="headings",height="7")
    trv.pack()
    

    trv.heading(1,text="Id")
    trv.heading(2,text="Name")
    trv.heading(3,text="Phone")
    trv.heading(4,text="Address")
    trv.heading(5,text="Admit")
    trv.heading(6,text="Days")
    trv.heading(7,text="Discharge")
    trv.heading(8,text="Drname")
    trv.heading(9,text="DrVisitCharge")
    trv.heading(10,text="Tablet")
    trv.heading(11,text="Ward")
    trv.heading(12,text="Discriptions")

    trv.column(1,width=100)
    trv.column(2,width=100)
    trv.column(3,width=150)
    trv.column(4,width=200)
    trv.column(5,width=100)
    trv.column(6,width=100)
    trv.column(7,width=100)
    trv.column(8,width=100)
    trv.column(9,width=100)
    trv.column(10,width=100)
    trv.column(11,width=100)
    trv.column(12,width=300)
    
    sc=Scrollbar(xyz,orient=VERTICAL,command=trv.yview)
    sc1=Scrollbar(xyz,orient=HORIZONTAL,command=trv.xview)
    trv.configure(xscrollcommand=sc1.set,yscrollcommand=sc.set)
    
    sc.pack(side=RIGHT,fill=Y)
    sc1.pack(side=BOTTOM,fill=X)
    def data():
        sql="select * from info where admit between '"+t.get()+"' and '"+t1.get()+"'"
        cur.execute(sql)
        rows=cur.fetchall()
        global mydata
        mydata=rows
        trv.delete(*trv.get_children()) 
        for i in rows:
            trv.insert('','end',values=i)
    b1=Button(root,text="view",borderwidth=5, width =10,command=data)
    b1.place(x=700,y=400)

    def export():
        if len(trv.get_children()) < 1:
            msg.showerror("No Data","No data Available to export")
            return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File",".csv"),("All Files",".*")))
        with open(fln,mode='w' ) as myfile:
            exp=csv.writer(myfile,delimiter=",")
            for i in mydata:
                exp.writerow(i)
        msg.showinfo("Export Status","Exported Successfuly")
        

    b2=Button(root,text="Export",borderwidth=5, width =10,command=export)
    b2.place(x=800,y=400)
    
    def back():
        root.destroy()
        hreport()
        
    b=Button(root,text="Back",borderwidth=5, width =10,command=back)
    b.place(x=900,y=400)
    root.mainloop()
##############################################################################################
def lreport():
    db=my.connect(host="localhost",user="root",password="hitech",database="hospital")
    cur=db.cursor()
    root=Tk()
    root.geometry("1600x1600")
    root.title("LOCAL REPORT")

    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    
    m=Label(root,text="LOCAL REPORT",fg="black",bg="pink",borderwidth=5, width = 50)
    m.place(x=600,y=50)
    m.configure(font=("Algerian",17,"bold")) 
    w1=Label(root,text="ID")
    w1.place(x=500,y=150)
    w1.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w=Label(root,text="Starting Date")
    w.place(x=500,y=200)
    w.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    z=Label(root,text="Ending Date")
    z.place(x=500,y=250)
    z.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    t2=Entry(root,borderwidth=3, width = 25)
    t2.place(x=700,y=150)
    t2.configure(font=("Times New Roman",10,"bold"))
    t=DateEntry(root, width= 50, background= "magenta3", foreground= "white",bd=2)
    t.place(x=700,y=200)
    t.configure(font=("Times New Roman",10,"bold"))
    t1=DateEntry(root, width= 50, background= "magenta3", foreground= "white",bd=2)
    t1.place(x=700,y=250)
    t1.configure(font=("Times New Roman",10,"bold"))
    xyz=LabelFrame(root,text="report")
    xyz.place(x=50,y=500)
    trv=ttk.Treeview(xyz,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show="headings",height="7")
    trv.pack()
    

    trv.heading(1,text="Id")
    trv.heading(2,text="Name")
    trv.heading(3,text="Phone")
    trv.heading(4,text="Address")
    trv.heading(5,text="Admit")
    trv.heading(6,text="Days")
    trv.heading(7,text="Discharge")
    trv.heading(8,text="Drname")
    trv.heading(9,text="DrVisitCharge")
    trv.heading(10,text="Tablet")
    trv.heading(11,text="Ward")
    trv.heading(12,text="Discriptions")

    trv.column(1,width=100)
    trv.column(2,width=100)
    trv.column(3,width=150)
    trv.column(4,width=200)
    trv.column(5,width=100)
    trv.column(6,width=100)
    trv.column(7,width=100)
    trv.column(8,width=100)
    trv.column(9,width=100)
    trv.column(10,width=100)
    trv.column(11,width=100)
    trv.column(12,width=300)
    
    sc=Scrollbar(xyz,orient=VERTICAL,command=trv.yview)
    sc1=Scrollbar(xyz,orient=HORIZONTAL,command=trv.xview)
    trv.configure(xscrollcommand=sc1.set,yscrollcommand=sc.set)
    
    sc.pack(side=RIGHT,fill=Y)
    sc1.pack(side=BOTTOM,fill=X)
    def data():
        sql="select * from info where id='"+t2.get()+"' and admit between '"+t.get()+"' and '"+t1.get()+"'"
        cur.execute(sql)
        rows=cur.fetchall()
        global mydata
        mydata=rows
        trv.delete(*trv.get_children()) 
        for i in rows:
            trv.insert('','end',values=i)
    b1=Button(root,text="view",borderwidth=5, width =10,command=data)
    b1.place(x=700,y=400)

    def export():
        if len(trv.get_children()) < 1:
            msg.showerror("No Data","No data Available to export")
            return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File",".csv"),("All Files",".*")))
        with open(fln,mode='w' ) as myfile:
            exp=csv.writer(myfile,delimiter=",")
            for i in mydata:
                exp.writerow(i)
        msg.showinfo("Export Status","Exported Successfuly")
        

    b2=Button(root,text="Export",borderwidth=5, width =10,command=export)
    b2.place(x=800,y=400)
    
    def back():
        root.destroy()
        hreport()
    b=Button(root,text="Back",borderwidth=5, width =10,command=back)
    b.place(x=900,y=400)
    root.mainloop()
#########################################################################################
def hospital():
    root=Tk()
    root.geometry("1600x1600")
    root.title("Hospital page")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    
    m=Label(root,text="HOSPITAL PAGE",fg="black",bg="blue",borderwidth=5, width =50)
    m.place(x=500,y=50)
    m.configure(font=("Algerian",17,"bold"))
    def addd():
        root.destroy()
        addpat()
    b1=Button(root,text="Add Patients Info",borderwidth=5, width =30,command=addd)
    b1.place(x=600,y=200)
    b1.configure(font=("Times New Roman",15,"bold"))

    def upp():
        root.destroy()
        up()
    b=Button(root,text="update Patients Info",borderwidth=5, width =30,command=upp)
    b.place(x=600,y=300)
    b.configure(font=("Times New Roman",15,"bold"))
    def his():
        root.destroy()
        ph()
    b2=Button(root,text="Patients History",borderwidth=5, width =30,command=his)
    b2.place(x=600,y=400)
    b2.configure(font=("Times New Roman",15,"bold"))
    def repp():
        root.destroy()
        rh()
    b3=Button(root,text="Reports",borderwidth=5, width =30,command=repp)
    b3.place(x=600,y=500)
    b3.configure(font=("Times New Roman",15,"bold"))
    def back():
        root.destroy()
        hoslog()
    b4=Button(root,text="Back",borderwidth=5, width =17,command=back)
    b4.place(x=700,y=600)
    b4.configure(font=("Times New Roman",15,"bold"))
    root.mainloop()
##############################################################################################
def addpat():
    root=Tk()
    root.geometry("1600x1600")   
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    
    m=Label(root,text="ADD PATIENT INFO",fg="black",bg="blue",borderwidth=5, width = 50)
    m.place(x=600,y=50)
    m.configure(font=("Algerian",17,"bold")) 
    w=Label(root,text="Patient ID")
    w.place(x=100,y=100)
    w.configure(bg="yellow",font=("Castellar",10,"bold"))
    
    w1=Label(root,text="Name")
    w1.place(x=100,y=150)
    w1.configure(bg="yellow",font=("Castellar",10,"bold"))
    w2=Label(root,text="Contact Number")
    w2.place(x=100,y=200)
    w2.configure(bg="yellow",font=("Castellar",10,"bold"))
    w3=Label(root,text="Date of Birth")
    w3.place(x=100,y=250)
    w3.configure(bg="yellow",font=("Castellar",10,"bold"))
    w4=Label(root,text="Gender")
    w4.place(x=100,y=300)
    w4.configure(bg="yellow",font=("Castellar",10,"bold"))
    
    w5=Label(root,text="Blood Group")
    w5.place(x=100,y=350)
    w5.configure(bg="yellow",font=("Castellar",10,"bold"))
    w6=Label(root,text="Aadhar Number")
    w6.place(x=100,y=400)
    w6.configure(bg="yellow",font=("Castellar",10,"bold"))
    w7=Label(root,text="Address")
    w7.place(x=100,y=480)
    w7.configure(bg="yellow",font=("Castellar",10,"bold"))
    w8=Label(root,text="Any Major Disease Suffered Earlier")
    w8.place(x=100,y=580)
    w8.configure(bg="yellow",font=("Castellar",10,"bold"))
    w9=Label(root,text="Date")
    w9.place(x=100,y=650)
    w9.configure(bg="yellow",font=("Castellar",10,"bold"))
    t=Entry(root,borderwidth=5, width = 50)
    t.place(x=350,y=100)
    t.configure(font=("Times New Roman",10,"bold"))
    t1=Entry(root,borderwidth=5, width = 50)
    t1.place(x=350,y=150)
    t1.configure(font=("Times New Roman",10,"bold"))
    t2=Entry(root,borderwidth=5, width = 50)
    t2.place(x=350,y=200)
    t2.configure(font=("Times New Roman",10,"bold"))
    t3 = DateEntry(root, width= 50, background= "magenta3", foreground= "white",bd=2)
    t3.place(x=350,y=250)
    t3.configure(font=("Times New Roman",10,"bold"))
    t4= StringVar(root)
    t4.set("Select")
    a= OptionMenu(root, t4, "Male","Female","Others")
    
    a.place(x=350,y=300)
    a.configure(width=45,font=("Times New Roman",10,"bold"))
    t5=Entry(root,borderwidth=5, width = 50)
    t5.place(x=350,y=350)
    t5.configure(font=("Times New Roman",10,"bold"))
    t6=Entry(root,borderwidth=5, width = 50)
    t6.place(x=350,y=400)
    t6.configure(font=("Times New Roman",10,"bold"))
    t7=Text(root,borderwidth=4, width = 40,height=4)
    t7.place(x=350,y=450)
    t7.configure(font=("Times New Roman",13,"bold"))
    t8=Text(root,borderwidth=4, width = 40,height=4)
    t8.place(x=350,y=570)
    t8.configure(font=("Times New Roman",13,"bold"))
    t9 = DateEntry(root, width= 50, background= "magenta3", foreground= "white",bd=2)
    t9.place(x=350,y=670)
    t9.configure(font=("Times New Roman",10,"bold"))
    def att():
        con=my.connect(host="localhost",user="root",password="hitech",database="hospital")

        cursor=con.cursor()
        s="INSERT INTO pat(id,name,contact,dob,gender,blood,aadhar,address,disease,date) values('"+t.get()+"','"+t1.get()+"','"+t2.get()+"','"+t3.get()+"','"+t4.get()+"','"+t5.get()+"','"+t6.get()+"','"+t7.get("1.0",END)+"','"+t8.get("1.0",END)+"','"+t9.get()+"')"
        cursor.execute(s)
        cursor.execute("commit")
        msg.showinfo("Submit Status","Added Successfully")
    b=Button(root,text="Submit",borderwidth=5, width =10,command=att)
    b.place(x=700,y=50)    
    def clear():
        t.delete(0,END)
        t1.delete(0,END)
        t2.delete(0,END)
        t5.delete(0,END)
        t6.delete(0,END)
        t7.delete("1.0","end")
        t8.delete("1.0","end")
        
        msg.showinfo("Delete Status","Record Cleared")
    b1=Button(root,text="Reset",borderwidth=5, width =10,command=clear)
    b1.place(x=700,y=80)
    def back():
        root.destroy()
        hospital()
    b2=Button(root,text="Back",borderwidth=5, width =10,command=back)
    b2.place(x=750,y=105)
    root.mainloop()
#################################################################################################
def up():
    root=Tk()
    root.geometry("1200x600")
    root.title("UPDATE PAIENTS INFO")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    m=Label(root,text="UPDATE PATIENTS DETAILS",fg="black",bg="blue",borderwidth=5, width =30)
    m.place(x=450,y=50)
    m.configure(font=("Algerian",17,"bold")) 
    w=Label(root,text="Patient ID",borderwidth=5, width =10)
    w.place(x=100,y=100)
    w.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w1=Label(root,text="Name",borderwidth=5, width =10)
    w1.place(x=100,y=150)
    w1.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w2=Label(root,text="Contact Number",borderwidth=5, width =17)
    w2.place(x=100,y=200)
    w2.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w3=Label(root,text="Date of Birth",borderwidth=5, width =17)
    w3.place(x=100,y=250)
    w3.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w4=Label(root,text="Gender",borderwidth=5, width =10)
    w4.place(x=100,y=300)
    w4.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w5=Label(root,text="Blood Group",borderwidth=5, width =10)
    w5.place(x=100,y=350)
    w5.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w6=Label(root,text="Aadhar Number",borderwidth=5, width =17)
    w6.place(x=100,y=400)
    w6.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w7=Label(root,text="Address",borderwidth=5, width =10)
    w7.place(x=100,y=450)
    w7.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w8=Label(root,text="Major Disease Suffered Earlier",borderwidth=5, width =35)
    w8.place(x=100,y=500)
    w8.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w9=Label(root,text="Date",borderwidth=5, width =10)
    w9.place(x=100,y=550)
    w9.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    t=Entry(root,borderwidth=5, width = 50)
    t.place(x=450,y=100)
    t.configure(font=("Times New Roman",10,"bold"))
    t1=Entry(root,borderwidth=5, width = 50)
    t1.place(x=450,y=150)
    t1.configure(font=("Times New Roman",10,"bold"))
    t2=Entry(root,borderwidth=5, width = 50)
    t2.place(x=450,y=200)
    t2.configure(font=("Times New Roman",10,"bold"))
    t3=Entry(root,borderwidth=5, width = 50)
    t3.place(x=450,y=250)
    t3.configure(font=("Times New Roman",10,"bold"))
    t4=Entry(root,borderwidth=5, width = 50)
    t4.place(x=450,y=300)
    t4.configure(font=("Times New Roman",10,"bold"))
    t5=Entry(root,borderwidth=5, width = 50)
    t5.place(x=450,y=350)
    t5.configure(font=("Times New Roman",10,"bold"))
    t6=Entry(root,borderwidth=5, width = 50)
    t6.place(x=450,y=400)
    t6.configure(font=("Times New Roman",10,"bold"))
    t7=Entry(root,borderwidth=5, width = 50)
    t7.place(x=450,y=450)
    t7.configure(font=("Times New Roman",10,"bold"))
    t8=Entry(root,borderwidth=5, width = 50)
    t8.place(x=450,y=500)
    t8.configure(font=("Times New Roman",10,"bold"))
    t9=Entry(root,borderwidth=5, width = 50)
    t9.place(x=450,y=550)
    t9.configure(font=("Times New Roman",10,"bold"))
    def retrive():
        i=0
        id=t.get()
        if (id==""):
            msg.showinfo("Retrive Status","Required Id Field")
        else:
            con=my.connect(host="localhost",user="root",password="hitech",database="hospital")
            cursor=con.cursor()
            cursor.execute("select * from pat where id='"+id+"'")
            rows=cursor.fetchall()

            for i in rows:
                t1.insert(0,i[1])
                t2.insert(0,i[2])
                t3.insert(0,i[3])
                t4.insert(0,i[4])
                t5.insert(0,i[5])
                t6.insert(0,i[6])
                t7.insert(0,i[7])
                t8.insert(0,i[8])
                t9.insert(0,i[9])
                
                msg.showinfo("Retrive Status","Record Found")
            if i not in rows:
                msg.showinfo("Retrive Status","Record Not Found")
            con.close();

    b=Button(root,text="Search",borderwidth=5, width =10,command=retrive)
    b.place(x=450,y=120)
    def back():
        root.destroy()
        hospital()
    b2=Button(root,text="Back",borderwidth=5, width =10,command=back)
    b2.place(x=750,y=105)
    root.mainloop()

    def update():
        id=t.get()
       

        if (id==" "):
            msg.showinfo("Update Status","All the Fields")
        else:
            con=my.connect(host="localhost",user="root",password="hitech",database="hospital")
            cursor=con.cursor()
            cursor.execute("update pat set name='"+t1.get()+"',contact='"+t2.get()+"', dob='"+t3.get()+"',gender='"+t4.get()+"',blood='"+t5.get()+"',aadhar='"+t6.get()+"',address='"+t7.get()+"',disease='"+t8.get()+"',date='"+t9.get()+"' where id='"+t.get()+"'")
            cursor.execute("commit");
            msg.showinfo("Update Status","Updated Successfully")
            con.close();
            t.delete(0,END)
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            t5.delete(0,END)
            t6.delete(0,END)
            t7.delete(0,END)
            t8.delete(0,END)
            t9.delete(0,END)
    b1=Button(root,text="Update",borderwidth=5, width =10,command=update)
    b1.place(x=500,y=150)


    def delete():
        id=t.get()
    
        if (id==""):
            MessageBox.showinfo("Delete Status","All the Fields")
        else:
            con=my.connect(host="localhost",user="root",password="hitech",database="hospital")
            cursor=con.cursor()
            cursor.execute("delete from pat where id='"+id+"'")
            cursor.execute("commit");
            msg.showinfo("Delete Status","Deleted Successfully")
            con.close();
            t.delete(0,END)
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            t5.delete(0,END)
            t6.delete(0,END)
            t7.delete(0,END)
            t8.delete(0,END)
            t9.delete(0,END)
    b2=Button(root,text="Delete",borderwidth=5, width =10,command=delete)
    b2.place(x=750,y=100)



    
    def clear():
        t.delete(0,END)
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)
        t6.delete(0,END)
        t7.delete(0,END)
        t8.delete(0,END)
        t9.delete(0,END)
        msg.showinfo("Delete Status","Record Cleared")
    b3=Button(root,text="Clear",borderwidth=5, width =10,command=clear)
    b3.place(x=450,y=700)
    def back():
        
        root.destroy()
        hospital()
    b4=Button(root,text="Back",borderwidth=5, width =10,command=back)
    
    b4.place(x=550,y=700)
    root.mainloop()
#############################################################################################################################
def ph():
    db=my.connect(host="localhost",user="root",password="hitech",database="hospital")
    cur=db.cursor()
    root=Tk()
    root.geometry("1600x1600")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    root.title("Human Login")
    m=Label(root,text="PATIENT REPORT",fg="black",bg="pink",borderwidth=5, width = 50)
    m.place(x=600,y=50)
    m.configure(font=("Algerian",17,"bold")) 
    w=Label(root,text="Starting Date")
    w.place(x=500,y=200)
    w.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    z=Label(root,text="Ending Date")
    z.place(x=500,y=250)
    z.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    t=DateEntry(root, width= 25, background= "magenta3", foreground= "white",bd=2)
    t.place(x=800,y=200)
    t.configure(font=("Times New Roman",10,"bold"))
    t1= DateEntry(root, width= 25, background= "magenta3", foreground= "white",bd=2)
    t1.place(x=800,y=250)
    t1.configure(font=("Times New Roman",10,"bold"))

    xyz=LabelFrame(root,text="report")
    xyz.place(x=50,y=500)
    trv=ttk.Treeview(xyz,columns=(1,2,3,4,5,6,7,8,9,10),show="headings",height="7")
    trv.pack()
    

    trv.heading(1,text="Id")
    trv.heading(2,text="Name")
    trv.heading(3,text="Contact")
    trv.heading(4,text="DOB")
    trv.heading(5,text="Gender")
    trv.heading(6,text="Blood")
    trv.heading(7,text="Aadhar")
    trv.heading(8,text="Address")
    trv.heading(9,text="Disease")
    trv.heading(10,text="Date")
   

    trv.column(1,width=100)
    trv.column(2,width=100)
    trv.column(3,width=150)
    trv.column(4,width=200)
    trv.column(5,width=100)
    trv.column(6,width=100)
    trv.column(7,width=100)
    trv.column(8,width=100)
    trv.column(9,width=100)
    trv.column(10,width=100)
    
    
    sc=Scrollbar(xyz,orient=VERTICAL,command=trv.yview)
    sc1=Scrollbar(xyz,orient=HORIZONTAL,command=trv.xview)
    trv.configure(xscrollcommand=sc1.set,yscrollcommand=sc.set)
    
    sc.pack(side=RIGHT,fill=Y)
    sc1.pack(side=BOTTOM,fill=X)
    def data():
        sql="select * from pat where date between '"+t.get()+"' and '"+t1.get()+"'"
        cur.execute(sql)
        rows=cur.fetchall()
        global mydata
        mydata=rows
        trv.delete(*trv.get_children()) 
        for i in rows:
            trv.insert('','end',values=i)
    b1=Button(root,text="view",borderwidth=5, width =10,command=data)
    b1.place(x=700,y=400)

    def export():
        if len(trv.get_children()) < 1:
            msg.showerror("No Data","No data Available to export")
            return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File",".csv"),("All Files",".*")))
        with open(fln,mode='w' ) as myfile:
            exp=csv.writer(myfile,delimiter=",")
            for i in mydata:
                exp.writerow(i)
        msg.showinfo("Export Status","Exported Successfuly")
        

    b2=Button(root,text="Export",borderwidth=5, width =10,command=export)
    b2.place(x=800,y=400)
    

    def back():
        root.destroy()
        hospital()
        
    b2=Button(root,text="Back",borderwidth=5, width =10,command=back)
    b2.place(x=750,y=105)
    root.mainloop() 
####################################################################################################################

def rh():
    root=Tk()
    root.geometry("1600x1600")
    root.title("Paitents Report")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    m=Label(root,text="PATIENTS REPORT",fg="black",bg="blue",borderwidth=5, width = 50)
    m.place(x=600,y=50)
    m.configure(font=("Algerian",17,"bold"))
    def gp():
        root.destroy()
        gpp()
        
    b2=Button(root,text="Get Patients Info",borderwidth=5, width =25,command=gp)
    b2.place(x=700,y=200)
    b2.configure(font=("Times New Roman",15,"bold"))
    def ui():
        root.destroy()
        uii()
        
    b=Button(root,text="Update Info",borderwidth=5, width =25,command=ui)
    b.place(x=700,y=300)
    b.configure(font=("Times New Roman",15,"bold"))
    def back():
        root.destroy()
        hospital()
        
    b3=Button(root,text="Back",borderwidth=5, width =10,command=back)
    b3.place(x=850,y=400)
    b3.configure(font=("Times New Roman",15,"bold"))
    root.mainloop()
##################################################################################################################
def gpp():
    root = Tk()
    root.title("CENTRALIZED HOSPITAL MANAGEMENT FOR PAITENTS")
    root.geometry("1600x1600")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    m=Label(root,text="ADD PATIENT DETAILS",fg="blue",bg="pink",borderwidth=5, width = 50)
    m.place(x=600,y=50)
    m.configure(font=("Algerian",17,"bold")) 
    w=Label(root,text="Patient ID")
    w.place(x=100,y=100)
    w.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w1=Label(root,text="Name")
    w1.place(x=100,y=150)
    w1.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w2=Label(root,text="Phone Number")
    w2.place(x=100,y=200)
    w2.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w3=Label(root,text="Address")
    w3.place(x=100,y=250)
    w3.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w4=Label(root,text="Date of admit")
    w4.place(x=100,y=350)
    w4.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w5=Label(root,text="No.Of.Days")
    w5.place(x=100,y=400)
    w5.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w6=Label(root,text="Date of Discharge")
    w6.place(x=100,y=450)
    w6.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w7=Label(root,text="Dr Name")
    w7.place(x=100,y=500)
    w7.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w8=Label(root,text="Dr Visit Charge")
    w8.place(x=100,y=550)
    w8.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w9=Label(root,text="Tablet Consume")
    w9.place(x=100,y=600)
    w9.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w10=Label(root,text="Ward Charges")
    w10.place(x=100,y=650)
    w10.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    w11=Label(root,text="Discriptions")
    w11.place(x=100,y=700)
    w11.configure(bg="#856ff8",font=("Castellar",10,"bold"))
    t=Entry(root,borderwidth=5, width = 50)
    t.place(x=300,y=100)
    t.configure(font=("Times New Roman",10,"bold"))
    t1=Entry(root,borderwidth=5, width = 50)
    t1.place(x=300,y=150)
    t1.configure(font=("Times New Roman",10,"bold"))
    t2=Entry(root,borderwidth=5, width = 50)
    t2.place(x=300,y=200)
    t2.configure(font=("Times New Roman",10,"bold"))
    t3=Text(root,borderwidth=2, width = 30,height=3)
    t3.place(x=300,y=250)
    t3.configure(font=("Times New Roman",17,"bold"))
    t4 = DateEntry(root, width=50, background= "magenta3", foreground= "white",bd=2)
    t4.place(x=300,y=350)
    t4.configure(font=("Times New Roman",10,"bold"))
    t5=Entry(root,borderwidth=5, width = 50)
    t5.place(x=300,y=400)
    t5.configure(font=("Times New Roman",10,"bold"))
    t6= DateEntry(root, width=50, background= "magenta3", foreground= "white",bd=2)
    t6.place(x=300,y=450)
    t6.configure(font=("Times New Roman",10,"bold"))
    t7=Entry(root,borderwidth=5, width = 50)
    t7.place(x=300,y=500)
    t7.configure(font=("Times New Roman",10,"bold"))
    t8=Entry(root,borderwidth=5, width = 50)
    t8.place(x=300,y=550)
    t8.configure(font=("Times New Roman",10,"bold"))
    t9=Entry(root,borderwidth=5, width = 50)
    t9.place(x=300,y=600)
    t9.configure(font=("Times New Roman",10,"bold"))
    t10=Entry(root,borderwidth=5, width = 50)
    t10.place(x=300,y=650)
    t10.configure(font=("Times New Roman",10,"bold"))
    t11=Text(root,borderwidth=2, width = 30,height=3)
    t11.place(x=300,y=700)
    t11.configure(font=("Times New Roman",17,"bold"))

    def att():
        con=my.connect(host="localhost",user="root",password="hitech",database="hospital")

        cursor=con.cursor()
        s="INSERT INTO info(id,name,phone,address,admit,days,discharge,dname,dvisitcharge,tablet,ward,discriptions) values('"+t.get()+"','"+t1.get()+"','"+t2.get()+"','"+t3.get("1.0",END)+"','"+t4.get()+"','"+t5.get()+"','"+t6.get()+"','"+t7.get()+"','"+t8.get()+"','"+t9.get()+"','"+t10.get()+"','"+t11.get("1.0",END)+"')"
        cursor.execute(s)
        cursor.execute("commit")
        msg.showinfo("Submit Status","Added Successfully")
    b=Button(root,text="Submit",borderwidth=5, width =10,command=att)
    b.place(x=250,y=800)

    def clear():
        t.delete(0,END)
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)
        t6.delete(0,END)
        t7.delete(0,END)
        t8.delete(0,END)
        t9.delete(0,END)
        t10.delete(0,END)
        t11.delete(0,END)
        msg.showinfo("Clear Status","Data has been cleared")       
    b1=Button(root,text="Reset",borderwidth=5, width =10,command=clear)
    b1.place(x=350,y=800)
    def back():
        root.destroy()
        rh()
       
    b2=Button(root,text="Back",borderwidth=5, width =10,command=back)
    b2.place(x=450,y=800)
    root.mainloop()
################################################################################################################
def uii():
    root = Tk()
    root.title("UPDATE PATIENTS INFoS")
    root.geometry("1600x1600")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)
    m=Label(root,text="UPDATE PATIENTS DETAILS",fg="black",bg="blue",borderwidth=5, width = 50)
    m.place(x=450,y=50)
    m.configure(font=("Algerian",17,"bold"))
    w=Label(root,text="Patient ID")
    w.place(x=100,y=100)
    w.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w1=Label(root,text="Name")
    w1.place(x=100,y=150)
    w1.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w2=Label(root,text="Phone Number")
    w2.place(x=100,y=200)
    w2.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w3=Label(root,text="Address")
    w3.place(x=100,y=250)
    w3.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w4=Label(root,text="Date of admit")
    w4.place(x=100,y=300)
    w4.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w5=Label(root,text="No.Of.Days")
    w5.place(x=100,y=350)
    w5.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w6=Label(root,text="Date of Discharge")
    w6.place(x=100,y=400)
    w6.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w7=Label(root,text="Dr Name")
    w7.place(x=100,y=450)
    w7.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w8=Label(root,text="Dr Visit Charge")
    w8.place(x=100,y=500)
    w8.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w9=Label(root,text="Tablet Consume")
    w9.place(x=100,y=550)
    w9.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w10=Label(root,text="Ward Charges")
    w10.place(x=100,y=600)
    w10.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    w11=Label(root,text="Discriptions")
    w11.place(x=100,y=650)
    w11.configure(bg='#856ff8',font=("Castellar",10,"bold"))
    t=Entry(root,borderwidth=5, width = 35)
    t.place(x=450,y=100)
    t.configure(font=("Times New Roman",10,"bold"))
    t1=Entry(root,borderwidth=5, width = 35)
    t1.place(x=450,y=150)
    t1.configure(font=("Times New Roman",10,"bold"))
    t2=Entry(root,borderwidth=5, width = 35)
    t2.place(x=450,y=200)
    t2.configure(font=("Times New Roman",10,"bold"))
    t3=Entry(root,borderwidth=5, width = 35)
    t3.place(x=450,y=250)
    t3.configure(font=("Times New Roman",10,"bold"))
    t4=Entry(root,borderwidth=5, width = 35)
    t4.place(x=450,y=300)
    t4.configure(font=("Times New Roman",10,"bold"))
    t5=Entry(root,borderwidth=5, width = 35)
    t5.place(x=450,y=350)
    t5.configure(font=("Times New Roman",10,"bold"))
    t6=Entry(root,borderwidth=5, width = 35)
    t6.place(x=450,y=400)
    t6.configure(font=("Times New Roman",10,"bold"))
    t7=Entry(root,borderwidth=5, width = 35)
    t7.place(x=450,y=450)
    t7.configure(font=("Times New Roman",10,"bold"))
    t8=Entry(root,borderwidth=5, width = 35)
    t8.place(x=450,y=500)
    t8.configure(font=("Times New Roman",10,"bold"))
    t9=Entry(root,borderwidth=5, width = 35)
    t9.place(x=450,y=550)
    t9.configure(font=("Times New Roman",10,"bold"))
    t10=Entry(root,borderwidth=5, width = 35)
    t10.place(x=450,y=600)
    t10.configure(font=("Times New Roman",10,"bold"))
    t11=Entry(root,borderwidth=5, width = 35)
    t11.place(x=450,y=650)
    t11.configure(font=("Times New Roman",10,"bold"))
    def retrive():
        i=0
        id=t.get()
        if (id==""):
            msg.showinfo("Retrive Status","Required Id Field")
        else:
            con=my.connect(host="localhost",user="root",password="hitech",database="hospital")
            cursor=con.cursor()
            cursor.execute("select * from info where id='"+id+"'")
            rows=cursor.fetchall()

            for i in rows:
                t1.insert(0,i[1])
                t2.insert(0,i[2])
                t3.insert(0,i[3])
                t4.insert(0,i[4])
                t5.insert(0,i[5])
                t6.insert(0,i[6])
                t7.insert(0,i[7])
                t8.insert(0,i[8])
                t9.insert(0,i[9])
                t10.insert(0,i[10])
                t11.insert(0,i[11])
                
                msg.showinfo("Retrive Status","Record Found")
            if i not in rows:
                msg.showinfo("Retrive Status","Record Not Found")
            con.close();

    b=Button(root,text="Search",borderwidth=5, width =10,command=retrive)
    b.place(x=450,y=120)

    def update():
        id=t.get()
       

        if (id==" "):
            msg.showinfo("Update Status","All the Fields")
        else:
            con=my.connect(host="localhost",user="root",password="hitech",database="hospital")
            cursor=con.cursor()
            cursor.execute("update info set name='"+t1.get()+"',phone='"+t2.get()+"', address='"+t3.get()+"',admit='"+t4.get()+"',days='"+t5.get()+"',discharge='"+t6.get()+"',dname='"+t7.get()+"',dvisitcharge='"+t8.get()+"',tablet='"+t9.get()+"',ward='"+t10.get()+"',discriptions='"+t11.get()+"' where id='"+t.get()+"'")
            cursor.execute("commit");
            msg.showinfo("Update Status","Updated Successfully")
            con.close();
            t.delete(0,END)
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            t5.delete(0,END)
            t6.delete(0,END)
            t7.delete(0,END)
            t8.delete(0,END)
            t9.delete(0,END)
            t10.delete(0,END)
            t11.delete(0,END)

    b1=Button(root,text="Update",borderwidth=5, width =10,command=update)
    b1.place(x=200,y=700)

    def delete():
        id=t.get()
    
        if (id==""):
            MessageBox.showinfo("Delete Status","All the Fields")
        else:
            con=my.connect(host="localhost",user="root",password="hitech",database="hospital")
            cursor=con.cursor()
            cursor.execute("delete from info where id='"+id+"'")
            cursor.execute("commit");
            msg.showinfo("Delete Status","Deleted Successfully")
            con.close();
            t.delete(0,END)
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            t5.delete(0,END)
            t6.delete(0,END)
            t7.delete(0,END)
            t8.delete(0,END)
            t9.delete(0,END)
            t10.delete(0,END)
            t11.delete(0,END)
    b2=Button(root,text="Delete",borderwidth=5, width =10,command=delete)
    b2.place(x=350,y=700)

    
    def back():
        root.destroy()
        rh()
        
    b4=Button(root,text="Back",borderwidth=5, width =10,command=back)
    b4.place(x=450,y=700)

    def clear():
        t.delete(0,END)
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)
        t6.delete(0,END)
        t7.delete(0,END)
        t8.delete(0,END)
        t9.delete(0,END)
        t10.delete(0,END)
        t11.delete(0,END)
        msg.showinfo("Delete Status","Record Cleared")
    b3=Button(root,text="Clear",borderwidth=5, width =10,command=clear)
    b3.place(x=550,y=700)
    root.mainloop()
if __name__ == '__main__':
    
    call() #Call through procedure.


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class itemno_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Canteen management System")
        self.root.geometry("1200x550+0+190")
        
        #variables
        self.c1=StringVar()
        self.n1=StringVar()
        self.n2=StringVar()
        self.n3=StringVar()
        self.n4=StringVar()
        self.n5=StringVar()
        
        
        #title
        ti=Label(self.root,text="ITEMNO DETAILS",bg="black",fg="red",font=("arabic",18,"bold"))
        ti.place(x=0,y=0,width=1295,height=30)  
        
        #label frame in frame we can also write text
        lbf=LabelFrame(self.root,bd=2,relief=RIDGE,text="ITEMNO DETAILS",padx=2,font=("arabic",10,"bold"))
        lbf.place(x=10,y=60,width=425,height=440)
        
        #labels and entry
        cust_id=Label(lbf,text="Customer ID : ",font=("arabic",10,"bold"),padx=2,pady=15)
        cust_id.grid(row=0,column=0,sticky=W)
        
        id_eny=ttk.Entry(lbf,width=32,textvariable=self.c1,font=("arabic",10,"bold"))
        id_eny.grid(row=0,column=1,padx=5)
        
        name_item=Label(lbf,text="no. of Item1 : ",font=("arabic",10,"bold"),padx=2,pady=20)
        name_item.grid(row=1,column=0,sticky=W)
        
        it_eny=ttk.Entry(lbf,width=32,textvariable=self.n1,font=("arabic",10,"bold"))
        it_eny.grid(row=1,column=1)
        
        item_price=Label(lbf,text="no. of Item2 : ",font=("arabic",10,"bold"),padx=2,pady=20)
        item_price.grid(row=2,column=0,sticky=W)
        
        price_eny=ttk.Entry(lbf,width=32,textvariable=self.n2,font=("arabic",10,"bold"))
        price_eny.grid(row=2,column=1)
        
        it_price=Label(lbf,text="no. of Item3 : ",font=("arabic",10,"bold"),padx=2,pady=20)
        it_price.grid(row=3,column=0,sticky=W)
        
        pri_eny=ttk.Entry(lbf,width=32,textvariable=self.n3,font=("arabic",10,"bold"))
        pri_eny.grid(row=3,column=1)
        
        ite_price=Label(lbf,text="no. of Item4 : ",font=("arabic",10,"bold"),padx=2,pady=20)
        ite_price.grid(row=4,column=0,sticky=W)
        
        rice_eny=ttk.Entry(lbf,width=32,textvariable=self.n4,font=("arabic",10,"bold"))
        rice_eny.grid(row=4,column=1)
        
        ie_price=Label(lbf,text="no. of Item5 : ",font=("arabic",10,"bold"),padx=2,pady=20)
        ie_price.grid(row=5,column=0,sticky=W)
        
        rce_eny=ttk.Entry(lbf,width=32,textvariable=self.n5,font=("arabic",10,"bold"))
        rce_eny.grid(row=5,column=1)
        
        #btns for add,update
        fr=Frame(lbf,bd=2,relief=RIDGE)
        fr.place(x=125,y=355,width=150,height=40)
        
        addbtn=Button(fr,text="ADD / UPDATE",command=self.add1,font=("arabic",9,"bold"),bg="black",fg="blue",width=20,height=2)
        addbtn.grid(row=0,column=0)
        
        #table data
        tb=Frame(self.root,bd=2,relief=RIDGE)
        tb.place(x=450,y=70,width=720,height=400)
        
        scroll_y=ttk.Scrollbar(tb,orient=VERTICAL)
        
        self.i_det_table=ttk.Treeview(tb,column=("c","IT","PR","TP","CG","s"),yscrollcommand=scroll_y.set) #makes table
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.i_det_table.yview)
        
        self.i_det_table.heading("c",text="Customer_id")
        self.i_det_table.heading("IT",text="no. of Item1")  #this text will be seen as column name to user
        self.i_det_table.heading("PR",text="no. of Item2")
        self.i_det_table.heading("TP",text="no. of Item3")
        self.i_det_table.heading("CG",text="no. of Item4")
        self.i_det_table.heading("s",text="no. of Item5")
        
        self.i_det_table["show"]="headings"
        
        self.i_det_table.column("c",width=50)
        self.i_det_table.column("IT",width=50)
        self.i_det_table.column("PR",width=20)
        self.i_det_table.column("TP",width=30)
        self.i_det_table.column("CG",width=30)
        self.i_det_table.column("s",width=30)
       
        self.i_det_table.pack(fill=BOTH,expand=1)
        self.i_det_table.bind("<ButtonRelease-1>",self.getdata1) #binds data from table to entry field
        self.fetch1()
        
        
        
    def add1(self):
        if self.n1.get()=="" or self.n2.get()=="" or self.n3.get()=="" or self.n4.get()=="" or self.n5.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:  #bcoz of try except error is avoided in interpreter
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
                my_cursor=conn.cursor()
                
                #.get() takes the values stored in variable
                my_cursor.execute("update odr set na=%s,nb=%s,nc=%s,nd=%s,ne=%s where custid=%s",(self.n1.get(),self.n2.get(),self.n3.get(),self.n4.get(),self.n5.get(),self.c1.get()))
                conn.commit()
                self.fetch1()
                conn.close()
                
                messagebox.showinfo("success","item has been added",parent=self.root)
                
            except Exception as es:
                messagebox.showwarning("warning","something went wrong",parent=self.root)    
            
            
        
    def fetch1(self): #to show data in table
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select custid,na,nb,nc,nd,ne from odr")
        rows=my_cursor.fetchall()  #list of tuples
        if len(rows)!=0:
            self.i_det_table.delete(*self.i_det_table.get_children())
            for i in rows:
                self.i_det_table.insert("",END,values=i)  #insert values in table by row
            conn.commit()
            conn.close()    
            
    def getdata1(self,event=""): #when we click on data of one row it gets displayed on entry fields
        cursorrow=self.i_det_table.focus()  #store row of table on which we click
        content=self.i_det_table.item(cursorrow)       # stores data of that row
        row=content["values"]    #store data of that row in list
        self.c1.set(row[0])
        self.n1.set(row[1])
        self.n2.set(row[2])
        self.n3.set(row[3])
        self.n4.set(row[4]) 
        self.n5.set(row[5])
    

if __name__=="__main__":
    root=Tk()
    obj=itemno_win(root)
    root.mainloop()
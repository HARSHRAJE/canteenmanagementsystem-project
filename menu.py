from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class menu_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Canteen management System")
        self.root.geometry("1295x550+0+108")
        
        #variables
        self.it=StringVar()
        self.pr=StringVar()
        self.tp=StringVar()
        self.cg=StringVar()
        
        
        #title
        ti=Label(self.root,text="MENU DETAILS",bg="black",fg="red",font=("arabic",18,"bold"))
        ti.place(x=0,y=0,width=1295,height=30)  
        
        #label frame in frame we can also write text
        lbf=LabelFrame(self.root,bd=2,relief=RIDGE,text="MENU DETAILS",padx=2,font=("arabic",10,"bold"))
        lbf.place(x=5,y=70,width=425,height=385)
        
        #labels and entry
        name_item=Label(lbf,text="Name of Item : ",font=("arabic",10,"bold"),padx=2,pady=20)
        name_item.grid(row=0,column=0,sticky=W)
        
        it_eny=ttk.Entry(lbf,width=32,textvariable=self.it,font=("arabic",10,"bold"))
        it_eny.grid(row=0,column=1)
        
        item_price=Label(lbf,text="Price : ",font=("arabic",10,"bold"),padx=2,pady=20)
        item_price.grid(row=1,column=0,sticky=W)
        
        price_eny=ttk.Entry(lbf,width=32,textvariable=self.pr,font=("arabic",10,"bold"))
        price_eny.grid(row=1,column=1)
        
        cust_gen=Label(lbf,text="Veg / NonVeg :",font=("arabic",10,"bold"),padx=2,pady=20)
        cust_gen.grid(row=2,column=0,sticky=W)
        com_gen=ttk.Combobox(lbf,textvariable=self.tp,font=("arabic",10,"bold"),width=30) #drop down
        com_gen["value"]=("Veg","NonVeg")
        com_gen.grid(row=2,column=1)
        
        
        cust_gen=Label(lbf,text="Category : ",font=("arabic",10,"bold"),padx=2,pady=20)
        cust_gen.grid(row=3,column=0,sticky=W)
        com_gen=ttk.Combobox(lbf,textvariable=self.cg,font=("arabic",10,"bold"),width=30) #drop down
        com_gen["value"]=("Main_Course","Deserts","Breads","Juice","Rice","Starter")
        com_gen.grid(row=3,column=1)
        
        #btns for add,update,delete
        fr=Frame(lbf,bd=2,relief=RIDGE)
        fr.place(x=7,y=290,width=390,height=40)
        
        addbtn=Button(fr,text="ADD",command=self.add1,font=("arabic",8,"bold"),bg="black",fg="blue",width=17,height=2)
        addbtn.grid(row=0,column=0)
        
        updbtn=Button(fr,text="UPDATE",command=self.update1,font=("arabic",8,"bold"),bg="black",fg="blue",width=17,height=2)
        updbtn.grid(row=0,column=1)
        
        delbtn=Button(fr,text="DELETE",command=self.dele1,font=("arabic",8,"bold"),bg="black",fg="blue",width=17,height=2)
        delbtn.grid(row=0,column=2) 
        
        #table data
        tb=Frame(self.root,bd=2,relief=RIDGE)
        tb.place(x=450,y=70,width=720,height=400)
        
        scroll_y=ttk.Scrollbar(tb,orient=VERTICAL)
        
        self.menu_det_table=ttk.Treeview(tb,column=("IT","PR","TP","CG"),yscrollcommand=scroll_y.set) #makes table
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.menu_det_table.yview)
        
        self.menu_det_table.heading("IT",text="Name of Item")  #this text will be seen as column name to user
        self.menu_det_table.heading("PR",text="Price")
        self.menu_det_table.heading("TP",text="Veg / NonVeg")
        self.menu_det_table.heading("CG",text="Category")
        
        self.menu_det_table["show"]="headings"
        
        self.menu_det_table.column("IT",width=50)
        self.menu_det_table.column("PR",width=20)
        self.menu_det_table.column("TP",width=30)
        self.menu_det_table.column("CG",width=30)
       
        self.menu_det_table.pack(fill=BOTH,expand=1)
        self.menu_det_table.bind("<ButtonRelease-1>",self.getdata1) #binds data from table to entry field
        self.fetch1()
        
        
        
    def add1(self):
        if self.it.get()=="" or self.pr.get()=="" or self.tp.get()=="" or self.cg.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:  #bcoz of try except error is avoided in interpreter
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
                my_cursor=conn.cursor()
                
                #.get() takes the values stored in variable
                my_cursor.execute("insert into menu values(%s,%s,%s,%s)",(self.it.get(),self.pr.get(),self.tp.get(),self.cg.get()))
                conn.commit()
                self.fetch1()
                conn.close()
                
                messagebox.showinfo("success","item has been added",parent=self.root)
                
                
            
            except Exception as es:
                messagebox.showwarning("warning","something went wrong",parent=self.root)
        
    def fetch1(self): #to show data in table
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from menu")
        rows=my_cursor.fetchall()  #list of tuples
        if len(rows)!=0:
            self.menu_det_table.delete(*self.menu_det_table.get_children())
            for i in rows:
                self.menu_det_table.insert("",END,values=i)  #insert values in table by row
            conn.commit()
            conn.close()    
            
    def getdata1(self,event=""): #when we click on data of one row it gets displayed on entry fields
        cursorrow=self.menu_det_table.focus()  #store row of table on which we click
        content=self.menu_det_table.item(cursorrow)       # stores data of that row
        row=content["values"]    #store data of that row in list
        self.it.set(row[0])
        self.pr.set(row[1])
        self.tp.set(row[2])
        self.cg.set(row[3]) 
        
        
    def update1(self):
        if self.pr.get()=="":
            messagebox.showerror("Error","price not entered",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
            my_cursor=conn.cursor()
             
            my_cursor.execute("update menu set Price=%s,VegorNon=%s,category=%s where NameofITEM=%s",(self.pr.get(),self.tp.get(),self.cg.get(),self.it.get()))
            conn.commit()
            self.fetch1()
            conn.close()
            messagebox.showinfo("Updated","Details Updated",parent=self.root)
    
    def dele1(self):
        dele=messagebox.askyesno("canteen management","do you want to delete",parent=self.root)
        if dele>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
            my_cursor=conn.cursor()
             
            query="delete from menu where Price=%s"
            values=(self.pr.get(),)
            my_cursor.execute(query,values)
            
            
        else:
            if not dele:
                return
        
        
        conn.commit()
        self.fetch1()
        conn.close()

if __name__=="__main__":
    root=Tk()
    obj2=menu_win(root)
    root.mainloop()
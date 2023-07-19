from tkinter import *
from tkinter import ttk #have stylist entry
import mysql.connector
from tkinter import messagebox

class cust_win:
    def __init__(self,root): #constructor
        self.root=root
        self.root.title("Canteen management System")
        self.root.geometry("1295x550+0+108")
        
        
        #variables
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_ph=StringVar()
        self.var_gen=StringVar()
        self.var_eml=StringVar()
    
        
        #title
        ti=Label(self.root,text="ADD CUSTOMER DETAILS",bg="yellow",fg="black",font=("arabic",18,"bold"))
        ti.place(x=0,y=0,width=1295,height=30)  
        
        
        #label frame in frame we can also write text
        lbf=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",padx=2,font=("arabic",10,"bold"))
        lbf.place(x=5,y=50,width=425,height=450)
        
        #labels and entry
        cust_id=Label(lbf,text="Customer ID",font=("arabic",10,"bold"),padx=2,pady=20)
        cust_id.grid(row=0,column=0,sticky=W)
        
        id_eny=ttk.Entry(lbf,width=32,textvariable=self.var_id,font=("arabic",10,"bold"))
        id_eny.grid(row=0,column=1)
        
        cust_name=Label(lbf,text="Customer Name",font=("arabic",10,"bold"),padx=2,pady=20)
        cust_name.grid(row=1,column=0,sticky=W)
        
        name_eny=ttk.Entry(lbf,width=32,textvariable=self.var_name,font=("arabic",10,"bold"))
        name_eny.grid(row=1,column=1)
        
        
        cust_ph=Label(lbf,text="Phone no.",font=("arabic",10,"bold"),padx=2,pady=20)
        cust_ph.grid(row=2,column=0,sticky=W)
        
        ph_eny=ttk.Entry(lbf,width=32,textvariable=self.var_ph,font=("arabic",10,"bold"))
        ph_eny.grid(row=2,column=1)
        
        cust_gen=Label(lbf,text="Gender",font=("arabic",10,"bold"),padx=2,pady=20)
        cust_gen.grid(row=3,column=0,sticky=W)
        com_gen=ttk.Combobox(lbf,textvariable=self.var_gen,font=("arabic",10,"bold"),width=30) #drop down
        com_gen["value"]=("Male","Female","Other")
        com_gen.grid(row=3,column=1)
    
        cust_email=Label(lbf,text="Email",font=("arabic",10,"bold"),padx=2,pady=20)
        cust_email.grid(row=4,column=0,sticky=W)
        
        email_eny=ttk.Entry(lbf,width=32,textvariable=self.var_eml,font=("arabic",10,"bold"))
        email_eny.grid(row=4,column=1)
        
        #btns for add,update,delete
        fr=Frame(lbf,bd=2,relief=RIDGE)
        fr.place(x=7,y=320,width=390,height=40)
        
        addbtn=Button(fr,text="ADD",command=self.add,font=("arabic",8,"bold"),bg="black",fg="yellow",width=17,height=2)
        addbtn.grid(row=0,column=0)
        
        updbtn=Button(fr,text="UPDATE",command=self.update,font=("arabic",8,"bold"),bg="black",fg="yellow",width=17,height=2)
        updbtn.grid(row=0,column=1)
        
        delbtn=Button(fr,text="DELETE",command=self.dele,font=("arabic",8,"bold"),bg="black",fg="yellow",width=17,height=2)
        delbtn.grid(row=0,column=2) #arya

        
        #labelframe for table search
        
        tbf=LabelFrame(self.root,bd=2,relief=RIDGE,text="SEE DETAILS",font=("arabic",10,"bold"))
        tbf.place(x=440,y=50,width=840,height=490)

        cust_search=Label(tbf,text="Search By ID:",font=("arabic",12,"bold"),fg="green")
        cust_search.grid(row=0,column=0,sticky=W)
        
        #self.var_ser=StringVar()
        #cbx=ttk.Combobox(tbf,textvariable=self.var_ser,font=("arabic",9,"bold"),width=15)
        #cbx["value"]=("ID","Phone no.")
        #cbx.grid(row=0,column=1,padx=2)
        
        self.txt=StringVar()
        txt_eny=ttk.Entry(tbf,textvariable=self.txt,font=("arabic",10,"bold"),width=16)
        txt_eny.grid(row=0,column=1,padx=2)
        
        serbtn=Button(tbf,text="Search",command=self.ser,font=("arabic",10,"bold"),bg="black",fg="yellow",width=12,height=1)
        serbtn.grid(row=0,column=2,padx=2)
        
        shobtn=Button(tbf,text="Show all",command=self.fetch,font=("arabic",10,"bold"),bg="black",fg="yellow",width=12,height=1)
        shobtn.grid(row=0,column=3,padx=2) #vikram
        
        
        #table data
        tb=Frame(tbf,bd=2,relief=RIDGE)
        tb.place(x=0,y=50,width=835,height=400)
        
        scroll_y=ttk.Scrollbar(tb,orient=VERTICAL)
        
        self.cust_det_table=ttk.Treeview(tb,column=("ID","Name","Ph","G","E"),yscrollcommand=scroll_y.set) #makes table
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.cust_det_table.yview)
        
        self.cust_det_table.heading("ID",text="Customer_ID")  #this text will be seen as column name to user
        self.cust_det_table.heading("Name",text="Customer_Name")
        self.cust_det_table.heading("Ph",text="Phoneno")
        self.cust_det_table.heading("G",text="Gender")
        self.cust_det_table.heading("E",text="Email")
        
        self.cust_det_table["show"]="headings"
        
        
        self.cust_det_table.column("ID",width=30)
        self.cust_det_table.column("Name",width=77)
        self.cust_det_table.column("Ph",width=60)
        self.cust_det_table.column("G",width=30)
        self.cust_det_table.column("E",width=77)

        self.cust_det_table.pack(fill=BOTH,expand=1)
        self.cust_det_table.bind("<ButtonRelease-1>",self.getdata) #binds data from table to entry field
        self.fetch()    #samadhan
    
    def add(self):
        if self.var_ph.get()=="" or self.var_eml=="" or self.var_gen=="" or self.var_name=="" or self.var_id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:  #bcoz of try except error is avoided in interpreter
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
                my_cursor=conn.cursor()
                
                #.get() takes the values stored in variable
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s)",(self.var_id.get(),self.var_name.get(),self.var_ph.get(),self.var_gen.get(),self.var_eml.get()))
                conn.commit()
                self.fetch()
                conn.close()
                
                messagebox.showinfo("success","customer has been added",parent=self.root)
                
                
            
            except Exception as es:
                messagebox.showwarning("warning","something went wrong",parent=self.root)
        
    def fetch(self): #to show data in table
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()  #list of tuples
        if len(rows)!=0:
            self.cust_det_table.delete(*self.cust_det_table.get_children())
            for i in rows:
                self.cust_det_table.insert("",END,values=i)  #insert values in table by row
            conn.commit()
            conn.close()    
            
    def getdata(self,event=""): #when we click on data of one row it gets displayed on entry fields
        cursorrow=self.cust_det_table.focus()  #store row of table on which we click
        content=self.cust_det_table.item(cursorrow)       # stores data of that row
        row=content["values"]    #store data of that row in list
        self.var_id.set(row[0])
        self.var_name.set(row[1])
        self.var_ph.set(row[2])
        self.var_gen.set(row[3])
        self.var_eml.set(row[4])

    def update(self):
        if self.var_ph.get()=="":
            messagebox.showerror("Error","mobile no. not entered",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
            my_cursor=conn.cursor() 
            my_cursor.execute("update customer set Customer_Name=%s,Phoneno=%s,Gender=%s,Email=%s where Customer_ID=%s",(self.var_name.get(),self.var_ph.get(),self.var_gen.get(),self.var_eml.get(),self.var_id.get()))
            conn.commit()
            self.fetch()
            conn.close()
            messagebox.showinfo("Updated","Details Updated",parent=self.root)
            
    def dele(self):
        dele=messagebox.askyesno("canteen management","do you want to delete",parent=self.root)
        if dele>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
            my_cursor=conn.cursor()
            
            query="delete from customer where Customer_ID=%s"
            values=(self.var_id.get(),)
            my_cursor.execute(query,values)
            
        else:
            if not dele:
                return
        
        
        conn.commit()
        self.fetch()
        conn.close()

    def ser(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
        my_cursor=conn.cursor()
        
        qu="select * from customer where Customer_ID=%s"
        val=(self.txt.get(),)
        my_cursor.execute(qu,val)
        
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.cust_det_table.delete(*self.cust_det_table.get_children())
            for i in row:
                self.cust_det_table.insert("",END,values=i)
            conn.commit()
            conn.close()

















if __name__=="__main__":
    root=Tk()
    obj1=cust_win(root)
    root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from noofitems import itemno_win

class order_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Canteen management System")
        self.root.geometry("1480x720+40+40")
        
        self.p1=StringVar()
        self.p2=StringVar()
        self.p3=StringVar()
        self.p4=StringVar()
        self.p5=StringVar()
        self.tp=StringVar()
        
        self.id=StringVar()
        
        self.it1=StringVar()
        self.it2=StringVar()
        self.it3=StringVar()
        self.it4=StringVar()
        self.it5=StringVar()
        
        ti=Label(self.root,text="ORDER DETAILS",bg="black",fg="red",font=("arabic",18,"bold"))
        ti.place(x=0,y=0,width=1500,height=30)  
        
        lbf=LabelFrame(self.root,bd=2,relief=RIDGE,text="ORDER DETAILS",padx=2,font=("arabic",10,"bold"))
        lbf.place(x=1090,y=40,width=375,height=655)
        
        #full right side frame
        cust_id=Label(lbf,text="Customer ID : ",font=("arabic",10,"bold"),padx=2,pady=15)
        cust_id.grid(row=0,column=0,sticky=W)
        
        id_eny=ttk.Entry(lbf,width=32,textvariable=self.id,font=("arabic",10,"bold"))
        id_eny.grid(row=0,column=1,padx=5)
        
        it1_name=Label(lbf,text="Item 1 : ",font=("arabic",10,"bold"),padx=2,pady=12)
        it1_name.grid(row=1,column=0,sticky=W)
        
        it1_eny=ttk.Entry(lbf,width=32,textvariable=self.it1,font=("arabic",10,"bold"))
        it1_eny.grid(row=1,column=1)
        
        p1_name=Label(lbf,text="Price 1 : ",font=("arabic",10,"bold"),padx=2,pady=12)
        p1_name.grid(row=2,column=0,sticky=W)
        
        p1_eny=ttk.Entry(lbf,width=32,textvariable=self.p1,font=("arabic",10,"bold"))
        p1_eny.grid(row=2,column=1)
        
        it2_name=Label(lbf,text="Item 2 : ",font=("arabic",10,"bold"),padx=2,pady=12)
        it2_name.grid(row=3,column=0,sticky=W)
        
        it2_eny=ttk.Entry(lbf,width=32,textvariable=self.it2,font=("arabic",10,"bold"))
        it2_eny.grid(row=3,column=1)
        
        p2_name=Label(lbf,text="Price 2 : ",font=("arabic",10,"bold"),padx=2,pady=12)
        p2_name.grid(row=4,column=0,sticky=W)
        
        p2_eny=ttk.Entry(lbf,width=32,textvariable=self.p2,font=("arabic",10,"bold"))
        p2_eny.grid(row=4,column=1)
        
        it3_name=Label(lbf,text="Item 3 : ",font=("arabic",10,"bold"),padx=2,pady=12)
        it3_name.grid(row=5,column=0,sticky=W)
        
        it3_eny=ttk.Entry(lbf,width=32,textvariable=self.it3,font=("arabic",10,"bold"))
        it3_eny.grid(row=5,column=1)
        
        p3_name=Label(lbf,text="Price 3 : ",font=("arabic",10,"bold"),padx=2,pady=12)
        p3_name.grid(row=6,column=0,sticky=W)
        
        p3_eny=ttk.Entry(lbf,width=32,textvariable=self.p3,font=("arabic",10,"bold"))
        p3_eny.grid(row=6,column=1)
        
        it4_name=Label(lbf,text="Item 4 : ",font=("arabic",10,"bold"),padx=2,pady=12)
        it4_name.grid(row=7,column=0,sticky=W)
        
        it4_eny=ttk.Entry(lbf,width=32,textvariable=self.it4,font=("arabic",10,"bold"))
        it4_eny.grid(row=7,column=1)
        
        p4_name=Label(lbf,text="Price 4 : ",font=("arabic",10,"bold"),padx=2,pady=12)
        p4_name.grid(row=8,column=0,sticky=W)
        
        p4_eny=ttk.Entry(lbf,width=32,textvariable=self.p4,font=("arabic",10,"bold"))
        p4_eny.grid(row=8,column=1)
        
        it5_name=Label(lbf,text="Item 5 : ",font=("arabic",10,"bold"),padx=2,pady=12)
        it5_name.grid(row=9,column=0,sticky=W)
        
        it5_eny=ttk.Entry(lbf,width=32,textvariable=self.it5,font=("arabic",10,"bold"))
        it5_eny.grid(row=9,column=1)
        
        p5_name=Label(lbf,text="Price 5 : ",font=("arabic",10,"bold"),padx=2,pady=12)
        p5_name.grid(row=10,column=0,sticky=W)
        
        p5_eny=ttk.Entry(lbf,width=32,textvariable=self.p5,font=("arabic",10,"bold"))
        p5_eny.grid(row=10,column=1)
        
        tp_name=Label(lbf,text="Total Price : ",font=("arabic",10,"bold"),padx=2,pady=9)
        tp_name.grid(row=11,column=0,sticky=W)
        
        tp_eny=ttk.Entry(lbf,width=32,textvariable=self.tp,font=("arabic",10,"bold"))
        tp_eny.grid(row=11,column=1)
        
        ib=Button(lbf,text="Enternoofitem",command=self.item_det,width=13,font=("arabic",15,"bold"),bg="black",fg="blue",bd=0,cursor="hand2")
        ib.grid(row=12,column=0,padx=10)
        
        fr=Frame(lbf,bd=2,relief=RIDGE)
        fr.place(x=7,y=580,width=350,height=40)
        
        addbtn=Button(fr,text="ADD",command=self.add2,font=("arabic",8,"bold"),bg="black",fg="blue",width=13,height=2)
        addbtn.grid(row=0,column=0)
        
        updbtn=Button(fr,text="UPDATE",command=self.update2,font=("arabic",8,"bold"),bg="black",fg="blue",width=13,height=2)
        updbtn.grid(row=0,column=1)
        
        delbtn=Button(fr,text="DELETE",command=self.dele2,font=("arabic",8,"bold"),bg="black",fg="blue",width=13,height=2)
        delbtn.grid(row=0,column=2) 
        
        tbb=Button(fr,text="tot",command=self.tt,font=("arabic",8,"bold"),bg="black",fg="blue",width=5,height=2)
        tbb.grid(row=0,column=3)
        
        
        #tabel
        
        tb=Frame(self.root,bd=2,relief=RIDGE)
        tb.place(x=20,y=70,width=1050,height=580)
        
        scroll_x=ttk.Scrollbar(tb,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tb,orient=VERTICAL)
        
        self.order_det_table=ttk.Treeview(tb,column=("Id","i1","p1","i2","p2","i3","p3","i4","p4","i5","p5","tp"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) #makes table
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.order_det_table.xview)
        scroll_y.config(command=self.order_det_table.yview)
        
        
        self.order_det_table.heading("Id",text="Customer Id")  #this text will be seen as column name to user
        self.order_det_table.heading("i1",text="item1")
        self.order_det_table.heading("p1",text="price1")
        self.order_det_table.heading("i2",text="item2")
        self.order_det_table.heading("p2",text="price2")
        self.order_det_table.heading("i3",text="item3")
        self.order_det_table.heading("p3",text="price3")
        self.order_det_table.heading("i4",text="item4")
        self.order_det_table.heading("p4",text="price4")
        self.order_det_table.heading("i5",text="item5")
        self.order_det_table.heading("p5",text="price5")
        self.order_det_table.heading("tp",text="TotalPrice")  
        
        
        self.order_det_table["show"]="headings"
        
        self.order_det_table.column("Id",width=50)
        self.order_det_table.column("i1",width=20)
        self.order_det_table.column("p1",width=40)
        self.order_det_table.column("i2",width=40)
        self.order_det_table.column("p2",width=40)
        self.order_det_table.column("i3",width=40)
        self.order_det_table.column("p3",width=40)
        self.order_det_table.column("i4",width=40)
        self.order_det_table.column("p4",width=40)
        self.order_det_table.column("i5",width=40)
        self.order_det_table.column("p5",width=40)
        self.order_det_table.column("tp",width=40)
        
       
        self.order_det_table.pack(fill=BOTH,expand=1)
        self.order_det_table.bind("<ButtonRelease-1>",self.getdata2) #binds data from table to entry field
        self.fetch2()  #here if table is empty it will show error
        
        
        
        
    def add2(self):   
        if self.it1.get()=="" or self.it2.get()=="" or self.it3.get()=="" or self.it4.get()=="" or self.it5.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:  #bcoz of try except error is avoided in interpreter
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
                my_cursor=conn.cursor()
                
                #.get() takes the values stored in variable
                my_cursor.execute("insert into odr (custid,ia,pa,ib,pb,ic,pc,id,pd,ie,pe,tp) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.id.get(),self.it1.get(),self.p1.get(),self.it2.get(),self.p2.get(),self.it3.get(),self.p3.get(),self.it4.get(),self.p4.get(),self.it5.get(),self.p5.get(),self.tp.get()))
                conn.commit()
                self.fetch2()
                conn.close()
                
                messagebox.showinfo("success","item has been added",parent=self.root)
                
                
            
            except Exception as es:
                messagebox.showwarning("warning","something went wrong",parent=self.root)
           
    def fetch2(self): #to show data in gui table
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from odr")
        rows=my_cursor.fetchall()  #list of tuples
        if len(rows)!=0:
            self.order_det_table.delete(*self.order_det_table.get_children())
            for i in rows:
                self.order_det_table.insert("",END,values=i)  #insert values in table by row
            conn.commit()
            conn.close()   
    
    
    def update2(self):
        if self.p1.get()=="":
            messagebox.showerror("Error","price not entered",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
            my_cursor=conn.cursor()
             
            my_cursor.execute("update odr set ia=%s,ib=%s,ic=%s,id=%s,ie=%s,pa=%s,pb=%s,pc=%s,pd=%s,pe=%s,tp=%s where custid=%s",(self.it1.get(),self.it2.get(),self.it3.get(),self.it4.get(),self.it5.get(),self.p1.get(),self.p2.get(),self.p3.get(),self.p4.get(),self.p5.get(),self.tp.get(),self.id.get()))
            conn.commit()
            self.fetch2()
            conn.close()
            messagebox.showinfo("Updated","Details Updated",parent=self.root)
    
            
    def dele2(self):
        dele=messagebox.askyesno("canteen management","do you want to delete",parent=self.root)
        if dele>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
            my_cursor=conn.cursor()
             
            query="delete from odr where custid=%s"
            values=(self.id.get(),)
            my_cursor.execute(query,values)
        
        else:
            if not dele:
                return
        
        
        conn.commit()
        self.fetch2()
        conn.close()
        
    def getdata2(self,event=""): #when we click on data of one row it gets displayed on entry fields
        cursorrow=self.order_det_table.focus()  #store row of table on which we click
        content=self.order_det_table.item(cursorrow)       # stores data of that row
        row=content["values"]    #store data of that row in list
        self.id.set(row[0])
        self.it1.set(row[1])
        self.p1.set(row[2])
        self.it2.set(row[3])
        self.p2.set(row[4])
        self.it3.set(row[5])     
        self.p3.set(row[6]) 
        self.it4.set(row[7])    
        self.p4.set(row[8])   
        self.it5.set(row[9])  
        self.p5.set(row[10]) 
        self.tp.set(row[11])
        
    def tt(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="canteen_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from odr")
        row=my_cursor.fetchall()  #list of tuples
        a=int(self.p1.get())
        b=int(self.p2.get())
        c=int(self.p3.get())
        d=int(self.p4.get())
        e=int(self.p5.get())
        
        sum=0
        for i in row:
            cs=self.id.get()
            if (cs==i[0]):
                sum=a*int(i[12])+b*int(i[13])+c*int(i[14])+d*int(i[15])+e*int(i[16])
            
        self.tp.set(sum)
        
        

    def item_det(self):
        self.itemno_new=Toplevel(self.root)
        self.itno=itemno_win(self.itemno_new)
        
        
   
        
        
        
        
        
        
        

if __name__=="__main__":
    root=Tk()
    obj=order_win(root)
    root.mainloop()
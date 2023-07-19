from tkinter import *
from PIL import Image,ImageTk
from cust import cust_win
from menu import menu_win
from order import order_win

class Canteenmanagement:
    def __init__(self,root): #constructor
        self.root=root
        self.root.title("Canteen management System")
        self.root.geometry("1550x800+0+0")
        
        
        #image
        img=Image.open("img1.jpg")
        img=img.resize((1550,800),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        l=Label(self.root,image=self.photoimg,bd=4,relief=RIDGE)
        l.place(x=0,y=0,width=1550,height=800)
        
        #title
        lb=Label(self.root,text="CANTEEN MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="white",fg="red",bd=4,relief=RIDGE)
        lb.place(x=0,y=0,width=1550,height=50)
        
        #main_frame
        mainfr=Frame(self.root,bd=4,relief=RIDGE)
        mainfr.place(x=980,y=280,width=550,height=165)
        
        #customerbtn
        cb=Button(mainfr,text="CUSTOMER",command=self.cust_det,width=33,font=("times new roman",20,"bold"),bg="white",fg="red",bd=0,cursor="hand2")
        cb.grid(row=0,column=0,pady=1) #ayush
        
        
        #menubtn
        mb=Button(mainfr,text="MENU",command=self.menu_det,width=33,font=("times new roman",20,"bold"),bg="white",fg="red",bd=0,cursor="hand2")
        mb.grid(row=1,column=0,pady=1)
        
        #orderbtn
        ob=Button(mainfr,text="ORDER",command=self.order_det,width=33,font=("times new roman",20,"bold"),bg="white",fg="red",bd=0,cursor="hand2")
        ob.grid(row=2,column=0,pady=1)
        
        
    def cust_det(self):
        self.cust_new=Toplevel(self.root)
        self.add=cust_win(self.cust_new)
    
    def menu_det(self):
        self.menu_new=Toplevel(self.root)
        self.show=menu_win(self.menu_new)
        
    def order_det(self):
        self.order_new=Toplevel(self.root)
        self.order=order_win(self.order_new)
    
        
        
                
        

if __name__=="__main__":
    root=Tk()
    obj=Canteenmanagement(root)
    root.mainloop()
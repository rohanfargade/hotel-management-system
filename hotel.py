from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Roombooking

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

            #main bg
        img1=Image.open(r"E:\Rohan_project\Hotel_management\images\hotelbgmain.jpg")
        img1=img1.resize((1550,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=200)

            #logo
        img2=Image.open(r"E:\Rohan_project\Hotel_management\images\logo1.png")
        img2=img2.resize((230,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=200)


            #title
        lbl_title=Label(self.root,text="TRIOSTAY HOTELS",font=("woodcut",36),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=200,width=1550,height=70)

            #main frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=250,width=1550,height=620)

            #menu
        lbl_menu=Label(main_frame,text="MENU",font=("french script mt",20,"italic","bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

            # buttons
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=240)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=19,font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        cust_btn=Button(btn_frame,text="ROOM",width=19,command=self.roombooking,font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,cursor="hand1")
        cust_btn.grid(row=1,column=0,pady=1)

        cust_btn=Button(btn_frame,text="DETAILS",width=19,font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,cursor="hand1")
        cust_btn.grid(row=2,column=0,pady=1)

        cust_btn=Button(btn_frame,text="REPORT",width=19,font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,cursor="hand1")
        cust_btn.grid(row=3,column=0,pady=1)

        cust_btn=Button(btn_frame,text="LOGOUT",width=19,font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,cursor="hand1")
        cust_btn.grid(row=4,column=0,pady=1)


        # right side image

        img3=Image.open(r"E:\Rohan_project\Hotel_management\images\img3(1).jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=230,y=250,width=1310,height=590)

        # down images

        img4=Image.open(r"E:\Rohan_project\Hotel_management\images\img4.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=550,width=230,height=210)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

        
        
if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()


    
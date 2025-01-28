from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")
        self.root.geometry("1550x800+0+0")

                #   var

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",36),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=50)
        
        
        img2=Image.open(r"E:\Rohan_project\Hotel_management\images\logo1.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("arial",15,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=530,height=600)

        lbl_cust_contact=Label(labelframeleft,text="Customer Contact :",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(labelframeleft,testvariable=self.var_contact,font=("arial",15,"bold"),width=29)
        enty_contact.grid(row=0,column=1)

        # fetch data
        btnFetchData=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnFetchData.place(x=420,y=4)

        # buttons

        check_in_date=Label(labelframeleft,text="Check In :",font=("arial",15,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,testvariable=self.var_checkin,font=("arial",15,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        lbl_Check_out=Label(labelframeleft,text="Check Out :",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,testvariable=self.var_checkout,font=("arial",15,"bold"),width=29)
        txt_Check_out.grid(row=2,column=1)
#from here
        label_RoomType=Label(labelframeleft,font=("arial",15,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType=ttk.Combobox(labelframeleft,testvariable=self.var_roomtype,font=("arial",15,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)


        #Available Room
        lblRoomAvailable=Label(labelframeleft,font=("arial",15,"bold"),text="Available room:",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,testvariable=self.var_roomavailable,font=("arial",15,"bold"),width=29)
        txtRoomAvailable.grid(row=4,column=1)


        #Meal
        lblMeal=Label(labelframeleft,font=("arial",15,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,testvariable=self.var_meal,font=("arial",15,"bold"),width=29)
        txtMeal.grid(row=5,column=1)


        # No Of Days
        lblNoOfDays=Label(labelframeleft,font=("arial",15,"bold"),text="No Of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,testvariable=self.var_noofdays,font=("arial",15,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)


        # Paid tax
        lblNoOfDays=Label(labelframeleft,font=("arial",15,"bold"),text="Paid tax:",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,testvariable=self.var_paidtax,font=("arial",15,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)


        # Sub Total
        lblNoOfDays=Label(labelframeleft,font=("arial",15,"bold"),text="Sub Total:",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,testvariable=self.var_total,font=("arial",15,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)


        # Total Cost
        lblIdNumber=Label(labelframeleft,font=("arial",15,"bold"),text="Total Cost:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,testvariable=self.var_actualtotal,font=("arial",15,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        btnBill = Button(labelframeleft, text="Bill",  font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1)

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=480,width=775,height=40)

        btnAdd = Button(btn_frame, text="ADD",  font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",  font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        #right side image
        '''
        img6=Image.open(r"E:\Rohan_project\Hotel_management\images\hotelbgmain.jpg")
        img6=img6.resize((930,250),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        lblimg=Label(self.root,image=self.photoimg6,bd=4,relief=RIDGE)
        lblimg.place(x=550,y=50,width=930,height=250,pady=4)  '''

        # table frame starts here

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search system", font=("arial", 15, "bold"), padx=2)
        Table_Frame.place(x=550,y=50,width=930,height=600)

        lblSearchBy = LabelFrame(Table_Frame, font=("arial", 15, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        combo_id = ttk.Combobox(Table_Frame, font=("arial", 15, "bold"), width=24, state="readonly")
        combo_id["values"] = ("Select", "Contact", "Room")
        combo_id.current(0)
        combo_id.grid(row=0, column=1, padx=2)

        txtSearch = ttk.Entry(Table_Frame, font=("arial", 15, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", font=("arial", 15, "bold"), bg="black", fg="gold", width=6)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", font=("arial", 15, "bold"), bg="black", fg="gold", width=8)
        btnShowAll.grid(row=0, column=4, padx=1)
        

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0,y=50,width=1020,height=450)


        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("contact", "checkindate", "checkoutdate", "roomtype", "roomavailable", "meal", "noofdays"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("contact", text="Contact")
        self.Cust_Details_Table.heading("checkindate", text="Check-in")
        self.Cust_Details_Table.heading("checkoutdate", text="Check-out")
        self.Cust_Details_Table.heading("roomtype", text="Room Type")
        self.Cust_Details_Table.heading("roomavailable", text="Room Available")
        self.Cust_Details_Table.heading("meal", text="Meal")
        self.Cust_Details_Table.heading("noofdays", text="NoOfDays")
        

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)

        self.Cust_Details_Table.heading("contact", text="Contact")
        self.Cust_Details_Table.heading("checkindate", text="Check-in")
        self.Cust_Details_Table.heading("checkoutdate", text="Check-out")
        self.Cust_Details_Table.heading("roomtype", text="Room Type")
        self.Cust_Details_Table.heading("roomavailable", text="Room Available")
        self.Cust_Details_Table.heading("meal", text="Meal")
        self.Cust_Details_Table.heading("noofdays", text="NoOfDays")

        #self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter the Contact Number.",parent=self.root())
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            query=("select name from customer where Mobile=%s")
            value=(self.var_contact.get())
            my_cursor.execute(query,value)
            

   







if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        self.root.geometry("1550x800+0+0")
        
        # Variables
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()

        # Title
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 36), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=50)

        # Logo
        img2 = Image.open(r"E:\Rohan_project\Hotel_management\images\logo1.png")  # Update the path to your logo image
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        # Label Frame for Customer Details
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",15,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=510,height=600)

        #5-----------------------------
        #===========================labels and entries=========================
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref :",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelframeleft,self.var_ref.set(str(x)),font=("arial",15,"bold"),width=29)
        enty_ref.grid(row=0,column=1)

        #=========================cust name===================================
        cname=Label(labelframeleft,text="Customer name :",font=("arial",15,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",15,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        #=========================mother name==================================
        lblmname=Label(labelframeleft,text="Mother name :",font=("arial",15,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("arial",15,"bold"),width=29)
        txtcname.grid(row=2,column=1)

        #==========================gender combobox===================================
        label_gender=Label(labelframeleft,text="Gender :",font=("arial",15,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",15,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Select","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)



        #=======================postcode==============================================
        lblPostCode=Label(labelframeleft,text="Post Code :",font=("arial",15,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",15,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        #===============================mobile number==============================
        lblMobile=Label(labelframeleft,text="Mobile No. :",font=("arial",15,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",15,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        #=============================email======================================
        lblEmail=Label(labelframeleft,text="Email :",font=("arial",15,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",15,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        #============================nationality============================
        lblNationality=Label(labelframeleft,text="Nationality :",font=("arial",15,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",15,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Select","Indian","American","Russian")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        #==========================idproof===============================
        lblIdProof=Label(labelframeleft,text="ID Proof :",font=("arial",15,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",15,"bold"),width=27,state="readonly")
        combo_id["value"]=("Select","Adhaar card","Licence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #=============================idnumber=============================
        lblIdNumber=Label(labelframeleft,text="Id Number:",font=("arial",15,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",15,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        #==================address=======================================
        lblAddress=Label(labelframeleft,text="Address:",font=("arial",15,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",15,"bold"),width=29)
        txtAddress.grid(row=10,column=1)
        
        """labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("arial", 15, "bold"), padx=2)
        labelframeleft.place(x=20,y=100,width=425,height=490)

        # Labels and Entries 
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref:", textvariable=self.var_ref, font=("arial", 15, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        enty_ref = ttk.Entry(labelframeleft, font=("arial", 15, "bold"), width=29,state="readonly")
        enty_ref.grid(row=0, column=1)

        # Customer Name 
        cname = Label(labelframeleft, text="Customer Name:",textvariable=self.var_cust_name,  font=("arial", 15, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, font=("arial", 15, "bold"), width=29)
        txtcname.grid(row=1, column=1)

        # Mother Name  
        lblmname = Label(labelframeleft, text="Mother Name:", textvariable=self.var_mother,font=("arial", 15, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft, font=("arial", 15, "bold"), width=29)
        txtmname.grid(row=2, column=1)

        # Gender   
        label_gender = Label(labelframeleft, text="Gender:",textvariable=self.var_gender, font=("arial", 15, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, font=("arial", 15, "bold"), width=27, state="readonly")
        combo_gender["values"] = ("Select", "Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Postcode  
        lblPostCode = Label(labelframeleft, text="Post Code:", textvariable=self.var_post,font=("arial", 15, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelframeleft, font=("arial", 15, "bold"), width=29)
        txtPostCode.grid(row=4, column=1)

        # Mobile Number  
        lblMobile = Label(labelframeleft, text="Mobile No.:",textvariable=self.var_mobile, font=("arial", 15, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft, font=("arial", 15, "bold"), width=29)
        txtMobile.grid(row=5, column=1)

        # Email  
        lblEmail = Label(labelframeleft, text="Email:",textvariable=self.var_email, font=("arial", 15, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft, font=("arial", 15, "bold"), width=29)
        txtEmail.grid(row=6, column=1)

        # Nationality 
        lblNationality = Label(labelframeleft, text="Nationality:", textvariable=self.var_nationality, font=("arial", 15, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        combo_Nationality = ttk.Combobox(labelframeleft, font=("arial", 15, "bold"), width=27, state="readonly")
        combo_Nationality["values"] = ("Select", "Indian", "American", "Russian")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        # ID Proof 
        lblIdProof = Label(labelframeleft, text="ID Proof:", textvariable=self.var_id_proof, font=("arial", 15, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)
        combo_id = ttk.Combobox(labelframeleft, font=("arial", 15, "bold"), width=27, state="readonly")
        combo_id["values"] = ("Select", "Adhaar card", "Licence", "Passport")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # ID Number 
        lblIdNumber = Label(labelframeleft, text="ID Number:",textvariable=self.var_id_number,  font=("arial", 15, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, font=("arial", 15, "bold"), width=29)
        txtIdNumber.grid(row=9, column=1)

        # Address 
        lblAddress = Label(labelframeleft, text="Address:", textvariable=self.var_address, font=("arial", 15, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft, font=("arial", 15, "bold"), width=29)
        txtAddress.grid(row=10, column=1)"""

        # Buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=480,width=775,height=40)

        btnAdd = Button(btn_frame, text="ADD", command=self.add_data, font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # Table Frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search system", font=("arial", 15, "bold"), padx=2)
        Table_Frame.place(x=520,y=50,width=1020,height=600)

        lblSearchBy = LabelFrame(Table_Frame, font=("arial", 15, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        combo_id = ttk.Combobox(Table_Frame, font=("arial", 15, "bold"), width=24, state="readonly")
        combo_id["values"] = ("Select", "Mobile No", "Ref")
        combo_id.current(0)
        combo_id.grid(row=0, column=1, padx=2)

        txtSearch = ttk.Entry(Table_Frame, font=("arial", 15, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", font=("arial", 15, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Show Data Table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0,y=50,width=1020,height=450)


        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="Post Code")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="ID Proof")
        self.Cust_Details_Table.heading("idnumber", text="ID Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.heading("name",width=100)
        self.Cust_Details_Table.heading("mother",width=100)
        self.Cust_Details_Table.heading("gender",width=100)
        self.Cust_Details_Table.heading("post",width=100)
        self.Cust_Details_Table.heading("mobile",width=100)
        self.Cust_Details_Table.heading("email",width=100)
        self.Cust_Details_Table.heading("nationality",width=100)
        self.Cust_Details_Table.heading("idproof",width=100)
        self.Cust_Details_Table.heading("idnumber",width=100)
        self.Cust_Details_Table.heading("address",width=100)
        #self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_mother.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_id_proof.get(),
                                                                                    self.var_id_number.get(),
                                                                                    self.var_address.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,idnumber=%s,Address=%s where Ref=%s", (
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details updated successfully", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="management")
            my_cursor = conn.cursor()
            query = "delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()

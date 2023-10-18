from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self ,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("%dx%d+%d+%d" % (1350, 650, int(0), int(0)))

# ===============================================variable======================================================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.Dateborrowed_var = StringVar()
        self.Datedue_var = StringVar()
        self.Daysonbook_var = StringVar()
        self.Latereturnfine_var = StringVar()
        self.Dateoverdue_var = StringVar()
        self.Finalprice_var = StringVar()



        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=15,relief="ridge",font=("times new roman",40,"bold"),pady=2,padx=2)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=10,relief="ridge",padx=15,bg="powder blue")
        frame.place(x=0,y=100,width=1430,height=330,)

    #====================dataframeleft=============================================================

        DataFrameLeft=LabelFrame(frame,text="Library Membership information",bg="powder blue",fg="green",bd=8,relief="ridge",font=("times new roman",10,"bold"))
        DataFrameLeft.place(x=0,y=5,width=800,height=310)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=2)
        lblMember.grid(row=0,column=0,sticky="w")

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",15,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN NO:", font=("times new roman", 15, "bold"),padx=2, pady=2)
        lblPRN_No.grid(row=1, column=0, sticky="w")
        txtPRN_NO=Entry(DataFrameLeft,textvariable=self.prn_var,font=("times new roman",15,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblID_No = Label(DataFrameLeft, bg="powder blue", text="ID NO:", font=("times new roman", 15, "bold"), padx=2,
                          pady=2)
        lblID_No.grid(row=2, column=0, sticky="w")
        txtID_NO = Entry(DataFrameLeft,textvariable=self.id_var, font=("times new roman", 15, "bold"), width=29)
        txtID_NO.grid(row=2, column=1)

        lblFname = Label(DataFrameLeft, bg="powder blue", text="FirstName:", font=("times new roman", 15, "bold"), padx=2,
                         pady=2)
        lblFname.grid(row=3, column=0, sticky="w")
        txtFname = Entry(DataFrameLeft,textvariable=self.firstname_var, font=("times new roman", 15, "bold"), width=29)
        txtFname.grid(row=3, column=1)

        lblLname = Label(DataFrameLeft, bg="powder blue", text="LastName:", font=("times new roman", 15, "bold"),
                         padx=2,
                         pady=2)
        lblLname.grid(row=4, column=0, sticky="w")
        txtLname = Entry(DataFrameLeft,textvariable=self.lastname_var, font=("times new roman", 15, "bold"), width=29)
        txtLname.grid(row=4, column=1)

        lbladd1 = Label(DataFrameLeft, bg="powder blue", text="Address1:", font=("times new roman", 15, "bold"),
                         padx=2,
                         pady=2)
        lbladd1.grid(row=5, column=0, sticky="w")
        txtadd1 = Entry(DataFrameLeft,textvariable=self.address1_var, font=("times new roman", 15, "bold"), width=29)
        txtadd1.grid(row=5, column=1)

        lbladd2 = Label(DataFrameLeft, bg="powder blue", text="Address2:", font=("times new roman", 15, "bold"),
                        padx=2,
                        pady=2)
        lbladd2.grid(row=6, column=0, sticky="w")
        txtadd2 = Entry(DataFrameLeft,textvariable=self.address2_var, font=("times new roman", 15, "bold"), width=29)
        txtadd2.grid(row=6, column=1)

        lblpostalcode = Label(DataFrameLeft, bg="powder blue", text="Postalcode:", font=("times new roman", 15, "bold"),
                        padx=2,
                        pady=2)
        lblpostalcode.grid(row=7, column=0, sticky="w")
        txtpostalcode = Entry(DataFrameLeft,textvariable=self.postcode_var, font=("times new roman", 15, "bold"), width=29)
        txtpostalcode.grid(row=7, column=1)

        lblmobile = Label(DataFrameLeft, bg="powder blue", text="Mobile:", font=("times new roman", 15, "bold"),
                              padx=2,
                              pady=2)
        lblmobile.grid(row=8, column=0, sticky="w")
        txtmobile = Entry(DataFrameLeft,textvariable=self.mobile_var, font=("times new roman", 15, "bold"), width=29)
        txtmobile.grid(row=8, column=1)

        lblbookid = Label(DataFrameLeft, bg="powder blue", text="Book id:", font=("times new roman", 15, "bold"),
                          padx=2,
                          pady=2)
        lblbookid.grid(row=0, column=2, sticky="w")
        txtbookid = Entry(DataFrameLeft,textvariable=self.bookid_var, font=("times new roman", 15, "bold"), width=22)
        txtbookid.grid(row=0, column=3)

        lblbooktitle = Label(DataFrameLeft, bg="powder blue", text="Book title:", font=("times new roman", 15, "bold"),
                     padx=2,
                     pady=2)
        lblbooktitle.grid(row=1, column=2, sticky="w")
        txtbooktitle = Entry(DataFrameLeft,textvariable=self.booktitle_var, font=("times new roman", 15, "bold"), width=22)
        txtbooktitle.grid(row=1, column=3)

        lblauthorname = Label(DataFrameLeft, bg="powder blue", text="Author:", font=("times new roman", 15, "bold"),
                             padx=2,
                             pady=2)
        lblauthorname.grid(row=2, column=2, sticky="w")
        txtauthorname = Entry(DataFrameLeft,textvariable=self.author_var, font=("times new roman", 15, "bold"), width=22)
        txtauthorname.grid(row=2, column=3)

        lblissue = Label(DataFrameLeft, bg="powder blue", text="Issue Date:", font=("times new roman", 15, "bold"),
                              padx=2,
                              pady=2)
        lblissue.grid(row=3, column=2, sticky="w")
        txtissue = Entry(DataFrameLeft,textvariable=self.Dateborrowed_var, font=("times new roman", 15, "bold"), width=22)
        txtissue.grid(row=3, column=3)

        lbldatedue = Label(DataFrameLeft, bg="powder blue", text="Date Due:", font=("times new roman", 15, "bold"),
                         padx=2,
                         pady=2)
        lbldatedue.grid(row=4, column=2, sticky="w")
        txtdatedue = Entry(DataFrameLeft,textvariable=self.Datedue_var, font=("times new roman", 15, "bold"), width=22)
        txtdatedue.grid(row=4, column=3)

        lbldaysonbook = Label(DataFrameLeft, bg="powder blue", text="Days on book:", font=("times new roman", 15, "bold"),
                           padx=2,
                           pady=2)
        lbldaysonbook.grid(row=5, column=2, sticky="w")
        txtdaysonbook = Entry(DataFrameLeft,textvariable=self.Daysonbook_var, font=("times new roman", 15, "bold"), width=22)
        txtdaysonbook.grid(row=5, column=3)

        lbllatefine = Label(DataFrameLeft, bg="powder blue", text="Late fine:",
                              font=("times new roman", 15, "bold"),
                              padx=2,
                              pady=2)
        lbllatefine.grid(row=6, column=2, sticky="w")
        txtlatefine = Entry(DataFrameLeft,textvariable=self.Latereturnfine_var, font=("times new roman", 15, "bold"), width=22)
        txtlatefine.grid(row=6, column=3)

        lbldateoverdue = Label(DataFrameLeft, bg="powder blue", text="Date over due:",
                            font=("times new roman", 15, "bold"),
                            padx=2,
                            pady=2)
        lbldateoverdue.grid(row=7, column=2, sticky="w")
        txtdateoverdue = Entry(DataFrameLeft,textvariable=self.Dateoverdue_var, font=("times new roman", 15, "bold"), width=22)
        txtdateoverdue.grid(row=7, column=3)

        lblactualprice = Label(DataFrameLeft, bg="powder blue", text="Actual Price:",
                               font=("times new roman", 15, "bold"),
                               padx=2,
                               pady=2)
        lblactualprice.grid(row=8, column=2, sticky="w")
        txtactualprice = Entry(DataFrameLeft,textvariable=self.Finalprice_var, font=("times new roman", 15, "bold"), width=22)
        txtactualprice.grid(row=8, column=3)

#================================== Dataframe right ==============================================================

        DataFrameRight = LabelFrame(frame, text="Book details", bg="powder blue", fg="green", bd=8,
                                   relief="ridge", font=("times new roman", 10, "bold"))
        DataFrameRight.place(x=800, y=5, width=510, height=310)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=15,padx=2,pady=2)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head firt book','Learn Python The Hard Way','Python Programming','Secrete Rahshy','Python CookBook','Into to machine Lear','Machine techno','My Python','Joss Ellif Guru',
                 'Elite jungle python','Hadoop with python','Python for everybody','Effective python','Python in Education','Jungli python','Machine python','Advance Python','Inton python','Redchilli','Ishq Python']


        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection))
            x=value
            if (x=="Head firt book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Dateborrowed_var.set(d1)
                self.Datedue_var.set(d3)
                self.Daysonbook_var.set(15)
                self.Latereturnfine_var.set("Rs.50")
                self.Dateoverdue_var.set("NO")
                self.Finalprice_var.set("Rs.788")


        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

#==================================Buttons frame ==================================================================
        Framebutton = Frame(self.root, bd=10, relief="ridge", padx=15, bg="powder blue")
        Framebutton.place(x=0, y=430, width=1430, height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnshowdata = Button(Framebutton, text="Show Data", font=("arial", 12, "bold"), width=21, bg="blue", fg="white")
        btnshowdata.grid(row=0, column=1)

        btnupdatedata = Button(Framebutton, text="Update Data", font=("arial", 12, "bold"), width=21, bg="blue", fg="white")
        btnupdatedata.grid(row=0, column=2)

        btndeletedata = Button(Framebutton, text="Delete Data", font=("arial", 12, "bold"), width=21, bg="blue", fg="white")
        btndeletedata.grid(row=0, column=3)

        btnresetdata = Button(Framebutton, text="Reset Data", font=("arial", 12, "bold"), width=21, bg="blue", fg="white")
        btnresetdata.grid(row=0, column=4)

        btnexit = Button(Framebutton, text="Exit", font=("arial", 12, "bold"), width=21, bg="blue", fg="white")
        btnexit.grid(row=0, column=5)

# ============================Information Frame ======================================================================================

        FrameDetails = Frame(self.root, bd=10, relief="ridge", padx=15, bg="powder blue")
        FrameDetails.place(x=0, y=500, width=1430, height=150)

        Table_frame=Frame(self.root,bd=5, relief="ridge", bg="powder blue")
        Table_frame.place(x=2, y=510, width=1350, height=140)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)



        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2",
                                                            "postid","mobile","bookid","booktitle","author","Dateborrowed","Datedue","Days",
                                                            "Latereturnfine","Dateoverdue","Finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill='x')
        yscroll.pack(side=RIGHT, fill='y')

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post Id")
        self.library_table.heading("mobile", text="Moblie Number")
        self.library_table.heading("bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("Dateborrowed", text="Date of Borrowed")
        self.library_table.heading("Datedue", text="Date Due")
        self.library_table.heading("Days", text="DaysOnBook")
        self.library_table.heading("Latereturnfine", text="LateReturnFine")
        self.library_table.heading("Dateoverdue", text="DateOverDue")
        self.library_table.heading("Finalprice", text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("Dateborrowed", width=100)
        self.library_table.column("Datedue", width=100)
        self.library_table.column("Days", width=100)
        self.library_table.column("Latereturnfine", width=100)
        self.library_table.column("Dateoverdue", width=100)
        self.library_table.column("Finalprice", width=100)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root", password="root",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(
                                                                                                                 self.member_var.get(),
                                                                                                                 self.prn_var.get(),
                                                                                                                 self.id_var.get(),
                                                                                                                 self.firstname_var.get(),
                                                                                                                 self.lastname_var.get(),
                                                                                                                 self.address1_var.get(),
                                                                                                                 self.address2_var.get(),
                                                                                                                 self.postcode_var.get(),
                                                                                                                 self.mobile_var.get(),
                                                                                                                 self.bookid_var.get(),
                                                                                                                 self.booktitle_var.get(),
                                                                                                                 self.author_var.get(),
                                                                                                                 self.Dateborrowed_var.get(),
                                                                                                                 self.Datedue_var.get(),
                                                                                                                 self.Daysonbook_var.get(),
                                                                                                                 self.Latereturnfine_var.get(),
                                                                                                                 self.Dateoverdue_var.get(),
                                                                                                                 self.Finalprice_var.get()))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success","Member Has been inserted successfully")


if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()

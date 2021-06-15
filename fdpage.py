# from tkinter import *
# import tkinter.messagebox as tmsg
#
# root = Tk()
# # GUI LOGIC HERE
# root.title("Feedback Page")
# root.wm_iconbitmap("charitybox.ico")
# root.attributes("-fullscreen", True)
# root.wm_attributes("-topmost", 1)  # keep on top
# # root.focus_set()
#
# root.bind("<Escape>", lambda event: root.destroy())
#
# root.geometry("1200x1200")
# root.configure(background='rosyBrown1')
#
# def nextPage():
#     root.destroy()
#     import aboutus
#
#
# # def prevPage():
# #    root.destroy()
# #    import donatepage
#
# def submit():
#     tmsg.showinfo("Feedback", "Thank you your feedback has been submitted")
#
#
# # Frame
# manage_canvas1 = Canvas(root, background='seashell')
# manage_canvas1.place(x=50, y=50, width=1180, height=600)
# manage_canvas1.create_line(25, 90, 1150, 90)
# # Title1
# title1 = Label(manage_canvas1, text="Feedback", bg="seashell", font=("Arial", 30, "bold"))
# title1.pack(pady=20)
# # title2
# title2 = Label(manage_canvas1, text="Let us know your thought", font=("Arial", 25, "bold"), bg="seashell", fg="black")
# title2.pack(pady=60)
# # box for let us know your thought part
# txt_thought = Entry(manage_canvas1, font=("Arial", 13))
# txt_thought.place(x=400, y=200, width=400, height=200)
# # Email part
# lbl_email = Label(manage_canvas1, text="Email", bg="seashell", fg="black", font=("Arial", 20, "bold"))
# lbl_email.place(x=400, y=450, width=80, height=40)
# txt_email = Entry(manage_canvas1, font=("Arial", 13))
# txt_email.place(x=520, y=450, width=250, height=30)
# # submit button
# backbtn1 = Button(root, text='SUBMIT', font="Arial 15 bold", borderwidth=0, bg='grey56', command=submit)
# backbtn1.place(x=590, y=590, width=100, height=50)
#
# # back button
# backbtn1 = Button(root, text='Next', font="Arial 10 bold", borderwidth=0, bg='grey56', command=nextPage)
# backbtn1.place(x=1150, y=10, width=80, height=30)
#
# # backbtn1=Button(root,text='Back',font="Arial 10 bold",borderwidth=0,bg='grey56',command=prevPage)
# # backbtn1.place(x=20,y=15,width=80,height=30)
#
# root.mainloop()



from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Page")
        self.root.geometry("1300x700+0+0")



        #Manage frame
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="RosyBrown1")
        Manage_frame.place(x=20,y=80,width=500,height=580)

        #manage title
        M_title=Label(Manage_frame,text="MANAGE INVENTORY",font=("times new roman",20,"bold"),fg="black",bg="RosyBrown1",bd=3,relief=RAISED)
        M_title.grid(row=0,column=0,padx=20,pady=20)

        #image
        img_left = Image.open("image23.png")
        img_left = img_left.resize((620, 200), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Manage_frame, image=self.photoimg_left)
        f_lbl.place(x=20, y=280, width=450, height=180)

        lbl_name = Label(Manage_frame, text="Name", font=("times new roman", 20, "bold"), fg="black",bg="RosyBrown1")
        lbl_name.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        name_entry = ttk.Entry(Manage_frame, font=("times new roman", 15, "bold"))
        name_entry.grid(row=1, column=0, padx=180, pady=5, sticky="w")

        lbl_email = Label(Manage_frame, text="Block No", font=("times new roman", 20, "bold"), fg="black",bg="RosyBrown1")
        lbl_email.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        email_entry = ttk.Entry(Manage_frame, font=("times new roman", 15, "bold"))
        email_entry.grid(row=2, column=0, padx=180, pady=5, sticky="w")

        lbl_gender = Label(Manage_frame, text="Available No", font=("times new roman", 20, "bold"), fg="black",bg="RosyBrown1")
        lbl_gender.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        combo_gender=ttk.Combobox(Manage_frame,width=18,font=("times new roman", 15, "bold"),state="readonly")
        combo_gender["values"]=("1 units","2 units","3 units","4 units","5 units")
        combo_gender.grid(row=3,column=0,padx=180,pady=5,sticky="w")


        lbl_contact = Label(Manage_frame, text="Wanted No", font=("times new roman", 20, "bold"), fg="black",bg="RosyBrown1")
        lbl_contact.grid(row=4, column=0, padx=20, pady=5, sticky="w")
        contact_entry = ttk.Entry(Manage_frame, font=("times new roman", 15, "bold"))
        contact_entry.grid(row=4, column=0, padx=180, pady=5, sticky="w")




        #Buttons Frame
        btn_frame = Frame(self.root, bd=4, relief=RIDGE,bg="RosyBrown1")
        btn_frame.place(x=40, y=560, width=450)

        add_btn=Button(btn_frame,text="ADD",width=11,height=2,fg="black",bg="seashell")
        add_btn.grid(row=0,column=0,padx=10,pady=10)

        update_btn = Button(btn_frame, text="UPDATE", width=11, height=2, fg="black", bg="seashell")
        update_btn.grid(row=0, column=1, padx=10, pady=10)

        delete_btn = Button(btn_frame, text="DELETE", width=11, height=2, fg="black", bg="seashell")
        delete_btn.grid(row=0, column=2, padx=10, pady=10)

        clear_btn = Button(btn_frame, text="CLEAR", width=11, height=2, fg="black", bg="seashell")
        clear_btn.grid(row=0, column=3, padx=10, pady=10)

        #Details Frame
        Details_frame = Frame(self.root, bd=4, relief=RIDGE,bg="RosyBrown1")
        Details_frame.place(x=540, y=80, width=710, height=580)


        search_lbl=Label(Details_frame,text="Details of available Inventory at Orphange", font=("times new roman", 18, "bold"), fg="black",bg="RosyBrown1")
        search_lbl.grid(row=1,column=0,padx=5,pady=10,sticky="w")


        #Table Frame

        Table_frame = Frame(Details_frame, bd=4, relief=RIDGE,bg="RosyBrown1")
        Table_frame.place(x=10, y=70, width=680, height=490)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)


        self.student_table=ttk.Treeview(Table_frame,column=("name","block","available","wanted"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("name", text="Name")
        self.student_table.heading("block", text="Block No")
        self.student_table.heading("available", text="Available No")
        self.student_table.heading("wanted", text="Wanted No")


        self.student_table["show"]="headings"

        self.student_table.column("name", width=180)
        self.student_table.column("block", width=140)
        self.student_table.column("available", width=140)
        self.student_table.column("wanted", width=140)
        self.student_table.pack(fill=BOTH,expand=1)

        backbtn1 = Button(self.root, text='Next', font=("times new roman", 15 ,"bold"), borderwidth=0, bg='grey56')
        backbtn1.place(x=1150, y=25, width=80, height=30)

        prebtn1 = Button(self.root, text='Previous', font=("times new roman", 15 ,"bold"), borderwidth=0, bg='grey56')
        prebtn1.place(x=40, y=25, width=80, height=30)



root=Tk()
ob=Student(root)
root.mainloop()
from tkinter import *
from tkinter import ttk
import mysql.connector
import random

root=Tk()
#GUI LOGIC HERE
root.title("Orphanage Management")
root.iconbitmap("charitybox.ico")
root.attributes("-fullscreen",True)
root.wm_attributes("-topmost", 1) # keep on top
#root.focus_set()

root.bind("<Escape>", lambda event:root.destroy())

root.geometry("1200x1200")
root.configure(background='seashell')

def nextPage():
    root.destroy()
    import donarpage

    var_roll=int()
    x=random.randint(1,1000)
    var_roll.set(str(x))

    var_name=StringVar()
    var_email = StringVar()
    var_gender=StringVar()
    var_dob=StringVar()
    var_contact=StringVar()
    var_address=StringVar()





title=Label(root,text="Orphan Management",font=("Arial",25 ,"bold"),bg="seashell",fg="black")
title.pack(side=TOP,pady=20)

#Manage Frame
Manage_Frame=Frame(root,bd=4,relief=RIDGE,bg="rosyBrown1")
Manage_Frame.place(x=20,y=100,width=450,height=580)




m_title=Label(Manage_Frame,text="Manage Orphan",bg="rosyBrown1",fg="black",font=("Arial",20,"bold"))
m_title.grid(row=0,columnspan=2,pady=20)

lbl_roll=Label(Manage_Frame,text="Orphan Id",bg="rosyBrown1",fg="black",font=("Arial",20,"bold"))
lbl_roll.grid(row=1,column=0,pady=10,padx=15,sticky="w")
txt_roll=Entry(Manage_Frame,text=var_roll,font=("Arial",13,"bold"),relief=GROOVE,bd=5)
txt_roll.grid(row=1,column=1,pady=10,padx=15,sticky="w")

lbl_name=Label(Manage_Frame,text="Orphan Name",bg="rosyBrown1",fg="black",font=("Arial",20,"bold"))
lbl_name.grid(row=2,column=0,pady=10,padx=15,sticky="w")
txt_name=Entry(Manage_Frame,text=var_name,font=("Arial",13,"bold"),relief=GROOVE,bd=5)
txt_name.grid(row=2,column=1,pady=10,padx=15,sticky="w")

lbl_Email=Label(Manage_Frame,text="Orphan Age",bg="rosyBrown1",fg="black",font=("Arial",20,"bold"))
lbl_Email.grid(row=3,column=0,pady=10,padx=15,sticky="w")
txt_Email=Entry(Manage_Frame,text=var_age,font=("Arial",13,"bold"),relief=GROOVE,bd=5)
txt_Email.grid(row=3,column=1,pady=10,padx=15,sticky="w")

lbl_Gender=Label(Manage_Frame,text="Gender",bg="rosyBrown1",fg="black",font=("Arial",20,"bold"))
lbl_Gender.grid(row=4,column=0,pady=10,padx=15,sticky="w")
combo_gender=ttk.Combobox(Manage_Frame,font=("Arial",13,"bold"),state="readonly")
combo_gender['values']=("male","female")
combo_gender.grid(row=4,column=1,pady=10,padx=10)


lbl_dob=Label(Manage_Frame,text="DOB",bg="rosyBrown1",fg="black",font=("Arial",20,"bold"))
lbl_dob.grid(row=5,column=0,pady=10,padx=15,sticky="w")
txt_dob=Entry(Manage_Frame,text=var_dob,bd=5,relief=GROOVE,font=("Arial",13,"bold"))
txt_dob.grid(row=5,column=1,pady=10,padx=15,sticky="w")


lbl_contact=Label(Manage_Frame,text="Block no",bg="rosyBrown1",fg="black",font=("Arial",20,"bold"))
lbl_contact.grid(row=6,column=0,pady=10,padx=15,sticky="w")
txt_contact=Entry(Manage_Frame,bd=5,relief=GROOVE,font=("Arial",13,"bold"))
txt_contact.grid(row=6,column=1,pady=10,padx=15,sticky="w")

lbl_address=Label(Manage_Frame,text="Division",bg="rosyBrown1",fg="black",font=("Arial",20,"bold"))
lbl_address.grid(row=7,column=0,pady=10,padx=13,sticky="w")
txt_dob=Entry(Manage_Frame,bd=5,relief=GROOVE,font=("Arial",13,"bold"))
txt_dob.grid(row=7,column=1,pady=10,padx=13,sticky="w")


#Buttons Frame
btn_Manage_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="rosyBrown1")
btn_Manage_Frame.place(x=15,y=500,width=420)

addbtn=Button(btn_Manage_Frame,text="Add",width=10,font="Arial 10 bold",borderwidth=0,bg='grey56').grid(row=0,column=0,padx=10,pady=7)
updatebtn=Button(btn_Manage_Frame,text="Update",width=10,font="Arial 10 bold",borderwidth=0,bg='grey56').grid(row=0,column=1,padx=7,pady=10)
deletebtn=Button(btn_Manage_Frame,text="Delete",width=10,font="Arial 10 bold",borderwidth=0,bg='grey56').grid(row=0,column=2,padx=7,pady=10)
clearbtn=Button(btn_Manage_Frame,text="Clear",width=10,font="Arial 10 bold",borderwidth=0,bg='grey56').grid(row=0,column=3,padx=7,pady=10)

#Detail Frame
Detail_Frame=Frame(root,bd=4,relief=RIDGE,bg="rosyBrown1")
Detail_Frame.place(x=500,y=100,width=800,height=580)

lbl_search=Label(Detail_Frame,text="Search",bg="rosyBrown1",fg="black",font=("Arial",20,"bold"))
lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
combo_search=ttk.Combobox(Detail_Frame,width=10,font=("Arial",13,"bold"),state="readonly")
combo_search['values']=("Orphan Id","Orphan Name")
combo_search.grid(row=0,column=1,pady=10,padx=20)

txt_search=Entry(Detail_Frame,width=15,bd=5,relief=GROOVE,font=("Arial",13,"bold"))
txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

searchbtn=Button(Detail_Frame,pady=5,text="Search",width=10,font="Arial 10 bold",borderwidth=0,bg='grey56').grid(row=0,column=3,padx=10,pady=10)
showbtn=Button(Detail_Frame,pady=5,text="Show All",width=10,font="Arial 10 bold",borderwidth=0,bg='grey56').grid(row=0,column=4,padx=10,pady=10)

#Table Frame

table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="rosyBrown1")
table_Frame.place(x=10,y=70,width=760,height=500)

scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
scroll_y=Scrollbar(table_Frame,orient=VERTICAL)
orphan_table=ttk.Treeview(table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=orphan_table.xview)
scroll_y.config(command=orphan_table.yview)
orphan_table.heading("roll",text="Orphan Id")
orphan_table.heading("name",text="Orphan Name")
orphan_table.heading("email",text="Orphan Age")
orphan_table.heading("gender",text="Gender")
orphan_table.heading("dob",text="DOB")
orphan_table.heading("contact",text="Block No")
orphan_table.heading("address",text="Division")
orphan_table['show']='headings'
orphan_table.column("roll",width=100)
orphan_table.column("name",width=150)
orphan_table.column("email",width=100)
orphan_table.column("gender",width=100)
orphan_table.column("contact",width=100)
orphan_table.column("dob",width=100)
orphan_table.column("address",width=100)


orphan_table.pack(fill=BOTH,expand=1)

backbtn1=Button(root,text='Next',font="Arial 10 bold",borderwidth=0,bg='grey56',command=nextPage)
backbtn1.place(x=1150,y=25,width=80,height=30)
root.mainloop()
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class orphans:
	def __init__(self, root):
		self.root = root
		self.root.title("Orphanage management system")
		self.root.geometry("1200x1200")

		self.id_var = StringVar()
		self.name_var = StringVar()
		self.email_var = StringVar()
		self.gender_var = StringVar()
		self.dob_var = StringVar()
		self.contact_var = StringVar()
		self.search_by=StringVar()
		self.search_txt=StringVar()

		title = Label(self.root, text="ORPHANAGE MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), fg="black",bg="RosyBrown1", bd=4, relief=RAISED)
		title.pack(side=TOP, fill=X)

		# Manage frame
		Manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="RosyBrown1")
		Manage_frame.place(x=20, y=80, width=500, height=580)

		# manage title
		M_title = Label(Manage_frame, text="MANAGE ORPHAN", font=("times new roman", 20, "bold"), fg="black",bg="RosyBrown1", bd=3, relief=RAISED)
		M_title.grid(row=0, column=0, padx=20, pady=20)

		# Next Button
		backbtn4 = Button(self.root, text='Next', font="Arial 10 bold", borderwidth=0, bg='grey56')
		backbtn4.place(x=1150, y=10, width=80, height=30)

		# labels
		lbl_roll = Label(Manage_frame, text="Id", font=("times new roman", 20, "bold"), fg="black", bg="RosyBrown1")
		lbl_roll.grid(row=1, column=0, padx=20, pady=5, sticky="w")
		roll_entry = ttk.Entry(Manage_frame, textvariable=self.id_var, font=("times new roman", 15, "bold"))
		roll_entry.grid(row=1, column=0, padx=180, pady=5, sticky="w")

		lbl_name = Label(Manage_frame, text="Name", font=("times new roman", 20, "bold"), fg="black", bg="RosyBrown1")
		lbl_name.grid(row=2, column=0, padx=20, pady=5, sticky="w")
		name_entry = ttk.Entry(Manage_frame, textvariable=self.name_var, font=("times new roman", 15, "bold"))
		name_entry.grid(row=2, column=0, padx=180, pady=5, sticky="w")

		lbl_email = Label(Manage_frame, text="Email", font=("times new roman", 20, "bold"), fg="black", bg="RosyBrown1")
		lbl_email.grid(row=3, column=0, padx=20, pady=5, sticky="w")
		email_entry = ttk.Entry(Manage_frame, textvariable=self.email_var, font=("times new roman", 15, "bold"))
		email_entry.grid(row=3, column=0, padx=180, pady=5, sticky="w")

		lbl_gender = Label(Manage_frame, text="Gender", font=("times new roman", 20, "bold"), fg="black", bg="RosyBrown1")
		lbl_gender.grid(row=4, column=0, padx=20, pady=5, sticky="w")
		combo_gender = ttk.Combobox(Manage_frame, textvariable=self.gender_var, width=18, font=("times new roman", 15, "bold"), state="readonly")
		combo_gender["values"] = ("Male", "Female", "other")
		combo_gender.grid(row=4, column=0, padx=180, pady=5, sticky="w")

		lbl_contact = Label(Manage_frame, text="Contact", font=("times new roman", 20, "bold"), fg="black",bg="RosyBrown1")
		lbl_contact.grid(row=5, column=0, padx=20, pady=5, sticky="w")
		contact_entry = ttk.Entry(Manage_frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"))
		contact_entry.grid(row=5, column=0, padx=180, pady=5, sticky="w")

		lbl_dob = Label(Manage_frame, text="DOB", font=("times new roman", 20, "bold"), fg="black", bg="RosyBrown1")
		lbl_dob.grid(row=6, column=0, padx=20, pady=5, sticky="w")
		dob_entry = ttk.Entry(Manage_frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"))
		dob_entry.grid(row=6, column=0, padx=180, pady=5, sticky="w")

		lbl_address = Label(Manage_frame, text="Address", font=("times new roman", 20, "bold"), fg="black", bg="RosyBrown1")
		lbl_address.grid(row=7, column=0, padx=20, pady=5, sticky="w")
		self.address_text = Text(Manage_frame, width=20, height=3, font=("times new roman", 15, "bold"))
		self.address_text.grid(row=7, column=0, padx=180, pady=5, sticky="w")

		# Buttons Frame
		btn_frame = Frame(self.root, bd=4, relief=RIDGE, bg="RosyBrown1")
		btn_frame.place(x=40, y=560, width=450)

		add_btn = Button(btn_frame, text="ADD", command=self.add_orphans, width=11, height=2, fg="black", bg="seashell")
		add_btn.grid(row=0, column=0, padx=10, pady=10)

		update_btn = Button(btn_frame, text="UPDATE", command=self.update_orphans, width=11, height=2, fg="black", bg="seashell")
		update_btn.grid(row=0, column=1, padx=10, pady=10)

		delete_btn = Button(btn_frame, text="DELETE", command=self.delete_orphans, width=11, height=2, fg="black", bg="seashell")
		delete_btn.grid(row=0, column=2, padx=10, pady=10)

		clear_btn = Button(btn_frame, text="CLEAR", command=self.clear, width=11, height=2, fg="black", bg="seashell")
		clear_btn.grid(row=0, column=3, padx=10, pady=10)

		# Details Frame
		Details_frame = Frame(self.root, bd=4, relief=RIDGE, bg="RosyBrown1")
		Details_frame.place(x=540, y=80, width=710, height=580)

		search_lbl = Label(Details_frame, text="Search By", font=("times new roman", 18, "bold"), fg="black", bg="RosyBrown1")
		search_lbl.grid(row=1, column=0, padx=5, pady=10, sticky="w")

		search_combo = ttk.Combobox(Details_frame, width=16, font=("times new roman", 13, "bold"), state="readonly")
		search_combo["values"] = ("Select option", "Id", "Name", "Contact")
		search_combo.grid(row=1, column=1, padx=5, pady=10, sticky="w")
		search_combo.current(0)

		search_entry = ttk.Entry(Details_frame, font=("times new roman", 13, "bold"))
		search_entry.grid(row=1, column=2, padx=5, pady=10, sticky="w")

		search_btn = Button(Details_frame, command=self.search_orphans, text="Search", width=8, height=2, fg="black", bg="seashell")
		search_btn.grid(row=1, column=3, padx=10, pady=10)

		showall_btn = Button(Details_frame, text="Show All", width=8, height=2, fg="black", bg="seashell")
		showall_btn.grid(row=1, column=4, padx=10, pady=10)

		# Table Frame

		Table_frame = Frame(Details_frame, bd=4, relief=RIDGE, bg="RosyBrown1")
		Table_frame.place(x=10, y=70, width=680, height=490)

		scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
		scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

		self.orphans_table = ttk.Treeview(Table_frame, column=("id", "name", "email", "dob", "gender", "contact", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM, fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)

		scroll_x.config(command=self.orphans_table.xview)
		scroll_y.config(command=self.orphans_table.yview)

		self.orphans_table.heading("id", text="Id")
		self.orphans_table.heading("name", text="Name")
		self.orphans_table.heading("email", text="Email")
		self.orphans_table.heading("dob", text="DOB")
		self.orphans_table.heading("gender", text="Gender")
		self.orphans_table.heading("contact", text="Contact")
		self.orphans_table.heading("address", text="Address")

		self.orphans_table["show"] = "headings"
		self.orphans_table.column("id", width=90)
		self.orphans_table.column("name", width=130)
		self.orphans_table.column("email", width=130)
		self.orphans_table.column("dob", width=100)
		self.orphans_table.column("gender", width=100)
		self.orphans_table.column("contact", width=100)
		self.orphans_table.column("address", width=180)
		self.orphans_table.pack(fill=BOTH, expand=1)

		self.orphans_table.bind("<ButtonRelease-1>",self.get_cursor)

		self.fetch_data()

	def add_orphans(self):

		conn = mysql.connector.connect(host="localhost", username="root", password="Loveurlife762", database="orphanage")

		my_cursor = conn.cursor()
		my_cursor.execute("insert into orphans values(%s,%s,%s,%s,%s,%s,%s)", (
																			self.id_var.get(),
																			self.name_var.get(),
																			self.email_var.get(),
																			self.gender_var.get(),
																			self.dob_var.get(),
																			self.contact_var.get(),
																			self.address_text.get("1.0", END)

																			))

		conn.commit()
		self.fetch_data()
		conn.close()

	def fetch_data(self):
		conn = mysql.connector.connect(host="localhost", username="root", password="Loveurlife762", database="orphanage")
		my_cursor = conn.cursor()
		my_cursor.execute("select * from orphans")
		rows = my_cursor.fetchall()
		if len(rows) != 0:
			self.orphans_table.delete(*self.orphans_table.get_children())
			for i in rows:
				self.orphans_table.insert("", END, values=i)
			conn.commit()
			conn.close()

	def clear(self):
		self.id_var.set("")
		self.name_var.set("")
		self.email_var.set("")
		self.gender_var.set("")
		self.dob_var.set("")
		self.contact_var.set("")
		self.address_text.delete("1.0", END)

	def get_cursor(self,event=""):
		cursor_row=self.orphans_table.focus()
		content=self.orphans_table.item(cursor_row)
		row=content["values"]
		self.id_var.set(row[0])
		self.name_var.set(row[1])
		self.email_var.set(row[2])
		self.gender_var.set(row[3])
		self.dob_var.set(row[4])
		self.contact_var.set(row[5])
		self.address_text.delete("1.0", END)
		self.address_text.insert(END,row[6])

	def update_orphans(self):
		conn = mysql.connector.connect(host="localhost", username="root", password="Loveurlife762", database="orphanage")
		my_cursor = conn.cursor()
		my_cursor.execute("update orphans set name=%s,email=%s,gender=%s,dob=%s,contact=%s,address=%s where id=%s", (
																													self.name_var.get(),
																													self.email_var.get(),
																													self.gender_var.get(),
																													self.dob_var.get(),
																													self.contact_var.get(),
																													self.address_text.get("1.0", END),
																													self.id_var.get()

																													))

		conn.commit()
		self.fetch_data()
		self.clear()
		conn.close()
		messagebox.showinfo("Update","Record has been updated successfully!")

	def delete_orphans(self):
		conn = mysql.connector.connect(host="localhost", username="root", password="Loveurlife762", database="orphanage")
		my_cursor = conn.cursor()
		query="delete from orphans where id=%s"
		value=(self.id_var.get(),)
		my_cursor.execute(query,value)

		conn.commit()
		conn.close()
		self.fetch_data()
		self.clear()

		messagebox.showinfo("Delete","Record has been deleted successfully")

	def search_orphans(self):
		conn = mysql.connector.connect(host="localhost", username="root", password="Loveurlife762", database="orphanage")
		my_cursor = conn.cursor()
		my_cursor.execute("select * from orphans where "+str(self.search_by.get())+"LIKE"+str(self.search_txt.get())+"%")
		rows = my_cursor.fetchall()

		if len(rows)!=0:
			self.orphans_table.delete(*self.orphans_table.get_children())
			for i in rows:
				self.orphans_table.insert("",END,values=i)
			conn.commit()
		conn.close()

		backbtn1 = Button(self.root, text='Next', font=("times new roman", 15, "bold"), borderwidth=0, bg='grey56')
		backbtn1.place(x=1150, y=25, width=80, height=30)

		prebtn1 = Button(self.root, text='Previous', font=("times new roman", 15, "bold"), borderwidth=0, bg='grey56')
		prebtn1.place(x=40, y=25, width=80, height=30)


root = Tk()
ob = orphans(root)
root.mainloop()

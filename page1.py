from tkinter import *
import mysql.connector

root = Tk()
# GUI LOGIC HERE
root.title("Orphanage Management System")
root.wm_iconbitmap("charitybox.ico")
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes("-fullscreen", True)
root.wm_attributes("-topmost", 1)  # keep on top
# root.focus_set()

root.bind("<Escape>", lambda event: root.destroy())
root.geometry("1200x1200")
root.configure(background='rosyBrown1')


def nextPage():
    root.destroy()
    import menu

manage_frame1 = Frame(root, background='seashell', relief=SUNKEN)
manage_frame1.place(x=50, y=50, width=1180, height=600)

label_home = Label(manage_frame1, text='Small Effort', font='Arial 50 bold', background='seashell')
label_home.place(anchor='w', x=40, y=150)
label_home = Label(manage_frame1, text='Make Big Change', font='Arial 50 bold', background='seashell')
label_home.place(anchor='w', x=40, y=220)
label_home = Label(manage_frame1, text='Volunteers do not necessarily have the time they', font='Arial 18 bold',
                   background='seashell')
label_home.place(anchor='w', x=40, y=300)
label_home = Label(manage_frame1, text='just have heart.', font='Arial 18 bold', background='seashell')
label_home.place(anchor='w', x=40, y=330)
b1 = Button(manage_frame1, fg="black", bg='grey56', text="Start Here", font="Arial 18 bold", borderwidth=0,
            command=nextPage)
b1.place(anchor='w', x=40, y=450)
kindness = PhotoImage(file="kindness3.png", width=513, height=430)
kindness_label = Label(manage_frame1, image=kindness, background='seashell')
kindness_label.pack(anchor='w', ipadx=30, ipady=20, side='right')

root.mainloop()

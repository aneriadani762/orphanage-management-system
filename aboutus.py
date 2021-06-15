from tkinter import *

root=Tk()
#GUI LOGIC HERE
root.title("About Us Page")
root.wm_iconbitmap("charitybox.ico")
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes("-fullscreen",True)
root.wm_attributes("-topmost", 1) # keep on top
#root.focus_set()

root.bind("<Escape>", lambda event:root.destroy())

root.geometry("1200x1200")
root.configure(background='rosyBrown1')

def prevPage():
    root.destroy()
    import page1

#manage_frame1=Frame(root,background='seashell',relief=SUNKEN)
#manage_frame1.place(x=50,y=50,width=1180,height=600)
#Frame
manage_canvas1=Canvas(root,background='seashell')
manage_canvas1.place(x=50,y=50,width=1180,height=600)
manage_canvas1.create_line(25, 90, 1150, 90)
#Title1
title1=Label(manage_canvas1,text="About Us",bg="seashell",font=("Arial",30,"bold"))
title1.pack(pady=20)


donation = PhotoImage(file="donation4.png",width=1000,height=400)
donation_label = Label(manage_canvas1,image=donation,background='seashell')
donation_label.pack(pady=50)

label_home=Label(manage_canvas1,text='Our Orphanage focuses to empower the',font='Arial 18 bold',background='seashell')
label_home.place(anchor='w',x=620,y=200)
label_home=Label(manage_canvas1,text='orphans to get access to more opportunities ',font='Arial 18 bold',background='seashell')
label_home.place(anchor='w',x=620,y=234)
label_home=Label(manage_canvas1,text='with the help of education and guidance.',font='Arial 18 bold',background='seashell')
label_home.place(anchor='w',x=620,y=268)
label_home=Label(manage_canvas1,text='Our mission is to work hard to provide ',font='Arial 18 bold',background='seashell')
label_home.place(anchor='w',x=620,y=300)
label_home=Label(manage_canvas1,text="a loving home and family for every children.",font='Arial 18 bold',background='seashell')
label_home.place(anchor='w',x=620,y=334)
label_home=Label(manage_canvas1,text="and to show the world that every child,",font='Arial 18 bold',background='seashell')
label_home.place(anchor='w',x=620,y=368)
label_home=Label(manage_canvas1,text="regardless of their needs, deserves to have",font='Arial 18 bold',background='seashell')
label_home.place(anchor='w',x=620,y=400)
label_home=Label(manage_canvas1,text="a loving childhood and to be treated with",font='Arial 18 bold',background='seashell')
label_home.place(anchor='w',x=620,y=434)
label_home=Label(manage_canvas1,text="dignity and care.",font='Arial 18 bold',background='seashell')
label_home.place(anchor='w',x=620,y=468)
backbtn3=Button(root,text='back',font="Arial 10 bold",borderwidth=0,bg='grey56',command=prevPage)
backbtn3.place(x=20,y=15,width=80,height=30)




root.mainloop()
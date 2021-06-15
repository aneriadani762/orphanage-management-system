from tkinter import *

root=Tk()
#GUI LOGIC HERE
root.title("Dashboard")
root.wm_iconbitmap("charitybox.ico")
root.attributes("-fullscreen",True)
root.wm_attributes("-topmost", 1) # keep on top
#root.focus_set()

root.bind("<Escape>", lambda event:root.destroy())


root.geometry("1200x1200")
root.configure(background='rosyBrown1')


def orphan_image_place():
    root.destroy()
    import page2


def donar_image_place():
    root.destroy()
    import donarpage

def inventory_image_place():
    root.destroy()
    import inventorypage

def aboutus_image_place():
    root.destroy()
    import aboutus

def donate_image_place():
    root.destroy()
    import donatepage

def fd_image_place():
    root.destroy()
    import fdpage


#code for canvas
manage_canvas1=Canvas(root,background='seashell')
manage_canvas1.place(x=50,y=50,width=1180,height=600)
manage_canvas1.create_line(25, 90, 1150, 90)
title_canvas=Label(manage_canvas1,text="Welcome to Dashboard",font=("Arial",40 ,"bold"),bg="seashell")
title_canvas.pack(side=TOP)


#first row starts here
#to place image on orphan button
orphanbtn_image=PhotoImage(file="Orphan.png")
orphanbtn_image_label=Label(image=orphanbtn_image)
#my_label=Label(manage_canvas1)
#my_label.pack()
orphanbtn=Button(manage_canvas1,image=orphanbtn_image,font="Arial 10 bold",borderwidth=0,bg='grey56',command=orphan_image_place)
orphanbtn.place(x=200,y=200,width=150,height=108)

#to place image on donar button
donarbtn_image=PhotoImage(file="donor1.png")
donarbtn_image_label=Label(image=donarbtn_image)
#my_label1=Label(manage_canvas1)
#my_label1.pack()
donarbtn=Button(manage_canvas1,image=donarbtn_image,font="Arial 10 bold",borderwidth=0,bg='grey56',command=donar_image_place)
donarbtn.place(x=550,y=200,width=150,height=110)

#to place image on inventory button
inventorybtn_image=PhotoImage(file="inventory.png")
inventorybtn_image_label=Label(image=inventorybtn_image)
#my_label2=Label(manage_canvas1)
#my_label2.pack()
inventorybtn=Button(manage_canvas1,image=inventorybtn_image,font="Arial 10 bold",borderwidth=0,bg='grey56',command=inventory_image_place)
inventorybtn.place(x=900,y=200,width=150,height=110)

#second row starts here
#Donate buttons
donatebtn_image=PhotoImage(file="donate.png")
donatebtn_image_label=Label(image=donatebtn_image)
#my_label3=Label(manage_canvas1)
#my_label3.pack()
donatebtn=Button(manage_canvas1,image=donatebtn_image,font="Arial 10 bold",borderwidth=0,bg='grey56',command=donate_image_place)
donatebtn.place(x=200,y=400,width=150,height=110)


#feedback
fdbtn_image=PhotoImage(file="feedback.png")
fdbtn_image_label=Label(image=fdbtn_image)
#my_label4=Label(manage_canvas1)
#my_label4.pack()
fdbtn=Button(manage_canvas1,image=fdbtn_image,font="Arial 10 bold",borderwidth=0,bg='grey56',command=fd_image_place)
fdbtn.place(x=550,y=400,width=150,height=112)

#aboutus
aboutusbtn_image=PhotoImage(file="aboutus.png")
aboutusbtn_image_label=Label(image=aboutusbtn_image)
#my_label5=Label(manage_canvas1)
#my_label5.pack()
aboutusbtn=Button(manage_canvas1,image=aboutusbtn_image,font="Arial 10 bold",borderwidth=0,bg='grey56',command=aboutus_image_place)
aboutusbtn.place(x=900,y=400,width=150,height=112)





root.mainloop()
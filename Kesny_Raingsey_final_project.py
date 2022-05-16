from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

mainWindow = Tk()
#adjut the file from the page
mainWindow.geometry("600x500")
#name title
mainWindow.title("The Cake ordering app")
#background image
#img= ImageTk.PhotoImage(Image.open("Cake1.jpg"))
img= ImageTk.PhotoImage(Image.open("Cake1.jpg"))


#add image to screen
#piclabel = Label(mainWindow, image= img)
##piclabel.place(x=0, y=0, relwidth=1, relheight= 1)


#create a canvas
my_canvas = Canvas(mainWindow, width = 500, height = 600)
my_canvas.pack(fill ="both", expand = True)

#set image in Canvas
my_canvas.create_image(0,0, image=img, anchor ="nw")

#add a logo
my_canvas.create_text(140, 120, text="The Cake", font=("Arial", 30, "bold italic"), fill="#876445")

"""
#add logo
logo = Label(mainWindow, text="The Cake", font=("Helvetica", 30), fg ="#F9CEEE" )
logo.pack(pady=70)

#create a frame put button to the smae frame

my_frame = Frame(mainWindow)
my_frame.pack(pady=20)

"""
def open():
  top=Toplevel()
  top.geometry("600x500")
  top.title("The Cake ordering app")
  top['bg']= "#F4DFBA"
  
  

  #__________create a frame1_________
  frame1 = LabelFrame(top, bg="#F4DFBA", bd =0, padx = 50, pady = 30)
  frame1.grid(row = 0, column = 0, columnspan = 10, rowspan = 10)

  #____________create a title____________
  title=Label(frame1, text="The Cake Ordering App", font='times 18 bold',   bg="#F4DFBA", fg="#876445", anchor=CENTER)
  title.grid(row=0, column=5, columnspan = 6, pady= 10, sticky= "N")

  #Variable 
  Name = StringVar()
  Number = IntVar()
  Address = StringVar()

  Name.set("")
  Number.set("")
  Address.set("")

  #name label
  name_label = Label(frame1, text="Customer Name: ", bg="#F4DFBA", fg="#876445")
  name_label.grid(row=2, column=5, padx= 20, sticky ="nw")

  #name for user to enter
  name_entry = Entry(frame1, width=40,textvariable= Name)
  name_entry.grid(row=2, column=6)

  #phone label
  phone_label = Label(frame1, text="Phone Number: ", bg="#F4DFBA", fg="#876445")
  phone_label.grid(row=3, column=5, padx= 20, pady= 5, sticky ="nw")

  #phone for user to enter
  phone_entry = Entry(frame1, width=40, textvariable=Number)
  phone_entry.grid(row=3, column=6, pady= 5)

  #address label
  address_label = Label(frame1, text="Address: ", bg="#F4DFBA", fg="#876445")
  address_label.grid(row=4, column=5, padx= 20, sticky ="nw")

  #addressfor user to enter
  address_entry = Entry(frame1, width=40, textvariable=Address)
  address_entry.grid(row=4, column=6)

  #___________create a frame2___________
  frame2 = LabelFrame(top,   bg="#DFD3C3",highlightbackground="black",highlightthickness=1, height =200, width=200, bd=1, padx = 35, pady = 15)
  frame2.grid(row = 10, column = 0, columnspan = 10, rowspan = 10, padx= 50,sticky = "NW")

  #-----menu section ----
  menu=Label(frame2, text="Menu", font="times 12 bold", bg="#DFD3C3", fg="#5C3D2E")
  menu.grid(row=0, column=1, columnspan= 10, pady= 10, sticky = "NW")

  sCake=Label(frame2, text="Small Cake     ", bg="#DFD3C3", fg="#5C3D2E")
  sCake.grid(row=1, column=5,sticky = "NW")

  mCake=Label(frame2, text="Medium Cake       ", bg="#DFD3C3", fg="#5C3D2E")
  mCake.grid(row=2, column=5,sticky = "W")

  lCake=Label(frame2, text="Large Cake       ", bg="#DFD3C3", fg="#5C3D2E")
  lCake.grid(row=3, column=5, sticky = "W")

  cCake=Label(frame2, text="Cupcake        ", bg="#DFD3C3", fg="#5C3D2E")
  cCake.grid(row=4, column=5, sticky = "W")

  #-----Price secton ----
  p1=Label(frame2, text="$25 ", bg="#DFD3C3", fg="#5C3D2E")
  p1.grid(row=1, column=6,sticky = "W")

  p2=Label(frame2, text="$35 ", bg="#DFD3C3", fg="#5C3D2E")
  p2.grid(row=2, column=6,sticky = "W")

  p3=Label(frame2, text="$45 ", bg="#DFD3C3", fg="#5C3D2E")
  p3.grid(row=3, column=6, sticky = "W")

  p4=Label(frame2, text="$1.5 ", bg="#DFD3C3", fg="#5C3D2E")
  p4.grid(row=4, column=6, sticky = "W")

  #-----Variable----
  e1_v= StringVar()
  e2_v= StringVar()
  e3_v= StringVar()
  e4_v= StringVar()
  
  e1_v.get()
  e2_v.get()
  e3_v.get()
  e4_v.get()

  #------Billing section------
  qty=Label(frame2, text="Qty", font="times 12 bold", bg="#DFD3C3", fg="#5C3D2E")
  qty.grid(row=0, column=7)

  e1=Entry(frame2, width= 5,  textvariable=e1_v)
  e1.grid(row=1, column=7)

  e2=Entry(frame2, width= 5, textvariable=e2_v)
  e2.grid(row=2, column=7)

  e3=Entry(frame2, width= 5, textvariable=e3_v)
  e3.grid(row=3, column=7)

  e4=Entry(frame2, width= 5, textvariable=e4_v)
  e4.grid(row=4, column=7)


  #___________create a frame3_____________
  frame3 = LabelFrame(top, bg="#DFD3C3",highlightbackground="black",highlightthickness=1, height =200, width=200, bd=1, padx = 35, pady = 15)
  frame3.grid(row = 10, column = 6, columnspan = 10, rowspan = 10, padx = 30, sticky = "NW")
  
  #------flavors section------
  flavors=Label(frame3, text="Flavors", font="times 12 bold", bg="#DFD3C3", fg="#5C3D2E")
  flavors.grid(row=0, column=10, pady= 10, sticky = "NW" )

  #----radio button variable----
  var1 = StringVar()
  var2 = StringVar()
  var3 = StringVar()
  var4 = StringVar()

  var1.set(" ")
  var2.set(" ")
  var3.set(" ")
  var4.set(" ")
  #radio button
  radio1 = Radiobutton(frame3, text="Chololate",bg="#DFD3C3", fg="#5C3D2E", variable = var1)
  radio1.grid(row=1, column=10, sticky = "W")
  radio2 = Radiobutton(frame3, text="Strawberry",bg="#DFD3C3", fg="#5C3D2E", variable = var2)
  radio2.grid(row=2, column=10, sticky = "W")
  radio3 = Radiobutton(frame3, text="Red Velvet",bg="#DFD3C3", fg="#5C3D2E", variable = var3)
  radio3.grid(row=3, column=10, sticky = "W")
  radio4 = Radiobutton(frame3, text="Vanilla",bg="#DFD3C3", fg="#5C3D2E", variable = var4)
  radio4.grid(row=4, column=10, sticky = "W")

  #____________create a textbox____________

  text_box = Text(top, height =5, width =42)
  text_box.place(x=25, y= 370)
  text_box.config(state="normal")
  Des= Label(top, text="Description:",font="times 9 bold underline", bg="#F4DFBA", fg="#5C3D2E" )
  Des.place(x=25, y= 350)
    
  def Total():

    try:small_price =int(e1.get())
    except: 
      small_price = 0
      e1.configure(state =DISABLED)  
    try:med_price =int(e2.get())
    except:
      med_price = 0
      e2.configure(state =DISABLED)
    try:large_price =int(e3.get())
    except: 
      large_price = 0
      e3.configure(state =DISABLED)
    try:cup_price =int(e4.get())
    except: 
      cup_price = 0
      e4.configure(state =DISABLED)


    s_cake  = small_price * 25
    med_cake = med_price * 35
    large_cake = large_price * 45
    cup_cake = cup_price * 1.5
    total = s_cake + med_cake + large_cake + cup_cake
    total_bill = format(float(total), '.2f')
    tax = total * 0.10
    Tax = format(float(tax), '.2f')
    total_tax = tax + total
    All_total = format(float(total_tax), '.2f')
  
    buttontext = Label(top, text= "Total $" +total_bill+ "\nTax: $" +Tax+ "\nYour total is $" +All_total, font='times 10 bold', bg="white", fg="#876445")
    buttontext.place(x=380, y= 375)
  
  
  # total button
  calcButton=Button(top, text="Total", font="Arial", bg="#CA965C", fg="white", activebackground="#876445", command = Total)
  calcButton.place(x=25, y= 452)

  def order():
    ordername = str(name_entry.get())
    orderphone = str(phone_entry.get())
    orderaddress = str(address_entry.get())
    chocolate = var1.get()
    strawberry = var2.get()
    redvelvet = var3.get()
    vanilla = var4.get()
 
    e1.configure(state =DISABLED)  
    e2.configure(state =DISABLED)
    e3.configure(state =DISABLED)
    e4.configure(state =DISABLED)
    
    validName = False
    #Consider the while condition to be true and prompt the user to enter the input
    while not validName:

 	     #The input entered by the user is checked to see if they're alpha or words
      if ordername and orderphone and orderaddress:
        		#The flag is set to true if the if condition is true
        validName = True
        name_entry.configure(state =DISABLED)
        phone_entry.configure(state =DISABLED)
        address_entry.configure(state =DISABLED)
        text_box.configure(state =DISABLED)
      else:
        messagebox.showerror("Invalid","Invalid Information")
        break
      ordertext = Label(top, text= "Your order is complete!\nThank " +ordername, font='times 10 bold', bg="white", fg="#876445", height = 3)
      ordertext.place(x=380, y= 375)

  
  # order button
  orderButton=Button(top, text="Order", font="Arial", bg="#CA965C", fg="white", activebackground="#876445", command = order)
  orderButton.place(x=370, y= 452)

  def Reset():
    Name.set("")
    Number.set("")
    Address.set("")
    e1_v.set(" ")
    e2_v.set(" ")
    e3_v.set(" ")
    e4_v.set(" ")
    var1.set(" ")
    var2.set(" ")
    var3.set(" ")
    var4.set(" ")
    name_entry.configure(state =NORMAL)
    phone_entry.configure(state =NORMAL)
    address_entry.configure(state =NORMAL)
    e1.configure(state =NORMAL)
    e2.configure(state =NORMAL)
    e3.configure(state =NORMAL)
    e4.configure(state =NORMAL)
    text_box = Text(top, height =5, width =42)
    text_box.place(x=25, y= 370)
    text_box.config(state="normal")
    cleartext = Label(top, bg="#F4DFBA",height = 5, width = 30)
    cleartext.place(x=380, y= 375)

  # Reset button
  resetButton=Button(top, text="reset", font="Arial", bg="#CA965C", fg="white", activebackground="#876445", command = Reset)
  resetButton.place(x=255, y= 452)


  def Exit():
    exit = messagebox.askyesno("Ordering System", "Do you want to exit the system?")
    if exit > 0:
      top.destroy()
      mainWindow.destroy()
      return


  # Exit button
  exitButton=Button(top, text="exit", font="Arial", bg="#CA965C", fg="white", activebackground="#876445", command = Exit)
  exitButton.place(x=490, y= 452)
  
#Add some buttons
my_button1 = Button(mainWindow, text="Order Now", font="Arial", bg="#CA965C", fg="white", activebackground="#876445", command=open)
my_button1_window = my_canvas.create_window(85,190, anchor="nw", window= my_button1)


mainWindow.mainloop()
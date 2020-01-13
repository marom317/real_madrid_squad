from tkinter import *
from PIL import ImageTk,Image

root = Tk()

# Create title, logo and frame
root.title('Real Madrid')
root.iconbitmap('logo1.ico')
frame = LabelFrame(root, text='This is Real Radrid squad')
frame.pack(padx=20, pady=20 )

# Upload and resize Images
my_img0 = ImageTk.PhotoImage(Image.open('logo.JFIF').resize((250,250),Image.ANTIALIAS))
my_img1 = ImageTk.PhotoImage(Image.open('1.JFIF').resize((250,250),Image.ANTIALIAS))
my_img2 = ImageTk.PhotoImage(Image.open('2.JFIF').resize((250,250),Image.ANTIALIAS))
my_img3 = ImageTk.PhotoImage(Image.open('3.JFIF').resize((250,250),Image.ANTIALIAS))
my_img4 = ImageTk.PhotoImage(Image.open('4.JFIF').resize((250,250),Image.ANTIALIAS))
my_img5 = ImageTk.PhotoImage(Image.open('5.JFIF').resize((250,250),Image.ANTIALIAS))
my_img6 = ImageTk.PhotoImage(Image.open('6.JFIF').resize((250,250),Image.ANTIALIAS))
my_img7 = ImageTk.PhotoImage(Image.open('hames.JFIF').resize((250,250),Image.ANTIALIAS))
my_img8 = ImageTk.PhotoImage(Image.open('rodrigo.JFIF').resize((250,250),Image.ANTIALIAS))
my_img9 = ImageTk.PhotoImage(Image.open('tivo.JFIF').resize((250,250),Image.ANTIALIAS))
my_img10 = ImageTk.PhotoImage(Image.open('varan.JFIF').resize((250,250),Image.ANTIALIAS))
my_img11 = ImageTk.PhotoImage(Image.open('casamiro.JFIF').resize((250,250),Image.ANTIALIAS))
my_img12 = ImageTk.PhotoImage(Image.open('yuvic.JFIF').resize((250,250),Image.ANTIALIAS))
my_img13 = ImageTk.PhotoImage(Image.open('ramos.JFIF').resize((250,250),Image.ANTIALIAS))
my_img14 = ImageTk.PhotoImage(Image.open('vini.JFIF').resize((250,250),Image.ANTIALIAS))
my_img15= ImageTk.PhotoImage(Image.open('marcelo.JFIF').resize((250,250),Image.ANTIALIAS))
# Create a list of the images
images = [my_img0, my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img11, my_img12, my_img13, my_img14, my_img15]
my_label = Label(frame,image = images[0])
my_label.grid(row=0,column=1)

# Creating description for the players and club

madrid = 'REAL MADRID  \n 1987-2001'
hazerd = 'Age : 25 \n Position : ST \n No: 7'
benzema = 'Age : 32 \n Position : ST \n No: 9'
bale = 'Age : 30 \n Position : RW \n No: 11'
kros = 'Age : 30 \n Position : CM \n No: 8'
valverde = 'Age : 21 \n Position : CM \n No: 15'
modrich = 'Age : 34 \n Position : CM \n No: 10'
hames = 'Age : 28 \n Position : CM \n No: 16'
rodrigo = 'Age : 19 \n Position : RW \n No: 27'
tivo = 'Age : 27 \n Position : GK \n No: 13'
varan ='Age : 26 \n Position : CB \n No: 5'
casamiro ='Age : 27 \n Position : CM \n No: 14'
yuvic ='Age : 22 \n Position : ST \n No: 19'
ramos = 'Age : 33 \n Position : CB \n No: 4'
vini ='Age : 19 \n Position : LW \n No: 25'
marcelo = 'Age : 31 \n Position : LB \n No: 12'
desc_label = Label(frame, text=madrid).grid(row=0,column=2)
players = [
    ("Hazard",1),
    ("Benzema",2),
    ("Bale",3),
    ("Kros",4,),
    ("Valverde",5),
    ("Modrich",6),
    ("Hames",7),
    ("Rodrigo",8),
    ("Tivo",9),
    ("Varan",10),
    ("Casamiro",11),
    ("Yuvic",12),
    ("Ramos",13),
    ("Vini",14),
    ("Marcelo",15),
]
var = IntVar()

# For loop to create radio buttons of each player
for i,v in players:
    Radiobutton(frame,text=i,variable=var,value=v).grid(row=v,column=0,sticky=W)

var.set("Hazard")

# Define a func that grid specific picture
def click(value):
    global my_label
    global desc_label
    if value == 1:
        my_label.grid_forget()
        my_label= Label(frame,image=images[value] )
        my_label.grid(row=0,column=1)
        desc_label = Label(frame, text=hazerd).grid(row=0, column=2)

    elif value == 2:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=benzema).grid(row=0, column=2)
    elif value == 3:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=bale).grid(row=0, column=2)
    elif value == 4:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=kros).grid(row=0, column=2)
    elif value == 5:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=valverde).grid(row=0, column=2)
    elif value == 6:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=modrich).grid(row=0, column=2)
    elif value == 7:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=hames).grid(row=0, column=2)
    elif value == 8:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=rodrigo).grid(row=0, column=2)
    elif value == 9:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=tivo).grid(row=0, column=2)
    elif value == 10:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=varan).grid(row=0, column=2)
    elif value == 11:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=casamiro).grid(row=0, column=2)
    elif value == 12:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=yuvic).grid(row=0, column=2)
    elif value == 13:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=ramos).grid(row=0, column=2)
    elif value == 14:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=vini).grid(row=0, column=2)
    elif value == 15:
        my_label.grid_forget()
        my_label = Label(frame, image=images[value])
        my_label.grid(row=0, column=1)
        my_label.grid(row=0, column=1)
        desc_label = Label(frame, text=marcelo).grid(row=0, column=2)

# Add button
button = Button(frame,text='Show details',command=lambda: click(var.get()))
button.grid(row=2,column=2)

mainloop()
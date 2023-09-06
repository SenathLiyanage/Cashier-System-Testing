# tkinter is a module/container/file which contain classes and methods which help to create GUI.
from tkinter import *
# import 'messagebox' from tkinter to display msg box
from tkinter import messagebox
# import 'random' module to generate a bill number.
# import 'os' module to create a folder
import random,os

# -------functionality Part-------

# if there is no 'bills' folder, then create a folder using 'os' module
if  not os.path.exists('bills'):
    # make a folder
    os.mkdir('bills')

# define 'total' function. use 'get()' method to get values from entry and stor inside a variable.
def total():
    # make variables public using 'global' to use them in other methods
    global soapprice,body_lotionprice,hair_gelprice,hair_sprayprice,face_washprice,face_creamprice
    global sugarprice,wheatprice,daalprice,oilprice,riceprice,teaprice
    global cococolaprice,frootiprice,dewprice,spriteprice,pepsiprice,maazaprice
    global totalbill

    # Cosmetics
    soapprice = int(soapEntry.get()) * 20
    face_creamprice = int(face_creamEntry.get()) * 50
    face_washprice = int(face_washEntry.get()) * 100
    hair_sprayprice = int(hair_sprayEntry.get()) * 200
    hair_gelprice = int(hair_gelEntry.get()) * 150
    body_lotionprice = int(body_lotionEntry.get()) * 80

    total_cosmetic_price = soapprice + face_creamprice + face_washprice + hair_sprayprice + hair_gelprice + body_lotionprice
    # before enter total value, delete the values inside the entry field using 'delete()' method. 'delete(0,END)' ---> delete from start to end
    cosmetic_price_Entry.delete(0,END)
    # convert 'total_cosmetic_price' into string using 'str()' or f'{total_cosmetic_price} Rs'
    cosmetic_price_Entry.insert(0,'Rs. '+str(total_cosmetic_price))
    # cosmetic tax calculation
    cosmetictax = total_cosmetic_price * 0.12
    cosmetic_tax_Entry.delete(0,END)
    cosmetic_tax_Entry.insert(0, 'Rs. '+str(cosmetictax))

    # Grocery
    riceprice = int(riceEntry.get()) * 100
    oilprice = int(oilEntry.get()) * 200
    daalprice = int(daalEntry.get()) * 150
    wheatprice = int(wheetEntry.get()) * 80
    sugarprice = int(sugarEntry.get()) * 50
    teaprice = int(teaEntry.get()) * 60

    total_grocery_price = riceprice + oilprice + daalprice + wheatprice + sugarprice + teaprice
    grocery_price_Entry.delete(0,END)
    grocery_price_Entry.insert(0,'Rs. '+str(total_grocery_price))
    # grocery tax calculation
    grocerytax = total_grocery_price * 0.15
    grocery_tax_Entry.delete(0,END)
    grocery_tax_Entry.insert(0,'Rs. '+str(grocerytax))

    # Cool Drinks
    maazaprice = int(maazaEntry.get()) * 60
    pepsiprice = int(pepsiEntry.get()) * 100
    spriteprice = int(spriteEntry.get()) * 70
    dewprice = int(dewEntry.get()) * 60
    frootiprice = int(frootiEntry.get()) * 80
    cococolaprice = int(coco_colaEntry.get()) * 100

    total_cool_drink_price = maazaprice + pepsiprice + spriteprice + dewprice + frootiprice + cococolaprice
    drink_price_Entry.delete(0,END)
    drink_price_Entry.insert(0,'Rs. '+str(total_cool_drink_price))
    # cool drinks tax calculation
    drinkstax = total_cool_drink_price * 0.08
    drink_tax_Entry.delete(0,END)
    drink_tax_Entry.insert(0,'Rs. '+str(drinkstax))

    totalbill = total_cosmetic_price+total_grocery_price+total_cool_drink_price+cosmetictax+grocerytax+drinkstax

# the bill button functions

def save_bill():
    global billnumber
    # 'askyesno()' method will return tru or false. That return will store result variable
    result = messagebox.askyesno('Confirm','Do you want to save the bill?')
    # 'if result' = the condition is true following code will executed
    if result:
        # get every thing in the text area (1.0 to end) and save it in the 'bill_content' area
        bill_content = textarea.get(1.0,END)
        # then write the bill_content into a file (File name is 'file'). Open 'bills' folder and save the file with the bill number in write mode ('w').
        file = open(f'bills/ {billnumber}.txt','w')
        # use 'write()' method to write the bill
        file.write(bill_content)
        # close the file when content is returned using 'close()' method
        file.close()
        # show a msg box when the save is success
        messagebox.showinfo('Success',f'Bill number {billnumber} is saved successfully')
        # when saved bill, the bill number must re-new (Bill number do not duplicate)
        billnumber = random.randint(500, 1000)

# define 'billnumber' variable and pass the values of starting number(500) and ending number(1000). Random value between 500 to 1000
billnumber = random.randint(500,1000)

def bill_area():
    # msg box for enter customer details if the field is empty
    if nameEntry.get() == '' or phoneEntry.get() == '':
        # import tkinter messagebox at the top and use showerror('title','msg') method
        messagebox.showerror('Error!','Customer Details Are Required')
    # use 'and' gate for the  error msg display only when all the entry fields are empty
    elif cosmetic_price_Entry.get()=='' and grocery_price_Entry.get()=='' and drink_price_Entry.get()=='':
        messagebox.showerror('Error!','Please generate the total field')
    elif cosmetic_price_Entry.get()=='Rs. 0' and grocery_price_Entry.get()=='Rs. 0' and drink_price_Entry.get()=='Rs. 0':
        messagebox.showerror('Error!','Please select minimum one product')
    else:
        # delete previous things in the bill before start a new one
        textarea.delete(1.0,END)
        # use '\t' for tab spaces. '\n' to line break
        textarea.insert(END,('\t\t*** Welcome Customer! ***\n\n'))
        textarea.insert(END,f'Bill Number: {billnumber}\n')
        textarea.insert(END,f'Customer Name: {nameEntry.get()}\n')
        textarea.insert(END,f'Customer Phone Number: {phoneEntry.get()}\n')
        textarea.insert(END,f'=======================================================\n')
        textarea.insert(END,f'Product\t\t\tQuantity\t\t\tPrice\n')
        textarea.insert(END,f'=======================================================\n')
        if soapEntry.get()!='0':
            textarea.insert(END,f'Bath Soap\t\t\t{soapEntry.get()}\t\t\tRs.{soapprice}\n')
        if face_creamEntry.get()!='0':
            textarea.insert(END, f'Face Cream\t\t\t{face_creamEntry.get()}\t\t\tRs.{face_creamprice}\n')
        if face_washEntry.get()!='0':
            textarea.insert(END, f'Face Wash\t\t\t{face_washEntry.get()}\t\t\tRs.{face_washprice}\n')
        if hair_sprayEntry.get()!='0':
            textarea.insert(END, f'Hair Spray\t\t\t{hair_sprayEntry.get()}\t\t\tRs.{hair_sprayprice}\n')
        if hair_gelEntry.get()!='0':
            textarea.insert(END, f'Hair Gel\t\t\t{hair_gelEntry.get()}\t\t\tRs.{hair_gelprice}\n')
        if body_lotionEntry.get()!='0':
            textarea.insert(END, f'Body Lotion\t\t\t{body_lotionEntry.get()}\t\t\tRs.{body_lotionprice}\n')
        textarea.insert(END, f'-------------------------------------------------------\n')
        if riceEntry.get()!='0':
            textarea.insert(END, f'Rice\t\t\t{riceEntry.get()}\t\t\tRs.{riceprice}\n')
        if oilEntry.get()!='0':
            textarea.insert(END, f'Oil\t\t\t{oilEntry.get()}\t\t\tRs.{oilprice}\n')
        if daalEntry.get()!='0':
            textarea.insert(END, f'Daal\t\t\t{daalEntry.get()}\t\t\tRs.{daalprice}\n')
        if wheetEntry.get()!='0':
            textarea.insert(END, f'Wheat\t\t\t{wheetEntry.get()}\t\t\tRs.{wheatprice}\n')
        if sugarEntry.get()!='0':
            textarea.insert(END, f'Sugar\t\t\t{sugarEntry.get()}\t\t\tRs.{sugarprice}\n')
        if teaEntry.get()!='0':
            textarea.insert(END, f'Tea\t\t\t{teaEntry.get()}\t\t\tRs.{teaprice}\n')
        textarea.insert(END, f'-------------------------------------------------------\n')
        if maazaEntry.get()!='0':
            textarea.insert(END, f'Maaza\t\t\t{maazaEntry.get()}\t\t\tRs.{maazaprice}\n')
        if pepsiEntry.get()!='0':
            textarea.insert(END, f'Pepsi\t\t\t{pepsiEntry.get()}\t\t\tRs.{pepsiprice}\n')
        if spriteEntry.get()!='0':
            textarea.insert(END, f'Sprite\t\t\t{spriteEntry.get()}\t\t\tRs.{spriteprice}\n')
        if dewEntry.get()!='0':
            textarea.insert(END, f'Dew\t\t\t{dewEntry.get()}\t\t\tRs.{dewprice}\n')
        if frootiEntry.get()!='0':
            textarea.insert(END, f'Frooti\t\t\t{frootiEntry.get()}\t\t\tRs.{frootiprice}\n')
        if coco_colaEntry.get()!='0':
            textarea.insert(END, f'Coco Cola\t\t\t{coco_colaEntry.get()}\t\t\tRs.{cococolaprice}\n')
        textarea.insert(END,'-------------------------------------------------------\n')

        if cosmetic_tax_Entry.get()!='0.0 Rs':
            textarea.insert(END,f'Cosmetic Tax\t\t\t{cosmetic_tax_Entry.get()}\n')
        if grocery_tax_Entry.get()!='0.0 Rs':
            textarea.insert(END,f'Grocery Tax\t\t\t{grocery_tax_Entry.get()}\n')
        if drink_tax_Entry.get()!='0.0 Rs':
            textarea.insert(END,f'Cool Drinks Tax\t\t\t{drink_tax_Entry.get()}\n\n')

        textarea.insert(END,f'Total Bill\t\t\tRs. {totalbill}\n')
        textarea.insert(END,'-------------------------------------------------------\n')
        save_bill()

# command for search button
def search_bill():
    for i in os.listdir(f'bills/'):
        # if the bill number searching is matching with the file name
        # "i.split('.')" means i value (ex: 741.txt) will split into two by the . mark (741 & txt)
        # [0] compair the first element of the list
        if i.split('.')[0] == billEntry.get():
            # display the content of the bill on the bill area. Open the file in read mode
            f = open(f'bills/{i}', 'r')
            # delete everything in the area before display
            textarea.delete(1.0, END)
            # enter the content
            for data in f:
                textarea.insert(END, data)
            # close the file
            f.close()
            # if the bill successfully displayed, break the loop. So, the else part will not execute
            break

    # if the entered bill number is not valid
    else:
        messagebox.showerror('Error','Invalid Bill Number!')


# ------GUI Part-----

# create a window using TK() class. Assign the class to an object. 'root' is a object name/ window name
root=Tk()
# to change the title of the window use 'title()' method
root.title('Cashier System')
# to change the size of the window use 'geometry('width * height')' method
root.geometry('1300x685')
# to change/add an icon image use 'iconbitmap('icon_name')' method
root.iconbitmap('icon.ico')

# -----Heading------

# to add a text, first make a label using 'Label()' calss. 'Label(where the lable appear on/window_name, text, font(name,size,'bold'/'italic'/'underline'),
# background_color/bg_background,text_color/fg_foreground, boarder_bd, style to boarder_relief= GROOVE/FLAT/RIDGE)'
# 'headingLabel' is the name/ object_variable given to the label.
headingLabel = Label(root, text='Billing System', font=('times new roman', 30, 'bold'), bg='navy', fg='snow', bd=10, relief=RIDGE)
# to position the label on the window use pack() method. 'fill=X' will fill the label through the X axis
headingLabel.pack(fill=X)

# ------Customer Details Frame-------

# to create a label_frame use 'LabelFrame' class. There are two types---> LabelFrame() & Frame()
cus_detail_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'), bg='navy', fg='snow', bd=6, relief=RIDGE)
cus_detail_frame.pack(fill=X, pady=10)

# Name area
# create labels using Label() class. 'cus_detail_frame' is the place where the label appear
nameLabel = Label(cus_detail_frame, text='Name', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
# position the label using 'grid()' method. padx will make paddings to left & right. pady will make padding to top & bottom.
nameLabel.grid(row=0, column=0, padx=20, pady=2)
# create entry/text field using 'Entry()' class.'cus_detail_frame' is the place where the entry/text area appear
nameEntry = Entry(cus_detail_frame, font=('arial', 15), bd=6, width=18)
# position the entry/text field using 'grid()' method
nameEntry.grid(row=0, column=1, padx=8)

# Phone number area
phoneLabel = Label(cus_detail_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)
phoneEntry = Entry(cus_detail_frame, font=('arial', 15), bd=6, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

# Bill number area
billLabel = Label(cus_detail_frame, text='Bill Number', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
billLabel.grid(row=0, column=4, padx=20, pady=2)
billEntry = Entry(cus_detail_frame, font=('arial', 15), bd=6, width=18)
billEntry.grid(row=0, column=5, padx=8)

# search button
# create buttons using 'button()' class
searchButton = Button(cus_detail_frame, text='SEARCH', font=('arial', 12, 'bold'), bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

# -------Products Section-------

# create a frame using 'Frame()' class
productFrame = Frame(root)
productFrame.pack(fill=X)

# create a label frame inside the productFrame using 'LabelFrame()'
cosmeticsFrame = LabelFrame(productFrame, text='Cosmetics', font=('times new roman', 15, 'bold'), bg='navy', fg= 'snow', bd=6, relief=RIDGE)
cosmeticsFrame.grid(row=0, column=0, padx=5)

# the labels & entries under the cosmetics frame
# bath soap
soapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
soapLabel.grid(row=0, column=0, padx=10, pady=2, sticky='w')
# Entry() is a class and in that class there are methods 'get()' method to get the value from entry field and 'insert()' method to insert values to entry field.
soapEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
soapEntry.grid(row=0, column=1, padx=8, pady=5)
# insert() function will insert default value to entry field
soapEntry.insert(0,0)

# face cream
face_creamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
face_creamLabel.grid(row=1, column=0, padx=10, pady=2, sticky='w')
face_creamEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
face_creamEntry.grid(row=1, column=1, padx=8, pady=5)
face_creamEntry.insert(0,0)

# face wash
face_washLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
face_washLabel.grid(row=2, column=0, padx=10, pady=2, sticky='w')
face_washEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
face_washEntry.grid(row=2, column=1, padx=8, pady=5)
face_washEntry.insert(0,0)

# hair spray
hair_sprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
hair_sprayLabel.grid(row=3, column=0, padx=10, pady=2, sticky='w')
hair_sprayEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
hair_sprayEntry.grid(row=3, column=1, padx=8, pady=5)
hair_sprayEntry.insert(0,0)

# hair gel
hair_gelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
hair_gelLabel.grid(row=4, column=0, padx=10, pady=2, sticky='w')
hair_gelEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
hair_gelEntry.grid(row=4, column=1, padx=8, pady=5)
hair_gelEntry.insert(0,0)

# body lotion
body_lotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
body_lotionLabel.grid(row=5, column=0, padx=10, pady=2, sticky='w')
body_lotionEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
body_lotionEntry.grid(row=5, column=1, padx=8, pady=5)
body_lotionEntry.insert(0,0)


# create a label frame inside the productFrame using 'LabelFrame()'
groceryFrame = LabelFrame(productFrame, text='Grocery', font=('times new roman', 15, 'bold'), bg='navy', fg= 'snow', bd=6, relief=RIDGE)
groceryFrame.grid(row=0, column=1, padx=5)

# the labels & entries under the grocery frame
# Rice
riceLabel = Label(groceryFrame, text='Rice', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
riceLabel.grid(row=0, column=0, padx=10, pady=2, sticky='w')
riceEntry = Entry(groceryFrame, font=('arial', 15), bd=6, width=10)
riceEntry.grid(row=0, column=1, padx=8, pady=5)
riceEntry.insert(0,0)

# Oli
oilLabel = Label(groceryFrame, text='Oil', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
oilLabel.grid(row=1, column=0, padx=10, pady=2, sticky='w')
oilEntry = Entry(groceryFrame, font=('arial', 15), bd=6, width=10)
oilEntry.grid(row=1, column=1, padx=8, pady=5)
oilEntry.insert(0,0)

# Daal
daalLabel = Label(groceryFrame, text='Daal', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
daalLabel.grid(row=2, column=0, padx=10, pady=2, sticky='w')
daalEntry = Entry(groceryFrame, font=('arial', 15), bd=6, width=10)
daalEntry.grid(row=2, column=1, padx=8, pady=5)
daalEntry.insert(0,0)

# wheet
wheetLabel = Label(groceryFrame, text='Wheet', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
wheetLabel.grid(row=3, column=0, padx=10, pady=2, sticky='w')
wheetEntry = Entry(groceryFrame, font=('arial', 15), bd=6, width=10)
wheetEntry.grid(row=3, column=1, padx=8, pady=5)
wheetEntry.insert(0,0)

# sugar
sugarLabel = Label(groceryFrame, text='Sugar', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
sugarLabel.grid(row=4, column=0, padx=10, pady=2, sticky='w')
sugarEntry = Entry(groceryFrame, font=('arial', 15), bd=6, width=10)
sugarEntry.grid(row=4, column=1, padx=8, pady=5)
sugarEntry.insert(0,0)

# tea
teaLabel = Label(groceryFrame, text='Tea', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
teaLabel.grid(row=5, column=0, padx=10, pady=2, sticky='w')
teaEntry = Entry(groceryFrame, font=('arial', 15), bd=6, width=10)
teaEntry.grid(row=5, column=1, padx=8, pady=5)
teaEntry.insert(0,0)


# create a label frame inside the productFrame using 'LabelFrame()'
cool_drinks_Frame = LabelFrame(productFrame, text='Cool Drinks', font=('times new roman', 15, 'bold'), bg='navy', fg= 'snow', bd=6, relief=RIDGE)
cool_drinks_Frame.grid(row=0, column=2, padx=5)

# the labels & entries under the cool drinks frame
# maaza
maazaLabel = Label(cool_drinks_Frame, text='Maaza', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
maazaLabel.grid(row=0, column=0, padx=10, pady=2, sticky='w')
maazaEntry = Entry(cool_drinks_Frame, font=('arial', 15), bd=6, width=10)
maazaEntry.grid(row=0, column=1, padx=8, pady=5)
maazaEntry.insert(0,0)

# pepsi
pepsiLabel = Label(cool_drinks_Frame, text='Pepsi', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
pepsiLabel.grid(row=1, column=0, padx=10, pady=2, sticky='w')
pepsiEntry = Entry(cool_drinks_Frame, font=('arial', 15), bd=6, width=10)
pepsiEntry.grid(row=1, column=1, padx=8, pady=5)
pepsiEntry.insert(0,0)

# sprite
spriteLabel = Label(cool_drinks_Frame, text='Sprite', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
spriteLabel.grid(row=2, column=0, padx=10, pady=2, sticky='w')
spriteEntry = Entry(cool_drinks_Frame, font=('arial', 15), bd=6, width=10)
spriteEntry.grid(row=2, column=1, padx=8, pady=5)
spriteEntry.insert(0,0)

# dew
dewLabel = Label(cool_drinks_Frame, text='Dew', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
dewLabel.grid(row=3, column=0, padx=10, pady=2, sticky='w')
dewEntry = Entry(cool_drinks_Frame, font=('arial', 15), bd=6, width=10)
dewEntry.grid(row=3, column=1, padx=8, pady=5)
dewEntry.insert(0,0)

# frooti
frootiLabel = Label(cool_drinks_Frame, text='Frooti', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
frootiLabel.grid(row=4, column=0, padx=10, pady=2, sticky='w')
frootiEntry = Entry(cool_drinks_Frame, font=('arial', 15), bd=6, width=10)
frootiEntry.grid(row=4, column=1, padx=8, pady=5)
frootiEntry.insert(0,0)

# coco_cola
coco_colaLabel = Label(cool_drinks_Frame, text='Coco Cola', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
coco_colaLabel.grid(row=5, column=0, padx=10, pady=2, sticky='w')
coco_colaEntry = Entry(cool_drinks_Frame, font=('arial', 15), bd=6, width=10)
coco_colaEntry.grid(row=5, column=1, padx=8, pady=5)
coco_colaEntry.insert(0,0)


# -------Bill Area-------

billFrame = Frame(productFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3, padx=8)

bill_area_Label = Label(billFrame, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE, bg='navy', fg='snow')
bill_area_Label.pack(fill=X)

# to add a scrollbar, use 'Scrollbar()' class. Use orient to to make vertical or horizontal scrollbar
scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# to create a text area, use 'text()' class. To set the scrollbar with the text area, use 'yscrollcommand=scrollbar.set' command.
textarea = Text(billFrame, height=15, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
#set the scrollbar comparatively to the text
scrollbar.config(command=textarea.yview)

# ------Bill Menue------

# Bill menu frame
bill_menu_Frame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'), bg='navy', fg= 'snow', bd=6, relief=RIDGE)

bill_menu_Frame.pack(pady=10)

# cosmetic price
cosmetic_price_Label = Label(bill_menu_Frame, text='Cosmetic Price', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
cosmetic_price_Label.grid(row=0, column=0, padx=10, pady=2, sticky='w')
cosmetic_price_Entry = Entry(bill_menu_Frame, font=('arial', 15), bd=6, width=10)
cosmetic_price_Entry.grid(row=0, column=1, padx=10, pady=5)
# grocery price
grocery_price_Label = Label(bill_menu_Frame, text='Grocery Price', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
grocery_price_Label.grid(row=1, column=0, padx=10, pady=2, sticky='w')
grocery_price_Entry = Entry(bill_menu_Frame, font=('arial', 15), bd=6, width=10)
grocery_price_Entry.grid(row=1, column=1, padx=10, pady=5)
# cool drink price
drink_price_Label = Label(bill_menu_Frame, text='Cool Drink Price', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
drink_price_Label.grid(row=2, column=0, padx=10, pady=2, sticky='w')
drink_price_Entry = Entry(bill_menu_Frame, font=('arial', 15), bd=6, width=10)
drink_price_Entry.grid(row=2, column=1, padx=10, pady=5)

# cosmetic tax
cosmetic_tax_Label = Label(bill_menu_Frame, text='Cosmetic Tax', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
cosmetic_tax_Label.grid(row=0, column=2, padx=10, pady=2, sticky='w')
cosmetic_tax_Entry = Entry(bill_menu_Frame, font=('arial', 15), bd=6, width=10)
cosmetic_tax_Entry.grid(row=0, column=3, padx=10, pady=5)
# grocery tax
grocery_tax_Label = Label(bill_menu_Frame, text='Grocery Tax', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
grocery_tax_Label.grid(row=1, column=2, padx=10, pady=2, sticky='w')
grocery_tax_Entry = Entry(bill_menu_Frame, font=('arial', 15), bd=6, width=10)
grocery_tax_Entry.grid(row=1, column=3, padx=10, pady=5)
# cool drink tax
drink_tax_Label = Label(bill_menu_Frame, text='Cool Drink Tax', font=('times new roman', 15, 'bold'), bg='navy', fg='snow')
drink_tax_Label.grid(row=2, column=2, padx=10, pady=2, sticky='w')
drink_tax_Entry = Entry(bill_menu_Frame, font=('arial', 15), bd=6, width=10)
drink_tax_Entry.grid(row=2, column=3, padx=10, pady=5)

# ------ BUTTONS-------

# create a frame for buttons
buttonFrame = Frame(bill_menu_Frame, bd=6, relief=GROOVE)
# rowspan will combine rows
buttonFrame.grid(row=0, column=4, rowspan=3, padx=5)

# create buttons using button class. Add commands to the button
# In command, total is a function name and must define the function at the top.
totalButton = Button(buttonFrame, text='Total', font=('arial',16,'bold'), bg='navy', fg='snow', bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonFrame, text='Bill', font=('arial',16,'bold'), bg='navy', fg='snow', bd=5, width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonFrame, text='Email', font=('arial',16,'bold'), bg='navy', fg='snow', bd=5, width=8, pady=10)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(buttonFrame, text='Print', font=('arial',16,'bold'), bg='navy', fg='snow', bd=5, width=8, pady=10)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonFrame, text='Clear', font=('arial',16,'bold'), bg='navy', fg='snow', bd=5, width=8, pady=10)
clearButton.grid(row=0, column=4, pady=20, padx=5)

# to see the window continuously/hold the window use 'mainloop()' method inside TK class
root.mainloop()
# tkinter is a module/container/file which contain classes and methods which help to create GUI.
from tkinter import *
# create a window using TK() class. Assign the class to an object. 'root' is a object name/ window name
root=Tk()
# to change the title of the window use 'title()' method
root.title('Cashier System')
# to change the size of the window use 'geometry('width * height')' method
root.geometry('1270x685')
# to change/add an icon image use 'iconbitmap('icon_name')' method
root.iconbitmap('icon.ico')

# -----Heading------

# to add a text, first make a label using 'Label()' calss. 'Label(where the lable appear on/window_name, text, font(name,size,'bold'/'italic'/'underline'),
# background_color/bg_background,text_color/fg_foreground, boarder_bd, style to boarder_relief= GROOVE/FLAT/RIDGE)'
# 'headingLabel' is the name/ object_variable given to the label.
headingLabel = Label(root, text='Billing System', font=('times new roman', 30, 'bold'), bg='MistyRose4', fg='snow', bd=10, relief=RIDGE)
# to position the label on the window use pack() method. 'fill=X' will fill the label through the X axis
headingLabel.pack(fill=X)

# ------Customer Details Frame-------

# to create a label_frame use 'LabelFrame' class. There are two types---> LabelFrame() & Frame()
cus_detail_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow', bd=6, relief=RIDGE)
cus_detail_frame.pack(fill=X, pady=10)

# Name area
# create labels using Label() class. 'cus_detail_frame' is the place where the label appear
nameLabel = Label(cus_detail_frame, text='Name', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
# position the label using 'grid()' method. padx will make paddings to left & right. pady will make padding to top & bottom.
nameLabel.grid(row=0, column=0, padx=20, pady=2)
# create entry/text field using 'Entry()' class.'cus_detail_frame' is the place where the entry/text area appear
nameEntry = Entry(cus_detail_frame, font=('arial', 15), bd=6, width=18)
# position the entry/text field using 'grid()' method
nameEntry.grid(row=0, column=1, padx=8)

# Phone number area
phoneLabel = Label(cus_detail_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)
phoneEntry = Entry(cus_detail_frame, font=('arial', 15), bd=6, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

# Bill number area
billLabel = Label(cus_detail_frame, text='Bill Number', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
billLabel.grid(row=0, column=4, padx=20, pady=2)
billEntry = Entry(cus_detail_frame, font=('arial', 15), bd=6, width=18)
billEntry.grid(row=0, column=5, padx=8)

# search button
# create buttons using 'button()' class
searchButton = Button(cus_detail_frame, text='SEARCH', font=('arial', 12, 'bold'), bd=7, width=10)
searchButton.grid(row=0, column=6, padx=20, pady=8)

# -------Products Section-------

# create a frame using 'Frame()' class
productFrame = Frame(root)
productFrame.pack(fill=X)

# create a label frame inside the productFrame using 'LabelFrame()'
cosmeticsFrame = LabelFrame(productFrame, text='Cosmetics', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg= 'snow', bd=6, relief=RIDGE)
cosmeticsFrame.grid(row=0, column=0, padx=5)

# the labels & entries under the cosmetics frame
# bath soap
soapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
soapLabel.grid(row=0, column=0, padx=10, pady=2, sticky='w')
soapEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
soapEntry.grid(row=0, column=1, padx=8, pady=3)

# face cream
face_creamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
face_creamLabel.grid(row=1, column=0, padx=10, pady=2, sticky='w')
face_creamEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
face_creamEntry.grid(row=1, column=1, padx=8, pady=3)

# face wash
face_washLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
face_washLabel.grid(row=2, column=0, padx=10, pady=2, sticky='w')
face_washEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
face_washEntry.grid(row=2, column=1, padx=8, pady=3)

# hair spray
hair_sprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
hair_sprayLabel.grid(row=3, column=0, padx=10, pady=2, sticky='w')
hair_sprayEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
hair_sprayEntry.grid(row=3, column=1, padx=8, pady=3)

# hair gel
hair_gelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
hair_gelLabel.grid(row=4, column=0, padx=10, pady=2, sticky='w')
hair_gelEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
hair_gelEntry.grid(row=4, column=1, padx=8, pady=3)

# body lotion
body_lotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
body_lotionLabel.grid(row=5, column=0, padx=10, pady=2, sticky='w')
body_lotionEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
body_lotionEntry.grid(row=5, column=1, padx=8, pady=3)

# create a label frame inside the productFrame using 'LabelFrame()'
cosmeticsFrame = LabelFrame(productFrame, text='Cosmetics', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg= 'snow', bd=6, relief=RIDGE)
cosmeticsFrame.grid(row=0, column=1, padx=5)

# the labels & entries under the cosmetics frame
# bath soap
soapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
soapLabel.grid(row=0, column=0, padx=10, pady=2, sticky='w')
soapEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
soapEntry.grid(row=0, column=1, padx=8, pady=3)

# face cream
face_creamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
face_creamLabel.grid(row=1, column=0, padx=10, pady=2, sticky='w')
face_creamEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
face_creamEntry.grid(row=1, column=1, padx=8, pady=3)

# face wash
face_washLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
face_washLabel.grid(row=2, column=0, padx=10, pady=2, sticky='w')
face_washEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
face_washEntry.grid(row=2, column=1, padx=8, pady=3)

# hair spray
hair_sprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
hair_sprayLabel.grid(row=3, column=0, padx=10, pady=2, sticky='w')
hair_sprayEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
hair_sprayEntry.grid(row=3, column=1, padx=8, pady=3)

# hair gel
hair_gelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
hair_gelLabel.grid(row=4, column=0, padx=10, pady=2, sticky='w')
hair_gelEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
hair_gelEntry.grid(row=4, column=1, padx=8, pady=3)

# body lotion
body_lotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
body_lotionLabel.grid(row=5, column=0, padx=10, pady=2, sticky='w')
body_lotionEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
body_lotionEntry.grid(row=5, column=1, padx=8, pady=3)


# create a label frame inside the productFrame using 'LabelFrame()'
cosmeticsFrame = LabelFrame(productFrame, text='Cosmetics', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg= 'snow', bd=6, relief=RIDGE)
cosmeticsFrame.grid(row=0, column=2, padx=5)

# the labels & entries under the cosmetics frame
# bath soap
soapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
soapLabel.grid(row=0, column=0, padx=10, pady=2, sticky='w')
soapEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
soapEntry.grid(row=0, column=1, padx=8, pady=3)

# face cream
face_creamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
face_creamLabel.grid(row=1, column=0, padx=10, pady=2, sticky='w')
face_creamEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
face_creamEntry.grid(row=1, column=1, padx=8, pady=3)

# face wash
face_washLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
face_washLabel.grid(row=2, column=0, padx=10, pady=2, sticky='w')
face_washEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
face_washEntry.grid(row=2, column=1, padx=8, pady=3)

# hair spray
hair_sprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
hair_sprayLabel.grid(row=3, column=0, padx=10, pady=2, sticky='w')
hair_sprayEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
hair_sprayEntry.grid(row=3, column=1, padx=8, pady=3)

# hair gel
hair_gelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
hair_gelLabel.grid(row=4, column=0, padx=10, pady=2, sticky='w')
hair_gelEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
hair_gelEntry.grid(row=4, column=1, padx=8, pady=3)

# body lotion
body_lotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), bg='MistyRose4', fg='snow')
body_lotionLabel.grid(row=5, column=0, padx=10, pady=2, sticky='w')
body_lotionEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=6, width=10)
body_lotionEntry.grid(row=5, column=1, padx=8, pady=3)


# -------Bill Area-------

billFrame = Frame(productFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3)

bill_area_Label = Label(billFrame, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
bill_area_Label.pack(fill=X)

# to create a text area, use 'text()' class.
textarea = Text(billFrame, height=15, width=45)
textarea.pack()

# to see the window continuously/hold the window use 'mainloop()' method inside TK class
root.mainloop()
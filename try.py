from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random,os,tempfile,smtplib
import subprocess

root=Tk()
root.geometry("1525x900+0+0")
root.config(bg="white")
img = PhotoImage(file='C:/project/lg.png')
Label(root,image=img,bg='white').place(x=50,y=150)
global c,d
c=StringVar()
d=StringVar()
frame=Frame(root,width=450,height=450,bg="white")
frame.place(x=880,y=170)

heading=Label(frame,text='USER LOGIN ',fg='black',bg='white',font=('times',23,'bold'))
heading.place(x=100,y=0)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg="white",textvariable=c,font=('times',15))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code = Entry(frame,width=25,fg='black',border=0,bg="white",textvariable=d,font=('times',15))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
####################################################################


def login():
    try:
        conn=mysql.connector.connect(host="localhost",user="root",password="",port="3306",database="supermarket")
        cursor=conn.cursor()
    except:
        messagebox.showerror("Error","unable to connect")

    username1=user.get()
    password1=code.get()
    

    insert_query="select * from employ where `employId`=%s and password=%s;"
    vals=(username1,password1)
    cursor.execute(insert_query,vals)
    a=cursor.fetchone()
    if a:
        root.destroy()
        root1 = Tk()
        root1.title('Retail Billing System')
        root1.geometry('1700x925+0+0')
        root1.config(bg="white")
        def clear():
            bathsoapEntry.delete(0,END)
            facewashEntry.delete(0,END)
            facecreamEntry.delete(0,END)
            bodylotionEntry.delete(0,END)
            hairgelEntry.delete(0,END)
            hairsprayEntry.delete(0,END)
            daalEntry.delete(0,END)
            wheatEntry.delete(0,END)
            riceEntry.delete(0,END)
            oilEntry.delete(0,END)
            sugarEntry.delete(0,END)
            teaEntry.delete(0,END)

            cococolaEntry.delete(0,END)
            pepsiEntry.delete(0,END)
            dewEntry.delete(0,END)
            maazaEntry.delete(0,END)
            frootiEntry.delete(0,END)
            spriteEntry.delete(0,END)

            bathsoapEntry.insert(0, 0)
            facecreamEntry.insert(0, 0)
            hairsprayEntry.insert(0, 0)
            hairgelEntry.insert(0, 0)
            bodylotionEntry.insert(0, 0)
            facewashEntry.insert(0, 0)

            daalEntry.insert(0, 0)
            wheatEntry.insert(0, 0)
            riceEntry.insert(0, 0)
            oilEntry.insert(0, 0)
            sugarEntry.insert(0, 0)
            teaEntry.insert(0, 0)

            pepsiEntry.insert(0, 0)
            cococolaEntry.insert(0, 0)
            maazaEntry.insert(0, 0)
            dewEntry.insert(0, 0)
            spriteEntry.insert(0, 0)
            frootiEntry.insert(0,0)

            cosmetictaxEntry.delete(0,END)
            grocerytaxEntry.delete(0,END)
            drinkstaxEntry.delete(0,END)

            cosmeticpriceEntry.delete(0,END)
            grocerypriceEntry.delete(0,END)
            drinkspriceEntry.delete(0,END)

            nameEntry.delete(0,END)
            phoneEntry.delete(0,END)
            
            
            
            phoneEntry.insert(END,"+91")
            billnumberEntry.delete(0,END)

            textarea.delete(1.0,END)
        def print_bill():
            if textarea.get(1.0,END)=='\n':
                messagebox.showerror('Error','Bill is empty')
            else:
                file=tempfile.mktemp('.txt')
                open(file,'w').write(textarea.get(1.0,END))
                os.startfile(file,'print')
        def search_bill():
            for i in os.listdir('bills/'):
                if i.split('.')[0] == billnumberEntry.get():
                    f = open(f'bills/{i}', 'r')
                    textarea.delete('1.0', END)
                    for data in f:
                        textarea.insert(END, data)
                    f.close()
                    break
            else:
                messagebox.showerror('Error','Invalid Bill Number')
        if not os.path.exists('bills'):
           os.mkdir('bills')
        billnumber=random.randint(500,1000)
        def save_bill():
           
            
            result=messagebox.askyesno('Confirm','Do you want to save the bill?')
            if result:
                bill_content=textarea.get(1.0,END)
                billnumber=random.randint(500,1000)
                file=open(f'bills/{billnumber}.txt','w')
                file.write(bill_content)
                file.close()
                messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
                billnumber = random.randint(500, 1000)

        billnumber=random.randint(500,1000)
        def add():
            emp=employEntry.get()
            bill=billnumberEntry.get()
            conn=mysql.connector.connect(host="localhost",username="root",password="",port="3306",database="supermarket")
            cursor=conn.cursor()
            sql7=f"INSERT INTO `report`( `employ id`, `billno`) VALUES ('{emp}','{bill}')"
            #sql2=f"INSERT INTO employ(`employId`,``) VALUES('','{name}','{password}','{designation}','{Native}','{ phoneno}','{aadharno}'"
            cursor.execute(sql7)
            conn.commit()
            conn.close()
        def bill_area():
            billnumberEntry.insert(END,billnumber)
            if nameEntry.get()=='' or phoneEntry.get()=='':
                messagebox.showerror('Error','Customer Details Are Required')
               
                
               
            elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
                messagebox.showerror('Error', 'No Products are selected')
            elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
                messagebox.showerror('Error', 'No Products are selected')
            else:
                textarea.delete(1.0,END)
                textarea.insert(END,'\t\t**Welcome Customer**\n')
                textarea.insert(END,f'\nBill Number: {billnumber}\n')
                textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
                textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}\n')
                textarea.insert(END,'\n=======================================================')
                textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
                textarea.insert(END, '\n=======================================================')
                if bathsoapEntry.get()!='0':
                    textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
                if hairsprayEntry.get()!='0':
                    textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
                if hairgelEntry.get()!='0':
                    textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
                if facecreamEntry.get()!='0':
                    textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
                if facewashEntry.get()!='0':
                    textarea.insert(END,f'\nBody Lotion\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
                if bodylotionEntry.get()!='0':
                    textarea.insert(END,f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')
                
                if riceEntry.get()!='0':
                    textarea.insert(END,f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
                if oilEntry.get()!='0':
                    textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
                if sugarEntry.get()!='0':
                    textarea.insert(END,f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
                if wheatEntry.get()!='0':
                    textarea.insert(END,f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
                if daalEntry.get()!='0':
                    textarea.insert(END,f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
                if teaEntry.get()!='0':
                    textarea.insert(END,f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')
                if maazaEntry.get()!='0':
                    textarea.insert(END,f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
                if frootiEntry.get()!='0':
                    textarea.insert(END,f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
                if pepsiEntry.get()!='0':
                    textarea.insert(END,f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
                if cococolaEntry.get()!='0':
                    textarea.insert(END,f'\nCoco Cola\t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice} Rs')
                if dewEntry.get()!='0':
                    textarea.insert(END,f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')
                if spriteEntry.get()!='0':
                    textarea.insert(END,f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
                textarea.insert(END, '\n-------------------------------------------------------')
                if cosmetictaxEntry.get()!='0.0 Rs':
                    textarea.insert(END,f'\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}')
                if grocerytaxEntry.get()!='0.0 Rs':
                    textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')
                if drinkstaxEntry.get()!='0.0 Rs':
                    textarea.insert(END,f'\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()}')
                textarea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')
                textarea.insert(END, '\n-------------------------------------------------------')
                save_bill()
                add()
        def total():
            global soapprice,hairsprayprice,hairgelprice,facecreamprice,facewashprice,bodylotionprice
            global riceprice,daalprice,oilprice,sugarprice,wheatprice,teaprice
            global frootiprice,dewprice,pepsiprice,spriteprice,cococolaprice,maazaprice
            global totalbill
            #cosmetics price calculation
            soapprice=int(bathsoapEntry.get())*20
            facecreamprice=int(facecreamEntry.get())*50
            facewashprice = int(facewashEntry.get()) * 100
            hairsprayprice = int(hairsprayEntry.get()) * 150
            hairgelprice = int(hairgelEntry.get()) * 80
            bodylotionprice = int(bodylotionEntry.get()) * 60

            totalcosmeticprice=soapprice+facewashprice+facecreamprice+hairgelprice+hairsprayprice+bodylotionprice
            cosmeticpriceEntry.delete(0,END)
            cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
            cosmtictax=totalcosmeticprice*0.12
            cosmetictaxEntry.delete(0,END)
            cosmetictaxEntry.insert(0,str(cosmtictax) +' Rs')


            #grocery price calculation
            riceprice=int(riceEntry.get())*30
            daalprice=int(daalEntry.get())*100
            oilprice=int(oilEntry.get())*120
            sugarprice=int(sugarEntry.get())*50
            teaprice=int(teaEntry.get())*140
            wheatprice=int(wheatEntry.get())*80

            totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
            grocerypriceEntry.delete(0,END)
            grocerypriceEntry.insert(0,str(totalgroceryprice)+' Rs')
            grocerytax = totalgroceryprice * 0.05
            grocerytaxEntry.delete(0, END)
            grocerytaxEntry.insert(0, str(grocerytax) + ' Rs')

            maazaprice = int(maazaEntry.get()) * 50
            frootiprice = int(frootiEntry.get()) * 20
            dewprice = int(dewEntry.get()) * 30
            pepsiprice = int(pepsiEntry.get()) * 20
            spriteprice = int(spriteEntry.get()) * 45
            cococolaprice = int(cococolaEntry.get()) * 90

            totaldrinksprice=maazaprice+frootiprice+dewprice+pepsiprice+spriteprice+cococolaprice
            drinkspriceEntry.delete(0,END)
            drinkspriceEntry.insert(0,str(totaldrinksprice)+' Rs')
            drinkstax = totaldrinksprice * 0.08
            drinkstaxEntry.delete(0, END)
            drinkstaxEntry.insert(0, str(drinkstax) + ' Rs')

            totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmtictax+grocerytax+drinkstax




                


        headingLabel = Label(root1, text='Billing System', font=('times new roman', 30, 'bold'), bg='blue2', fg='gold', bd=12, relief=GROOVE)
        headingLabel.pack(fill=X)
        def logout():
            root1.destroy()
        sButton = Button(root1, text='logout',font=('times', 14, 'bold'), bd=7, width=12,command=logout)
        sButton.place(x=1290,y=9)
        emplabel=Label(root1,text="Employ ID", font=('times new roman', 15, 'bold'),bg="blue2",fg="white").place(x=20,y=20)
        employEntry = Entry(root1, font=('arial',15), bd=7,text="" ,width=18)
        employEntry.place(x=150,y=20)
        employEntry.insert(END,username1)

        customer_details_frame = LabelFrame(root1, text='Customer Details', font=('times new roman', 15, 'bold'),
                                        fg='gold', bd=8, relief=GROOVE, bg='blue2')
        customer_details_frame.pack(fill=X)

        nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'), bg='blue2',
                      fg='white')
        nameLabel.grid(row=0, column=0, padx=20)

        nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
        nameEntry.grid(row=0, column=1, padx=8)

        phoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='blue2',
                       fg='white')
        phoneLabel.grid(row=0, column=2, padx=20, pady=2)
        g=StringVar()
        phoneEntry = Entry(customer_details_frame, font=('arial', 15),textvariable=g, bd=7, width=18)
        phoneEntry.grid(row=0, column=3, padx=8)
        phoneEntry.insert(END,"+91")

        billnumberLabel = Label(customer_details_frame, text='Bill Number', font=('times new roman', 15, 'bold'), bg='blue2',
                            fg='white')
        billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

        billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7,text="" ,width=18)
        billnumberEntry.grid(row=0, column=5, padx=8)



        searchButton = Button(customer_details_frame, text='SEARCH',font=('arial', 12, 'bold'), bd=7, width=10,command=search_bill)
        searchButton.grid(row=0, column=6, padx=20, pady=8)

        productsFrame = Frame(root1)
        productsFrame.pack()

        cosmeticsFrame = LabelFrame(productsFrame, text='Cosmetics', font=('times new roman', 15, 'bold'),
                                fg='gold', bd=8, relief=GROOVE, bg='blue2')
        cosmeticsFrame.grid(row=0, column=0)

        bathsoapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), bg='blue2',
                          fg='white')
        bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

        bathsoapEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        bathsoapEntry.grid(row=0, column=1, pady=9, padx=10)
        bathsoapEntry.insert(0,0)

        facecreamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), bg='blue2',
                           fg='white')
        facecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

        facecreamEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        facecreamEntry.grid(row=1, column=1, pady=9, padx=10)
        facecreamEntry.insert(0,0)

        facewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='blue2',
                          fg='white')
        facewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

        facewashEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        facewashEntry.grid(row=2, column=1, pady=9, padx=10)
        facewashEntry.insert(0,0)

        hairsprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='blue2',
                           fg='white')
        hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

        hairsprayEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        hairsprayEntry.grid(row=3, column=1, pady=9, padx=10)
        hairsprayEntry.insert(0,0)

        hairgelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='blue2', fg='white')
        hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

        hairgelEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        hairgelEntry.grid(row=4, column=1, pady=9, padx=10)
        hairgelEntry.insert(0,0)

        bodylotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), bg='blue2',fg='white')
        bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

        bodylotionEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        bodylotionEntry.grid(row=5, column=1, pady=9, padx=10)
        bodylotionEntry.insert(0,0)

        groceryFrame = LabelFrame(productsFrame, text='Grocery', font=('times new roman', 15, 'bold'),
                              fg='gold', bd=8, relief=GROOVE, bg='blue2')
        groceryFrame.grid(row=0, column=1)

        riceLabel = Label(groceryFrame, text='Rice', font=('times new roman', 15, 'bold'), bg='blue2',
                      fg='white')
        riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

        riceEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        riceEntry.grid(row=0, column=1, pady=9, padx=10)
        riceEntry.insert(0,0)

        oilLabel = Label(groceryFrame, text='Oil', font=('times new roman', 15, 'bold'), bg='blue2',
                     fg='white')
        oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

        oilEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        oilEntry.grid(row=1, column=1, pady=9, padx=10)
        oilEntry.insert(0,0)

        daalLabel = Label(groceryFrame, text='Daal', font=('times new roman', 15, 'bold'), bg='blue2',
                      fg='white')
        daalLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

        daalEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        daalEntry.grid(row=2, column=1, pady=9, padx=10)
        daalEntry.insert(0,0)

        wheatLabel = Label(groceryFrame, text='Wheat', font=('times new roman', 15, 'bold'), bg='blue2',
                       fg='white')
        wheatLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

        wheatEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        wheatEntry.grid(row=3, column=1, pady=9, padx=10)
        wheatEntry.insert(0,0)

        sugarLabel = Label(groceryFrame, text='Sugar', font=('times new roman', 15, 'bold'), bg='blue2',
                       fg='white')
        sugarLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

        sugarEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        sugarEntry.grid(row=4, column=1, pady=9, padx=10)
        sugarEntry.insert(0,0)

        teaLabel = Label(groceryFrame, text='Tea', font=('times new roman', 15, 'bold'), bg='blue2',
                     fg='white')
        teaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

        teaEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        teaEntry.grid(row=5, column=1, pady=9, padx=10)
        teaEntry.insert(0,0)

        drinksFrame = LabelFrame(productsFrame, text='Cold Drinks', font=('times new roman', 15, 'bold'),
                             fg='gold', bd=8, relief=GROOVE, bg='blue2')
        drinksFrame.grid(row=0, column=2)

        maazaLabel = Label(drinksFrame, text='Maaza', font=('times new roman', 15, 'bold'), bg='blue2',
                       fg='white')
        maazaLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

        maazaEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        maazaEntry.grid(row=0, column=1, pady=9, padx=10)
        maazaEntry.insert(0,0)

        pepsiLabel = Label(drinksFrame, text='Pepsi', font=('times new roman', 15, 'bold'), bg='blue2',
                       fg='white')
        pepsiLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

        pepsiEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        pepsiEntry.grid(row=1, column=1, pady=9, padx=10)
        pepsiEntry.insert(0,0)

        spriteLabel = Label(drinksFrame, text='Sprite', font=('times new roman', 15, 'bold'), bg='blue2',
                        fg='white')
        spriteLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

        spriteEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        spriteEntry.grid(row=2, column=1, pady=9, padx=10)
        spriteEntry.insert(0,0)

        dewLabel = Label(drinksFrame, text='Dew', font=('times new roman', 15, 'bold'), bg='blue2',
                     fg='white')
        dewLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

        dewEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        dewEntry.grid(row=3, column=1, pady=9, padx=10)
        dewEntry.insert(0,0)

        frootiLabel = Label(drinksFrame, text='Frooti', font=('times new roman', 15, 'bold'), bg='blue2',
                        fg='white')
        frootiLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

        frootiEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        frootiEntry.grid(row=4, column=1, pady=9, padx=10)
        frootiEntry.insert(0,0)

        cococolaLabel = Label(drinksFrame, text='Coco Cola', font=('times new roman', 15, 'bold'), bg='blue2',
                          fg='white')
        cococolaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

        cococolaEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
        cococolaEntry.grid(row=5, column=1, pady=9, padx=10)
        cococolaEntry.insert(0,0)

        billframe = Frame(productsFrame, bd=8, relief=GROOVE)
        billframe.grid(row=0, column=3, padx=10)

        billareaLabel = Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
        billareaLabel.pack(fill=X)

        scrollbar = Scrollbar(billframe, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        textarea = Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
        textarea.pack()
        scrollbar.config(command=textarea.yview)

        billmenuFrame = LabelFrame(root1, text='Bill Menu', font=('times new roman', 15, 'bold'),
                               fg='gold', bd=8, relief=GROOVE, bg='blue2')
        billmenuFrame.pack()

        cosmeticpriceLabel = Label(billmenuFrame, text='Cosmetic Price', font=('times new roman', 14, 'bold'), bg='blue2',
                               fg='white')
        cosmeticpriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')

        cosmeticpriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
        cosmeticpriceEntry.grid(row=0, column=1, pady=6, padx=10)

        grocerypriceLabel = Label(billmenuFrame, text='Grocery Price', font=('times new roman', 14, 'bold'), bg='blue2',
                              fg='white')
        grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')

        grocerypriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
        grocerypriceEntry.grid(row=1, column=1, pady=6, padx=10)

        drinkspriceLabel = Label(billmenuFrame, text='Cold Drink Price', font=('times new roman', 14, 'bold'), bg='blue2',
                             fg='white')
        drinkspriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')

        drinkspriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
        drinkspriceEntry.grid(row=2, column=1, pady=6, padx=10)

        cosmetictaxLabel = Label(billmenuFrame, text='Cosmetic Tax', font=('times new roman', 14, 'bold'), bg='blue2',
                             fg='white')
        cosmetictaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')

        cosmetictaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
        cosmetictaxEntry.grid(row=0, column=3, pady=6, padx=10)

        grocerytaxLabel = Label(billmenuFrame, text='Grocery Tax', font=('times new roman', 14, 'bold'), bg='blue2',
                            fg='white')
        grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')

        grocerytaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
        grocerytaxEntry.grid(row=1, column=3, pady=6, padx=10)

        drinkstaxLabel = Label(billmenuFrame, text='Cold Drink Tax', font=('times new roman', 14, 'bold'), bg='blue2',
                           fg='white')
        drinkstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky='w')

        drinkstaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
        drinkstaxEntry.grid(row=2, column=3, pady=6, padx=10)

        buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
        buttonFrame.grid(row=0, column=4, rowspan=3)

        totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='blue2', fg='white', bd=5, width=8, pady=10,command=total)
        totalButton.grid(row=0, column=0, pady=20, padx=5)

        billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='blue2', fg='white'
                        , bd=5, width=8, pady=10,command=bill_area)
        billButton.grid(row=0, column=1, pady=20, padx=5)


        printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='blue2', fg='white'
                         , bd=5, width=8, pady=10,command=print_bill)
        printButton.grid(row=0, column=2, pady=20, padx=5)

        clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='blue2', fg='white'
                         , bd=5, width=8, pady=10,command=clear)
        clearButton.grid(row=0, column=3, pady=20, padx=5)

 
       
        root1.mainloop()
            
    else:
        messagebox.showerror("info","not match")
        
   

Button(frame,width=11,pady=10,text='Sign in',bg='red',fg='white',font=('times',15,"bold"),border=0,command=login).place(x=115,y=264)
if __name__ == '__main__':
    root.mainloop()

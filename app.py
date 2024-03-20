from tkinter import *
import time
import datetime
from tkinter import messagebox
import pygame
import sys
import random

#========================FORMULARIO==============================
pygame.init()
root = Tk()
root.title("SISTEMA LOJA: ")
root.resizable(False, False)

root.configure(background='blue')

FrameABC = Frame(root, bg = "black", bd=20, relief = RIDGE)
FrameABC.grid()

#=============================FRAMES=================================

FrameABC1 = Frame(FrameABC, bg = "green", bd=10, relief = RIDGE)
FrameABC1.grid(row=0 ,column = 0, columnspan = 4, sticky=W)

FrameABC2 = Frame(FrameABC, bg = "green", bd=10, relief = RIDGE)
FrameABC2.grid(row=1 ,column = 0, sticky=W)

FrameABC3 = Frame(FrameABC, bg = "green", bd=10, relief = RIDGE)
FrameABC3.grid(row=1 ,column = 1, sticky=W)

FrameABC4 = Frame(FrameABC, bg = "green", bd=10, relief = RIDGE)
FrameABC4.grid(row=1 ,column = 2, sticky=W)

FrameABC5 = Frame(FrameABC4, bg = "green", bd=10, relief = RIDGE)
FrameABC5.grid(row=0 ,column = 0, sticky=W)

FrameABC6 = Frame(FrameABC4, bg = "green", bd=10, relief = RIDGE)
FrameABC6.grid(row=1 ,column = 0, columnspan = 4, sticky=W)

#==================================VARIAVEIS============================

Date1 = StringVar ()
Time1 = StringVar ()

Receipt_Ref =  StringVar ()
Tax = StringVar ()
SubTotal = StringVar ()
Total = StringVar ()

Jeans_Jeggers = StringVar ()
Coats_Jackets = StringVar ()
Sportwear = StringVar ()
Dresses = StringVar ()
Skirts = StringVar()
Swimwear = StringVar ()
School_Uniform = StringVar ()
Pyjamas = StringVar ()

Jackets_Blazers = StringVar ()
Formal_Trousers = StringVar ()
Formal_Shirts = StringVar ()
Mens_Boots = StringVar ()

Bed_Sheet = StringVar ()
Pillows = StringVar ()
Patterned_Bedding = StringVar ()
Mattress_Protectors = StringVar ()

Jeans_Jeggers.set ("0")
Coats_Jackets.set ("0")
Sportwear.set ("0")
Dresses.set ("0")
Skirts.set ("0")
Swimwear.set ("0")
School_Uniform.set ("0")
Pyjamas.set ("0")
Jackets_Blazers.set ("0")
Formal_Trousers.set ("0")
Formal_Shirts.set ("0")
Mens_Boots.set ("0")
Bed_Sheet.set ("0")
Pillows.set ("0")
Patterned_Bedding.set ("0")
Mattress_Protectors.set ("0")

Date1.set(time.strftime ("%d/%m/%Y"))
Time1.set(time.strftime ("%H:%M:%S"))

#===================================FUNÇÕES=================================

def Exit (): 
    result = messagebox.askquestion("Cliente", "Deseja realmente sair?")
    if result == 'yes' :
        root.destroy ()
        return

def reset (): 
    txtReceipt.delete("1.0", END)
    Jeans_Jeggers.set ("0")
    Coats_Jackets.set ("0")
    Sportwear.set ("0")
    Dresses.set ("0")
    Skirts.set ("0")
    Swimwear.set ("0")
    School_Uniform.set ("0")
    Pyjamas.set ("0")
    Jackets_Blazers.set ("0")
    Formal_Trousers.set ("0")
    Formal_Shirts.set ("0")
    Mens_Boots.set ("0")
    Bed_Sheet.set ("0")
    Pillows.set ("0")
    Patterned_Bedding.set ("0")
    Mattress_Protectors.set ("0")


def Total (): 
    
    Item1 = float(Jeans_Jeggers.get())
    Item2 = float(Coats_Jackets.get())
    Item3 = float(Sportwear.get())
    Item4 = float(Dresses.get())
    Item5 = float(Skirts.get())
    Item6 = float(Swimwear.get())
    Item7 = float(School_Uniform.get())
    Item8 = float(Pyjamas.get())
    Item9 = float(Jackets_Blazers.get())
    Item10 = float(Formal_Trousers.get())
    Item11 = float(Formal_Shirts.get())
    Item12 = float(Mens_Boots.get())
    Item13 = float(Bed_Sheet.get())
    Item14 = float(Pillows.get())
    Item15 = float(Patterned_Bedding.get())
    Item16 = float(Mattress_Protectors.get())

    PriceofItem1 = ("$") + str('%.2f'%(Item1 * 80.00))
    PriceofItem2 = ("$") + str('%.2f'%(Item2 * 95.00))
    PriceofItem3 = ("$") + str('%.2f'%(Item3 * 50.00))
    PriceofItem4 = ("$") + str('%.2f'%(Item4 * 120.00))

    PriceofItem5 = ("$") + str('%.2f'%(Item5 * 60.00))
    PriceofItem6 = ("$") + str('%.2f'%(Item6 * 45.00))
    PriceofItem7 = ("$") + str('%.2f'%(Item7 * 70.00))
    PriceofItem8 = ("$") + str('%.2f'%(Item8 * 50.00))

    PriceofItem9 = ("$") + str('%.2f'%(Item9 * 110.00))
    PriceofItem10 = ("$") + str('%.2f'%(Item10 * 90.00))
    PriceofItem11 = ("$") + str('%.2f'%(Item11 * 75.00))
    PriceofItem12 = ("$") + str('%.2f'%(Item12 * 80.00))

    PriceofItem13 = ("$") + str('%.2f'%(Item13 * 40.00)) 
    PriceofItem14 = ("$") + str('%.2f'%(Item14 * 30.00))
    PriceofItem15 = ("$") + str('%.2f'%(Item15 * 60.00))
    PriceofItem16 = ("$") + str('%.2f'%(Item16 * 400.00))

    Feminino = (Item1 * 80.00) + (Item2 * 95.00) + (Item3 * 50.00) + (Item4 * 120.00)
    Criança = (Item5 * 60.00) + (Item6 * 45.00) + (Item7 * 70.00) + (Item8 * 50.00)
    Masculino = (Item9 * 110.00) + (Item10 * 90.00) + (Item11 * 75.00) + (Item12 * 80.00)
    Casa = (Item13 * 40.00) + (Item14 * 30.00) + (Item15 * 60.00) + (Item16 * 400.00)

    SubTotalofITEMS = ("$") + str('%.2f'%(Feminino + Criança +  Masculino + Casa))
    Tax = ("$") + str('%.2f'%((Feminino + Criança +  Masculino + Casa) * 0.25))

    TT = (Feminino + Criança +  Masculino + Casa)
    TC = ((Feminino + Criança +  Masculino + Casa) * 0.25)

    TotalCost = ("$") + str('%.2f'% (TT + TC))

    txtReceipt.delete("1.0", END)
    x = random.randint(10747, 500298)
    randomRef = str(x)
    Receipt_Ref.set("CUPOM" + randomRef)
    txtReceipt.insert(END, 'Cupom Ref: \t\t\t' + Receipt_Ref.get() + '\n' + Date1.get() + '\t\t\t' + Time1.get() + '\n')
    txtReceipt.insert(END, '-----------------------------------------------------------------' + '\n')
    txtReceipt.insert(END, 'Item: \t\t\t '+ "Preço do Item \n")
    txtReceipt.insert(END, '-----------------------------------------------------------------' + '\n')

    txtReceipt.insert(END, 'Blusa Jeans: \t\t\t '+ PriceofItem1 + "\n")
    txtReceipt.insert(END, 'Casaco: \t\t\t '+  PriceofItem2 + "\n")
    txtReceipt.insert(END, 'Roupa Sport: \t\t\t '+ PriceofItem3 + "\n")
    txtReceipt.insert(END, 'Vestidos: \t\t\t '+ PriceofItem4 + "\n")

    txtReceipt.insert(END, 'Saias: \t\t\t '+ PriceofItem5 + "\n")
    txtReceipt.insert(END, 'Natação: \t\t\t '+ PriceofItem6 + "\n")
    txtReceipt.insert(END, 'Uniforme: \t\t\t '+ PriceofItem7 + "\n")
    txtReceipt.insert(END, 'Pijama: \t\t\t '+ PriceofItem8 + "\n")

    txtReceipt.insert(END, 'Casacos: \t\t\t '+ PriceofItem9 + "\n")
    txtReceipt.insert(END, 'Calças: \t\t\t '+ PriceofItem10 + "\n")
    txtReceipt.insert(END, 'Camisetas: \t\t\t '+ PriceofItem11 + "\n")
    txtReceipt.insert(END, 'Calçados: \t\t\t '+ PriceofItem12 + "\n")

    txtReceipt.insert(END, 'Lençol: \t\t\t '+ PriceofItem13 + "\n")
    txtReceipt.insert(END, 'Travesseiro: \t\t\t '+ PriceofItem14 + "\n")
    txtReceipt.insert(END, 'Edredom: \t\t\t '+ PriceofItem15 + "\n")
    txtReceipt.insert(END, 'Colchão: \t\t\t '+ PriceofItem16 + "\n")

#===================================CAIXA DE HORAS/DATA/TITULO=================================

lblDate = Label(FrameABC1, width = 16, textvariable = Date1,font=('arial',30,'bold'), padx = 9 , pady =9,
                bd = 14, bg="Cadet Blue", fg="Cornsilk", justify=CENTER) .grid(row=0, column = 0)

lblTitle = Label(FrameABC1, width = 16, text ="\tSistema de loja\t",font=('arial',31,'bold'), padx = 9 , pady =9,
                bd = 14, bg="Cadet Blue", fg="Cornsilk", justify=CENTER) .grid(row=0, column = 1)

lblTime = Label(FrameABC1, width = 16, textvariable = Time1,font=('arial',30,'bold'), padx = 9 , pady =9,
                bd = 14, bg="Cadet Blue", fg="Cornsilk", justify=CENTER) .grid(row=0, column = 2)

#===================================LABEL FEMININO=================================

lblFeminino = Label(FrameABC2, text="Feminino",font=('arial',20,'bold'), padx = 8 , pady =1,
                bd = 8, bg="yellow", fg="black", width = 25 ,justify=CENTER) .grid(row=0, column = 0, columnspan = 4)

lblJeans_Jeggers = Label(FrameABC2, text="Blusa Jeans: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=1, column = 0,)

lblCoats_jackets = Label(FrameABC2, text="Casaco: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=2, column = 0)

lblSportwear = Label(FrameABC2, text="Roupa Sport: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=3, column = 0)

lblDresses = Label(FrameABC2, text="Vestidos: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=4, column = 0)

#=================================CAIXA DE TEXTO FEMININO============================

txtJeans_Jeggers = Entry (FrameABC2,textvariable = Jeans_Jeggers ,font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=1, column = 1, pady = 1)

txtCoats_jackets = Entry (FrameABC2,textvariable = Coats_Jackets ,font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=2, column = 1, pady = 1)

txtSportwear = Entry (FrameABC2,textvariable = Sportwear, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=3, column = 1, pady = 1)

txtlDresses = Entry(FrameABC2,textvariable = Dresses ,font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=4, column = 1, pady = 1)

#====================================LABEL CRIANÇAS=================================

lblCriança = Label(FrameABC2, text="Crianças",font=('arial',20,'bold'), padx = 8 , pady =1,
                bd = 8, bg="yellow", fg="black", width = 25 ,justify=CENTER) .grid(row=5, column = 0, columnspan = 4)

lblSkirts = Label(FrameABC2, text="Saias: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=6, column = 0,)

lblSwimwear = Label(FrameABC2, text="Natação: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=7, column = 0)

lblSchoolUniform = Label(FrameABC2, text="Uniforme: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=8, column = 0)

lblPyjamas = Label(FrameABC2, text="Pijama: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=9, column = 0)

#==================================CAIXA DE TEXTO CRIANÇAS===========================

txtSkirts = Entry (FrameABC2, textvariable = Skirts, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=6, column = 1, pady = 1)

txtSwimwear = Entry (FrameABC2, textvariable = Swimwear, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=7, column = 1, pady = 1)

txtSchoolUniform = Entry (FrameABC2, textvariable = School_Uniform, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=8, column = 1, pady = 1)

txtPyjamas = Entry(FrameABC2, textvariable = Pyjamas, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=9, column = 1, pady = 1)

#========================================LABEL MASCULINO=====================================

lblMasculino = Label(FrameABC3, text="Masculino",font=('arial',20,'bold'), padx = 8 , pady =1,
                bd = 8, bg="yellow", fg="black", width = 25 ,justify=CENTER) .grid(row=0, column = 0, columnspan = 4)

lblJackets_Blazers = Label(FrameABC3, text="Casacos: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=1, column = 0,)

lblFormal_Trousers = Label(FrameABC3, text="Calças: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=2, column = 0)

lblFormal_Shirts = Label(FrameABC3, text="Camisetas: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=3, column = 0)

lblMens_Boots = Label(FrameABC3, text="Calçados: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=4, column = 0)

#======================================CAIXA DE TEXTO MASCULINO=============================

txtJackets_Blazers = Entry (FrameABC3, textvariable = Jackets_Blazers, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=1, column = 1, pady = 1)

txtFormal_Trousers = Entry (FrameABC3, textvariable = Formal_Trousers, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=2, column = 1, pady = 1)

txtFormal_Shirts = Entry (FrameABC3, textvariable = Formal_Shirts, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=3, column = 1, pady = 1)

txtlMens_Boots = Entry(FrameABC3, textvariable = Mens_Boots, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=4, column = 1, pady = 1)

#========================================LABEL CASA=====================================

lblHome = Label(FrameABC3, text="Casa",font=('arial',20,'bold'), padx = 8 , pady =1,
                bd = 8, bg="yellow", fg="black", width = 25 ,justify=CENTER) .grid(row=5, column = 0, columnspan = 4)

lblBed_Sheet = Label(FrameABC3, text="Lençol: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=6, column = 0,)

lblsPillow = Label(FrameABC3, text="Travesseiro: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=7, column = 0)

lblPatterned_Bedding = Label(FrameABC3, text="Edredom: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=8, column = 0)

lblMattress_Protectors= Label(FrameABC3, text="Colchão: ",font=('arial',18,'bold'), padx = 8 , pady =9,
                bd = 8, bg="green", fg="black", justify=LEFT) .grid(row=9, column = 0)

#=======================================CAIXA DE TEXTO CASA==================================

txtBed_Sheet = Entry (FrameABC3, textvariable = Bed_Sheet, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=6, column = 1, pady = 1)

txtPillows = Entry (FrameABC3, textvariable = Pillows, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=7, column = 1, pady = 1)

txtPatterned_Bedding = Entry (FrameABC3, textvariable = Patterned_Bedding, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=8, column = 1, pady = 1)

txtMattress_Protectors = Entry(FrameABC3, textvariable = Mattress_Protectors, font=('arial',18,'bold'),
                bd = 2, bg="white", fg="black", justify=CENTER) .grid(row=9, column = 1, pady = 1)

#=============================================RECIBO===============================================

txtReceipt = Text(FrameABC5, height = 31, width = 40, bd = 23, font=('arial',9,'bold'))
txtReceipt.grid (row = 0, column= 0)

#==============================================BOTÕES==============================================

bntTotal = Button(FrameABC6, padx = 1, pady = 1, bd = 4, fg = "black",command = Total, font=('arial',17,'bold'),
                  width = 7, bg = "orange", text = "Total"). grid(row = 0, column = 0)

bntRest = Button(FrameABC6, padx = 1, pady = 1, bd = 4, fg = "black",command = reset, font=('arial',16,'bold'),
                  width = 7, bg = "yellow", text = "Limpar"). grid(row = 0, column = 2)

bntExit = Button(FrameABC6, padx = 1, pady = 1, bd = 4, fg = "black",command = Exit ,font=('arial',17,'bold'),
                  width = 7, bg = "red", text = "Sair"). grid(row = 0, column = 3)

root.mainloop()
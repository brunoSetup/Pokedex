# -*- coding: latin-1 -*-
from tkinter import *
import tkinter as tka
from winsound import *
from random import *
import tkinter





root = Tk() # Cria a Janela tkinter

rootCanvas = Canvas(root)
root.geometry("900x300")
root.configure(background='White')
root.title("Pokedex Marota -> Desenvolvedor: Bruno Vieira")

fonte0 = ("Comic Sans MS",29,"bold")#LABELS - fonte Para títulos
fonte1 = ("Comic Sans MS",12,"bold")#LABELS - fonte Para títulos
fonte2 = ("Comic Sans MS",10,"bold")#LABELS - fonte Para títulos

def passagem2():
    PlaySound('passagem2.wav', SND_FILENAME)
def passagem():
    PlaySound('passagem.wav', SND_FILENAME)

def passagem3(a):
    PlaySound('passagem.wav', SND_FILENAME)
    a.destroy()
    
    
    
playE = lambda: PlaySound('E-sound.wav', SND_FILENAME)
playF = lambda: PlaySound('F-sound.wav', SND_FILENAME)
playV = lambda: PlaySound('V-sound.wav', SND_FILENAME)
playJ = lambda: PlaySound('J-sound.wav', SND_FILENAME)


def playaE():
    PlaySound("jogo.wav",SND_FILENAME)
def playaJ():
    PlaySound("jogo.wav",SND_FILENAME)  
def playaV():
    PlaySound("jogo.wav",SND_FILENAME)
def playaF():
    PlaySound("jogo.wav",SND_FILENAME)



def show_J():
    passagem2()
    D_jolteon = """As células de jolteon geram um baixo nível de energia elétrica.\nEste poder é amplificado pela eletricidade estática de sua pele,\npermitindo que o Pokémon para soltar raios.O pêlo eriçado é feita\nde agulhas eletricamente carregadas ."""
    
    fonte1 = ("Comic Sans MS",8,"bold")#LABELS - fonte Para títulos
    fonte2 = ("Comic Sans MS",10,"bold")
    top = Toplevel()
    top.configure(bg ="orange")
   
    top.geometry("700x330")
    jo = PhotoImage(file = "j.png")
    a = jo.subsample(1,1)
    stat = PhotoImage(file = "j-status.png")
    b = stat.subsample(1,1)
    
    label11 = Label(top,image =b ,bg= "white")
    label11.image = b
    canvas = Canvas(top,bg = "black",width=175, height=150)
    label1 = Label(top,image = a,bg= "black")
    label1.image = a
    
    label2 = Label(top,bg= "black",text = "Nome: Jolteon\nTipo: Elétrico\nNúmero ID: 135",font = fonte1 ,fg="white")
    label3 = Label(top,text ="Descrição:",font = fonte2,bg = "orange",fg = "black")
    label4 = Label(top,text = D_jolteon,font = fonte2,bg = "orange",fg = "black")
    
    
    label11.place(x =60, y =30)
    label1.place(x =65, y =60)
    label2.place(x = 130,y=75)
    label3.place(x =260 ,y = 50)
    label4.place(x =260 ,y = 70)
    canvas.place(x =60 ,y =30)

    area= PhotoImage(file ="map.png")
    ar = area.subsample(3,3)
    aud= PhotoImage(file ="aud.png")
    ch = aud.subsample(3,3)
    exi= PhotoImage(file ="exi.png")
    ex = exi.subsample(4,4)
    
    btm1 = Button(top,text ="Mostrar Área de Ocorrência",font = fonte2,command = J_Area,image = ar,bg ="white")
    btm1.config(image = ar,compound =RIGHT)
    btm1.image = ar
    btm1.place(x=260,y=200)

    btm2 = Button(top,text ="Mostrar Choro",font = fonte2,command = playJ,image = ch,bg ="white")
    btm2.config(image = ch,compound =RIGHT)
    btm2.image = ch
    btm2.place(x=520,y=200)

    btm3 = Button(top,text ="Sair",font = fonte2,image = ex,bg ="white",command = lambda: passagem3(top))
    btm3.config(image = ex,compound =RIGHT)
    btm3.image = ex
    btm3.place(x=260,y=280)
    
    
def J_Area():
    passagem2()
    outra = Toplevel()
    
    outra.geometry("580x470")
    menus = Menu(outra)
    sub = Menu()
    outra.config(menu = menus)
    menus.add_cascade(label= "Exit",font = ("Aria",15,"bold"),menu = sub)
    sub.add_command(label = "Sair de Mapa",font = ("Comic Sans MS",8),command = lambda: passagem3(outra))
    
    mapa = PhotoImage(file = "mapas.png")
    maps = mapa.subsample(1,1)
    lbl = Label(outra,image = maps)
    lbl.image = maps
    lbl.place(x= 0,y=0)

def show_E():
    
    passagem2()
    D_jolteon = """Eevee tem uma composição genética instável que,\n de repente se transforma devido ao ambiente em que vive .\n Radiação de várias pedras faz com que esse Pokémon evoluir."""
    fonte1 = ("Comic Sans MS",8,"bold")#LABELS - fonte Para títulos
    fonte2 = ("Comic Sans MS",10,"bold")
    top = Toplevel()
    top.configure(bg ="Brown")
   
    top.geometry("700x370")
    jo = PhotoImage(file = "Eevee.png")
    a = jo.subsample(1,1)
    stat = PhotoImage(file = "eeve.gif")
    b = stat.subsample(1,1)
    
    label11 = Label(top,image =b ,bg= "white")
    label11.image = b
    canvas = Canvas(top,bg = "black",width=170, height=80)
    label1 = Label(top,image = a,bg= "black")
    label1.image = a
    
    label2 = Label(top,bg= "black",text = "Nome: Eeve\nTipo: Normal\nNúmero ID: 131",font = fonte1 ,fg="white")
    label3 = Label(top,text ="Descrição:",font = fonte2,bg = "brown",fg = "white")
    label4 = Label(top,text = D_jolteon,font = fonte2,bg = "brown",fg = "white")
    
    
    label11.place(x =20, y =85)
    label1.place(x =55, y =5)
    label2.place(x = 125,y=5)
    label3.place(x =280 ,y = 50)
    label4.place(x =280 ,y = 70)
    canvas.place(x =50 ,y = 0)

    area= PhotoImage(file ="map.png")
    ar = area.subsample(3,3)
    aud= PhotoImage(file ="aud.png")
    ch = aud.subsample(3,3)
    exi= PhotoImage(file ="exi.png")
    ex = exi.subsample(4,4)
    
    btm1 = Button(top,text ="Mostrar Área de Ocorrência",font = fonte2,command = J_Area,image = ar,bg ="white")
    btm1.config(image = ar,compound =RIGHT)
    btm1.image = ar
    btm1.place(x=280,y=200)

    btm2 = Button(top,text ="Mostrar Choro",font = fonte2,command = playE,image = ch,bg ="white")
    btm2.config(image = ch,compound =RIGHT)
    btm2.image = ch
    btm2.place(x=540,y=200)

    btm3 = Button(top,text ="Sair",font = fonte2,image = ex,bg ="white",command = lambda: passagem3(top))
    btm3.config(image = ex,compound =RIGHT)
    btm3.image = ex
    btm3.place(x=280,y=280)
    
    
    

def show_V():
    
    passagem2()
    D_jolteon = """Vaporeon sofreu uma mutação espontânea e cresceu barbatanas\n e brânquias que lhe permitem viver debaixo d'água. \nEste Pokémon tem a capacidade\n de controlar livremente água."""
    
    fonte1 = ("Comic Sans MS",8,"bold")#LABELS - fonte Para títulos
    fonte2 = ("Comic Sans MS",10,"bold")
    top = Toplevel()
    top.configure(bg ="blue")
   
    top.geometry("850x480")
    jo = PhotoImage(file = "Vaporeon.png")
    a = jo.subsample(1,1)
    stat = PhotoImage(file = "V-sta.png")
    b = stat.subsample(1,1)
    
    label11 = Label(top,image =b ,bg= "white")
    label11.image = b
    canvas = Canvas(top,bg = "black",width=247, height=190)
    label1 = Label(top,image = a,bg= "black")
    label1.image = a
    
    label2 = Label(top,bg= "black",text = "Nome: Vaporeon\nTipo: Aquático\nNúmero ID: 134",font = fonte1 ,fg="white")
    label3 = Label(top,text ="Descrição:",font = fonte2,bg = "blue",fg = "white")
    label4 = Label(top,text = D_jolteon,font = fonte2,bg = "blue",fg = "white")
    
    
    label11.place(x =60, y =30)
    label1.place(x =105, y =80)
    label2.place(x = 185,y=85)
    label3.place(x =360 ,y = 50)
    label4.place(x =360 ,y = 70)
    canvas.place(x =60 ,y =30)

    area= PhotoImage(file ="map.png")
    ar = area.subsample(3,3)
    aud= PhotoImage(file ="aud.png")
    ch = aud.subsample(3,3)
    exi= PhotoImage(file ="exi.png")
    ex = exi.subsample(4,4)
    
    btm1 = Button(top,text ="Mostrar Área de Ocorrência",font = fonte2,command = J_Area,image = ar,bg ="white")
    btm1.config(image = ar,compound =RIGHT)
    btm1.image = ar
    btm1.place(x=360,y=250)

    btm2 = Button(top,text ="Mostrar Choro",font = fonte2,command = playV,image = ch,bg ="white")
    btm2.config(image = ch,compound =RIGHT)
    btm2.image = ch
    btm2.place(x=620,y=250)

    btm3 = Button(top,text ="Sair",font = fonte2,image = ex,bg ="white",command = lambda: passagem3(top))
    btm3.config(image = ex,compound =RIGHT)
    btm3.image = ex
    btm3.place(x=360,y=350)

def show_F():
    
    passagem2()
    D_jolteon = """"""
    
    fonte1 = ("Comic Sans MS",8,"bold")#LABELS - fonte Para títulos
    fonte2 = ("Comic Sans MS",10,"bold")
    top = Toplevel()
    top.configure(bg ="Red")
   
    top.geometry("850x480")
    jo = PhotoImage(file = "Flareon.png")
    a = jo.subsample(1,1)
    stat = PhotoImage(file = "F-state.png")
    b = stat.subsample(1,1)
    
    label11 = Label(top,image =b ,bg= "white")
    label11.image = b
    canvas = Canvas(top,bg = "black",width=237, height=200)
    label1 = Label(top,image = a,bg= "black")
    label1.image = a
    
    label2 = Label(top,bg= "black",text = "Nome: Flareon\nTipo: Fogo\nNúmero ID: 132",font = fonte1 ,fg="white")
    label3 = Label(top,text ="Descrição:",font = fonte2,bg = "red",fg = "white")
    label4 = Label(top,text = D_jolteon,font = fonte2,bg = "red",fg = "white")
    
    
    label11.place(x =60, y =50)
    label1.place(x =105, y =80)
    label2.place(x = 185,y=85)
    label3.place(x =360 ,y = 50)
    label4.place(x =360 ,y = 70)
    canvas.place(x =60 ,y =30)

    area= PhotoImage(file ="map.png")
    ar = area.subsample(3,3)
    aud= PhotoImage(file ="aud.png")
    ch = aud.subsample(3,3)
    exi= PhotoImage(file ="exi.png")
    ex = exi.subsample(4,4)
    
    btm1 = Button(top,text ="Mostrar Área de Ocorrência",font = fonte2,command = J_Area,image = ar,bg ="white")
    btm1.config(image = ar,compound =RIGHT)
    btm1.image = ar
    btm1.place(x=360,y=250)

    btm2 = Button(top,text ="Mostrar Choro",font = fonte2,command = playF,image = ch,bg ="white")
    btm2.config(image = ch,compound =RIGHT)
    btm2.image = ch
    btm2.place(x=620,y=250)

    btm3 = Button(top,text ="Sair",font = fonte2,image = ex,bg ="white",command = lambda: passagem3(top))
    btm3.config(image = ex,compound =RIGHT)
    btm3.image = ex
    btm3.place(x=360,y=350)


poke = PhotoImage(master = rootCanvas, file = "poke.png")
e = poke.subsample(1,1)
info = PhotoImage(master = rootCanvas,file = "info.png")
f = info.subsample(3,3)

lbl0 = Label(root,image = e,bg = "white")
lbl0.place(x=230 , y =-15)

lbl1 = Label(root,text = "Jolteon",font = fonte1,bg ="white",fg = "orange")
lbl1.place(x = 120,y = 80)
lbl2 = Label(root,text = "Eeve",font = fonte1,bg ="white",fg = "brown")
lbl2.place(x = 330,y = 80)
lbl3 = Label(root,text = "Vaporeon",font = fonte1,bg ="white",fg = "blue")
lbl3.place(x = 510,y = 80)
lbl4 = Label(root,text = "Flareon",font = fonte1,bg ="white",fg = "red")
lbl4.place(x = 720,y = 80)

jolteon = PhotoImage(master = rootCanvas,file = "Jolteon2.png")
a = jolteon.subsample(2,2)
joel = Label(root,image = a,bg = "white")
joel.place(x=100 , y =120)

eeve = PhotoImage(master = rootCanvas,file = "E2.png")
b = eeve.subsample(2,2)
eve = Label(root,bg = "White",image = b)
eve.place(x = 300,y = 110)

vaporeon = PhotoImage(master = rootCanvas,file = "V2.png")
c = vaporeon.subsample(2,2)
vapo = Label(root,image= c,bg = "White")
vapo.place(x = 500 ,y = 110)

flareon = PhotoImage(master = rootCanvas,file = "F2.png")
d = flareon.subsample(2,2)
flare = Label(root,image = d,bg = "White")
flare.place(x =700 , y = 110)

botaofoto = PhotoImage(master = rootCanvas,file = "botao.png")
tmi = botaofoto.subsample(3,3)

button0 = Button(root, text = 'Info', font =fonte2 ,command = show_J)
button0.place(x = 90 ,y = 241)
button0.config(image = f,compound =RIGHT)
button01 = Button(root, text = 'Play', font =fonte2 ,command = playaJ)
button01.place(x = 170 ,y = 240)
button01.config(image = tmi,compound =RIGHT)

button1 = Button(root, text = 'Info', font =fonte2, command = show_E)
button1.place(x = 290 ,y = 241)
button1.config(image = f,compound =RIGHT)
button11 = Button(root, text = 'Play', font =fonte2 ,command = playaE)
button11.place(x = 370 ,y = 240)
button11.config(image = tmi,compound =RIGHT)

button2 = Button(root, text = 'Info', font =fonte2, command = show_V)
button2.place(x = 480 ,y = 241)
button2.config(image = f,compound =RIGHT)
button21 = Button(root, text = 'Play', font =fonte2, command = playaV)
button21.place(x = 560 ,y = 240)
button21.config(image = tmi,compound =RIGHT)

button3 = Button(root, text = 'Info', font =fonte2, command = show_F)
button3.place(x = 690 ,y = 241)
button3.config(image = f,compound =RIGHT)
button31 = Button(root, text = 'Play', font =fonte2, command = playaF)
button31.place(x = 770 ,y = 240)
button31.config(image = tmi,compound =RIGHT)

class popupWindow(object):
    def __init__(self,master):
        top = self.top= Toplevel(master)
        top.geometry("400x100")
        top.title("Qual seu nome?")
        self.l=Label(top,text="Digite o seu nome:",font = ("Arial",15,"bold"))
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
        
def def_nome(root):
    root.update()
    a = popupWindow(root)
    root.wait_window(a.top)
    nome = a.value
    label = Label(root,text= "Jogador: "+nome,font = ("Arial",15,"bold"),bg = "White")
    label.place(x = 700,y=0)

def def_des(root):
    
    a = tkinter.messagebox.showinfo("Desenvolvedor","Bruno Vieira Dutra-2016\nGraduando em Engenharia de Redes de Comuncação\nAmante de Pokemon")
    

    
    
menus =Menu(root)
sub1 = Menu()
sub2 = Menu()
sub3 = Menu()
root.config(menu = menus)
menus.add_cascade(label = "Opções", menu = sub1)
sub1.add_command(label = "Definir nome de Jogador",font = ("Comic Sans MS",8,"bold"),command =  lambda: def_nome(root))
menus.add_cascade(label = "Info", menu = sub2)
sub2.add_command(label = "Informações do Desenvolvedor",font = ("Comic Sans MS",8,"bold"),command =  lambda: def_des(root))
menus.add_cascade(label = "Exit", menu = sub3)
sub3.add_command(label = "Sair do Jogo",font = ("Comic Sans MS",8,"bold"),command =  lambda: passagem3(root))

root.update()
root.mainloop()



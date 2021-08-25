    
from tkinter import *
from winsound import *
import tkinter as tk,math, random,sys,os,time
root=Tk()
root.title("TEACH YOUR KID")
root.geometry("1280x1000")


def quit():
    global root
    root.quit()

def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
root.wm_iconbitmap(resource_path0("0.ico"))
def A():
    f = open(resource_path0("a.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('a.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("a.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
       
def B():
    f = open(resource_path0("b.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('b.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("b.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)

def C():
    f = open(resource_path0("c.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('c.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("c.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)

def D():
    f = open(resource_path0("d.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('d.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("d.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)

def E():
    f = open(resource_path0("e.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('e.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("e.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
       
def F():
    f = open(resource_path0("f.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('f.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("f.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def G():
    f = open(resource_path0("g.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('g.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("g.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def H():
    f = open(resource_path0("h.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('h.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("h.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def I():
    f = open(resource_path0("i.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('i.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("i.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def J():
    f = open(resource_path0("j.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('j.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("j.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def K():
    f = open(resource_path0("k.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('k.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("k.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def L():
    f = open(resource_path0("l.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('l.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("l.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def M():
    f = open(resource_path0("m.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('m.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("m.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def N():
    f = open(resource_path0("n.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('n.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("n.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def O():
    f = open(resource_path0("o.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('o.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("o.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def P():
    f = open(resource_path0("p.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('p.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("p.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def Q():
    f = open(resource_path0("q.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('q.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("q.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def R():
    f = open(resource_path0("r.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('r.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("r.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def S():
    f = open(resource_path0("s.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('s.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("s.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def T():
    f = open(resource_path0("t.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('t.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("t.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def U():
    f = open(resource_path0("u.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('u.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("u.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)

def V():
    f = open(resource_path0("v.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('v.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("v.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def W():
    f = open(resource_path0("w.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('w.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("w.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def X():
    f = open(resource_path0("x.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('x.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("x.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def Y():
    f = open(resource_path0("y.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('y.wav'), SND_FILENAME)
    global img1
    img1=PhotoImage(file=resource_path0("y.png"))
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def Z():
    f = open(resource_path0("z.txt"),"r")
    f1=f.read()
    my_text.delete("1.0","end")
    my_text.insert(END,f1)
    f.read()
    f.close()
    PlaySound(resource_path0('z.wav'), SND_FILENAME)
    path = resource_path0("z.png")
    global img1
    img1 = tk.PhotoImage(file=path)
    my_text1.delete("1.0","end")
    my_text1.image_create(END,image=img1)
  
def CREDIT():
            PlaySound(resource_path0(resource_path0('CREDITS.wav')), SND_FILENAME)
            f = open(resource_path0("CREDITSt.txt"),"r")
            f1=f.read()
            my_text.delete("1.0","end")
            my_text.insert(END,f1)
            f.read()
            f.close()
            f = open(resource_path0("CREDITS.txt"),"r")
            f1=f.read()
            my_text1.delete("1.0","end")
            my_text1.insert(END,f1)
            f.read()
            f.close()
   
       


credit=Label(text="TEACH  YOUR KID",bg="green",fg="white",font="bold")
credit.pack(fill="x",anchor="se")

credit=Label(text="SRI OME HOTHA",bg="yellow",fg="brown",font="bold")
credit.pack(fill="x",side="top")


frame = Frame(root,borderwidth=10 , bg = "pink")
frame.pack(fill = BOTH, expand = True )

        
          
b1 = Button(frame,text="A",bg='#ffb3fe',command=A,padx=5)
b1.pack(side="left",padx=9)
b2 = Button(frame,text="B",bg='#ffb3fe',command=B,padx=5)
b2.pack(side="left",padx=9)
b3 = Button(frame,text="C",bg='#ffb3fe',command=C,padx=5)
b3.pack(side="left",padx=9)
b4 = Button(frame,text="D",bg='#ffb3fe',command=D,padx=5)
b4.pack(side="left",padx=9)
b5 = Button(frame,text="E",bg='#ffb3fe',command=E,padx=5)
b5.pack(side="left",padx=9)
b6 = Button(frame,text="F",bg='#ffb3fe',command=F,padx=5)
b6.pack(side="left",padx=9)
b7 = Button(frame,text="G",bg='#ffb3fe',command=G,padx=5)
b7.pack(side="left",padx=9)
b8 = Button(frame,text="H",bg='#ffb3fe',command=H,padx=5)
b8.pack(side="left",padx=9)
b9 = Button(frame,text="I",bg='#ffb3fe',command=I,padx=5)
b9.pack(side="left",padx=9)
b10 = Button(frame,text="J",bg='#ffb3fe',command=J,padx=5)
b10.pack(side="left",padx=9)
b11 = Button(frame,text="K",bg='#ffb3fe',command=K,padx=5)
b11.pack(side="left",padx=9)
b12 = Button(frame,text="L",bg='#ffb3fe',command=L,padx=5)
b12.pack(side="left",padx=6)
b13 = Button(frame,text="M",bg='#ffb3fe',command=M,padx=5)
b13.pack(side="left",padx=6)
b14 = Button(frame,text="N",bg='#ffb3fe',command=N,padx=5)
b14.pack(side="left",padx=6)
b15 = Button(frame,text="O",bg='#ffb3fe',command=O,padx=5)
b15.pack(side="left",padx=6)
b16 = Button(frame,text="P",bg='#ffb3fe',command=P,padx=5)
b16.pack(side="left",padx=6)
b17 = Button(frame,text="Q",bg='#ffb3fe',command=Q,padx=5)
b17.pack(side="left",padx=6)
b18 = Button(frame,text="R",bg='#ffb3fe',command=R,padx=5)
b18.pack(side="left",padx=6)
b19 = Button(frame,text="S",bg='#ffb3fe',command=S,padx=5)
b19.pack(side="left",padx=6)
b20 = Button(frame,text="T",bg='#ffb3fe',command=T,padx=5)
b20.pack(side="left",padx=6)
b21 = Button(frame,text="U",bg='#ffb3fe',command=U,padx=5)
b21.pack(side="left",padx=6)
b22 = Button(frame,text="V",bg='#ffb3fe',command=V,padx=5)
b22.pack(side="left")
b23 = Button(frame,text="W",bg='#ffb3fe',command=W,padx=5)
b23.pack(side="left",padx=6)
b24 = Button(frame,text="X",bg='#ffb3fe',command=X,padx=5)
b24.pack(side="left",padx=6)
b25 = Button(frame,text="Y",bg='#ffb3fe',command=Y,padx=5)
b25.pack(side="left",padx=6)
b26 = Button(frame,text="Z",bg='#ffb3fe',command=Z,padx=5)
b26.pack(side="left",padx=6)



b27 = Button(frame,text="QUIT",bg='red',fg = "white",command=quit,padx=2)
b27.pack(side="right",padx=6)

b28 = Button(frame,text="DEVELOPER",bg='red',fg = "white",command=CREDIT,padx=2)
b28.pack(side="right",padx=6)

my_text=Text(root,width=35,height=100, font = "Helvetica 25 bold",bg= "orange")
my_text.pack(side="left")


my_text1=Text(root,width=155,height=100,padx=2,bg= "white")
my_text1.pack(side="right")


root.mainloop()

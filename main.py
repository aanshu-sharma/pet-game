# pet-game

from tkinter import *
from tkinter import messagebox

w = Tk()
w.geometry("700x500")
w.title("Pet Game")

l = Label(w, text="Choose your Pet", font= ("Helvetica",24))
l.pack()
#setting canvas
#c for pet1
c1 = Canvas(w, width = 300, height = 300) 
c1.place(x=60,y=50)

#c for pet2
c2 = Canvas(w, width = 300, height = 300) 
c2.place(x=400,y=50)


def greet():
    messagebox.showinfo("Greetings", "Before you start playing with your pet, I hope you will enjoy this pet game ;-)")
b = Button(w, text="READ ME",fg="white",bg="black", command = greet)
b.pack()


""" PET1 """
#creating new window for goofy
def nwg():
    n1= Toplevel(w)
    c1 = Canvas(n1, width = 300, height = 300,bg='black')
    c1.place(x=60,y=50)

    c2 = Canvas(n1, width = 300, height = 300,bg='black') 
    c2.place(x=400,y=50)
    
    n1.title("Goofy's Time")
    n1.geometry('800x500')
    n1.configure(bg='black')
    Label(n1,text= 'What you want to do with Goofy', bg="black", fg="white").pack()
    pet1 = PhotoImage(file="D:\Downloads\play1.ppm")
    id1 = c1.create_image(50,0, anchor=NW, image=pet1)
    l1 = Label(n1, text='Play with goofy', fg="white", bg="black")
    l1.place(x=150,y=270)

    
    pet2 = PhotoImage(file="D:\Downloads\sleep1.ppm")      
    id2=c2.create_image(50,0, anchor=NW, image=pet2) 
    l2=Label(n1, text='Goofy Needs Rest', bg="black", fg="white")
    l2.place(x=500,y=270)
    def sleep():
        n2= Toplevel(n1)
        n2.title("Goofy is sleeping")
        n2.geometry('800x500')
        Label(n2,text= "Don't disturb the goofy, he is sleeping", font=('Arial',20)).pack()
        c3 = Canvas(n2, width = 600, height = 500)
        c3.place(x=60,y=50)
        
        play1 = PhotoImage(file="D:\Downloads\ds.gif")
        id1 = c3.create_image(50,0, anchor=NW, image=play1)
        
        n2.mainloop()
    
    def play():
        n3= Toplevel(n1)
        n3.title("Goofy is playing")
        n3.geometry('800x500')
        Label(n3,text= 'Goofy: Thanks for playing with me :-) , Now I need rest', font=('Arial',20)).pack()
        b4 = Button(n3,text = "sleep goofy", command = sleep)
        b4.pack()
        c4 = Canvas(n3, width = 600, height = 500)
        c4.place(x=60,y=70)
        
        play2 = PhotoImage(file="D:\Downloads\dp.gif")
        id2 = c4.create_image(50,0, anchor=NW, image=play2)

        n3.mainloop()
    b= Button(n1,text='  Play  ', command=play)
    b.place(x=170,y=290)
    b2= Button(n1,text='  Sleep  ', command=sleep)
    b2.place(x=520,y=290)
    n1.mainloop()

pet1 = PhotoImage(file="D:\Downloads\mainpet1.png")
id1 = c1.create_image(50,0, anchor=NW, image=pet1)
l1 = Label(w, text='Name: Goofy')
l1.place(x=150,y=250)
b1=Button(w, text="Play with\nGoofy", command=nwg)
b1.pack()

""" PET2 """

def nwd():
    n1= Toplevel(w)
    c1 = Canvas(n1, width = 300, height = 300,bg='black')
    c1.place(x=60,y=50)

    c2 = Canvas(n1, width = 300, height = 300,bg='black') 
    c2.place(x=400,y=50)
    
    n1.title("Doofy's Time")
    n1.geometry('800x500')
    n1.configure(bg='black')
    Label(n1,text= 'What you want to do with Goofy', bg="black", fg="white").pack()
    pet1 = PhotoImage(file="D:\Downloads\play2.ppm")
    id1 = c1.create_image(50,0, anchor=NW, image=pet1)
    l1 = Label(n1, text='Play with doofy', fg="white", bg="black")
    l1.place(x=150,y=270)

    
    pet2 = PhotoImage(file="D:\Downloads\sleep2.ppm")      
    id2=c2.create_image(50,0, anchor=NW, image=pet2) 
    l2=Label(n1, text='Doofy Needs Rest', bg="black", fg="white")
    l2.place(x=500,y=270)
    def sleep():
        n2= Toplevel(n1)
        
        n2.title("Doofy is sleeping")
        n2.geometry('800x500')
        Label(n2,text= "Don't disturb the Doofy, he is sleeping", font=('Arial',20)).pack()
        c3 = Canvas(n2, width = 600, height = 500)
        c3.place(x=60,y=50)
        
        play1 = PhotoImage(file="D:\Downloads\ds.gif")
        id1 = c3.create_image(50,0, anchor=NW, image=play1)
        
        n2.mainloop()
    
    def play():
        n3= Toplevel(n1)
        
        n3.title("Doofy is playing")
        n3.geometry('800x500')
        Label(n3,text= 'Doofy: Thanks for playing with me :-) , Now I need rest', font=('Arial',20)).pack()
        b4 = Button(n3,text = "sleep Doofy", command = sleep)
        b4.pack()
        c4 = Canvas(n3, width = 600, height = 500)
        c4.place(x=60,y=70)
        
        play2 = PhotoImage(file="D:\Downloads\dp.gif")
        id2 = c4.create_image(50,0, anchor=NW, image=play2)

        n3.mainloop()
    b= Button(n1,text='  Play  ', command=play)
    b.place(x=170,y=290)
    b2= Button(n1,text='  Sleep  ', command=sleep)
    b2.place(x=520,y=290)
    n1.mainloop()



pet2 = PhotoImage(file="D:\Downloads\mainpet2.png")      
id2=c2.create_image(50,0, anchor=NW, image=pet2)
l2 = Label(w, text='Name: Doofy')
l2.place(x=500,y=250)
b2=Button(w, text="Play with\nDoofy", command=nwd)
b2.pack()




    
    

w.mainloop()

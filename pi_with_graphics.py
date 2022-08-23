from tkinter import *
import time

class mass:

    def __init__(self,canvas,x1,y1,x2,y2,xVel,color,state):
        self.canvas = canvas
        self.image = canvas.create_rectangle(x1,y1,x2,y2,fill=color)
        self.xVel = xVel
        self.state = state
    def position(self):
        return self.canvas.coords(self.image)

def isCollide(mass1,mass2):
    if mass1.position()[2] > mass2.position()[0]:
        return True 


window = Tk()

count =0
window.title("Pi Counter")

e = Entry(window,width=5,bg="white",borderwidth=5,font=("Helvetica",16))
e.pack()
def vel(u1,u2):
    v_cm = (u1+int(e.get())*u2)/(int(e.get())+1)
    u1 = 2*v_cm-u1
    u2 = 2*v_cm-u2
    return u1,u2  


masstext = Label(window,text="Mass of large block:",font=("Helvetica",14))
masstext.place(x=140,y=10)

WIDTH= 800
HEIGHT = 600

canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg="black")
canvas.pack()

scoreLabel = Label(window,text="Collisions: "+str(count),font=("Helvetica",20,"bold"),bg="black",fg="white")
scoreLabel.place(x =500, y=100)

canvas.create_line(100,100,100,500,width=3,fill="white")
canvas.create_line(100,500,800,500,width=3,fill="white")

mass1 = mass(canvas,200,450,250,500,0,"red",False)
mass2 = mass(canvas,350,420,430,500,-1,"blue",True)

def click():
    count =0
    while True:
        mass1.canvas.move(mass1.image,mass1.xVel,0)
        mass2.canvas.move(mass2.image,mass2.xVel,0)
        if isCollide(mass1,mass2)==True:
            count +=1
            l = vel(mass1.xVel,mass2.xVel)
            mass1.xVel = l[0]
            mass2.xVel = l[1]
        if mass1.position()[0] <= 100:
            count+=1
            mass1.xVel = -mass1.xVel
        scoreLabel.config(text="Collisions: "+str(count))
        if mass2.position()[0] > 800:
            break
        window.update()
        time.sleep(0.01)

mybutton = Button(window,text="Submit",command=click,font=("Helvetica",14),borderwidth=1)
mybutton.place(x=450,y=5)
button_quit = Button(window,text="Exit",command=window.quit,font=("Helvetica",14))
button_quit.place(x=600,y=5)
window.mainloop()


        
    





    





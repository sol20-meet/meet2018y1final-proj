
import turtle
import random

turtle.tracer(1,0)

window_size_x=500#1920
window_size_y=800#1080

turtle.setup(window_size_x,window_size_y)

miss = []
score=[]
trash_pos=[]
theacher_pos=[]
hammer_pos=[]

hammer=turtle.clone()
hammer.penup()
trash=turtle.clone()
teachers=turtle.clone()
screen=turtle.clone()


turtle.register_shape("trash.gif")
turtle.register_shape("Calebb.gif")
turtle.register_shape("backpack.gif")
teachers.shape("Calebb.gif")

turtle.bgpic("backpack.gif")
trash = turtle.clone()
trash.shape("trash.gif")
trash.penup()

def show_trash():    
    hole = random.randint(1,4)
    if hole == 1:     
        trash.goto(192,88)
    elif hole == 2:
         trash.goto(-17,-216)
    elif hole == 3:
         trash.goto
    elif hole == 4:
         trash.goto
   
    
show_trash()
def click(x,y):
    print(x,y)
    hammer.goto(x,y)

turtle.onscreenclick(click)
def miss():
    if len(set(hammer_pos))!=len(set(miss)):
        quit()
def get_pos():
        x=hammer.pos()
        hammer_pos.append(x)
        
def check_hit(x,y):
    pass
       if hammer_pos[0] >= -113 and<= 82: 
          if hammer_pos[1] >= and <=:
    

show_trash()

turtle.mainloop()
                      


import turtle
import random

turtle.tracer(1,0)

window_size_x=1920#1920
window_size_y=1050#1080

turtle.setup(window_size_x,window_size_y)
global score
score = 0

miss = []
trash_pos=[]
theacher_pos=[]
hammer_pos=[]


turtle.addshape("hammer.gif")
hammer=turtle.clone()
hammer.shape("hammer.gif")
hammer.penup()
trash=turtle.clone()
teachers=turtle.clone()
screen=turtle.clone()
writer=turtle.clone() 
turtle.register_shape("heart.gif")
turtle.register_shape("trash.gif")
turtle.register_shape("Calebb.gif")
turtle.register_shape("backpack.gif")
teachers.shape("Calebb.gif")
turtle.addshape("heart.gif")
turtle.bgpic("backpack.gif")
trash = turtle.clone()
turtle.addshape("trash3.gif")
trash.shape("trash3.gif")
trash.penup()
heart = turtle.clone()
heart.shape("heart.gif")
heart.penup()
heart.goto(-700,400)
heart2 = turtle.clone()
heart2.shape("heart.gif")
heart2.penup()
heart2.goto(-770,400)
heart3= turtle.clone()
heart3.shape("heart.gif")
heart3.penup()
heart3.goto(-840,400)
turtle.undo()
heart.penup()
writer.penup()
teachers.penup()
def show_trash():
    
    global hole
    hole = random.randint(1,10)
    if hole == 1:
        trash.goto(483,
                   293)
    elif hole == 2:
        trash.goto(-14,289)
    elif hole == 3:
        trash.goto(-512,292)
    elif hole == 4:
        trash.goto(595,91)
    elif hole == 5:
        trash.goto(185,87)
    elif hole == 6:
        trash.goto(-217,90)
    elif hole == 7:
        trash.goto(633,88)
    elif hole == 8:
        trash.goto(496,-220)
    elif hole == 9:
        trash.goto(-20,-224)
    elif hole == 10:
        trash.goto(-537,-222)






def show_caleb():
    global hole2
    hole2 = random.randint(1,10)

    if hole2 == 1:
        teachers.goto(483,293)
    elif hole2 == 2:
        teachers.goto(-14,289)
    elif hole2 == 3:
        teachers.goto(-512,292)
    elif hole2 == 4:
        teachers.goto(595,91)
    elif hole2 == 5:
        teachers.goto(185,87)
    elif hole2 == 6:
        teachers.goto(-217,90)
    elif hole2 == 7:
        teachers.goto(633,88)
    elif hole2 == 8:
        teachers.goto(496,-220)
    elif hole2 == 9:
        teachers.goto(-20,-224)
    elif hole2 == 10:
        teachers.goto(-537,-222)
global Death
Death=0
def click(x,y):
    global Death, score
    hammer.goto(x,y)
    x=hammer.pos()[0]
    y=hammer.pos()[1]
    z=20
    if x in range (trash.pos()[0]-z,trash.pos()[0]+z) and y in range (trash.pos()[1]-z,trash.pos()[1]+z):
        show_trash()
        turtle.undo()
        turtle.hideturtle()
        turtle.penup()
        turtle.color('red')
        score+=1
        turtle.goto(900,450)
        turtle.write(score, move=False, align='left', font= ('Arial', 30,'normal'))
    
    else:
        Death+=1
        if x in range (teachers.pos()[0]-z,teachers.pos()[0]+z) and y in range (teachers.pos()[1]-z,teachers.pos()[1]+z):
            show_caleb()
            if Death == 1 :
                heart.ht()
            elif Death == 2 :
                heart2.ht()
            elif Death == 3 :
                
               heart3.ht()
               writer.ht()
               FONT = ('Arial',60,'normal')
               writer.color("white") 
               writer.goto(-200,0)
               writer.write("Game Over",font=FONT)
               return quit()
        else:
            if Death == 1 :
               heart.ht()
            elif Death == 2 :
               heart2.ht()
            elif Death == 3 :
               
               heart3.ht()
               writer.ht()
               FONT = ('Arial',60,'normal')
               writer.color("white") 
               writer.goto(-200,0)
               writer.write("Game Over",font=FONT)
               return quit()
            
turtle.onscreenclick(click)



show_trash()
show_caleb()
turtle.mainloop()
                      

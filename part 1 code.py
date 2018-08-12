
import turtle
import random

turtle.tracer(1,0)

window_size_x=1920
window_size_y=1080

turtle.setup(window_size_x,window_size_y)

miss = []
score=[]
trash_pos=[]
theacher_pos=[]

hammer=turtle.clone()
trash=turtle.clone()
teachers=turtle.clone()


turtle.register_shape("Calebb.gif")
turtle.register_shape("backpack.gif")
teachers.shape("Calebb.gif")

turtle.bgpic("backpack.gif")

turtle.mainloop()
                      

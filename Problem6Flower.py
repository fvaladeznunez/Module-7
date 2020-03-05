import turtle

def flower(t):
    for i in range(1,7):
        t.forward(100)
        t.left(60)

t= turtle.Turtle()

for i in range(1,11):
    flower(t)
    t.left(36)

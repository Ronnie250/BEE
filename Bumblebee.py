import pgzrun
import random

WIDTH=600
HEIGHT=500

bee=Actor("bee")
flower=Actor("flower")
flower.pos=300, 250
score=0

def draw():
    screen.blit("background", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score= "+str(score),(460,25), fontsize=40)

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2
    if bee.colliderect(flower):
        score = score+1
        flower.x=random.randint(20,580)
        flower.y=random.randint(20,480)

pgzrun.go()
import pgzrun
import random

WIDTH=600
HEIGHT=500

bee=Actor("bee")
flower=Actor("flower")
flower.pos=300, 250
score=0
timer=60
game_over=False

def draw():
    screen.blit("background", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score= "+str(score),(460,25), fontsize=40)
    if game_over:
        screen.blit("background", (0,0))
        screen.draw.text("Score= "+str(score),(175,325), fontsize=75)
    else:
        screen.draw.text(str(int(timer)), (300,20))

def update(dt):
    global score, timer
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
    if not game_over:
        timer=timer-dt

def time_up():
    global game_over
    game_over=True

clock.schedule(time_up, 60.0)

pgzrun.go()
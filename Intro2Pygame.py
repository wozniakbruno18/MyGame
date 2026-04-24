import pygame as py
from random import randint
py.init()

def randomColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return(r, g, b)

def randomSpeed():
    return randint(5, 10)

sWidth = 600
sHeight = 600
screen = py.display.set_mode((sWidth, sHeight))

x, y = sWidth/2, sHeight/2
a, b = sWidth/2, sWidth/2
speedX, speedY = 5, 8
speedA, speedB = 8, 4

rgb = randomColor()

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    screen.fill("#11DB9B")
    # py.draw.rect(screen, "#ff0000", (sWidth/2, sHeight/2,50, 50))
    # py.draw.line(screen,"#ffffff", (0,0), (600, 600))
    # py.draw.line(screen,"#ffffff", (600,0), (0, 600))
    # py.draw.line(screen,"#ffffff", (sWidth/2,0), (sWidth/2, 600))
    # py.draw.line(screen,"#ffffff", (0,sHeight/2), (600, sWidth/2))
    py.draw.circle(screen, rgb, (x, y), 50)
    py.draw.rect(screen, rgb, (a, b, 50, 50))
    # py.draw.ellipse(screen, "#77ff00", (400, 400, 50, 100))

    py.display.flip() #update the screen
    if x + 50 > 600 or x - 50 < 0:
        speedX = -speedX/abs(speedX)*randomSpeed()
        rgb = randomColor()
    x += speedX
    
    if y + 50 > 600 or y - 50 < 0:
        speedY = -speedY/abs(speedY)*randomSpeed()
        rgb = randomColor()
    y += speedY

    if a + 50 > 600 or a - 50 < 0:
        speedA = -speedA/abs(speedA)*randomSpeed()
        rgb = randomColor()
    a += speedA
    
    if b + 50 > 600 or b - 50 < 0:
        speedB = -speedB/abs(speedB)*randomSpeed()
        rgb = randomColor()
    b += speedB 
    py.time.delay(10)
py.quit
py.quit
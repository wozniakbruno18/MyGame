'''
Here we will work with images in Pygame. 
The way images work - they are drawn on a surface.
Create a rectangle of a given size and then we willl simply draw the image 
at the coordinates of the rectangle.
All the images which are used in a project must be located within the same folder 
as the python scypt.
You must never load an image inside the loop. You can draw inside a loop.
Char image ref: https://openclipart.org/detail/23511/cartoon-triceratops
'''
import pygame as py
py.init()

w, h = 600, 600
screen = py.display.set_mode((w, h))
py.display.set_caption("Working with Image in Pygame")
img = py.image.load("./GameProject/images.png")
img = py.transform.scale(img, (100, 100))
x, y = 0, 0
clock = py.time.Clock()
run = True
while run:
    clock.tick(25)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    screen.fill("#ffffff")
    screen.blit(img, (x, y))
    x, y = x+1, y+1

    py.display.flip()
py.quit()

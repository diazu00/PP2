import pygame, sys, datetime
from rotate import rot_center
pygame.init()

display = pygame.display.set_mode((600, 600))

#images
back = pygame.image.load('C:/Users/Hp/Documents/pp2_dias/PP2/lab 7/Mickey/back.jpeg')
right = pygame.image.load('C:/Users/Hp/Documents/pp2_dias/PP2/lab 7/Mickey/Long.png')
left = pygame.image.load('C:/Users/Hp/Documents/pp2_dias/PP2/lab 7/Mickey/Short.png')

back = pygame.transform.scale(back, (600, 600))
right = pygame.transform.scale(right, (300, 300))
left = pygame.transform.scale(left, (300, 300))

left = pygame.transform.flip(left, 180, 180)

while True:

    #Time
    sec = datetime.datetime.now().second
    min = datetime.datetime.now().minute

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #angle
    x = (-6*min)%360
    y = ((-1)*sec * 6)%360

    #rot_center
    rot_right, x = rot_center(right, x, 300, 300)
    rot_left, y = rot_center(left, y, 300, 300)

    #set
    display.blit(back, (0, 0))
    display.blit(rot_right, x)
    display.blit(rot_left, y)

    pygame.display.update()
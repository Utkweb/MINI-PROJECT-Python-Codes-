from rectangle import Rectangle
from snowflake import Snowflake
import random
import sys
import pygame
import pygame.locals
pygame.init()
surface = pygame.display.set_mode((400,500))
pygame.display.set_caption('Lab 5')
blue_rect = Rectangle(0,0,400,300,(0,0,255))
green_rect = Rectangle(0,300,400,200(0,255,0))
drawable = []
drawable.append(blue_rect)
drawable.append(green_rect)
x_loc = 0
y_loc = 0
snowflake = Snowflake(x_loc, y_loc)
land = random.randint(300,500)
snowflake.setMaxY(land)
drawable.append(snowflake)
fpsClock = pygame.time.Clock()
#game loop
pause = False
while True:
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN and event.__dict__['key'] ==pygame.K_SPACE):
            pause = not pause
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
            exit()
    if not pause:
        for item in drawable:
            item.draw(surface)
            if isinstance(item,Snowflake):
                location = item.getLoc()
                if (location[1] == item.getMaxY()):
                    continue
                else:
                    item.moveDown()
        x_loc = random.randint(0,400)
        snowflake = Snowflake(x_loc,y_loc)
        land = random.randint(300,500)
        snowflake.setMaxY(land)
        drawable.append(snowflake)
        pygame.display.update()
        fpsClock.tick(30)
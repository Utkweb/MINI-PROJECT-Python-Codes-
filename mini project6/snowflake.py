import pygame
from drawable import Drawable
class Snowflake(Drawable):
    def __init__(self, x = 0, y = 0):
        super().__init__(x,y)
        self.__color = (255, 255, 255)
        self.__max_y = 300
    def draw(self, surface):
        location = self.getLoc()
        pygame.draw.line(surface, self.__color, (location[0] - 5, location[1]), (location[0] + 5,location[1]))
        pygame.draw.line(surface, self.__color, (location[0], location[1] - 5), (location[0],location[1] + 5))
        pygame.draw.line(surface, self.__color, (location[0] - 5, location[1] - 5), (location[0] + 5,location[1] + 5))
        pygame.draw.line(surface, self.__color, (location[0] - 5), location[1] + 5), (location[0] +5, location[1] - 5)
    def moveDown(self):
        location = list(self.getLoc())
        location[1] = location[1] + 1
        location = tuple(location)
        self.setLoc(location)
    def setMaxY(self, max_y):
        self.__max_y = max_y
    def getMaxY(self):
        return self.__max_y
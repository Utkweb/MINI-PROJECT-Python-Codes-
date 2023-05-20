import random
import time
from sys import exit

import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT

random.seed(int(time.strftime('%H%M%S', time.localtime(time.time()))))


def get_random_integer(min_value=0, max_value=255):
   return random.randint(min_value, max_value)


def random_color(start_r=0, start_g=0, start_b=0, end_r=255, end_g=255, end_b=255):
   """
   generate random rgb value
   :param start_r: minimum value for red, default is 0
   :param start_g: minimum value for green, default is 0
   :param start_b: minimum value for blue, default is 0
   :param end_r: maximum value for red, default is 255
   :param end_g: maximum value for green, default is 255
   :param end_b: maximum value for blue, default is 255
   :return: a tuple(r,g,b)
   """
   r = max(min(random.randint(start_r, end_r), 255), 0)
   g = max(min(random.randint(start_g, end_g), 255), 0)
   b = max(min(random.randint(start_b, end_b), 255), 0)
   logs_print("r, g, b: {0}, {1}, {2}".format(r, g, b))
   return r, g, b


def logs_print(text, level=0):
   """
   print logsw
   :param text: log text
   :param level: levels 0, 1, and 2 correspond to normal logs, warnings, and errors;default level is normal logs
   :return: none
   """
   level = max(min(level, 2), 0)
   level_tuple = ("Logs", "Warning", "Error")
   print("{time} [{level}]: {text}".format(level=level_tuple[level], text=text,
                                           time=time.strftime('%H:%M:%S', time.localtime(time.time()))))


def refresh_screen(screen, fps=60., clear=True, background=(0, 0, 0)):
   """
   refresh screen
   :param screen: which screen to refresh
   :param fps: frame per second
   :param clear: whether clear old content; Notice: this will clear all old content
   :param background: backound color;(r, g, b)
   :return: none
   """
   if clear:
       pygame.display.update()
   fps = max(0.001, fps)
   time.sleep(1 / fps)
   screen.fill(background, )


def init_program(caption="Pygame", the_screen_size=(640, 480), icon=None):
   pygame.init()
   pygame.display.set_caption(caption)
   if icon is not None:
       icon = pygame.image.load(icon)
       pygame.display.set_icon(icon)
   return pygame.display.set_mode(the_screen_size, 0, 32), the_screen_size


class Circle:
   """ draw a solid circle, automatic detect border and automatic reverse
   """

   def __init__(self, surface, border, position, width=5, color=random_color(), speed=[5, 5],
                disappear_after_collision=False,
                rebound=True):
       """
       constructor function
       :param surface: assign surface to draw
       :param border: take a list (x, y); x and y correspond to the surface' x and y border
       :param position: position
       :param width: line width, when it is a circle it equals to radius
       :param color: (r, g, b); default value is random
       :param speed: take a list (x, y); it moves x unit length int the x direction and so is param y;can be minus
       :param disappear_after_collision: whether the circle disappear after collision with border
       :param rebound: whether the circle rebound after collision with border
       """
       self.surface = surface
       self.border = border
       self.x = position[0]
       self.y = position[1]
       self.width = width
       self.radius = [self.width, self.width]
       self.color = color
       self.speed = speed
       self.speed_value = list(map(abs, speed))
       self.throwaway = disappear_after_collision
       self.rebound = rebound
       self.movable = True
       logs_print("generating obj...")

   def move(self):
       if self.movable:
           x_direction, y_direction = self.can_continue()
           if x_direction:
               self.x += self.speed[0]
           else:
               if self.rebound:
                   self.speed[0] = -self.speed[0]
               if self.throwaway:
                   self.movable = False
           if y_direction:
               self.y += self.speed[1]
           else:
               if self.rebound:
                   self.speed[1] = -self.speed[1]
                   logs_print("rebound occurs...")
               if self.throwaway:
                   self.movable = False

           self.blit()
       else:
           logs_print("try to move but unmovable now", 1)
       # logs_print("current position: {0},{1}".format(self.x, self.y))

   def set_speed(self, key):
       if key == K_UP:
           self.speed = [0, -self.speed_value[1]]
       elif key == K_DOWN:
           self.speed = [0, self.speed_value[1]]
       elif key == K_LEFT:
           self.speed = [-self.speed_value[0], 0]
       elif key == K_RIGHT:
           self.speed = [self.speed_value[0], 0]

   def blit(self):
       pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.width)

   def can_continue(self):
       if self.x + self.speed[0] + self.radius[0] > self.border[0] or self.x + self.speed[0] - self.radius[0] < 0:
           x_direction = False
       else:
           x_direction = True
       if self.y + self.speed[1] + self.radius[1] > self.border[1] or self.y + self.speed[1] - self.radius[1] < 0:
           y_direction = False
       else:
           y_direction = True
       # logs_print("can continue: {0}, {1}".format(x_direction, y_direction))
       return x_direction, y_direction


screen, screen_size = init_program("Balls", (1800, 1000))

# ball_1 = Circle(screen, screen_size, (100, 150), width=5, speed=[1, 3])
# ball_2 = Circle(screen, screen_size, (400, 350), width=10, speed=[3, 1])
# ball_3 = Circle(screen, screen_size, (200, 450), width=15, speed=[3, 3])

ball_0 = Circle(screen, screen_size, (320, 240), width=10, color=(233, 159, 231), speed=[12, 12])
ball_list = []
for i in range(10000):
   locals()['ball' + str(i)] = Circle(screen, screen_size, (get_random_integer(50, 600), get_random_integer(30, 450)),
                                      width=7, speed=[get_random_integer(3, 10), get_random_integer(3, 10)],
                                      color=[get_random_integer(), get_random_integer(), get_random_integer()])
   ball_list.append(locals()['ball' + str(i)])

while True:
   refresh_screen(screen)
   for event in pygame.event.get():
       if event.type == QUIT:
           exit()
       if event.type == KEYDOWN:
           ball_0.set_speed(event.key)

   # ball_1.move()
   # ball_2.move()
   # ball_3.move()
   ball_0.move()
   for ball in ball_list:
       ball.move()
import pygame

class Ball():
    def __init__(self, 
                 posx:int, 
                 posy:int, 
                 radius:int,
                 speed:int, 
                 color:str, 
                 screen:any):
        self._posx = posx
        self._posy = posy
        self._radius = radius
        self._speed = speed
        self._color = color
        self._x_dir = 1
        self._y_dir = -1
        self._ball = pygame.draw.circle(
            screen, self._color, (self._posx, self._posy), self._radius)
        self._first_time = 1
 
    def display(self, screen:any):
        self._ball = pygame.draw.circle(
            screen, 
            self._color, 
            (self._posx, 
             self._posy), 
            self._radius)
 
    def update(self, height:int, width:int):
        self._posx += self._speed*self._x_dir
        self._posy += self._speed*self._y_dir
 
        if self._posy <= 0 or self._posy >= height:
            self._y_dir *= -1
 
        if self._posx <= 0 and self._first_time:
            self._first_time = 0
            return 1
        elif self._posx >= width and self._first_time:
            self._first_time = 0
            return -1
        else:
            return 0
 
    def reset(self, height:int, width:int):
        self._posx = width//2
        self._posy = height//2
        self._x_dir *= -1
        self._first_time = 1
 
    def hit(self):
        self._x_dir *= -1
    
    @property
    def get_rect(self):
        return self._ball
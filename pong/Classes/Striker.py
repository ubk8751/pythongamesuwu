import pygame

class Striker():
    def __init__(self,
                 posx:int,
                 posy:int,
                 width:int,
                 height:int,
                 speed:int,
                 color:str,
                 screen:any):
        self._posx = posx
        self._posy = posy
        self._width = width
        self._height = height
        self._speed = speed
        self._color = color
        self._rect = pygame.Rect(posx, posx, width, height)
        self._me = pygame.draw.rect(screen, self._color, self._rect)
 
    def display(self, screen:any):
        self._me = pygame.draw.rect(screen, self._color, self._rect)
 
    def update(self, direction: int, height: int):
        self._posy += self._speed * direction
        if self._posy <= 0:
            self._posy = 0
        elif self._posy + self._height >= height:
            self._posy = height - self._height
        self._rect = pygame.Rect(self._posx, self._posy, self._width, self._height)

    def displayScore(self,
                     text:str,
                     score:int,
                     x:int,
                     y:int,
                     color:str,
                     font:pygame.font.Font,
                     screen:any):
        text = font.render(text+str(score), True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
 
        screen.blit(text, text_rect)
    
    @property
    def get_rect(self):
        return self._rect
import pygame
from Classes import Ball, Striker
from utils.Constants import *

pygame.init()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font20 = pygame.font.Font('freesansbold.ttf', 20)

def main():
    running = True

    # Define the players
    player1 = Striker(posx=20,
                    posy=0,
                    width=10,
                    height=100,
                    speed=10,
                    color=GREEN,
                    screen=screen)
    player2 = Striker(posx=WIDTH-30,
                    posy=0,
                    width=10,
                    height=100,
                    speed=10,
                    color=GREEN,
                    screen=screen)
    # Get ur ball
    ball = Ball(posx=WIDTH//2,
                posy=HEIGHT//2,
                radius=7,
                speed=7,
                color=WHITE,
                screen=screen)
 
    lst_player = [player1, player2]
    player1Score, player2Score = 0, 0
    player1y_dir, player2y_dir = 0, 0
 
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2y_dir = -1
                if event.key == pygame.K_DOWN:
                    player2y_dir = 1
                if event.key == pygame.K_w:
                    player1y_dir = -1
                if event.key == pygame.K_s:
                    player1y_dir = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2y_dir = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1y_dir = 0
        
        for player in lst_player:
            if pygame.Rect.colliderect(ball.get_rect, player.get_rect):
                ball.hit()

        player1.update(direction=player1y_dir,
                       height=HEIGHT)
        player2.update(direction=player2y_dir,
                       height=HEIGHT)
        point = ball.update(height=HEIGHT,
                            width=WIDTH)
        
        if point == -1:
            player1Score += 1
        elif point == 1:
            player2Score += 1
 
        if point:
            ball.reset(height=HEIGHT,
                       width=WIDTH)
        
        player1.display(screen=screen)
        player2.display(screen=screen)
        ball.display(screen=screen)
 
        player1.displayScore(text="Player 1 : ",
                             score=player1Score,
                             x=100,
                             y=20,
                             color=WHITE,
                             font=font20,
                             screen=screen)
        player2.displayScore(text="Player 2 : ",
                             score=player2Score,
                             x=WIDTH-100,
                             y=20,
                             color=WHITE,
                             font=font20,
                             screen=screen)
 
        pygame.display.update()

        clock.tick(FPS)

if __name__ == '__main__':
    main()
    pygame.quit()
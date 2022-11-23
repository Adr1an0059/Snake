# Import libraries and modules
import pygame
from pygame.locals import *
import Constants

class Snake():
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.snake_body = pygame.image.load("images\snake_body.png")
        self.x = 376
        self.y = 276
    
    def draw(self):
        self.parent_window.fill(Constants.BG_COLOR)
        self.parent_window.blit(self.snake_body, (self.x, self.y))
        pygame.display.flip()
    
    def move_left(self):
        self.x -= 10
        self.draw()
    
    def move_right(self):
        self.x += 10
        self.draw()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
        self.draw()

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(Constants.SIZE)
        self.title = pygame.display.set_caption(Constants.TITLE)
        self.window.fill(Constants.BG_COLOR)
        icon = pygame.image.load("images\icon.png")
        pygame.display.set_icon(icon)
        self.snake = Snake(self.window)
        self.snake.draw()

        pygame.display.update()
    
    def run(self):
        RUNNING = True
        while RUNNING:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        RUNNING = False
                    
                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    
                    if event.key == K_UP:
                        self.snake.move_up()
                    
                    if event.key == K_DOWN:
                        self.snake.move_down()
                
                elif event.type == QUIT:
                    RUNNING = False

game = Game()
game.run()

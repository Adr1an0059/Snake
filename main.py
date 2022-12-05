# Import libraries and modules
import pygame
from pygame.locals import *
import Constants
import time

class Orange():
    def __init__(self, parent_window):
        self.image = pygame.image.load("images\orange.png")
        self.parent_window = parent_window
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_window.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Snake():
    def __init__(self, parent_window, length):
        self.parent_window = parent_window
        self.snake_body = pygame.image.load("images\snake_body.png")
        self.direction = "down"


        self.length = length
        self.x = [24]*length
        self.y = [24]*length

    def draw(self):
        self.parent_window.fill(Constants.BG_COLOR)

        for i in range(self.length):
            self.parent_window.blit(self.snake_body, (self.x[i], self.y[i]))
        pygame.display.flip()
    
    def move_left(self):
        self.direction = "left"
    
    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def walk(self):
        # Uptade body
        for i in range(self.length -1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        # Update head
        if self.direction == "left":
            self.x[0] -= Constants.SIZE_SNAKE
        
        if self.direction == "right":
            self.x[0] += Constants.SIZE_SNAKE
        
        if self.direction == "up":
            self.y[0] -= Constants.SIZE_SNAKE
        
        if self.direction == "down":
            self.y[0] += Constants.SIZE_SNAKE
        
        self.draw()

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(Constants.SIZE)
        self.title = pygame.display.set_caption(Constants.TITLE)
        self.window.fill(Constants.BG_COLOR)
        icon = pygame.image.load("images\icon.png")
        pygame.display.set_icon(icon)

        self.snake = Snake(self.window, 3)
        self.snake.draw()
        
        self.orange = Orange(self.window)
        self.orange.draw()

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

            self.snake.walk()
            self.orange.draw()
            time.sleep(0.050)

game = Game()
game.run() 

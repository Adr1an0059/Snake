# Import libraries and modules
import pygame
from pygame.locals import *
import Constants

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(Constants.SIZE)
        self.title = pygame.display.set_caption(Constants.TITLE)
        self.window.fill(Constants.BG_COLOR)
        icon = pygame.image.load("images\icon.png")
        pygame.display.set_icon(icon)
        pygame.display.update()
    
    def run(self):
        RUNNING = True
        while RUNNING:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        RUNNING = False
                
                elif event.type == QUIT:
                    RUNNING = False

game = Game()
game.run()
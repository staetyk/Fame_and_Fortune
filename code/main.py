import pygame, sys

from pygame.constants import K_END, QUIT, RESIZABLE
pygame.init()

scren = pygame.display.set_mode((0, 0), RESIZABLE)
size = pygame.display.get_window_size()
size = (size[0], size[1]-50)
pygame.display.quit()
pygame.display.init()
screen = pygame.display.set_mode(size)

favi = pygame.image.load("images\Favicon.png")
pygame.display.set_icon(favi)
pygame.display.set_caption("Fame & Fortune", "F&F")

while True:
    events = pygame.event.get()
    if pygame.event.Event(QUIT) in events or pygame.event.Event(K_END) in events:
        pygame.display.quit()
        pygame.quit()
        quit
import pygame, sys

from pygame.constants import K_END, QUIT
pygame.init()

scren = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
size = pygame.display.get_window_size()
size = (size[0], size[1]-50)
pygame.display.quit()
pygame.display.init()
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

while True:
    events = pygame.event.get()
    if pygame.event.Event(QUIT) in events or pygame.event.Event(K_END) in events:
        pygame.display.quit()
        pygame.quit()
        quit
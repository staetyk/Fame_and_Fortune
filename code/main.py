import pygame, sys

from pygame.constants import K_END, QUIT
pygame.init()

PINK = 0xFF4040
BLACK = 0x000000
BLUE = 0x0000FF

screen = pygame.display.set_mode((1536, 801), pygame.RESIZABLE)

while True:
    events = pygame.event.get()
    if pygame.event.Event(QUIT) in events or pygame.event.Event(K_END) in events:
        pygame.display.quit()
        pygame.quit()
        quit
    print(pygame.display.get_window_size())
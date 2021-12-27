import pygame, sys

from pygame.constants import K_END, K_RETURN, QUIT, RESIZABLE
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

def end():
    events = pygame.event.get()
    if pygame.event.Event(QUIT) in events or pygame.event.Event(K_END) in events:
        pygame.display.quit()
        pygame.quit()
        quit

def scale(img: pygame.Surface, width: int = None, hight: int = None) -> pygame.Surface:
    size = img.get_size()
    ratio = size[0] // size[1]
    if width == None:
        width = hight * ratio
    elif hight == None:
        hight = width // ratio
    img = pygame.transform.scale(img, (width, hight))
    return img

screen.fill(0x171717)
logo = pygame.image.load("images\LOGO.png")
logo = scale(logo, width = size[0]-10)
logo.set_colorkey((255,255,255))
screen.blit(logo, (0,100))
pygame.display.flip()


while True:
    end()
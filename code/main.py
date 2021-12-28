import pygame, sys

from pygame.constants import K_END, K_RETURN, QUIT, RESIZABLE
pygame.init()

monitor = pygame.display.Info()
pygame.display.init()
screen = pygame.display.set_mode((monitor.current_w, monitor.current_h -50), RESIZABLE)
size = pygame.display.get_surface().get_size()

favi = pygame.image.load(".venv\images\Favicon.png")
pygame.display.set_icon(favi)
pygame.display.set_caption("Fame & Fortune", "F&F")

def end():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
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
logo = pygame.image.load(".venv\images\LOGO.png")
logo = scale(logo, width = size[0]-10)
logo.set_colorkey((255,255,255))
screen.blit(logo, (0,100))
pygame.display.flip()


while True:
    end()
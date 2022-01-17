import pygame, sys

from pygame.constants import K_END, K_RETURN, QUIT, RESIZABLE
pygame.init()

monitor = pygame.display.Info()
pygame.display.init()
screen = pygame.display.set_mode((monitor.current_w, monitor.current_h -50), RESIZABLE)
size = pygame.display.get_surface().get_size()

favi = pygame.image.load("images//Favicon.png")
favi.set_colorkey((255,255,255))
pygame.display.set_icon(favi)
pygame.display.set_caption("Fame & Fortune", "F&F")

def end():
    if pygame.event.peek(QUIT):
        pygame.display.quit()
        pygame.quit()
        quit

def scale(img: pygame.Surface, width: int = None, height: int = None) -> pygame.Surface:
    size = img.get_size()
    ratio = size[0] // size[1]
    if width == None:
        width = height * ratio
    elif height == None:
        height = width // ratio
    img = pygame.transform.scale(img, (width, height))
    return img


NewArea = pygame.event.custom_type()


area = "logo"
area_que = ["main", "loading"]

pygame.time.set_timer(NewArea, 9600, 1)

music = pygame.mixer.Sound("music/theme.wav")
music.set_volume(0.75)
music.play(-1)
while True:
    end()

    if pygame.event.peek(NewArea):
        if pause:
            pygame.mixer.pause()
        area = area_que[0]
        area_que = area_que[1:]
        pygame.event.clear(NewArea)


    if area == "logo":
        music = pygame.mixer.Sound("music/theme.wav")
        pygame.mixer.unpause()
        pause = False

        screen.fill(0x171717)
        logo = pygame.image.load("images//LOGO.png")
        logo = scale(logo, width = size[0]-10)
        logo.set_colorkey((255,255,255))
        screen.blit(logo, (0,100))
        pygame.display.flip()
    

    elif area == "main":
        music = pygame.mixer.Sound("music/theme.wav")
        pygame.mixer.unpause()
        pause = True

        screen.fill(0x000011)
        logo = pygame.image.load("images//LOGO.png")
        logo = scale(logo, height = size[1]-600)
        logo.set_colorkey((255,255,255))
        screen.blit(logo, (0,100))
        pygame.display.flip()
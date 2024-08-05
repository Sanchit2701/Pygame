import pygame
pygame.init()
gamedisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("a bit of racing")
clock = pygame.time.Clock()
Crashed = False

while not Crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Crashed=True
        print(event)
    pygame.display.update()

    clock.tick(60)
pygame.quit()
quit()

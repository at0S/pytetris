import pygame

WIDTH, HEIGHT = 1024, 768
FPS = 60
GAME_RESOLUTION = (WIDTH, HEIGHT)

pygame.init()

screen = pygame.display.set_mode(GAME_RESOLUTION)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

while True:
    
    screen.fill(pygame.Color("black"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()
    clock.tick()


import pygame

class Dino:
    def __init__(self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw(self, surface):
        pygame.draw.rect(surface, (0,0,0), self.rect)
        
class Cactus:
    def __init__(self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw(self, surface):
        pygame.draw.rect(surface, (0,0,0), self.rect)

pygame.init()

screen = pygame.display.set_mode((1200, 400))

dino = pygame.image.load("trex1.png")
cacti = pygame.image.load("obstacle1.png")
ground = pygame.image.load("ground.png")

dino_rect = Dino(100, 250, 64, 64)
cactus_rect = Cactus(1100, 275, 32, 32)
ground_rect = pygame.Rect(0, 330, 1200, 2)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    dino_rect.draw(screen)
    cactus_rect.draw(screen)
    screen.blit(ground, ground_rect)
            
    pygame.display.update()
    pygame.time.delay(1)

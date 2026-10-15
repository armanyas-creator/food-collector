import sys
import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pet Food Collection Game")

try:
    bg_image = pygame.image.load("game background.jpg").convert()
    bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error:

    bg_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_image.fill((30, 30, 30))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255)) 
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

all_sprites = pygame.sprite.Group()
food_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

food_items = [Food(200, 200), Food(500, 150), Food(350, 450), Food(600, 400)]
for food in food_items:
    all_sprites.add(food)
    food_group.add(food)

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 48)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    collected_foods = pygame.sprite.spritecollide(player, food_group, True)
    for food in collected_foods:
        food.kill()

    screen.blit(bg_image, (0, 0))

    all_sprites.draw(screen)

    if len(food_group) == 0:
        win_text = game_font.render("All Food Collected! Great Job!", True, (255, 255, 255))
        text_rect = win_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(win_text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
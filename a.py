import pygame, sys, random

pygame.init()
WIDTH, HEIGHT = 640, 480
TILESIZE = 32
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)

# --- Classes ---
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, walls_group):
        super().__init__()
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = 10
        self.walls = walls_group


    def update(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_a]: dx = -4
        if keys[pygame.K_d]: dx = 4
        if keys[pygame.K_w]: dy = -4
        if keys[pygame.K_s]: dy = 4
        self.rect.x += dx
        self.rect.y += dy

        for wall in pygame.sprite.spritecollide(self, walls, False):
            if dx > 0:  # moving right
                self.rect.right = wall.rect.left
            if dx < 0:  # moving left
                self.rect.left = wall.rect.right

        for wall in pygame.sprite.spritecollide(self, walls, False):
            if dy > 0:  # moving down
                self.rect.bottom = wall.rect.top
            if dy < 0:  # moving up
                self.rect.top = wall.rect.bottom

    def shoot(self, target_pos):
        bullet = Projectile(self.rect.centerx, self.rect.centery, target_pos)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = 3

    def update(self):
        # Random movement
        if random.randint(0, 20) == 0:
            self.rect.x += random.choice([-TILESIZE, TILESIZE, 0])
            self.rect.y += random.choice([-TILESIZE, TILESIZE, 0])

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, target_pos):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        # Calculate velocity towards target
        dx, dy = target_pos[0] - x, target_pos[1] - y
        dist = max(1, (dx**2 + dy**2) ** 0.5)
        self.vx, self.vy = dx / dist * 8, dy / dist * 8

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        # Remove if off screen
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

# --- Groups ---
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# --- Load map from file ---
player = None
with open("map.txt") as f:
    for row_idx, line in enumerate(f):
        for col_idx, char in enumerate(line.strip()):
            x, y = col_idx * TILESIZE, row_idx * TILESIZE
            if char == "1":
                wall = Wall(x, y)
                all_sprites.add(wall)
                walls.add(wall)
            elif char == "E":
                enemy = Enemy(x, y)
                all_sprites.add(enemy)
                enemies.add(enemy)
            elif char == "P":  # optional: place player in map
                player = Player(x, y,walls)
                all_sprites.add(player)

if not player:  # fallback if no P in map
    player = Player(50, 50,walls)
    all_sprites.add(player)

# --- Game loop ---
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.shoot(pygame.mouse.get_pos())

    # Update
    player.update(keys)
    enemies.update()
    bullets.update()

    # Collisions
    for bullet in bullets:
        if pygame.sprite.spritecollide(bullet, walls, False):
            bullet.kill()
        hit_list = pygame.sprite.spritecollide(bullet, enemies, False)
        for enemy in hit_list:
            enemy.health -= 1
            bullet.kill()
            if enemy.health <= 0:
                enemy.kill()

    if pygame.sprite.spritecollide(player, enemies, False):
        player.health -= 1
        if player.health <= 0:
            print("Game Over!")
            pygame.quit(); sys.exit()

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.set_caption(f"Health: {player.health}")
    pygame.display.flip()
    clock.tick(60)
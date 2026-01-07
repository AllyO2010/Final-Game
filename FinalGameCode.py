import random
import pygame
import sys
# Initialize Pygame
pygame.init()

# --- Constants and Colors ---
TILE_SIZE = 70
WIDTH = 15 * TILE_SIZE
HEIGHT = 15 * TILE_SIZE
FPS = 60
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
scissors = pygame.sprite.Group()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PURPLE = (170,0,128)

#Create player and updating player postion
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("landa.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 110))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
        self.currentweapon="Nothing"
        self.speed = 5
    def update(self, walls, rocks, trees, cavewalls, bushes, housewalls, hole, crates, basementwalls, move, couch, stand, stove, bed, box, INVENTORY, tables):
        old_x, old_y = self.rect.topleft
        keys = pygame.key.get_pressed()
        if move:
           if keys[pygame.K_LEFT]:
               self.rect.x -= self.speed
           if keys[pygame.K_RIGHT]:
               self.rect.x += self.speed
           if pygame.sprite.spritecollide(self, walls, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, rocks, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, trees, False, pygame.sprite.collide_mask)\
              or pygame.sprite.spritecollide(self, cavewalls, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, bushes, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, housewalls, False, pygame.sprite.collide_mask)\
              or pygame.sprite.spritecollide(self, hole, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, crates, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, basementwalls, False, pygame.sprite.collide_mask)\
              or pygame.sprite.spritecollide(self, stand, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, bed, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, tables, False, pygame.sprite.collide_mask):               self.rect.x = old_x
           if stove and pygame.sprite.collide_mask(self, stove):
               self.rect.x = old_x
           if couch and pygame.sprite.collide_mask(self, couch):
               self.rect.x = old_x
           if box and pygame.sprite.collide_mask(self, box):
               self.rect.x = old_x
           if keys[pygame.K_UP]:
               self.rect.y -= self.speed
           if keys[pygame.K_DOWN]:
               self.rect.y += self.speed
           if pygame.sprite.spritecollide(self, walls, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, rocks, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, trees, False, pygame.sprite.collide_mask)\
              or pygame.sprite.spritecollide(self, cavewalls, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, bushes, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, housewalls, False, pygame.sprite.collide_mask)\
              or pygame.sprite.spritecollide(self, hole, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, crates, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, basementwalls, False, pygame.sprite.collide_mask)\
              or pygame.sprite.spritecollide(self, stand, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, bed, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, tables, False, pygame.sprite.collide_mask):
               self.rect.y = old_y
           if stove and pygame.sprite.collide_mask(self, stove):
               self.rect.y = old_y
           if couch and pygame.sprite.collide_mask(self, couch):
               self.rect.y = old_y
           if box and pygame.sprite.collide_mask(self, box):
               self.rect.y = old_y
           if keys[pygame.K_1] and "Knife" in INVENTORY:
               self.image = pygame.image.load("landaKnife.png").convert_alpha()
               self.image = pygame.transform.scale(self.image, (75, 110))
               self.currentweapon="Knife"
               if "ShrinkPotion" in INVENTORY:
                  self.image = pygame.image.load("landaKnife.png").convert_alpha()
                  self.image = pygame.transform.scale(self.image, (60, 60))
               
           if keys[pygame.K_2] and "Gun" in INVENTORY:
               self.image = pygame.image.load("landaGun.png").convert_alpha()
               self.image = pygame.transform.scale(self.image, (75, 110))
               self.currentweapon="Gun"
               if "ShrinkPotion" in INVENTORY:
                  self.image = pygame.image.load("landaGun.png").convert_alpha()
                  self.image = pygame.transform.scale(self.image, (60, 60))
           if keys[pygame.K_3] and "Scissors" in INVENTORY:
               self.image = pygame.image.load("landaScissors.png").convert_alpha()
               self.image = pygame.transform.scale(self.image, (75, 110))
               self.currentweapon="Scissors"
    def shoot(self, target_pos):
        bullet = Bullet(self.rect.centerx, self.rect.centery, target_pos)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootScissors(self, target_pos):
        scissor = Scissor(self.rect.centerx, self.rect.centery, target_pos)
        scissorX=scissor.rect.x
        scissorY=scissor.rect.y
        targetX= target_pos[0]
        if targetX < scissorX:   
            scissor.image = pygame.image.load("ScissorsL.png").convert_alpha()
            scissor.image = pygame.transform.scale(scissor.image, (40, 40))
        if targetX > scissorX:   
            scissor.image = pygame.image.load("ScissorsR.png").convert_alpha()
            scissor.image = pygame.transform.scale(scissor.image, (40, 40))
        all_sprites.add(scissors)
        scissors.add(scissor)

         
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("wall.png").convert()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
class HouseWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("HouseWall").convert()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("wall.png").convert()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
class CaveWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("CaveWall.png").convert()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("tree.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (650, 650))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
class Cave(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("cave.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (550, 550))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("rock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
class Chest(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("chest.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("diamond.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("gun.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(bottomleft=(x, y))
class Knife(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("knife.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(bottomleft=(x, y))
class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("lava.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class BasementWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("BasementWall.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Bush(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bush.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
class KeyBush(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bush.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
class Cabin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("cabin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (350, 350))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("key.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Hole(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("hole.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 100))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
class Crate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("crate.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Door.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Stand(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Nightstand.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Lake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Lake.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Bed(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Bed.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Stove(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Stove.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Boxes.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Couch(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Couch.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Rope(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Rope.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Potion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("potion.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Rug(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Rug2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect(topleft=(x, y))
class Table(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Table.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
class Mountain(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("mountain.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (700, 450))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
class npc(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("RedDuck.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topright=(x, y))
class keypiece(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("keyPiece.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topright=(x, y))
class Bullet(pygame.sprite.Sprite):
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
        if self.rect.right < 0 or self.rect.left> WIDTH or self.rect.bottom<0 or self.rect.top>HEIGHT:
            self.kill()
class Scissor(pygame.sprite.Sprite):
    def __init__(self, x, y, target_pos):
        super().__init__()
        self.image = pygame.image.load("ScissorsR.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        # Calculate velocity towards target
        dx, dy = target_pos[0] - x, target_pos[1] - y
        dist = max(1, (dx**2 + dy**2) ** 0.5)
        self.vx, self.vy = dx / dist * 8, dy / dist * 8

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        # Remove if off screen
        if self.rect.right < 0 or self.rect.left> WIDTH or self.rect.bottom<0 or self.rect.top>HEIGHT:
            self.kill()      
  

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("phoneR.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 10
    def updateEnemy(self, walls, DIRECTION):     
        old_x = self.rect.x
        if DIRECTION=="+":  
           self.rect.x += self.speed
           self.image = pygame.image.load("phoneR.png").convert_alpha()
           self.image = pygame.transform.scale(self.image, (100, 100))
           if pygame.sprite.spritecollide(self, walls, False, pygame.sprite.collide_mask):
                  self.rect.x = old_x
                  DIRECTION= "-"
        if DIRECTION=="-":  
           self.rect.x -= self.speed
           self.image = pygame.image.load("phoneL.png").convert_alpha()
           self.image = pygame.transform.scale(self.image, (100, 100))
           if pygame.sprite.spritecollide(self, walls, False, pygame.sprite.collide_mask):
                  self.rect.x = old_x
                  DIRECTION= "+"      
        return DIRECTION  
    def UPDATEenemy(self, solid_sprites):
      old_x, old_y = self.rect.topleft
      if random.randint(0, 7) == 0:
         self.rect.x += random.choice([-TILE_SIZE, TILE_SIZE, 0])
         self.rect.y += random.choice([-TILE_SIZE, TILE_SIZE, 0])
      if pygame.sprite.spritecollide(self, solid_sprites, False, pygame.sprite.collide_mask):
         self.rect.x = old_x
         self.rect.y = old_y

      
#read file and convert it onto the screen
def load_maze(filename):
    wall_sprites = pygame.sprite.Group()
    cavewall_sprites = pygame.sprite.Group()
    lava_sprites = pygame.sprite.Group()
    bush_sprites = pygame.sprite.Group()
    housewall_sprites = pygame.sprite.Group()
    hole_sprites = pygame.sprite.Group()
    crate_sprites = pygame.sprite.Group()
    door_sprites = pygame.sprite.Group()
    basementwall_sprites = pygame.sprite.Group()
    stand_sprites = pygame.sprite.Group()
    bed_sprites = pygame.sprite.Group()
    table_sprites = pygame.sprite.Group()
    potion=None
    box=None
    couch=None
    stove=None
    gun=None
    key=None
    knife=None
    chest=None
    cabin=None
    keybush=None
    diamond= None
    player = None
    mountain=None
    lake=None
    rope=None
    enemy=None
    KeyPiece=None
    NPC=None
    rug=None
    tree_sprites= pygame.sprite.Group()
    cave=None
    rock_sprites=pygame.sprite.Group()
    maze_level = []
    with open(filename, "r") as file:
        for line in file:
            maze_level.append(line.strip())
    for row_index, row in enumerate(maze_level):
        for col_index, char in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            if char == '1':
                wall = Wall(x, y)
                all_sprites.add(wall)
                wall_sprites.add(wall)
            if char == '4':
                housewall = HouseWall(x, y)
                all_sprites.add(housewall)
                housewall_sprites.add(housewall)
            elif char == 'T':
                tree = Tree(x, y)
                all_sprites.add(tree)
                tree_sprites.add(tree)
            elif char == 't':
                table = Table(x, y)
                all_sprites.add(table)
                table_sprites.add(table)
            elif char == 'x':
                rug = Rug(x, y)
                all_sprites.add(rug)
            elif char == '2':
                caveWall = CaveWall(x, y)
                all_sprites.add(caveWall)
                cavewall_sprites.add(caveWall)
            elif char == '3':
                crate = Crate(x, y)
                all_sprites.add(crate)
                crate_sprites.add(crate)
            elif char == '5':
                basementWall = BasementWall(x, y)
                all_sprites.add(basementWall)
                basementwall_sprites.add(basementWall)
            elif char == 'C':
                cave = Cave(x, y)
                all_sprites.add(cave)
            elif char == 'E':
                enemy = Enemy(x, y)
                all_sprites.add(enemy)
            elif char == 'D':
                door = Door(x, y)
                all_sprites.add(door)
                door_sprites.add(door)
            elif char == 'd':
                diamond = Diamond(x, y)
                all_sprites.add(diamond)
            elif char == 'r':
                NPC = npc(x, y)
                all_sprites.add(NPC)
            elif char == 'R':
                rock = Rock(x, y)
                all_sprites.add(rock)
                rock_sprites.add(rock)
            elif char == 'B':
                bush = Bush(x, y)
                all_sprites.add(bush)
                bush_sprites.add(bush)
            elif char == 'b':
                keybush = KeyBush(x, y)
                all_sprites.add(keybush)
            elif char == 'z':
                rope = Rope(x, y)
                all_sprites.add(rope)
            elif char == 'c':
                cabin = Cabin(x, y)
                all_sprites.add(cabin)
            elif char == 'l':
                lake = Lake(x, y)
                all_sprites.add(lake)
            elif char == 'L':
                lava = Lava(x, y)
                all_sprites.add(lava)
                lava_sprites.add(lava)
            elif char == 'H':
                chest = Chest(x, y)
                all_sprites.add(chest)
            elif char == 'M':
                mountain = Mountain(x, y)
                all_sprites.add(mountain)
            elif char == 'h':
                hole = Hole(x, y)
                all_sprites.add(hole)
                hole_sprites.add(hole)
            elif char == 'G':
                gun = Gun(x, y)
                all_sprites.add(gun)
            elif char == 'K':
                knife = Knife(x, y)
                all_sprites.add(knife)
            elif char == 'S':
                stove = Stove(x, y)
                all_sprites.add(stove)
            elif char == 'q':
                couch = Couch(x, y)
                all_sprites.add(couch)
            elif char == 'Q':
                stand = Stand(x, y)
                all_sprites.add(stand)
                stand_sprites.add(stand)
            elif char == 's':
                bed = Bed(x, y)
                all_sprites.add(bed)
                bed_sprites.add(bed)
            elif char == 'k':
                key = Key(x, y)
                all_sprites.add(key)
            elif char == 'p':
                potion = Potion(x, y)
                all_sprites.add(potion)
            elif char == 'W':
                box = Box(x, y)
                all_sprites.add(box)
            elif char == 'f':
                KeyPiece = keypiece(x, y)
                all_sprites.add(KeyPiece)
            elif char == 'P':
                player = Player(x, y)
                all_sprites.add(player)
    return all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush,  cabin, housewall_sprites, chest,\
           gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug


def main():
    #LEVELS/LOCATIONS
    LEVEL=3
    LOCATION=3
    #Screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites,keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites,\
    key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
    #Dialogue
    key_message_time=0
    sleep_message_time=0
    L1L8Key_message_time=0
    dialog_active=False
    dialog_index=0
    RedDuckDialog_lines = [
    "Red Duck: Hello Mr. Landa",
    "Landa: Hi, I'm trying to save Chuck",
    "Red Duck: Inside that cave is a diamond, grab it",
    "Red Duck: And it will send you on your quest",
    "Landa: Thanks!"
]
    BlueDuckDialog_lines = [
    "Blue Duck: Afternoon Mr. Landa",
    "Landa: Hi do you know what is in that cabin",
    "Blue Duck: This is the cabin of the evil phones",
    "Blue Duck: There are weapons inside...",
    "Blue Duck: but be careful",
    "Landa: Thank for the advice!"
]
    GreenDuckDialog_lines = [
    "Green Duck: Hello there, I need some help",
    "Landa: What do you need?",
    "Green Duck: I've been stuck down here",
    "Green Duck: I don't know how to get out",
    "Green Duck: We can both find a way to escape"
]
    GreenDuckDialog_lines2 = [
    "Green Duck: Thanks you for saving me",
    "Landa: Do you know how I can get to chuck",
    "Green Duck: Up on the mountain are the...",
    "Green Duck: Chromebooks. Once you get past...",
    "Green Duck: You will be closer to saving Chcuk"
]
    PurpleDuckDialog_lines = [
    "Purple Duck: Can you help me find my lost bag?",
    "Landa: Whats in it for me?",
    "Purple Duck: I'll give you this key fragment",
]
    PurpleDuckDialog_lines2 = [
    "Purple Duck: You found my bag! Thank you",
    "Purple Duck: Here's the key fragment",
    "Landa: Thank you"
]

    font = pygame.font.SysFont(None, 50)
    L1L6EnemyDirection="+"
    running=True
    movement=True
    collidedkeybush=False
    collidedCabinChest=False
    inventory=["Gun"]
    level_won=False
    Lives=4
    pygame.display.set_caption("Lives: "+str(Lives))
    Phone_Lives=10
    Chromebook_Lives=30
    Paper_Lives=30
    solid_sprites= pygame.sprite.Group(wall_sprites,cavewall_sprites,housewall_sprites,basementwall_sprites,crate_sprites, bed_sprites, stand_sprites, rock_sprites, table_sprites, door_sprites, bush_sprites, tree_sprites)

    while running:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
               if player.currentweapon=="Gun":
                   player.shoot(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN:
               if player.currentweapon=="Scissors":
                   player.shootScissors(pygame.mouse.get_pos())
            

      if LEVEL==1:
         if LOCATION==1:
            background_color=(72,111,56)
            screen.fill(background_color) 
            if not level_won:
                 keys = pygame.key.get_pressed()
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if pygame.sprite.collide_mask(player, NPC) and not dialog_active:
                        if keys[pygame.K_e]:
                           dialog_active = True
                           movement = False
                           dialog_index = 0           
                 if dialog_active and keys[pygame.K_SPACE]:
                     dialog_index += 1
                     pygame.time.wait(200) 
                 if dialog_index >= len(RedDuckDialog_lines):
                     dialog_active = False
                     movement = True  
                 if dialog_active and dialog_index < len(RedDuckDialog_lines):
                     text = font.render(RedDuckDialog_lines[dialog_index], True, (0,0,0))
                     screen.blit(text, (80, 900))  
                 if cave and pygame.sprite.collide_mask(player, cave):
                        bullets.empty()
                        all_sprites.empty()
                        LOCATION=2
                        file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                        all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites, chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file) 
         if LOCATION==2:
            background_color=(103, 110, 112)
            screen.fill(background_color) 
            if not level_won:
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if pygame.sprite.spritecollide(player, lava_sprites, False, pygame.sprite.collide_mask):
                     player.rect.bottomleft = 80, 975
                     Lives-=1
                     pygame.display.set_caption("Lives: "+str(Lives))
                 if player.rect.right > 1070:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=3
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)            
         if LOCATION==3:
            background_color=(103, 110, 112)
            screen.fill(background_color) 
            if not level_won:
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if diamond and pygame.sprite.collide_mask(player, diamond):
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=4
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites ,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
                 if pygame.sprite.spritecollide(player, lava_sprites, False, pygame.sprite.collide_mask):
                     player.rect.bottomleft = 50, 190
                     Lives-=1
                     pygame.display.set_caption("Lives: "+str(Lives))
                 if player.rect.left < 0:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=2
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)            
                    player.rect.topleft = (960, 100)
         if LOCATION==4:
           background_color=(72,111,56)
           screen.fill(background_color)
           if not level_won:
                player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                if keybush and not collidedkeybush and pygame.sprite.collide_mask(player, keybush):
                      collidedkeybush=True
                      key_message_time=pygame.time.get_ticks() 
                      inventory.append("CabinKey")
                if collidedkeybush and pygame.time.get_ticks() - key_message_time < 2000:
                    text = font.render("You found a key!", True, (0,0,0))
                    screen.blit(text, (440, 500))
                if player.rect.bottom > 1050:
                    playerX=player.rect.x
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=5
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
                    player.rect.topleft = (playerX, 20)
         if LOCATION==5:
            NPC.image = pygame.image.load("BlueDuck.png").convert_alpha()
            NPC.image = pygame.transform.scale(NPC.image, (100, 100))
            background_color=(72,111,56)
            screen.fill(background_color) 
            if not level_won:
                 oldX=player.rect.x
                 oldY=player.rect.y
                 keys = pygame.key.get_pressed()
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if pygame.sprite.collide_mask(player, NPC) and not dialog_active:
                        if keys[pygame.K_e]:
                           dialog_active = True
                           movement = False
                           dialog_index = 0           
                 if dialog_active and keys[pygame.K_SPACE]:
                     dialog_index += 1
                     pygame.time.wait(200) 
                 if dialog_index >= len(BlueDuckDialog_lines):
                     dialog_active = False
                     movement = True  
                 if dialog_active and dialog_index < len(BlueDuckDialog_lines):
                     text = font.render(BlueDuckDialog_lines[dialog_index], True, (0,0,0))
                     screen.blit(text, (80, 900))
                 if pygame.sprite.collide_mask(player, cabin) and not "CabinKey" in inventory:
                     player.rect.topleft = (oldX, oldY)
                 if pygame.sprite.collide_mask(player, cabin) and "CabinKey" in inventory:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=6
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
                 if player.rect.top < 0:
                    playerX=player.rect.x
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=4
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites,crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
                    player.rect.topleft = (playerX, 940)
         if LOCATION==6:
            background_color=(153, 146, 142)
            screen.fill(background_color) 
            if not level_won:
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if chest and not collidedCabinChest and pygame.sprite.collide_mask(player, chest):
                      collidedCabinChest=True
                      L1L8Key_message_time=pygame.time.get_ticks() 
                      inventory.append("Gun")
                 if collidedCabinChest and pygame.time.get_ticks() - L1L8Key_message_time < 2000:
                      text = font.render("You found a Gun!", True, (0,0,0))
                      screen.blit(text, (440, 500))
                 if pygame.sprite.collide_mask(player, knife):
                     inventory.append("Knife")
                     knife.rect.topleft = (-100, -100)
                 if "Knife" in inventory:
                     knife.rect.topleft = (-100, -100)
                 if player.rect.right > 1070:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=7
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
         if LOCATION==7:
            background_color=(153, 146, 142)
            screen.fill(background_color) 
            if not level_won:
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if "BasementKey" in inventory:
                     key.rect.topleft = (-100, -100)
                 if player.rect.left < 0:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=6
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
                    player.rect.topleft = (960, 500)
                 if enemy and pygame.sprite.collide_mask(player, enemy):
                    player.rect.topleft = (0,70)
                    Lives-=1
                    pygame.display.set_caption("Lives: "+str(Lives))
                 if enemy:
                    L1L6EnemyDirection=enemy.updateEnemy(housewall_sprites, L1L6EnemyDirection) 
                 if key is not None and pygame.sprite.collide_mask(player, key):
                    inventory.append("BasementKey")
                    key.rect.topleft = (-100, -100)
                 if pygame.sprite.spritecollide(player, door_sprites, False, pygame.sprite.collide_mask) and "BasementKey" in inventory and "Gun" in inventory and "Knife" in inventory:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=8
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
         if LOCATION==8:
            background_color=(82, 84, 82)
            screen.fill(background_color)
            if not level_won:
                 keys = pygame.key.get_pressed()
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if pygame.sprite.spritecollide(player, door_sprites, False, pygame.sprite.collide_mask):
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=7
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
                    player.rect.topleft = (690, 825)
                 if player.rect.bottom > 470 and player.rect.right > 930 and player.currentweapon=="Knife":
                    if keys[pygame.K_e]:
                        box.rect.topleft = (-100, -100)
                 if key is not None and pygame.sprite.collide_mask(player, key):
                    inventory.append("L1L8KEY")
                    key.rect.topleft = (-100, -100)
                 if "L1L8KEY" in inventory:
                     key.rect.topleft = (-100, -100)
                 if player.rect.bottom > 1070:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=9
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
         if LOCATION==9:
            NPC.image = pygame.image.load("GreenDuck.png").convert_alpha()
            NPC.image = pygame.transform.scale(NPC.image, (100, 100))
            background_color=(82, 84, 82)
            screen.fill(background_color)
            if not level_won:
                 keys = pygame.key.get_pressed()
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if pygame.sprite.collide_mask(player, NPC) and not dialog_active:
                        if keys[pygame.K_e]:
                           dialog_active = True
                           movement = False
                           dialog_index = 0           
                 if dialog_active and keys[pygame.K_SPACE]:
                     dialog_index += 1
                     pygame.time.wait(200) 
                 if dialog_index >= len(GreenDuckDialog_lines):
                     dialog_active = False
                     movement = True  
                 if dialog_active and dialog_index < len(GreenDuckDialog_lines):
                     text = font.render(GreenDuckDialog_lines[dialog_index], True, (0,0,0))
                     screen.blit(text, (80, 850))                 
                 if player.rect.top < 0:
                    inventory.remove("ShrinkPotion")
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=8
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
                    player.rect.topleft = (70, 840)
                 if key is not None and pygame.sprite.collide_mask(player, key):
                    inventory.append("L1L9KEY")
                    key.rect.topleft = (-100, -100)
                 if "L1L9KEY" in inventory:
                     key.rect.topleft = (-100, -100)
                 if potion is not None and pygame.sprite.collide_mask(player, potion):
                    inventory.append("ShrinkPotion")
                    potion.rect.topleft = (-100, -100)
                 if "ShrinkPotion" in inventory:
                    player.image = pygame.transform.scale(player.image, (60, 60))
                    player.mask=pygame.mask.from_surface(player.image)
                 if player.rect.bottom > 900 and player.rect.left < 100 and player.currentweapon=="Knife":
                    if keys[pygame.K_e]:
                        box.rect.topleft = (-100, -100) 
                 if pygame.sprite.spritecollide(player, door_sprites, False, pygame.sprite.collide_mask) and "L1L9KEY" in inventory and "L1L8KEY" in inventory:
                     if "ShrinkPotion" in inventory:
                        inventory.remove("ShrinkPotion")
                     bullets.empty()
                     all_sprites.empty()
                     LEVEL=2
                     LOCATION=1
                   
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
         for bullet in bullets:
            if pygame.sprite.spritecollide(bullet, solid_sprites, False):
               bullet.kill()
            if enemy and pygame.sprite.collide_mask(bullet, enemy):
               Phone_Lives-=1
               bullet.kill()
         if enemy and Phone_Lives<=0:
            enemy.kill()
            enemy.rect.topleft = (-1000, -1000) 
            
         bullets.update()
         all_sprites.draw(screen)
         
         bullets.draw(screen)
         pygame.display.flip()  
         if Lives<=0:
            collidedkeybush=False
            collidedCabinChest=False
            inventory=[]
            level_won=False
            bullets.empty()
            all_sprites.empty()
            Lives=5
            pygame.display.set_caption("Lives: "+str(Lives))
            LEVEL=1
            LOCATION=1
            file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
            all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites,keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites,\
            key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
      if LEVEL==2: 
         if LOCATION==1:
            NPC.image = pygame.image.load("GreenDuck.png").convert_alpha()
            NPC.image = pygame.transform.scale(NPC.image, (100, 100))
            background_color=(72,111,56)
            screen.fill(background_color)
            if not level_won:
               oldX=player.rect.x
               oldY=player.rect.y
               keys = pygame.key.get_pressed()
               player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
               if pygame.sprite.collide_mask(player, NPC) and not dialog_active:
                        if keys[pygame.K_e]:
                           dialog_active = True
                           movement = False
                           dialog_index = 0           
               if dialog_active and keys[pygame.K_SPACE]:
                     dialog_index += 1
                     pygame.time.wait(200) 
               if dialog_index >= len(GreenDuckDialog_lines2):
                     dialog_active = False
                     movement = True  
               if dialog_active and dialog_index < len(GreenDuckDialog_lines2):
                     text = font.render(GreenDuckDialog_lines2[dialog_index], True, (0,0,0))
                     screen.blit(text, (80, 850))   
               if pygame.sprite.collide_mask(player, rope):
                   inventory.append("Rope")
                   rope.rect.topleft = (-100, -100)
               if pygame.sprite.collide_mask(player, mountain) and not "Rope" in inventory:
                  player.rect.topleft = (oldX, oldY)
               if pygame.sprite.collide_mask(player, mountain) and "Rope" in inventory:
                  bullets.empty()
                  all_sprites.empty()
                  LOCATION=2
                  file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                  all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
         if LOCATION==2:
            player.speed=9
            enemy.image = pygame.image.load("chromebook.png").convert_alpha()
            enemy.image = pygame.transform.scale(enemy.image, (300, 300))
            background_color=(103, 110, 112)
            screen.fill(background_color)
            if not level_won:
               if enemy.alive():
                  enemyX=enemy.rect.x
                  enemyY=enemy.rect.y
               player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
               if enemy and pygame.sprite.collide_mask(player, enemy):
                    player.rect.topleft = (100,100)
                    Lives-=1
                    pygame.display.set_caption("Lives: "+str(Lives))
               if enemy:
                    enemy.UPDATEenemy(solid_sprites)
   
               if not enemy.alive():
                  diamond.rect.topleft = (enemyX,enemyY)
               if diamond and pygame.sprite.collide_mask(player, diamond):
                  bullets.empty()
                  all_sprites.empty()
                  player.speed=6
                  LOCATION=3
                  file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                  all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
         if LOCATION==3:
            background_color=(72,111,56)
            screen.fill(background_color)
            if not level_won:
               playerX=player.rect.x
               playerY=player.rect.y
               player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
               if pygame.sprite.collide_mask(player, cabin):
                  if not "L3Piece" in inventory or not "L4Piece" in inventory or not "L5Piece" in inventory or not "L6Piece" in inventory:
                     player.rect.topleft = (playerX, playerY)
               if pygame.sprite.collide_mask(player, cabin) and "L3Piece" in inventory and "L4Piece" in inventory and "L5Piece" in inventory and "L6Piece" in inventory:
                  bullets.empty()
                  all_sprites.empty()
                  LOCATION=7
                  file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                  all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
               if KeyPiece and  pygame.sprite.collide_mask(player, KeyPiece):
                  inventory.append("L3Piece")
                  KeyPiece.rect.topleft = (-100, -100) 
               if lake and pygame.sprite.collide_mask(player, lake):
                  player.speed=3
               if lake and not pygame.sprite.collide_mask(player, lake):
                  player.speed=5
               if player.rect.bottom > 1050:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=5
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                    player.rect.topleft = (playerX, 50)
                    if "Bag" in inventory:
                        knife.rect.topleft = (-100, -100) 
                    if "L5Piece" in inventory:
                        KeyPiece.rect.topleft = (-100, -100) 
               if player.rect.right > 1070:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=4
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                    player.rect.topleft = (50, playerY)
                    if "L4Piece" in inventory:
                        KeyPiece.rect.topleft = (-100, -100) 
         if LOCATION==4:
            background_color=(72,111,56)
            screen.fill(background_color) 
            if not level_won:
                 playerX=player.rect.x
                 playerY=player.rect.y
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if pygame.sprite.collide_mask(player, KeyPiece):
                   inventory.append("L4Piece")
                   KeyPiece.rect.topleft = (-100, -100) 
                 
                 if player.rect.left < 0:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=3
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                    player.rect.topleft = (900, playerY)
                    if "L3Piece" in inventory:
                        KeyPiece.rect.topleft = (-100, -100) 
                 if player.rect.bottom > 1050:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=6
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                    player.rect.topleft = (playerX, 0)
         if LOCATION==5:
            knife.image = pygame.image.load("Backpack.png").convert_alpha()
            knife.image = pygame.transform.scale(knife.image, (75, 75))
            background_color=(72,111,56)
            screen.fill(background_color) 
            if not level_won:
                 playerX=player.rect.x
                 playerY=player.rect.y 
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if pygame.sprite.collide_mask(player, knife):
                    inventory.append("Bag")
                    knife.rect.topleft = (-100, -100) 
                 if pygame.sprite.collide_mask(player, KeyPiece):
                    inventory.append("L5Piece")
                    KeyPiece.rect.topleft = (-100, -100)
                 if player.rect.right > 1050:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=6
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                    player.rect.topleft = (50, playerY)
                 if player.rect.top < 0:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=3
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                    player.rect.topleft = (playerX, 900)
                    if "L3Piece" in inventory:
                        KeyPiece.rect.topleft = (-100, -100) 

         if LOCATION==6:
            NPC.image = pygame.image.load("PurpleDuck.png").convert_alpha()
            NPC.image = pygame.transform.scale(NPC.image, (100, 100))
            background_color=(72,111,56)
            screen.fill(background_color) 
            if not level_won:
                 keys = pygame.key.get_pressed()
                 playerX=player.rect.x
                 playerY=player.rect.y
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if "L6Piece" not in inventory:
                    if pygame.sprite.collide_mask(player, NPC) and not dialog_active:
                           if keys[pygame.K_e]:
                              dialog_active = True
                              movement = False
                              dialog_index = 0 
                                 
                    if "Bag" not in inventory:   
                           if dialog_active and keys[pygame.K_SPACE]:
                              dialog_index += 1
                              pygame.time.wait(200) 
                           if dialog_index >= len(PurpleDuckDialog_lines):
                              dialog_active = False
                              movement = True  
                           if dialog_active and dialog_index < len(PurpleDuckDialog_lines):
                              text = font.render(PurpleDuckDialog_lines[dialog_index], True, (0,0,0))
                              screen.blit(text, (80, 900)) 

                    if "Bag" in inventory and dialog_active:   
                           if dialog_active and keys[pygame.K_SPACE]:
                              dialog_index += 1
                              pygame.time.wait(200) 
                           if dialog_index >= len(PurpleDuckDialog_lines2):
                              dialog_active = False
                              movement = True 
                              inventory.append("L6Piece") 
                           if dialog_active and dialog_index < len(PurpleDuckDialog_lines2):
                              text = font.render(PurpleDuckDialog_lines2[dialog_index], True, (0,0,0))
                              screen.blit(text, (80, 900)) 
                          
                 if player.rect.left < 0:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=5
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                    player.rect.topleft = (900, playerY)
                    if "Bag" in inventory:
                        knife.rect.topleft = (-100, -100) 
                    if "L5Piece" in inventory:
                        KeyPiece.rect.topleft = (-100, -100) 
                 if player.rect.top < 0:
                    bullets.empty()
                    all_sprites.empty()
                    LOCATION=4
                    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                    player.rect.topleft = (playerX, 900)
                    if "L4Piece" in inventory:
                        KeyPiece.rect.topleft = (-100, -100) 
         if LOCATION==7:
            background_color=(153, 146, 142)
            screen.fill(background_color) 
            if not level_won:
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if player.rect.left < 0: 
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=9
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                 if player.rect.right > 1070:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=8
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                     if "HPotion" in inventory:
                       potion.rect.topleft = (-100, -100)  
                  
         if LOCATION==8:
            background_color=(153, 146, 142)
            screen.fill(background_color) 
            potion.image = pygame.image.load("HealthPotion.png").convert_alpha()
            potion.image = pygame.transform.scale(potion.image, (70, 70))
            if not level_won:
               player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
               if player.rect.left < 0: 
                  bullets.empty()
                  all_sprites.empty()
                  LOCATION=7
                  file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                  all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                  player.rect.topleft = (960, 500)
               if potion and pygame.sprite.collide_mask(player, potion) and Lives<5:
                  potion.rect.topleft = (-100, -100) 
                  Lives+=1
                  pygame.display.set_caption("Lives: "+str(Lives))
                  inventory.append("HPotion")
         if LOCATION==9:
            background_color=(153, 146, 142)
            screen.fill(background_color) 
            if not level_won:
               keys = pygame.key.get_pressed()
               player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
               if player.rect.right > 1070:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=7
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
               if player.rect.top < 100 and player.rect.right < 310:
                    if keys[pygame.K_e]:
                      bullets.empty()
                      all_sprites.empty()
                      LEVEL=3
                      LOCATION=1
                      file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                      all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
   
         for bullet in bullets:
            if pygame.sprite.spritecollide(bullet, solid_sprites, False):
               bullet.kill()
            if enemy and pygame.sprite.collide_mask(bullet, enemy):
               Chromebook_Lives-=1
               bullet.kill()
         if enemy and Chromebook_Lives<=0:
            enemy.kill()
            enemy.rect.topleft = (-1000, -1000) 
         bullets.update()
         all_sprites.draw(screen)
         
         bullets.draw(screen)
         pygame.display.flip()  
         if Lives<=0:
            collidedkeybush=False
            collidedCabinChest=False
            inventory=[]
            level_won=False
            bullets.empty()
            all_sprites.empty()
            Lives=5
            pygame.display.set_caption("Lives: "+str(Lives))
            LEVEL=1
            LOCATION=1
            file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
            all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites,keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites,\
            key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)
            
      if LEVEL==3:
         if LOCATION==1:
            background_color=(153, 146, 142)
            screen.fill(background_color) 
            if not level_won:
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if player.rect.right > 1070:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=2
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
         if LOCATION==2:
            background_color=(153, 146, 142)
            screen.fill(background_color) 
            if not level_won:
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if player.rect.left < 0:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=1
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                     player.rect.topleft = (960, 500)
                 if player.rect.bottom > 1050:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=3
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    

         if LOCATION==3:
            background_color=(153, 146, 142)
            screen.fill(background_color) 
            screen.fill((72,111,56), rect=(70, 700, 990, 370))
            enemy.image = pygame.image.load("Paper.png").convert_alpha()
            enemy.image = pygame.transform.scale(enemy.image, (350, 350))
            knife.image = pygame.image.load("ScissorsL.png").convert_alpha()
            knife.image = pygame.transform.scale(knife.image, (80, 80))
            if not level_won:
                 playerX=player.rect.x
                 playerY=player.rect.y
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if pygame.sprite.collide_mask(player, key):
                     inventory.append("OfficeKey")
                     key.rect.topleft = (-100, -100)
                     enemy.rect.topleft = (400, 300) 
                 if pygame.sprite.collide_mask(player, knife):
                     inventory.append("Scissors")
                     knife.rect.topleft = (-100, -100)
                 if pygame.sprite.spritecollide(player, door_sprites, False) and enemy.alive():
                     player.rect.topleft = (playerX, playerY) 
                 if enemy.alive() and "OfficeKey" in inventory:
                     enemy.UPDATEenemy(solid_sprites)
                 if enemy.alive() and pygame.sprite.collide_mask(player, enemy):
                     player.rect.topleft = (100,100)
                     Lives-=1
                     pygame.display.set_caption("Lives: "+str(Lives))
                 if player.rect.right > 1050:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=4
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
         if LOCATION==4:
            background_color=(72,111,56)
            screen.fill(background_color) 
            if not level_won:
                 playerX=player.rect.x
                 playerY=player.rect.y
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if player.rect.top < 0:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=5
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                     player.rect.topleft = (playerX, 900)
                 if player.rect.right > 1050:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=6
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                     player.rect.topleft = (25, playerY)
                 if player.rect.left < 0:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=3
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                     player.rect.topleft = (910, 790)
                     key.rect.topleft = (-100, -100)
                     knife.rect.topleft = (-100, -100)
                     enemy.kill()
         if LOCATION==5:
            background_color=(72,111,56)
            screen.fill(background_color) 
            enemy.image = pygame.image.load("Chromebook.png").convert_alpha()
            enemy.image = pygame.transform.scale(enemy.image, (400, 400))
            enemy.mask=pygame.mask.from_surface(enemy.image)
            if not level_won:
                 playerX=player.rect.x
                 playerY=player.rect.y
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if player.rect.bottom > 1050:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=4
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                     player.rect.topleft = (playerX, 25)
         if LOCATION==6:
            background_color=(72,111,56)
            screen.fill(background_color) 
            screen.fill((BLACK), rect=(630, 120, 50, 27))
            cabin.image = pygame.image.load("Jail.png").convert_alpha()
            cabin.image = pygame.transform.scale(cabin.image, (400, 400))
            cabin.mask=pygame.mask.from_surface(cabin.image)
            if not level_won:
                 playerX=player.rect.x
                 playerY=player.rect.y
                 player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites, hole_sprites, crate_sprites, basementwall_sprites, movement, couch, stand_sprites, stove, bed_sprites, box, inventory, table_sprites)
                 if player.rect.left < 0:
                     bullets.empty()
                     all_sprites.empty()
                     LOCATION=4
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites, key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)                    
                     player.rect.topleft = (960, playerY)
                 if cabin and pygame.sprite.collide_mask(player, cabin):
                     player.rect.topleft = (playerX, playerY)



                     

                     
                 

                 
                 
                 
                 
    
         for bullet in bullets:
            if pygame.sprite.spritecollide(bullet, solid_sprites, False):
               bullet.kill()
            if enemy and pygame.sprite.collide_mask(bullet, enemy):
               bullet.kill()
         if enemy and Paper_Lives<=0:
            enemy.kill()
            enemy.rect.topleft = (-1000, -1000) 
         for scissor in scissors:
            if pygame.sprite.spritecollide(scissor, solid_sprites, False):
               scissor.kill()
            if enemy and pygame.sprite.collide_mask(scissor, enemy):
               scissor.kill()

                     
         scissors.update()
         bullets.update()
         all_sprites.draw(screen)
         
         bullets.draw(screen)
         pygame.display.flip()  
         if Lives<=0:
            collidedkeybush=False
            collidedCabinChest=False
            inventory=[]
            level_won=False
            bullets.empty()
            all_sprites.empty()
            Lives=5
            pygame.display.set_caption("Lives: "+str(Lives))
            LEVEL=1
            LOCATION=1
            file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
            all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites,keybush, cabin, housewall_sprites,chest, gun, knife, enemy, hole_sprites, crate_sprites,\
            key, NPC, door_sprites, basementwall_sprites, bed_sprites, stand_sprites, stove, couch, box, potion, mountain, rope, lake, KeyPiece, table_sprites, rug = load_maze(file)

      clock.tick(FPS)
main()
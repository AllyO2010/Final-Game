import pygame
import sys
# Initialize Pygame
pygame.init()

# --- Constants and Colors ---
TILE_SIZE = 70
WIDTH = 15 * TILE_SIZE
HEIGHT = 15 * TILE_SIZE
FPS = 60
LEVEL=1




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
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 6

    def update(self, walls, rocks, trees, cavewalls, bushes, housewalls):
        
        old_x, old_y = self.rect.topleft
        keys = pygame.key.get_pressed()
        

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        
        if pygame.sprite.spritecollide(self, walls, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, rocks, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, trees, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, cavewalls, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, bushes, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, housewalls, False, pygame.sprite.collide_mask):
            self.rect.x = old_x

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if pygame.sprite.spritecollide(self, walls, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, rocks, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, trees, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, cavewalls, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, bushes, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self, housewalls, False, pygame.sprite.collide_mask):
            self.rect.y = old_y
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("wall.png").convert()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
class HouseWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("houseWall.png").convert()
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
class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("lava.jpg").convert_alpha()
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
class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill((72,111,56))
        self.rect = self.image.get_rect(topleft=(x, y))



        
#read file and convert it onto the screen
def load_maze(filename):
    all_sprites = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()
    cavewall_sprites = pygame.sprite.Group()
    lava_sprites = pygame.sprite.Group()
    bush_sprites = pygame.sprite.Group()
    exit_sprites = pygame.sprite.Group()
    housewall_sprites = pygame.sprite.Group()
    chest=None
    cabin=None
    keybush=None
    diamond= None
    player = None
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
            elif char == '2':
                caveWall = CaveWall(x, y)
                all_sprites.add(caveWall)
                cavewall_sprites.add(caveWall)
            elif char == '3':
                exit = Exit(x, y)
                all_sprites.add(exit)
                exit_sprites.add(exit)
            elif char == 'C':
                cave = Cave(x, y)
                all_sprites.add(cave)
            elif char == 'D':
                diamond = Diamond(x, y)
                all_sprites.add(diamond)
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
            elif char == 'c':
                cabin = Cabin(x, y)
                all_sprites.add(cabin)
            elif char == 'L':
                lava = Lava(x, y)
                all_sprites.add(lava)
                lava_sprites.add(lava)
            elif char == 'H':
                chest = Chest(x, y)
                all_sprites.add(chest)
            elif char == 'P':
                player = Player(x, y)
                all_sprites.add(player)
    

    return all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, exit_sprites, cabin, housewall_sprites, chest
#work the game and what happens 
def main():
    LEVEL=1
    LOCATION=3
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Final Game--LEVEL 1")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 50)
    running=True
    file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
    all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites,keybush, exit_sprites, cabin, housewall_sprites,chest = load_maze(file)
    collidedkeybush=False
    collidedCabinChest=False
    inventory=[]
    level_won=False
    keys = pygame.key.get_pressed()
    while running:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
      if LOCATION==1:
         background_color=(72,111,56)
         screen.fill(background_color) 
         if not level_won:
              player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites)
              if cave and pygame.sprite.collide_mask(player, cave):
                     LOCATION=2
                     file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                     all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, exit_sprites, cabin, housewall_sprites, chest = load_maze(file)
                     
                     
      if LOCATION==2:
         background_color=(103, 110, 112)
         screen.fill(background_color) 
         if not level_won:
              player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites)
              if pygame.sprite.spritecollide(player, lava_sprites, False, pygame.sprite.collide_mask):
                  player.rect.bottomleft = 80, 975
              if diamond and pygame.sprite.collide_mask(player, diamond):
                  LOCATION=3
                  file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                  all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, exit_sprites, cabin, housewall_sprites ,chest = load_maze(file)
      if LOCATION==3:
         background_color=(72,111,56)
         screen.fill(background_color)
         if not level_won:
              player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites)
              if keybush and not collidedkeybush and pygame.sprite.collide_mask(player, keybush):
                    collidedkeybush=True
                    text = font.render("You Found a Key!", True, (0,0,0))
                    screen.blit(text, (400, 450))
                    inventory.append("CabinKey")
                    pygame.display.flip()  
                    pygame.time.delay(3000)
                      
                     
              if pygame.sprite.spritecollide(player, exit_sprites, False, pygame.sprite.collide_mask):
                  LOCATION=4
                  file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                  all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, exit_sprites, cabin, housewall_sprites,chest = load_maze(file)
      if LOCATION==4:
         background_color=(72,111,56)
         screen.fill(background_color) 
         if not level_won:
              player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites)
              if cabin and "CabinKey" in inventory and pygame.sprite.collide_mask(player, cabin):
                 LOCATION=5
                 file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                 all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, exit_sprites, cabin, housewall_sprites,chest = load_maze(file)
              if pygame.sprite.spritecollide(player, exit_sprites, False, pygame.sprite.collide_mask):
                 LOCATION=3
                 file="L"+str(LEVEL)+"L"+str(LOCATION)+".txt"
                 all_sprites, wall_sprites, player, tree_sprites, cave, rock_sprites, cavewall_sprites, diamond, lava_sprites, bush_sprites, keybush, exit_sprites, cabin, housewall_sprites,chest = load_maze(file)
                 x_value = player.rect.x
                 player.rect.bottomleft = x_value, 975

      if LOCATION==5:
         background_color=(216, 213, 210)
         screen.fill(background_color) 
         if not level_won:
              player.update(wall_sprites, rock_sprites, tree_sprites, cavewall_sprites,bush_sprites, housewall_sprites)
              if not collidedCabinChest and pygame.sprite.collide_mask(player, chest):
                  collidedCabinChest=True

              

                  
              

                     
                  

           
             
      
      all_sprites.draw(screen)
      pygame.display.flip()     
      clock.tick(FPS)





main()
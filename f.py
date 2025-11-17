import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Player and NPC setup
player = pygame.Rect(50, 50, 30, 30)
npc = pygame.Rect(200, 150, 30, 30)

move = True
dialog_active = False
dialog_index = 0

# Back-and-forth dialog lines
dialog_lines = [
    "NPC: Hello traveler!",
    "Player: Hi there!",
    "NPC: Be careful, monsters roam nearby.",
    "Player: Thanks for the warning!",
    "NPC: Safe journeys!"
]

font = pygame.font.SysFont(None, 28)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if move:
        if keys[pygame.K_LEFT]:
            player.x -= 3
        if keys[pygame.K_RIGHT]:
            player.x += 3
        if keys[pygame.K_UP]:
            player.y -= 3
        if keys[pygame.K_DOWN]:
            player.y += 3

    # Check proximity and press E to start dialog
    if player.colliderect(npc) and not dialog_active:
        if keys[pygame.K_e]:
            dialog_active = True
            move = False
            dialog_index = 0

    # Advance dialog with SPACE
    if dialog_active and keys[pygame.K_SPACE]:
        dialog_index += 1
        pygame.time.wait(200)  # small delay to avoid skipping multiple lines

        if dialog_index >= len(dialog_lines):
            dialog_active = False
            move = True

            # Push player away so they don't immediately retrigger
            if player.colliderect(npc):
                player.y = npc.top - player.height - 10

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, GREEN, npc)

    if dialog_active and dialog_index < len(dialog_lines):
        text = font.render(dialog_lines[dialog_index], True, (0,0,0))
        screen.blit(text, (50, 250))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```python
import pygame
import sys
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.centerx = screen_width // 2
player_rect.bottom = screen_height - 10

bullet_image = pygame.image.load("bullet.png")
bullet_rect = bullet_image.get_rect()
bullet_rect.center = player_rect.center
bullet_speed = 5
bullet_state = "ready"  # "ready", "fire"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= 5
            if event.key == pygame.K_RIGHT:
                player_rect.x += 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_rect.center = player_rect.center
                    bullet_state = "fire"

    if bullet_state == "fire":
        bullet_rect.y -= bullet_speed
        if bullet_rect.y < 0:
            bullet_state = "ready"
          
    screen.fill((0, 0, 0))  # Black background
    screen.blit(player_image, player_rect)

    if bullet_state == "fire":
        screen.blit(bullet_image, bullet_rect)

    # Update the screen
    pygame.display.update()
```
# Make sure to replace images with your choise 

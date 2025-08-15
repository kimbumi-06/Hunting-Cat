import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 플레이어
player = pygame.Rect(400, 300, 50, 50)  # (x, y, width, height)
speed = 5

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력 받기
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # 화면 그리기
    screen.fill((0, 0, 0))  # 배경색 검정
    pygame.draw.rect(screen, (0, 255, 0), player)  # 초록색 플레이어
    pygame.display.flip()
    clock.tick(60)
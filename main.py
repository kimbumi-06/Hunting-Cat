import pygame
import sys

#초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 플레이어
#player = pygame.Rect(400, 300, 50, 50)  # (x, y, width, height)
player_x = 200
player_y = 200
speed = 200 #루프 안에 다시 느리게 설정할 예정

player_fornt = pygame.image.load("assets/고양이 앞모습.png")  # 플레이어 이미지 로드
player_back = pygame.image.load("assets/고양이 뒷모습.png")
player_left = pygame.image.load("assets/고양이 왼쪽.png")
player_right = pygame.image.load("assets/고양이 오른쪽.png")
size = (250, 250)  # 이미지 크기
player_front = pygame.transform.scale(player_fornt, size)  # 이미지 크기 조정
player_back = pygame.transform.scale(player_back, size)
player_right = pygame.transform.scale(player_right, size)
player_left = pygame.transform.scale(player_left, size)

# 게임 루프(게임 가동)
while True:
    dt = clock.tick(60) / 1000.0  # 프레임 시간 (초 단위)
    speed = 200 * dt  # 그냥 speed하는 거랑 달리 모든 소프트웨어에서 같은 속도

    for event in pygame.event.get(): # 키 한번만 눌림
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    # 창 닫기

    player_img = player_front  # 기본 이미지 설정

    # 키 입력 받기 (키 눌려있음)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
        player_img = player_left  # 왼쪽 키를 누르면 왼쪽 이미지로 변경
    if keys[pygame.K_RIGHT]:
        player_x += speed
        player_img = player_right
    if keys[pygame.K_UP]:
        player_y -= speed
        player_img = player_back
    if keys[pygame.K_DOWN]:
        player_y += speed
        player_img = player_front

    # 화면 그리기
    screen.fill((255, 255, 255))  # 배경색 검정
    #pygame.draw.rect(screen, (0, 255, 0), player)  # 초록색 플레이어
    screen.blit(player_img, (player_x, player_y))  # 플레이어 이미지 그리기
    pygame.display.flip() # 화면 등장 명령어
    clock.tick(60) #1초당 프레임 갱식 수치


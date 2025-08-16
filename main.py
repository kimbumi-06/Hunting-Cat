import pygame
import sys
from cat import Cat # Player 클래스 가져옴


#초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 플레이어
player_size = (150, 150)
print(player_size)
player = Cat(400, 300, 200, player_size)  # Cat 클래스 인스턴스 생성


# 게임 루프(게임 가동)
while True:
    dt = clock.tick(60) / 1000.0  # 프레임 시간 (초 단위)
    speed = 200 * dt  # 그냥 speed하는 거랑 달리 모든 소프트웨어에서 같은 속도

    for event in pygame.event.get(): # 키 한번만 눌림
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    # 창 닫기

    keys = pygame.key.get_pressed() # 키 입력 받기
    player.handle_input(keys, dt)



    # 화면 그리기
    screen.fill((255, 255, 255))  # 배경색 검정
    player.draw(screen)  # Cat 클래스의 draw 메서드 호출
    pygame.display.flip() # 화면 등장 명령어
    clock.tick(60) #1초당 프레임 갱식 수치


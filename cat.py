import pygame
from bullets import Bullet

class Cat:
    def __init__(self, x, y, speed, size): 
        try: #try 예외처리 문법
            self.image_front = pygame.transform.scale(pygame.image.load("assets/고양이 앞모습.png"), size)
            self.image_back = pygame.transform.scale(pygame.image.load("assets/고양이 뒷모습.png"), size)
            self.image_left = pygame.transform.scale(pygame.image.load("assets/고양이 왼쪽.png"), size)
            self.image_right = pygame.transform.scale(pygame.image.load("assets/고양이 오른쪽.png"), size)
        except pygame.error as e:
            print(f"이미지 로딩 오류: {e}")
            self.image_front = pygame.Surface(size) #임시 사각형으로 대체
            self.image_front.fill((0, 0, 0))
            self.image_back = self.image_front
            self.image_left = self.image_front
            self.image_right = self.image_front
        
        self.current_image = self.image_front
        original_rect = self.current_image.get_rect(center=(x, y)) # 고양이 대신 사각형
        new_width = int(size[0] * 0.8)  # 원래 너비의 80%
        new_height = int(size[1] * 0.8)  
        # 새로운 사각형을 만들고, 중심을 원래 위치로 설정합니다.
        self.rect = pygame.Rect(0, 0, new_width, new_height)
        self.rect.center = original_rect.center
        self.speed = 200 # 픽셀/초 단위

        # 총알 방향 설정
        self.bullets = [] #총알 리스트
        self.last_shot_time = pygame.time.get_ticks()
        self.direction = [0, -1] 


    
    def handle_input(self, keys, dt):
        dx = 0
        dy = 0
        
        if keys[pygame.K_LEFT]:
            dx -= self.speed * dt
            self.current_image = self.image_left
            self.direction = [-1, 0] # 총알을 위한 방향
        if keys[pygame.K_RIGHT]:
            dx += self.speed * dt
            self.current_image = self.image_right
            self.direction = [1, 0]
        if keys[pygame.K_UP]:
            dy -= self.speed * dt
            self.current_image = self.image_back
            self.direction = [0, -1]
        if keys[pygame.K_DOWN]:
            dy += self.speed * dt
            self.current_image = self.image_front
            self.direction = [0, 1]
            
        self.rect.x += dx
        self.rect.y += dy


    def shoot(self): #총알 쏘기
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > 500:
            # 총알을 생성할 때 현재 방향(self.direction)을 함께 전달합니다.
            new_bullet = Bullet(self.rect.centerx, self.rect.centery, self.direction)
            self.bullets.append(new_bullet)
            self.last_shot_time = current_time


    def draw(self, screen):
        screen.blit(self.current_image, self.rect) #고양이 이미지를 네모 위치에 도장찍기






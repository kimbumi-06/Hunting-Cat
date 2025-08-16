# bullet.py
import pygame

class Bullet:
    def __init__(self, x, y, direction, speed=800):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction # 고양이로부터 받은 방향 저장
        
        self.width = 10
        self.height = 20
        self.rect = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

    def update(self, dt):
        # 방향에 맞춰 x, y 좌표를 동시에 이동시킵니다.
        self.x += self.speed * dt * self.direction[0]
        self.y += self.speed * dt * self.direction[1]
        self.rect.center = (int(self.x), int(self.y))
        
    def draw(self, screen):
        # 총알을 노란색 사각형으로 그립니다.
        pygame.draw.rect(screen, (255, 255, 0), self.rect)
# bullet.py
import pygame

class Bullet:
    def __init__(self, x, y, direction, speed=800):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction # 고양이로부터 받은 방향 저장
        
        self.width = 5
        self.height = 10
        self.rect = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

    def update(self, dt):
        # 방향에 맞춰 x, y 좌표를 동시에 이동시킵니다.
        self.x += self.speed * dt * self.direction[0]
        self.y += self.speed * dt * self.direction[1]
        self.rect.center = (int(self.x), int(self.y))
        
    def draw(self, screen):
        # 총알을 노란색 사각형으로 그립니다.
        pygame.draw.rect(screen, (255, 255, 0), self.rect)


class BulletManager:
    def __init__(self):
        self.all_bullets = []
        self.last_shot_time = 0

    def create_bullet(self, player_rect, direction):
        current_time = pygame.time.get_ticks()  # 현재 시간 (밀리초 단위)
        if current_time - self.last_shot_time > 500:  # 0.2초 간격으로 총알 발사
            new_bullet = Bullet(player_rect.centerx, player_rect.centery, direction)
            self.all_bullets.append(new_bullet)
            self.last_shot_time = current_time  # 마지막 발사 시간 업데이트

    def update(self, dt):
        """모든 총알의 위치를 업데이트하고 화면 밖으로 나간 총알을 제거합니다."""
        for bullet in self.all_bullets[:]:
            bullet.update(dt)
            if bullet.rect.bottom < 0 or bullet.rect.top > 600 or \
            bullet.rect.right < 0 or bullet.rect.left > 800:
                self.all_bullets.remove(bullet)

    def draw(self, screen):
        """모든 총알을 화면에 그립니다."""
        for bullet in self.all_bullets:
            bullet.draw(screen)
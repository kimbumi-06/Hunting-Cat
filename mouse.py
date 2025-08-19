import pygame
import random
import math

class Mouse:
    def __init__ (self, width, height):
        
        screen_width = width
        screen_height = height
        start_x = random.choice([0, screen_width])
        start_y = random.randint(0, screen_height)

        size = (50, 50)
        if start_x == 0:
            image = pygame.image.load("assets/쥐 왼쪽에서.png")
            self.image = pygame.transform.scale(image, size)
        else:
            image = pygame.image.load("assets/쥐 오른쪽에서.png")
            self.image = pygame.transform.flip(pygame.transform.scale(image, size), True, False)

        self.rect = self.image.get_rect(center=(start_x, start_y))


    def move(self, player_rect, dt):
        player_x, player_y = player_rect.center
        dx = player_x - self.rect.centerx
        dy = player_y - self.rect.centery

        distance = math.sqrt(dx**2 + dy**2)
        if distance > 0:
            dx /= distance
            dy /= distance

        self.rect.x += dx * 100 * dt
        self.rect.y += dy * 100 * dt
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class MouseManager:
    def __init__(self, screen_width, screen_height):
        self.mice = []
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    def create_mouse(self):
        new_mouse = Mouse(self.screen_width, self.screen_height)
        self.mice.append(new_mouse)
    
    def update(self, player_rect, dt):
        for enemy in self.mice[:]:
            enemy.move(player_rect, dt)
    
    def draw(self, screen):
        for enemy in self.mice:
            enemy.draw(screen)
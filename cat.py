import pygame

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
    
    def handle_input(self, keys, dt):
        dx = 0
        dy = 0
        
        if keys[pygame.K_LEFT]:
            dx -= self.speed * dt
            self.current_image = self.image_left
        if keys[pygame.K_RIGHT]:
            dx += self.speed * dt
            self.current_image = self.image_right
        if keys[pygame.K_UP]:
            dy -= self.speed * dt
            self.current_image = self.image_back
        if keys[pygame.K_DOWN]:
            dy += self.speed * dt
            self.current_image = self.image_front
            
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        screen.blit(self.current_image, self.rect)
    
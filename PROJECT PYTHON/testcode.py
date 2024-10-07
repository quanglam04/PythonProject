import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Shooting Game")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Lớp đạn
class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.radius = 5
        self.speed = 10
        self.direction = direction  # Hướng di chuyển

    def move(self):
        self.x += self.speed * self.direction

        # Kiểm tra va chạm với tường
        if self.x <= 0 or self.x >= WIDTH:
            self.direction *= -1  # Đảo ngược hướng

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

# Lớp xe tăng
class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        # Giới hạn di chuyển trong cửa sổ
        self.x = max(0, min(self.x, WIDTH))
        self.y = max(0, min(self.y, HEIGHT))

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 40, 20))  # Vẽ xe tăng

# Hàm chính
def main():
    clock = pygame.time.Clock()
    tank = Tank(400, 300)
    bullets = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Nhấn phím cách để bắn
                    # Tạo đạn với vị trí và hướng
                    direction = random.choice([-1, 1])
                    bullets.append(Bullet(tank.x + 20, tank.y + 10, direction))  # Vị trí khởi đầu của đạn

        # Xử lý di chuyển của xe tăng
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            tank.move(-tank.speed, 0)
        if keys[pygame.K_RIGHT]:
            tank.move(tank.speed, 0)
        if keys[pygame.K_UP]:
            tank.move(0, -tank.speed)
        if keys[pygame.K_DOWN]:
            tank.move(0, tank.speed)

        # Cập nhật vị trí đạn
        for bullet in bullets:
            bullet.move()

        # Vẽ
        screen.fill(BLACK)
        tank.draw(screen)  # Vẽ xe tăng
        for bullet in bullets:
            bullet.draw(screen)  # Vẽ đạn

        # Vẽ tường
        pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT), 5)  # Vẽ tường

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

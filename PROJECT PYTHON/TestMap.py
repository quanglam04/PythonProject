import pygame
import sys

# Cấu hình màn hình và màu sắc
WIDTH, HEIGHT = 1030, 700
TILE_SIZE = 16
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Khởi tạo Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Trouble Map")

# Hàm để đọc file nhị phân và chuyển đổi nó thành ma trận
def read_map(file_path):
    with open(file_path, 'r') as file:
        map_data = [line.strip() for line in file]
    return map_data

# Hàm để vẽ bản đồ từ ma trận
def draw_map(map_data):
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == '1':  # Tường
                color = BLACK
            elif tile == '0':  # Ô trống
                color = WHITE
            elif tile == '*':  # Người chơi
                color = BLUE
            elif tile == '-':  # Đối thủ
                color = RED
            else:
                continue
            pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Đọc bản đồ từ file
map_data = read_map('C:/Users/84334/Desktop/branchme/PythonProject/PROJECT PYTHON/MAP/map1.txt')

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vẽ màn hình
    screen.fill(WHITE)
    draw_map(map_data)
    pygame.display.flip()

# Thoát Pygame
pygame.quit()
sys.exit()

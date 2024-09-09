import pygame

# Bước 1: Khởi tạo Pygame
pygame.init()

# Bước 2: Thiết lập chế độ hiển thị (display mode)
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Bước 3: Tải hình ảnh
image = pygame.image.load("asset/speed.png").convert_alpha()

# Bước 4: Vẽ hình ảnh lên cửa sổ
window.blit(image, (100, 100))  # Vẽ hình ảnh tại vị trí (100, 100)

# Bước 5: Cập nhật màn hình để hiển thị hình ảnh
pygame.display.flip()

# Giữ cửa sổ mở trong một khoảng thời gian nhất định để xem kết quả
pygame.time.wait(3000)  # Giữ cửa sổ mở trong 3 giây

# Thoát Pygame
pygame.quit()

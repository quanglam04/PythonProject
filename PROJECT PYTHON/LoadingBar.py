import pygame
import time
import Setting

pygame.init()

screen = pygame.display.set_mode((Setting.WIDTH, Setting.HEIGHT))
pygame.display.set_caption(Setting.TITLE)


# Thiết lập hình chữ nhật của thanh loading
bar_width = 400
bar_height = 50
bar_x = (Setting.WIDTH - bar_width) // 2
bar_y = (Setting.HEIGHT - bar_height) // 2
border_thickness = 5


def render_text(screen, text, font_size, color, x, y):
    font = pygame.font.Font(pygame.font.match_font('freesansbold'), font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def draw_loading_bar(progress):


    # Vẽ khung của thanh loading
    pygame.draw.rect(screen, Setting.border_color, (
    bar_x - border_thickness, bar_y - border_thickness, bar_width + 2 * border_thickness,
    bar_height + 2 * border_thickness), border_thickness)


    # Vẽ thanh loading dựa trên progress
    pygame.draw.rect(screen, Setting.bar_color, (bar_x, bar_y, int(bar_width * progress), bar_height))

    percentage = int(progress * 100)
    render_text(screen, f"{percentage} %", 50, (255, 255, 255), bar_x + bar_width // 2, bar_y + bar_height // 2)




    # Vẽ đường viền
    pygame.draw.rect(screen, Setting.border_color, (bar_x - border_thickness-13, bar_y - border_thickness-13,
                                           bar_width + 2 * border_thickness+26, bar_height + 2 * border_thickness+26),border_thickness)



    # Cập nhật màn hình
    pygame.display.flip()


# Hàm hiển thị thông báo sau khi load xong
def show_message():
    message = "Press Enter to continue..."
    text_surface = Setting.font.render(message, True, Setting.text_color)
    text_rect = text_surface.get_rect(center=(Setting.WIDTH // 2, Setting.HEIGHT // 2 + 70))

    # Vẽ nền lại và hiển thị thông báo
    screen.fill(Setting.background_color)
    draw_loading_bar(1.0)  # Hiển thị thanh loading đầy
    screen.blit(text_surface, text_rect)
    render_text(screen, 'Tank Battle', 100, Setting.WHITE, 510, 250)
    pygame.display.flip()


def handle():
    running = True
    progress = 0.0
    loading_done = False
    screen.fill(Setting.background_color)
    render_text(screen, 'Tank Battle', 100, Setting.WHITE, 510, 250)
    check = False
    while running:
        percentage = int(progress * 100)
        render_text(screen, f"{percentage} %", 50, (255, 255, 255), bar_x + bar_width // 2, bar_y + bar_height // 2)
        if check == False: screen.fill(Setting.background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'Quit'

            # Kiểm tra nếu người dùng nhấn Enter sau khi thanh loading đầy
            if loading_done and event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key==pygame.K_KP_ENTER)  :

                return 'Enter'

        # Cập nhật progress
        if progress < 1.0:
            progress += 1
            draw_loading_bar(progress)
            time.sleep(0.05)

        # Nếu đã hoàn thành 100%, hiển thị thông báo và đợi người dùng nhấn Enter
        if progress >= 1.0 and not loading_done:
            check = True
            show_message()
            loading_done = True

    pygame.quit()


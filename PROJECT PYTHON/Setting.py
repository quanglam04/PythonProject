import random
import pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (120, 120, 120)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (120, 104, 82)
BLUE = (0, 0, 255)
# game settings

WIDTH = 1024
HEIGHT = 688
TITLE = "PROJECT GROUP 3 by Dat, Huy, Kien, Khoi, Lam"

# loading bar
#---------------------------------------------- Font chữ---------------------------------------------------
font = pygame.font.Font(None, 42)

#---------------------------------------------- Read file -----------------------------------------------
with open('../Setting game/Saved.txt', 'r') as file:
    lines = file.readlines()

# Lưu 5 dòng từ dòng số 5 đến dòng số 9 vào các biến tmp1, tmp2, tmp3, tmp4, tmp5
tmp1 = lines[4].strip()[0]
tmp2 = lines[5].strip()[0]
tmp3 = lines[6].strip()[0]
tmp4 = lines[7].strip()[0]
tmp5 = lines[8].strip()[0]
#---------------------------------------------- Key Press ---------------------------------

up_player_1 = ord(tmp1)
down_player_1 = ord(tmp2)
left_player_1 = ord(tmp3)
right_player_1 = ord(tmp4)
hit_player_1 = ord(tmp5)

#-------------------------------------------- Thiết lập hình chữ nhật của thanh loading ---------------------------------------------
bar_width = 400
bar_height = 50
bar_x = (WIDTH - bar_width) // 2
bar_y = (HEIGHT - bar_height) // 2
border_thickness = 5

background_color = (60, 94, 138)  # Màu nền xanh tối
border_color = (255, 85, 85)  # Màu viền đỏ
bar_color = (255, 85, 85)  # Màu thanh loading đỏ
text_color = (255, 255, 255)  # Màu chữ trắng
#------------------------------------------ player settings -------------------------------------------------------------------------

playerSpeed = 0.79
speedAdd = 0
angle = 0.68

#------------------------------------------ vị trí ban đầu -----------------------------------------------------------------------
x0 = 1
y0 = 1

# ---------------------------------------------- image ------------------------------------------------------------------------------
random_index = random.randint(1,3)
wall = f'asset/map/dirt{random_index}.png'


TankBlue = 'asset/Blue Tank.png'

gun = 'asset/item/gun.png'
hp = 'asset/item/hp.png'
laser_gun = 'asset/item/laser_gun.png'
speed = 'asset/item/speed.png'
x3 = 'asset/item/x3.png'

background = 'asset/background.jpg'
startBtn = 'asset/btn/start_btn_newVersion.png'
exitBtn = 'asset/btn/save_btn_newVersion.png'

optionBtnOne = 'asset/btn/1_player_btn.png'
optionBtnTwo = 'asset/btn/2_player_btn.png'
optionBtnThree = 'asset/btn/3_player_btn.png'
optionBtnFour = 'asset/btn/4_player_btn.png'

map_1 = 'asset/map/map1.png'
map_2 = 'asset/map/map2.png'
map_3 = 'asset/map/map3.png'
map_4 = 'asset/map/map4.png'
map_5 = 'asset/map/map5.png'
map_6 = 'asset/map/map6.png'
map_7 = 'asset/map/map7.png'
map_8 = 'asset/map/map8.png'
map_9 = 'asset/map/map9.png'
map_10 = 'asset/map/map10.png'

#---------------------------------------------------------- media ---------------------------------------------------------------------
backgroundMusic = 'asset/media/media.mp3'
bulletMusic = 'asset/media/normal bullet.flac'
#-------------------------------------------------------------------------------------------------------------------------------------















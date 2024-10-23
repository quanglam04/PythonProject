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
ORANGE=(255,165,0)
# game settings
#---------------------------------------------- Read file -----------------------------------------------
with open('../Setting game/Saved.txt', 'r') as file:
    lines = file.readlines()
WIDTH = 1024
HEIGHT = 688
TITLE = "PROJECT GROUP 3 by Dat, Huy, Kien, Khoi, Lam"

# loading bar
#---------------------------------------------- Font chữ---------------------------------------------------
font = pygame.font.Font(None, 42)


#   Các phím đặc biệt khi lưu dưới file không ở dưới dạng một char thì không thể dùng function ord     #

special_keys = {
    "BackSpace": 8,
    "Tab":9,
    "Enter": 13,
    "Alt_L": 1073742050,
    "Pause":1073741896,
    "Escape": 27,
    "Space":32,
    "PgUp":1073741899,
    "PgDn":1073741902,
    "End":1073741901,
    "Home":1073741898,
    "Left":1073741904,
    "Up":1073741906,
    "Right":1073741903,
    "Down":1073741905,
    "Insert":1073741897,
    "Delete":127,
    "Win_L":1073742051,
    "Win_R":1073742055,
    "App":1073741925,
    "F1": 1073741882,
    "F2": 1073741883,
    "F3": 1073741884,
    "F4": 1073741885,
    "F5": 1073741886,
    "F6": 1073741887,
    "F7": 1073741888,
    "F8": 1073741889,
    "F9": 1073741890,
    "F10": 1073741891,
    "F11": 1073741892,
    "F12": 1073741893,
    "Num_Lock":1073741907,
    "Scroll_Lock":1073741881,
    "Alt_R": 1073742054,
    "Np_0":1073741922,
    "Np_1":1073741913,
    "Np_2":1073741914,
    "Np_3":1073741915,
    "Np_4":1073741916,
    "Np_5":1073741917,
    "Np_6":1073741918,
    "Np_7":1073741919,
    "Np_8":1073741920,
    "Np_9":1073741921,
    "Np_/":1073741908,
    "Np_*":1073741909,
    "Np_-":1073741910,
    "Np_+":1073741911,
    "Np_.":1073741923,
    "Control_R":1073742052,
    "Control_L":1073742048
}
def get_key_code(key):
    if key in special_keys:
        return special_keys.get(key)
    else:
        return ord(key)
if lines[3].strip()=="True" :
    Window_mode=True
else:
    Window_mode=False
#---------------------------------------------- Key Press ---------------------------------
#player 1
up_player_1 = get_key_code(lines[4].strip())
down_player_1 = get_key_code(lines[5].strip())
right_player_1 = get_key_code(lines[6].strip())
left_player_1 = get_key_code(lines[7].strip())
hit_player_1=get_key_code(lines[8].strip())

#player2
up_player_2 =get_key_code(lines[9].strip())
down_player_2 =get_key_code(lines[10].strip())
right_player_2=get_key_code(lines[11].strip())
left_player_2=get_key_code(lines[12].strip())
hit_player_2=get_key_code(lines[13].strip())

#player3
up_player_3 =get_key_code(lines[14].strip())
down_player_3 =get_key_code(lines[15].strip())
right_player_3=get_key_code(lines[16].strip())
left_player_3=get_key_code(lines[17].strip())
hit_player_3=get_key_code(lines[18].strip())

#player4
up_player_4 =get_key_code(lines[19].strip())
down_player_4 =get_key_code(lines[20].strip())
right_player_4=get_key_code(lines[21].strip())
left_player_4=get_key_code(lines[22].strip())
hit_player_4=get_key_code(lines[23].strip())

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

playerSpeed =0.79
speedAdd = 1.5
angle = 1

#------------------------------------------ vị trí ban đầu -----------------------------------------------------------------------
x0 = 1
y0 = 1

# ---------------------------------------------- image ------------------------------------------------------------------------------
random_index = random.randint(1,3)
wall = f'asset/map/dirt{random_index}.png'

Blue_image="Blue Tank.png"
Red_image="Red Tank.png"
Green_image="Green Tank.png"
Orange_image="Orange Tank.png"
asset="asset/"
Laser_path="Laser/"
Tank_power_bullet="Tank_power_bullet/"


TankBlue = asset+Blue_image
Tankmodern = 'asset/newtank.png'
TankRed = asset + Red_image
TankGreen = asset + Green_image
TankOrange =asset + Orange_image
Tank_dark='asset/tank_dark.png'
Tank_sand="asset/tank_sand.png"
Tank_red="asset/tank_red.png"
Tank_green="asset/tank_green.png"
Tank_blue ='asset/tank_blue.png'

TankBlue_laser="asset/Laser/"




gun = 'asset/item/gun.png'
hp = 'asset/item/hp.png'
laser_gun = 'asset/item/laser_gun.png'
speed = 'asset/item/speed.png'
x3 = 'asset/item/x3.png'
laser_line = 'asset/item/Laser.png'

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















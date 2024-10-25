from pygame import image as img
from pygame import transform as tf
import Setting
import pygame
def caculate_frame(sheet_path,frame_width,frame_height):
    image= pygame.image.load(sheet_path).convert_alpha()
    frames=[]
    total_frame_width =image.get_width() // frame_width
    total_frame_height=image.get_height() // frame_height
    for i in range(total_frame_height):
        for j in range(total_frame_width):
            frame=image.subsurface(j * frame_width, i*frame_height, frame_width,frame_height)
            frames.append(frame)
    return frames

pygame.init()
temporary_screen = pygame.display.set_mode((1,1))
wall = img.load(Setting.wall).convert()
wall = tf.scale(wall, (Setting.title_size, Setting.title_size))

gunItem = img.load(Setting.gun).convert()
gunItem.set_colorkey(Setting.WHITE)
gunItem = tf.scale(gunItem, (25, 25))

hpImage = img.load(Setting.hp).convert()
hpImage.set_colorkey(Setting.WHITE)
hpImage = tf.scale(hpImage, (25,25))

laser_gunItem = img.load(Setting.laser_gun).convert()
laser_gunItem.set_colorkey(Setting.WHITE)
laser_gunItem = tf.scale(laser_gunItem, (25,25))

speedItem = img.load(Setting.speed).convert()
speedItem.set_colorkey(Setting.WHITE)
speedItem = tf.scale(speedItem, (25,25))

x3Item = img.load(Setting.x3).convert()
x3Item.set_colorkey(Setting.WHITE)
x3Item = tf.scale(x3Item, (25, 25))

laser_line = img.load(Setting.laser_line)
laser_line.set_colorkey(Setting.WHITE)
laser_line = tf.scale(laser_line, (25, 25))

expl_1_frames=caculate_frame(Setting.explosion_eff_1_sheet,256,256)
shot_frames =caculate_frame(Setting.shot_effect_sheet,256,256)
expl_4_frames= caculate_frame(Setting.explosion_eff_4_sheet,256,256)



pygame.display.quit()
pygame.quit()
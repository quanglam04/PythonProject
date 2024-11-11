from pygame import image as img
from pygame import transform as tf
import Setting
import pygame
def calculate_frame(sheet_path,frame_width,frame_height):
    image= pygame.image.load(sheet_path).convert_alpha()
    frames=[]
    total_frame_width =image.get_width() // frame_width
    total_frame_height=image.get_height() // frame_height
    for i in range(total_frame_height):
        for j in range(total_frame_width):
            frame=image.subsurface(j * frame_width, i*frame_height, frame_width,frame_height)
            frames.append(frame)
    return frames


def faded_eff(image):
    alpha = 255
    frames = [image]
    while alpha > 0:
        faded_image = image.copy()
        alpha = max(0, alpha - 51)
        faded_image.set_alpha(alpha)
        frames.append(faded_image)
    return frames
pygame.init()
temporary_screen = pygame.display.set_mode((1,1))
wall = img.load(Setting.wall).convert()
wall = tf.scale(wall, (Setting.tile_size, Setting.tile_size))

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

shield_item = img.load(Setting.shield).convert()
shield_item.set_colorkey(Setting.WHITE)
shield_item = tf.scale(shield_item, (25, 25))

laser_line = img.load(Setting.laser_line)
laser_line.set_colorkey(Setting.WHITE)
laser_line = tf.scale(laser_line, (25, 25))

machine_gun=img.load(Setting.machine_gun)
machine_gun.set_colorkey(Setting.WHITE)
machine_gun=tf.scale(machine_gun,(25,25))

missile_item=img.load(Setting.missile)
missile_item.set_colorkey(Setting.WHITE)
missile_item=tf.scale(missile_item,(25,25))

missile_image=img.load(Setting.missile_image)
missile_image=tf.scale(missile_image,(30,15))

#--smoke
normal_smoke =img.load(Setting.smoke_path+Setting.normal_smoke).convert_alpha()
normal_smoke.set_colorkey(Setting.WHITE)
normal_smoke=tf.scale(normal_smoke,(30,30))


blue_smoke=img.load(Setting.smoke_path+Setting.Blue_image).convert_alpha()
blue_smoke.set_colorkey(Setting.WHITE)
blue_smoke=tf.scale(blue_smoke,(30,30))

red_smoke=img.load(Setting.smoke_path+Setting.Red_image).convert_alpha()
red_smoke.set_colorkey(Setting.WHITE)
red_smoke=tf.scale(red_smoke,(30,30))

orange_smoke=img.load(Setting.smoke_path+Setting.Orange_image).convert_alpha()
orange_smoke.set_colorkey(Setting.WHITE)
orange_smoke=tf.scale(orange_smoke,(30,30))

green_smoke=img.load(Setting.smoke_path+Setting.Green_image).convert_alpha()
green_smoke.set_colorkey(Setting.WHITE)
green_smoke=tf.scale(green_smoke,(30,30))

normal_smoke_frames=faded_eff(normal_smoke)
blue_smoke_frames=faded_eff(blue_smoke)
red_smoke_frames=faded_eff(red_smoke)
orange_smoke_frames=faded_eff(orange_smoke)
green_smoke_frames=faded_eff(green_smoke)

smoke_tanks_frames=[blue_smoke_frames,red_smoke_frames,orange_smoke_frames,green_smoke_frames]


#---frames
expl_1_frames=calculate_frame(Setting.explosion_eff_1_sheet,256,256)
shot_frames =calculate_frame(Setting.shot_effect_sheet,256,256)
expl_4_frames= calculate_frame(Setting.explosion_eff_4_sheet,256,256)
expl_3_frames= calculate_frame(Setting.explosion_eff_3_sheet,256,256)
minigun_shot_frames=calculate_frame(Setting.mini_gun_shot_eff_sheet,192,192)
shield_frames=calculate_frame(Setting.shield_eff_path,128,128)

#--normal_tank
Blue_tank=img.load(Setting.TankBlue).convert_alpha()
Blue_tank=tf.smoothscale(Blue_tank,(45,30))

Red_tank=img.load(Setting.TankRed).convert_alpha()
Red_tank=tf.smoothscale(Red_tank,(45,30))

Orange_tank=img.load(Setting.TankOrange).convert_alpha()
Orange_tank=tf.smoothscale(Orange_tank,(45,30))

Green_tank=img.load(Setting.TankGreen).convert_alpha()
Green_tank=tf.smoothscale(Green_tank,(45,30))

normal_tanks=[Blue_tank,Red_tank,Orange_tank,Green_tank]

#--tank_laser
Blue_laser=img.load(Setting.asset+Setting.Laser_path+Setting.Blue_image)
Blue_laser=tf.smoothscale(Blue_laser,(45,30))

Red_laser=img.load(Setting.asset+Setting.Laser_path+Setting.Red_image)
Red_laser=tf.smoothscale(Red_laser,(45,30))

Orange_laser=img.load(Setting.asset+Setting.Laser_path+Setting.Orange_image)
Orange_laser=tf.smoothscale(Orange_laser,(45,30))

Green_laser=img.load(Setting.asset+Setting.Laser_path+Setting.Green_image)
Green_laser=tf.smoothscale(Green_laser,(45,30))

laser_tanks=[Blue_laser,Red_laser,Orange_laser,Green_laser]

#--machine tank
Blue_machine=img.load(Setting.asset+Setting.Machine_path+Setting.Blue_image)
Blue_machine=tf.smoothscale(Blue_machine,(45,30))

Red_machine=img.load(Setting.asset+Setting.Machine_path+Setting.Red_image)
Red_machine=tf.smoothscale(Red_machine,(45,30))

Orange_machine=img.load(Setting.asset+Setting.Machine_path+Setting.Orange_image)
Orange_machine=tf.smoothscale(Orange_machine,(45,30))

Green_machine=img.load(Setting.asset+Setting.Machine_path+Setting.Green_image)
Green_machine=tf.smoothscale(Green_machine,(45,30))

machine_tanks=[Blue_machine,Red_machine,Orange_machine,Green_machine]

#-- missile machine
Blue_missile=img.load(Setting.asset+Setting.missile_path+Setting.Blue_image)
Blue_missile=tf.smoothscale(Blue_missile,(45,30))

Red_missile=img.load(Setting.asset+Setting.missile_path+Setting.Red_image)
Red_missile=tf.smoothscale(Red_missile,(45,30))

Orange_missile=img.load(Setting.asset+Setting.missile_path+Setting.Orange_image)
Orange_missile=tf.smoothscale(Orange_missile,(45,30))

Green_missile=img.load(Setting.asset+Setting.missile_path+Setting.Green_image)
Green_missile=tf.smoothscale(Green_missile,(45,30))

missile_tanks=[Blue_missile,Red_missile,Orange_missile,Green_missile]

pygame.display.quit()
pygame.quit()
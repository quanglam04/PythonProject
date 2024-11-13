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
def create_frame(image,frame,color):
    merged_image = pygame.Surface((500, 19), pygame.SRCALPHA)
    rect_surface=pygame.Surface((50,10))
    rect_surface.fill(color)
    if frame==1:
        for i in range (0,10,2):
            merged_image.blit(image,(i*50,0))
        for i in range(1,10,2):
            merged_image.blit(rect_surface,(i*50,4))
    else:
        for i in range(0,10,2):
            merged_image.blit(rect_surface,(i*50,4))
        for i in range (1,10,2):
            merged_image.blit(image,(i*50,0))
    return merged_image

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

beam_item=img.load(Setting.beam)
beam_item.set_colorkey(Setting.WHITE)
beam_item=tf.scale(beam_item,(25,25))

shotgun_item=img.load(Setting.shotgun)
shotgun_item.set_colorkey(Setting.WHITE)
shotgun_item=tf.scale(shotgun_item,(25,25))



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

# ------ Beam_img --------------#
Blue_beam=img.load(Setting.Blue_beam_image_path).convert_alpha()
Blue_beam=tf.smoothscale(Blue_beam,(500,19))
Blue_beam_resize=Blue_beam.copy()
Blue_beam_resize=tf.smoothscale(Blue_beam_resize,(50,19))
Blue_beam_frames=[Blue_beam]
Blue_beam_frame_1=create_frame(Blue_beam_resize,1,Setting.BLUE_BEAM)
Blue_beam_frame_2=create_frame(Blue_beam_resize,2,Setting.BLUE_BEAM)
Blue_beam_frames.append(Blue_beam_frame_1)
Blue_beam_frames.append(Blue_beam_frame_2)


Red_beam=img.load(Setting.Red_beam_image_path).convert_alpha()
Red_beam=tf.smoothscale(Red_beam,(500,19))
Red_beam_resize=Red_beam.copy()
Red_beam_resize=tf.smoothscale(Red_beam_resize,(50,19))
Red_beam_frames=[Red_beam]
Red_beam_frame_1=create_frame(Red_beam_resize,1,Setting.RED_BEAM)
Red_beam_frame_2=create_frame(Red_beam_resize,2,Setting.RED_BEAM)
Red_beam_frames.append(Red_beam_frame_1)
Red_beam_frames.append(Red_beam_frame_2)



Orange_beam=img.load(Setting.Orange_beam_image_path).convert_alpha()
Orange_beam=tf.smoothscale(Orange_beam,(500,19))
Orange_beam_resize=Orange_beam.copy()
Orange_beam_resize=tf.smoothscale(Orange_beam_resize,(50,19))
Orange_beam_frames=[Orange_beam]
Orange_beam_frame_1=create_frame(Orange_beam_resize,1,Setting.ORANGE_BEAM)
Orange_beam_frame_2=create_frame(Orange_beam_resize,2,Setting.ORANGE_BEAM)
Orange_beam_frames.append(Orange_beam_frame_1)
Orange_beam_frames.append(Orange_beam_frame_2)



Green_beam=img.load(Setting.Green_beam_image_path).convert_alpha()
Green_beam=tf.smoothscale(Green_beam,(500,19))
Green_beam_resize=Green_beam.copy()
Green_beam_resize=tf.smoothscale(Green_beam_resize,(50,19))
Green_beam_frames=[Green_beam]
Green_beam_frame_1=create_frame(Green_beam_resize,1,Setting.GREEN_BEAM)
Green_beam_frame_2=create_frame(Green_beam_resize,2,Setting.GREEN_BEAM)
Green_beam_frames.append(Green_beam_frame_1)
Green_beam_frames.append(Green_beam_frame_2)



beams=[Blue_beam_frames,Red_beam_frames,Orange_beam_frames,Green_beam_frames]

#Beam tank
Blue_tank_beam_0=img.load(Setting.Blue_tank_beam_path_0)
Blue_tank_beam_0=tf.smoothscale(Blue_tank_beam_0,(45,30))

Red_tank_beam_0=img.load(Setting.Red_tank_beam_path_0)
Red_tank_beam_0=tf.smoothscale(Red_tank_beam_0,(45,30))

Orange_tank_beam_0=img.load(Setting.Orange_tank_beam_path_0)
Orange_tank_beam_0=tf.smoothscale(Orange_tank_beam_0,(45,30))

Green_tank_beam_0=img.load(Setting.Green_tank_beam_path_0)
Green_tank_beam_0=tf.smoothscale(Green_tank_beam_0,(45,30))

tanks_beam_0=[Blue_tank_beam_0,Red_tank_beam_0,Orange_tank_beam_0,Green_tank_beam_0]

Blue_tank_beam_1=img.load(Setting.Blue_tank_beam_path_1)
Blue_tank_beam_1=tf.smoothscale(Blue_tank_beam_1,(45,30))

Red_tank_beam_1=img.load(Setting.Red_tank_beam_path_1)
Red_tank_beam_1=tf.smoothscale(Red_tank_beam_1,(45,30))

Orange_tank_beam_1=img.load(Setting.Orange_tank_beam_path_1)
Orange_tank_beam_1=tf.smoothscale(Orange_tank_beam_1,(45,30))

Green_tank_beam_1=img.load(Setting.Green_tank_beam_path_1)
Green_tank_beam_1=tf.smoothscale(Green_tank_beam_1,(45,30))

tanks_beam_1=[Blue_tank_beam_1,Red_tank_beam_1,Orange_tank_beam_1,Green_tank_beam_1]

Blue_tank_beam_2=img.load(Setting.Blue_tank_beam_path_2)
Blue_tank_beam_2=tf.smoothscale(Blue_tank_beam_2,(45,30))

Red_tank_beam_2=img.load(Setting.Red_tank_beam_path_2)
Red_tank_beam_2=tf.smoothscale(Red_tank_beam_2,(45,30))

Orange_tank_beam_2=img.load(Setting.Orange_tank_beam_path_2)
Orange_tank_beam_2=tf.smoothscale(Orange_tank_beam_2,(45,30))

Green_tank_beam_2=img.load(Setting.Green_tank_beam_path_2)
Green_tank_beam_2=tf.smoothscale(Green_tank_beam_2,(45,30))

tanks_beam_2=[Blue_tank_beam_2,Red_tank_beam_2,Orange_tank_beam_2,Green_tank_beam_2]

Blue_tank_beam_3=img.load(Setting.Blue_tank_beam_path_3)
Blue_tank_beam_3=tf.smoothscale(Blue_tank_beam_3,(45,30))

Red_tank_beam_3=img.load(Setting.Red_tank_beam_path_3)
Red_tank_beam_3=tf.smoothscale(Red_tank_beam_3,(45,30))

Orange_tank_beam_3=img.load(Setting.Orange_tank_beam_path_3)
Orange_tank_beam_3=tf.smoothscale(Orange_tank_beam_3,(45,30))

Green_tank_beam_3=img.load(Setting.Green_tank_beam_path_3)
Green_tank_beam_3=tf.smoothscale(Green_tank_beam_3,(45,30))

tanks_beam_3=[Blue_tank_beam_3,Red_tank_beam_3,Orange_tank_beam_3,Green_tank_beam_3]


pygame.display.quit()
pygame.quit()
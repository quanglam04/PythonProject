import pygame
from pygame import image as img
from pygame import transform as tf
import Setting
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
pygame.display.quit()
pygame.quit()
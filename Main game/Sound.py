import pygame
from pygame import  mixer
import Setting
pygame.init()
#amo sound
bullet_sound=mixer.Sound(Setting.bulletMusic)
bullet_sound.set_volume(Setting.sf_volume)
laser_sound = mixer.Sound(Setting.laser_sound)
laser_sound.set_volume(Setting.sf_volume)
machine_gun_sound = mixer.Sound(Setting.machine_sound)
machine_gun_sound.set_volume(Setting.sf_volume)

beam_sound = mixer.Sound(Setting.beam_sound)
beam_sound.set_volume(Setting.sf_volume)

#item sound
mg_item_s=mixer.Sound(Setting.mg_item_se)
mg_item_s.set_volume(Setting.sf_volume)
ls_item_s=mixer.Sound(Setting.la_item_se)
ls_item_s.set_volume(Setting.sf_volume)

#bgm sound
music_bg_victory=mixer.Sound(Setting.backgroundMusic)
music_bg_victory.set_volume(Setting.bg_volume)

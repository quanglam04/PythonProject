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
missile_tracking_sound=mixer.Sound(Setting.missile_tracking_sound_path)
missile_tracking_sound.set_volume(Setting.sf_volume/2)
missile_shot_sound=mixer.Sound(Setting.missile_shot_sound_path)
missile_shot_sound.set_volume(Setting.sf_volume/2)
start_beam=mixer.Sound(Setting.starting_beam_sound_path)
start_beam.set_volume(Setting.sf_volume)
mega_beam=mixer.Sound(Setting.mege_beam_ray_sound_path)
mega_beam.set_volume(Setting.sf_volume)
shotgun_shot=mixer.Sound(Setting.shotgun_shot_sound_path)
shotgun_shot.set_volume(Setting.sf_volume)
shotgun_pump=mixer.Sound(Setting.shotgun_pump_sound_path)
shotgun_pump.set_volume(Setting.sf_volume)

#item sound
mg_item_s=mixer.Sound(Setting.mg_item_se)
mg_item_s.set_volume(Setting.sf_volume)
ls_item_s=mixer.Sound(Setting.la_item_se)
ls_item_s.set_volume(Setting.sf_volume)
missile_active_sound=mixer.Sound(Setting.missile_active_sound_path)
missile_active_sound.set_volume(Setting.sf_volume)

#bgm sound
music_bg_victory=mixer.Sound(Setting.backgroundMusic)
music_bg_victory.set_volume(Setting.bg_volume)

#sound crash
tank_death_sound=mixer.Sound(Setting.death_tank_sound_path)
tank_death_sound.set_volume(Setting.sf_volume/2)

missile_crash_tank_sound=mixer.Sound(Setting.missile_crash_sound_path)
missile_crash_tank_sound.set_volume(Setting.sf_volume/2)

normal_sound_crash=mixer.Sound(Setting.normal_crash_sound_path)
normal_sound_crash.set_volume(Setting.sf_volume)
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:19:42 2022

@author: 18705
"""

class Settings:
    '''存储游戏里的所有设置类'''
    def __init__(self):
        '''初始化游戏静态设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        
        #飞船设置
        #self.ship_speed = 1.5
        self.ship_limit = 3#飞船的数量
        
        #子弹设置
        
        self.bullet_width =5
        self.bullet_height =20
        self.bullet_color =(255,215,0)
        self.bullets_allowed = 15
        
        #超级武器设置
        self.bullet_width_s =600
        self.bullet_height_s =40
        self.bullet_color_s =(255,0,0)
        #外星人设置
        
        self.fleet_drop_speed =10
        
        #加快游戏节奏的速度
        self.speedup_scale = 1.2
        #外行人分数提高速度
        self.score_scale = 2
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        #self.ship_speed = 1.5
        self.bullet_speed =1.5
        self.alien_speed = 1.0
        self.bg_speed = 0.2
         #1是向右，-1是向左
        self.fleet_direction = 1
        #计分
        self.alien_points = 1
        
        
    def increase_speed(self):
        '''提高速度设置和外星人分数'''
        #self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bg_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
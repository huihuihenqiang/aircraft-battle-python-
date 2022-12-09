# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:57:51 2022

@author: 18705
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''单个外星人类'''
    def __init__(self,ai_game):
        '''在飞船当前位置创建一个子弹对象'''
        super().__init__()
        self.screen =ai_game.screen
        self.settings = ai_game.settings
        '''加载图像，注意和子弹不用图像的区别'''
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #存储外星人的精准水平位置
        self.x = float(self.rect.x)
        
    def check_edges(self):
        '''位于边缘，返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True
        
    def update(self):
        '''像→移动外星人'''
        self.x += (self.settings.alien_speed*
                   self.settings.fleet_direction)
        self.rect.x = self.x
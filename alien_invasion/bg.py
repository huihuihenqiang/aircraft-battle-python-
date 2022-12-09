# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:01:02 2022

@author: 18705
"""

import pygame
from settings import Settings

class Bg:
    def __init__(self,ai_game):
        '''初始化飞船并设置其初始位置'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings= ai_game.settings
        #加载飞船图像并获取其外接矩形
        self.image1 = pygame.image.load('images/bd3.jpg')
        self.image2 = pygame.image.load('images/bd3.jpg')
        #self.rect = self.image1.get_rect()
        #self.rect = self.image2.get_rect()
        #对于没搜辛飞船，都将其放在屏幕底部中央
        #self.rect.center = self.screen_rect.center
        self.settings = Settings()
        self.size=(self.settings.screen_width,self.settings.screen_height)
        self.scene = pygame.display.set_mode([self.size[0],self.size[1]])
        self.y1 = 0
        self.y2 = self.size[0]
        
    def action(self):
        self.y1 = self.y1 + self.settings.bg_speed
        self.y2 = self.y2 + self.settings.bg_speed
        if self.y1 >= self.size[1]:
            self.y1 = 0
        if self.y2 >= 0:
            self.y2 = -self.size[1]

    def blitme(self):
        '''在指定位置绘制飞船'''
        #self.screen.blit(self.image,self.rect)
        self.scene.blit(self.image1, (0, self.y1))
        self.scene.blit(self.image2, (0, self.y2))
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:41:00 2022

@author: 18705
"""

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''管理飞船的类'''
    #ai_game就是主函数，可能因为这个函数是个子函数
    def __init__(self,ai_game):
        '''初始化飞船并设置其初始位置'''
        super().__init__()
        self.screen = ai_game.screen
        #self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        #self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        
        #对于没搜辛飞船，都将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        #在飞船的x属性中存储小数值
        #self.x=float(self.rect.x)
        
        #移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        '''根据移动标志调整飞船的位置'''
        #更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        
        #根据self.x更新rect对象
        #self.rect.x = self.x
    
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        '''让飞船在屏幕底端居中'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
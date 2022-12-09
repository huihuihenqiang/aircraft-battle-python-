# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:02:43 2022

@author: 18705
"""

import pygame.font
from button import Button
class ButtonHelp:
    
    def __init__(self,ai_game,msg):
        '''初始化按钮的属性'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.button = Button(self,'play')
        #设置按钮的尺寸和其他属性
        self.width,self.height = 200,50
        self.button_color = (87,250,255)
        self.text_color = (255,128,0)
        self.font = pygame.font.SysFont(None, 48)
        
        #创建按钮的rect对象，并且让其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.bottom = self.button.rect.bottom + 100
        self.rect.right = self.button.rect.right 
        #self.rect.center = self.screen_rect.center
        
        #按钮的标签指创建一次
        self._prep_msg(msg)
    
    def _prep_msg(self,msg):
        '''将msg渲染成图像，显示在按钮上'''
        self.msg_image = self.font.render(msg,True,self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
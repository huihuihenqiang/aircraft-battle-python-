# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:20:27 2022

@author: 18705
"""

import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    '''显示得分·信息的类'''
    
    def __init__(self,ai_game):
        '''初始化显示得分涉及的属性'''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        #显示得分信息时使用的字体设置
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        #准备初始得分图像和最高得分
        self.ships = Group()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships
        
    def prep_score(self):
        '''将得分渲染成图像，好像所有的文字都需要渲染成图像再显示'''
        score_str = 'Score : '+str(self.stats.score)
        self.score_image = self.font.render(score_str,True, 
                    self.text_color)#self.settings.bg_color''')
        
        #屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 50
        self.score_rect.top = 20
    def prep_high_score(self):
        high_score_str = 'High Score : '+str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str,True, 
                    self.text_color)#self.settings.bg_color''')
        
        #屏幕右上角显示得分
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx -50
        self.high_score_rect.top = self.score_rect.top
    def prep_level(self):
        level_str = 'Level : '+str(self.stats.level)
        self.level_image = self.font.render(level_str,True, 
                    self.text_color)#self.settings.bg_color''')
        
        #屏幕右上角显示得分
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right 
        self.level_rect.top = self.score_rect.top+30
        
    def prep_ships(self):
        '''显示剩下多少搜飞船'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10+ship_number * ship.rect.width
            ship.rect.y =10
            self.ships.add(ship)
    def show_score(self):
        '''在屏幕上显示得分绘制飞船'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
    def check_high_score(self):
        '''检查是否诞生新的最高分'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
        
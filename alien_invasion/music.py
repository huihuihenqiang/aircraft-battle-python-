# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:44:21 2022

@author: 18705
"""
import pygame

class Music:
    '''游戏音乐和音效和爆炸效果'''
    def __init__(self,ai_game):
        #音效
        self.bow_sound = pygame.mixer.Sound("musics/bow.mp3")
        self.bow_sound.set_volume(0.2)

        self.piu_sound = pygame.mixer.Sound("musics/piu.mp3")
        self.piu_sound.set_volume(0.2)
        
        self.bow_d_sound = pygame.mixer.Sound("musics/bow_d.wav")
        
        #爆炸效果
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/bow.png')
        self.rect = self.image.get_rect()
        #self.rect.right = ai_game.ship.rect.right
        self.rect.center = self.screen_rect.center
        
    def bullet(self):
        self.piu_sound.play()
    def alien(self):
        self.bow_sound.play()
    def bow(self):
        self.bow_d_sound.play()
    def bullet_stop(self):
        self.piu_sound.stop()
    def alien_stop(self):
        self.bow_sound.stop()
    def bow_stop(self):
        self.bow_d_sound.stop()  
    
    def bgm2(self):
        #背景音乐
        #pygame.mixer.music.stop()
        pygame.mixer.music.load("musics/bg2.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
    def bgm1(self):
        #pygame.mixer.music.stop()
        pygame.mixer.music.load("musics/bg1.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
        
    def bgm_pause(self):
        pygame.mixer.music.pause()
    def bgm_unpause(self):
        pygame.mixer.music.unpause()

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)
        
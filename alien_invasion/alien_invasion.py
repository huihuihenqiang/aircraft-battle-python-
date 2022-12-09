# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:44:22 2022

@author: 18705
"""
'''self就是创建可以引用的一个值
可以传递的实参，其他形参靠他。
同时，self.name是属性，self.name()是方法。super是父类等等。'''

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from buttonhelp import ButtonHelp
from ship import Ship
from bg import Bg
from bullet import Bullet
from alien import Alien
from music import Music

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并且创建游戏资源'''
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height),pygame.RESIZABLE)
        icon = pygame.image.load("images/plant.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("星球大战")
        #创建一个用于统计游戏信息的示例
        #并创建记分牌
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        #外星飞船
        self.bg =Bg(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.music = Music(self)
        #背景音乐
        #背景音乐的播放不能放到主循环里面
        self.music.bgm2()
        #尝试换音乐，失败了
        '''
        self.control_bgm_t = True
        if self.control_bgm_t:
            self.music.bgm2()
        else:
            self.music.bgm1()
        '''
        self.control_bgm = False
        self.n=False
        #设置背景颜色
        #self.bg_color = (230,230,230)
        #创建外星人群
        self._create_fleet()
        
        #创建Play按钮
        self.play_button = Button(self,'play')
        #创建Help按钮
        self.help_button = ButtonHelp(self,'help')
        #连发子弹
        self.control_bullet = False
        #关闭音效
        self.control_sound = True
        self.nn = False
        #大子弹
        self.control_bullet_big = False
        
    def run_game(self):
        '''开始游戏的主循环'''
        
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
            #自动发射子弹
            if self.control_bullet:
                self._fire_bullet()
            #控制bgm开关
            if self.control_bgm:
                self.music.bgm_pause()
                self.n=True
            elif not self.control_bgm and self.n==True:
                self.music.bgm_unpause()
                self.n= not self.n
    def _check_events(self):
            #监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #将高分添加到txt中
                    with open('high_score.txt','w') as file_object:
                        file_object.write(str(self.stats.high_score))
                    file_object.close()
                    pygame.quit()
                    sys.exit()
                    #设置长按移动
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._check_mousebuttondown_events(event)
                    
    def _check_keydown_events(self,event):
        '''相应按键'''
        if event.key == pygame.K_d:
        #向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
        #向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            #将高分添加到txt中
            with open('high_score.txt','w') as file_object:
                file_object.write(str(self.stats.high_score))
            file_object.close()
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_w:
            self.control_bullet =not self.control_bullet 
        elif event.key == pygame.K_i:
            self.control_bgm = not self.control_bgm           
        elif event.key == pygame.K_o:
            self.control_sound = not self.control_sound 
        #elif event.key == pygame.K_p:
            #self.control_bgm_t = not self.control_bgm_t
        elif event.key == pygame.K_p:
            self.control_bullet_big = not self.control_bullet_big
            
    def _check_keyup_events(self,event):
        '''响应松开'''
        if event.key == pygame.K_d:
        #向右移动飞船
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
        #向右移动飞船
            self.ship.moving_left = False
    
    def _check_mousebuttondown_events(self,event):
        '''响应鼠标'''
        if event.button == 1:
            self._fire_bullet()
        #设置play的功能和help的功能，其实应该封装一下的，哈哈哈哈。偷懒了
        button_clicked = self.play_button.rect.collidepoint(event.pos)
        buttonhelp_clicked = self.help_button.rect.collidepoint(event.pos)
        if button_clicked and not self.stats.game_active:
            #重置游戏设置
            self.settings.initialize_dynamic_settings()
            #重置游戏统计·信息
            self.stats.reset_stats()
            self.stats.game_active = True 
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            #清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            
            #创建一群新外星人并且居中
            self._create_fleet()
            self.ship.center_ship()
            
            #隐藏鼠标光标
            pygame.mouse.set_visible(False)
        if buttonhelp_clicked and not self.stats.game_active:
            with open('help.txt',encoding='utf-8') as helptext:
                content = helptext.read()
            print(content)
            helptext.close()
    def _fire_bullet(self):
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            #控制子弹音效
            if self.control_sound:
                self.music.bullet()
                self.nn = True
            elif not self.control_sound and self.nn:
                self.music.bullet_stop()
                self.nn = not self.nn
    def _update_bullets(self):
         self.bullets.update()
            
            #删除消失的子弹
         for bullet in self.bullets.copy():
             if bullet.rect.bottom <=0:
                 self.bullets.remove(bullet)
         #print(len(self.bullets))
         #检查是否有子弹击中外星人
         self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        '''响应子弹和外星人碰撞'''
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                #控制子弹和外星人碰撞音效
                if self.control_sound:
                    self.music.alien()
                    self.nn = True
                elif not self.control_sound and self.nn:
                    self.music.alien_stop()
                    self.nn = not self.nn
                self.stats.score += self.settings.alien_points*len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
                
        if not self.aliens:
             #删除现有的子弹并新建一群外星人
             self.bullets.empty()
             self._create_fleet()
             self.settings.increase_speed()
             
             #提高等级
             self.stats.level +=1
             self.sb.prep_level()
         
         
    def _update_aliens(self):
        '''更新外星人位置'''
        self._check_fleet_edges()
        self.aliens.update()
        
        #检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            #print("Ship hit!!!")
            self._ship_hit()
        
        #检查是否有外星人到达了屏幕底端
        self._check_aliens_bottom()
        
    def _create_fleet(self):
        '''创建外星人群。'''
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)
        
        #计算屏幕可以容纳多少外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height) 
                             - ship_height)#每行不超过79个字符
        number_rows = available_space_y // (2*alien_height)
        
        #创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)
            
    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width*alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        '''有外星人到达边缘采取响应的措施'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        '''整群下移，改变方向'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *=-1
        
    def _ship_hit(self):
        '''响应飞船被外星人撞到'''
        if self.stats.ships_left >0:
            
        #将ship_left减一并更新记分牌
            self.stats.ships_left -=1
            self.sb.prep_ships()
        #清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
        
        #创建一群新的外星人，并将飞船放到屏幕底端的中央
            self._create_fleet()
            self.ship.center_ship()
        #爆炸效果
            self.music.blitme()
            pygame.display.flip()
            #控制飞船和外星人碰撞音效
            if self.control_sound:
                self.music.bow()
                self.nn = True
            elif not self.control_sound and self.nn:
                self.music.bow_stop()
                self.nn = not self.nn
            
        #暂停
            sleep(2)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        '''检查外星人是否到达了屏幕底端'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >=screen_rect.bottom:
                #像飞船悲壮一样处理
                self._ship_hit()
                break
        
    
    def _update_screen(self):
                
            #每次循环都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.bg.action()
            # 绘制元素图片
            self.bg.blitme()
            #self.bg.blitme()
            self.ship.blitme()
            #让最近绘制的屏幕可见
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            
            #显示得分
            self.sb.show_score()
            
            #如果游戏处于非活动状态，就绘制Play按钮
            if not self.stats.game_active:
                self.play_button.draw_button()
            if not self.stats.game_active:
                self.help_button.draw_button()
            
            pygame.display.flip()
        
if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:30:39 2022

@author: 18705
"""

class GameStats:
    '''跟踪游戏的统计信息'''
    def __init__(self,ai_game):
        '''初始化统计信息'''
        self.settings = ai_game.settings
        self.reset_stats()
        #游戏刚启动时候处于fei活动状态
        self.game_active = False
        #任何情况下都不应该重置最高得分
        with open('high_score.txt') as file_object:
            content = file_object.read()
        self.high_score = int(content)
        file_object.close()
    
    def reset_stats(self):
        '''初始化在游戏运行期间可能发生的统计信息'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
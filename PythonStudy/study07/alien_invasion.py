"""外星人入侵项目"""

import sys
import pygame
from study07.setting import *
from study07.ship import Ship
from study07.alien import Alien
from study07.game_stats import GameStats
from study07.button import Button
from study07.scoreboard import Scoreboard
from pygame.sprite import  Group
import study07.game_functions as gf

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_setting = Setings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_setting, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)
    # 创建Play按钮
    play_button = Button(ai_setting, screen, "Play")

    # 创建外星人群
    gf.create_fleet(ai_setting, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_setting, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()


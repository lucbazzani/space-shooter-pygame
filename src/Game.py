#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from src.Level import Level
from src.utils.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from src.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        running = True
        while running:

            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.screen, 'level1', menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                sys.exit()

#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from src.utils.Const import WIN_WIDTH, WIN_HEIGHT
from src.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        running = True
        while running:
            # é necessário varrer os eventos para que o pygame possa abrir a janela corretamente no Macbook
            for event in pygame.event.get():
                pass

            menu = Menu(self.screen)
            menu.run()

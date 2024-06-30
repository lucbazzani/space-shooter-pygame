#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from src.utils.Const import WIN_WIDTH, TITLE_TEXT_COLOR, MENU_OPTION, OPTION_TEXT_COLOR, SELECTED_OPTION_COLOR


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surf = pygame.image.load('./asset/menu_bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/sounds/electronic-diddie-2.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0
        running = True
        while running:
            # desenhar na tela
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text('Shooting', 50, TITLE_TEXT_COLOR, ((WIN_WIDTH / 2), 70))
            self.menu_text('Clouds', 50, TITLE_TEXT_COLOR, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(MENU_OPTION[i], 20, SELECTED_OPTION_COLOR, ((WIN_WIDTH / 2), 190 + 30 * i))
                else:
                    self.menu_text(MENU_OPTION[i], 20, OPTION_TEXT_COLOR, ((WIN_WIDTH / 2), 190 + 30 * i))
            pygame.display.flip()

            # verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # verificar se alguma tecla é pressionada
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text: str, size: int, color: tuple, center_pos: tuple):
        font: Font = pygame.font.SysFont(name='Pixelify Sans', size=size)
        surf: Surface = font.render(text, True, color)
        rect: Rect = surf.get_rect(center=center_pos)
        self.screen.blit(source=surf, dest=rect)

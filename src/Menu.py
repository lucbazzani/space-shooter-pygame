#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from src.utils.Const import WIN_WIDTH, GAME_TITLE_TEXT, TITLE_TEXT_COLOR


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surf = pygame.image.load('./asset/menu_bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/sounds/electronic-diddie-2.mp3')
        pygame.mixer_music.play(-1)
        running = True
        while running:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(GAME_TITLE_TEXT, 50, TITLE_TEXT_COLOR, ((WIN_WIDTH / 2), 70))
            pygame.display.flip()

    def menu_text(self, text: str, size: int, color: tuple, center_pos: tuple):
        font: Font = pygame.font.SysFont(name='Pixelify Sans', size=size)
        surf: Surface = font.render(text, True, color)
        rect: Rect = surf.get_rect(center=center_pos)
        self.screen.blit(source=surf, dest=rect)


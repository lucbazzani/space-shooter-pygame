#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.image
from pygame import Surface


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surf = pygame.image.load('./asset/menu_bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        running = True
        while running:
            self.screen.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

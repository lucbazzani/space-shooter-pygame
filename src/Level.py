#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Surface

from src.Entity import Entity
from src.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, mode):
        self.screen: Surface = screen
        self.name = name
        self.mode = mode  # opção do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1_bg'))

    def run(self, ):
        running = True
        while running:
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.flip()


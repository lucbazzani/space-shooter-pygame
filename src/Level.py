#!/usr/bin/python
#-*- coding: utf-8 -*-
from src.Entity import Entity


class Level:
    def __init__(self, screen, name, mode):
        self.screen = screen
        self.name = name
        self.mode = mode  # opção do menu
        self.entity_list: list[Entity] = []

    def run(self, ):
        pass


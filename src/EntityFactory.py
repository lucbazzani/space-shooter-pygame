#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.Background import Background
from src.utils.Const import BGS_LENGTH, WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1_bg':
                bg_list = []
                for i in range(BGS_LENGTH['level1_bg']):
                    name = f'level1_bg{i}'
                    bg_list.append(Background(name, (0, 0)))
                    bg_list.append(Background(name, (WIN_WIDTH, 0)))

                return bg_list

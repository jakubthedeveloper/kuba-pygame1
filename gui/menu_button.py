#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class MenuButton(object):
    BUTTON_WIDTH  = 260
    BUTTON_HEIGHT = 100
    BACKGROUND_COLOR_NORMAL = (61, 61, 61)
    BACKGROUND_COLOR_MOUSEOVER = (107, 107, 107)

    label = None
    label_font = None
    click_callback = None

    button_center_x = 0
    button_center_y = 0

    def __init__(self, label, button_center_x, button_center_y, click_callback):
        pygame.font.init()
        self.label = label
        self.button_center_x = button_center_x
        self.button_center_y = button_center_y
        self.click_callback = click_callback

        self.label_font = pygame.font.SysFont('Verdana', 24)
        self.button_rectangle = [
            button_center_x - (self.BUTTON_WIDTH / 2),
            button_center_y - (self.BUTTON_HEIGHT / 2),
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT
        ]

    def checkMouseOver(self, mouse_position):
        checkX = mouse_position[0] >= self.button_rectangle[0] and mouse_position[0] <= self.button_rectangle[0] + self.button_rectangle[2]
        checkY = mouse_position[1] >= self.button_rectangle[1] and mouse_position[1] <= self.button_rectangle[1] + self.button_rectangle[3]
        return checkX and checkY

    def draw(self, screen, mouse_position):
        is_mouse_over = self.checkMouseOver(mouse_position)
        pygame.draw.rect(screen, self.BACKGROUND_COLOR_NORMAL if not is_mouse_over else self.BACKGROUND_COLOR_MOUSEOVER, self.button_rectangle, 0)
        pygame.draw.rect(screen, (255, 255, 255), self.button_rectangle, 1)
        button_text = self.label_font.render(self.label, False, (255, 255, 255))
        screen.blit(button_text, (self.button_center_x - (button_text.get_width() / 2), self.button_center_y - 16))
